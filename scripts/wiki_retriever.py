# scripts/wiki_retriever.py
import wikipediaapi
import wikipedia
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compute_relevance(query, text):
    """
    Compute a cosine similarity score between the query and some text using TF-IDF.
    """
    vectorizer = TfidfVectorizer(stop_words='english')
    corpus = [query, text]
    tfidf_matrix = vectorizer.fit_transform(corpus)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return similarity

def is_medical_query(query):
    """
    Heuristically decide if the query is medical.
    """
    medical_keywords = ["heart", "attack", "cardiac", "infarction", "chest pain", "myocardial", "treatment", "prevent"]
    return any(kw in query.lower() for kw in medical_keywords)

def is_medically_relevant(page):
    """
    Check if a page is likely medically focused by looking at its categories.
    """
    medical_keywords = ["medicine", "medical", "health", "cardiology", "disease", "heart", "clinical", "treatment"]
    for cat in page.categories.keys():
        if any(kw in cat.lower() for kw in medical_keywords):
            return True
    return False

def is_entertainment_page(page):
    """
    Returns True if the page title indicates it’s about entertainment (e.g., a song, album, or film).
    """
    title = page.title.lower()
    if "(" in title and ")" in title:
        qualifier = title.split("(")[-1].split(")")[0].strip()
        if qualifier in {"song", "album", "film", "single", "music"}:
            return True
    return False

def get_wikipedia_content(query):
    """
    Retrieve a Wikipedia page based on the query.
    
    1. Try a direct lookup and gather candidate pages from wikipedia.search().
    2. Compute a TF-IDF–based relevance score using the page summary.
    3. Boost pages that appear medically relevant based on their categories.
    4. For medical queries, filter out candidates whose titles suggest entertainment.
    5. Rank candidates by their (boosted) scores and return the best candidate's text.
    """
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent="WikiChatbot/1.0 (contact: frankie.walsh@outlook.com)",
        language='en'
    )
    candidates = []
    
    # --- Direct lookup candidate ---
    direct_page = wiki_wiki.page(query)
    if direct_page.exists():
        score = compute_relevance(query, direct_page.summary)
        bonus = 0.2 if is_medically_relevant(direct_page) else 0.0
        candidates.append({"page": direct_page, "score": score + bonus})
    
    # --- Gather candidates from a search ---
    try:
        search_results = wikipedia.search(query)
    except Exception:
        search_results = []
    
    for title in search_results:
        page = wiki_wiki.page(title)
        if page.exists():
            score = compute_relevance(query, page.summary)
            bonus = 0.2 if is_medically_relevant(page) else 0.0
            candidates.append({"page": page, "score": score + bonus})
    
    if not candidates:
        return None  # No pages found.
    
    # --- For medical queries, filter out entertainment pages if possible ---
    if is_medical_query(query):
        filtered = [cand for cand in candidates if not is_entertainment_page(cand["page"])]
        if filtered:
            candidates = filtered
    
    # --- Rank candidates by the boosted score ---
    best_candidate = max(candidates, key=lambda cand: cand["score"])
    return f"Title: {best_candidate['page'].title}\n{best_candidate['page'].text}"
