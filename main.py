# main.py
from flask import Flask, request, jsonify
from scripts.wiki_retriever import get_wikipedia_content
from scripts.vector_search import search_content
from transformers import pipeline

app = Flask(__name__)

qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(query, search_results):
    """
    Combine the retrieved paragraphs and use a generative QA model to generate an answer.
    The prompt instructs the model to provide a detailed answer with background information.
    """
    # Combine the top paragraphs into a single context block.
    context = " ".join([result["paragraph"] for result in search_results])
    
    # Build a prompt that instructs the model to generate a detailed answer.
    prompt = (
        f"Answer the following question with a detailed explanation that includes background information:\n\n"
        f"Question: {query}\n\n"
        f"Context: {context}\n\n"
        "Answer:"
    )

    # Generate an answer using the generative QA pipeline.
    output = qa_pipeline(prompt, max_length=512, min_length=100, do_sample=False)
    return output[0]["generated_text"]

@app.route('/query', methods=['POST'])
def query_endpoint():
    data = request.get_json()
    if not data or "query" not in data:
        return jsonify({"error": "No query provided"}), 400

    user_query = data["query"]
    wiki_content = get_wikipedia_content(user_query)
    if not wiki_content:
        return jsonify({"error": "No relevant Wikipedia content found"}), 404

    search_results = search_content(user_query, wiki_content)
    if isinstance(search_results, str):  
        return jsonify({"error": search_results}), 500

    answer = generate_answer(user_query, search_results)
    return jsonify({"response": answer}), 200

if __name__ == '__main__':
    app.run(debug=True)
