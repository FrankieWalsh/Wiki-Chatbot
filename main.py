from flask import Flask, request, render_template, session
import os
from scripts.wiki_retriever import get_wikipedia_content
from scripts.vector_search import search_content
from transformers import pipeline

app = Flask(__name__)
app.secret_key = os.urandom(24)

qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(query, search_results, conversation_history):
    conversation_prompt = ""
    for turn in conversation_history:
        conversation_prompt += f"User: {turn['question']}\nAI: {turn['answer']}\n"
    context = " ".join([result["paragraph"] for result in search_results])
    prompt = (
        f"{conversation_prompt}"
        f"User: {query}\n"
        f"Context: {context}\n"
        "AI:"
    )
    output = qa_pipeline(prompt, max_length=512, min_length=100, do_sample=False)
    return output[0]["generated_text"]

@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize conversation history if it doesn't exist.
    if "history" not in session:
        session["history"] = []

    answer = None
    query = ""
    
    if request.method == "POST":
        if "reset" in request.form:
            session["history"] = []  # Manually clear chat history
            session.modified = True
            return render_template("index.html", conversation=[])
        query = request.form.get("query")
        if query:
            wiki_content = get_wikipedia_content(query)
            if not wiki_content:
                answer = "No relevant Wikipedia content found."
            else:
                search_results = search_content(query, wiki_content)
                if isinstance(search_results, str):  # Error message check.
                    answer = search_results
                else:
                    conversation_history = session["history"]
                    answer = generate_answer(query, search_results, conversation_history)
            
            # Append the current interaction to the conversation history.
            conversation_turn = {"question": query, "answer": answer}
            history = session.get("history", [])
            history.append(conversation_turn)
            session["history"] = history
    
    # Pass the conversation history to the template.
    return render_template("index.html", answer=answer, query=query, conversation=session.get("history"))

if __name__ == '__main__':
    app.run(debug=True)
