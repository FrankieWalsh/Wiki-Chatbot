# main.py
from flask import Flask, request, jsonify
from scripts.wiki_retriever import get_wikipedia_content
from scripts.vector_search import search_content
from transformers import pipeline

app = Flask(__name__)

# Initialize the summarization pipeline (this may take a minute on first run)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def generate_answer(query, search_results):
    """
    Combine the retrieved paragraphs and use the summarization model
    to generate an answer.
    """
    # Combine the top paragraphs into a single context block.
    context = " ".join([result["paragraph"] for result in search_results])
    
    # Build the input text.
    input_text = (
        f"Question: {query}\n\n"
        f"Context: {context}\n\n"
        "Please answer the question given the context:"
    )

    # Tokenize the input text with truncation.
    encoded = summarizer.tokenizer(
        input_text,
        truncation=True,
        max_length=1024,
        return_tensors="pt"
    )
    
    # Decode back to a string (this string is now within the model's limits).
    truncated_text = summarizer.tokenizer.decode(
        encoded["input_ids"][0],
        skip_special_tokens=True
    )

    # Generate the summary using the truncated text.
    summary = summarizer(
        truncated_text,
        max_length=300,   # maximum length for the generated summary
        min_length=40,    # minimum length for the generated summary
        do_sample=False
    )
    return summary[0]["summary_text"]

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
    if isinstance(search_results, str):  # error message returned from search_content
        return jsonify({"error": search_results}), 500

    answer = generate_answer(user_query, search_results)
    return jsonify({"response": answer}), 200

if __name__ == '__main__':
    app.run(debug=True)
