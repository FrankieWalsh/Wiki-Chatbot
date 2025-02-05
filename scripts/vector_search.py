# scripts/vector_search.py
import numpy as np
from sentence_transformers import SentenceTransformer, util

# Load the model (you can also share the same model instance if preferred)
model = SentenceTransformer('all-MiniLM-L6-v2')

def split_into_paragraphs(text):
    """
    Splits the input text into paragraphs using double newlines as delimiters.
    """
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return paragraphs

def search_content(query, content, top_k=7):
    """
    Splits the content into paragraphs, encodes them along with the query using dense embeddings,
    and returns the top_k paragraphs ranked by cosine similarity.
    
    Args:
        query (str): The user's query.
        content (str): Full text content (now from multiple Wikipedia pages).
        top_k (int): Number of top matching paragraphs to return.
    
    Returns:
        list: A list of dictionaries containing the paragraph and its similarity score.
    """
    paragraphs = split_into_paragraphs(content)
    if not paragraphs:
        return "No paragraphs found in the content."
    
    # Encode all paragraphs and the query
    paragraph_embeddings = model.encode(paragraphs, convert_to_tensor=True)
    query_embedding = model.encode(query, convert_to_tensor=True)
    
    # Compute cosine similarities using dense embeddings
    cosine_scores = util.cos_sim(query_embedding, paragraph_embeddings)[0]
    
    # Get indices of the top_k paragraphs
    top_indices = np.argsort(cosine_scores.cpu().numpy())[::-1][:top_k]
    results = []
    for idx in top_indices:
        results.append({
            "paragraph": paragraphs[idx],
            "similarity_score": float(cosine_scores[idx])
        })
    return results
