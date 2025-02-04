# main.py
from flask import Flask, request, jsonify
from scripts.wiki_retriever import get_wikipedia_content
from scripts.vector_search import search_content

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query_endpoint():
    """
    Expects a JSON payload with a "query" key.
    Retrieves Wikipedia content based on the query, performs vector search,
    and returns the top matching paragraphs.
    """
    data = request.get_json()
    if not data or 'query' not in data:
        return jsonify({"error": "No query provided"}), 400
    
    user_query = data['query']
    wiki_content = get_wikipedia_content(user_query)
    if not wiki_content:
        return jsonify({"error": "No relevant Wikipedia content found"}), 404
    
    search_results = search_content(user_query, wiki_content)
    if isinstance(search_results, str):  # In case of an error message
        return jsonify({"error": search_results}), 500

    return jsonify({"response": search_results}), 200

if __name__ == '__main__':
    app.run(debug=True)
