# vector_search.py
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def split_into_paragraphs(text):
    """
    Splits the input text into paragraphs using double newlines as delimiters.
    """
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return paragraphs

def search_content(query, content, top_k=3):
    """
    Splits the content into paragraphs, vectorizes them along with the query,
    and returns the top_k paragraphs ranked by cosine similarity.
    
    Args:
        query (str): The user's query.
        content (str): Full text content (e.g., from a Wikipedia page).
        top_k (int): Number of top matching paragraphs to return.
    
    Returns:
        list: A list of dictionaries containing paragraphs and their similarity scores.
    """
    paragraphs = split_into_paragraphs(content)
    if not paragraphs:
        return "No paragraphs found in the content."
    corpus = paragraphs + [query]
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
    tfidf_matrix = vectorizer.fit_transform(corpus)

    query_vector = tfidf_matrix[-1]
    paragraph_vectors = tfidf_matrix[:-1]
    similarities = cosine_similarity(query_vector, paragraph_vectors)[0]
    top_indices = np.argsort(similarities)[::-1][:top_k]

    results = []
    for idx in top_indices:
        sim_score = similarities[idx]
        results.append({
            "paragraph": paragraphs[idx],
            "similarity_score": float(sim_score)  # Convert numpy float to standard float.
        })

    return results
