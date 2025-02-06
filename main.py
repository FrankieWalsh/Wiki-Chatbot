from flask import Flask, request, render_template
from scripts.wiki_retriever import get_wikipedia_content
from scripts.vector_search import search_content
from transformers import pipeline

app = Flask(__name__)

# Initialize the QA pipeline using your generative model.
qa_pipeline = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_answer(query, search_results):
    """
    Combine the retrieved paragraphs and use the generative QA model to generate an answer.
    """
    context = " ".join([result["paragraph"] for result in search_results])
    prompt = (
        f"Answer the following question with a detailed explanation that includes background information:\n\n"
        f"Question: {query}\n\n"
        f"Context: {context}\n\n"
        "Answer:"
    )
    output = qa_pipeline(prompt, max_length=512, min_length=100, do_sample=False)
    return output[0]["generated_text"]

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    query = ""
    if request.method == "POST":
        query = request.form.get("query")
        if query:
            wiki_content = get_wikipedia_content(query)
            if not wiki_content:
                answer = "No relevant Wikipedia content found."
            else:
                search_results = search_content(query, wiki_content)
                if isinstance(search_results, str):  # This indicates an error message.
                    answer = search_results
                else:
                    answer = generate_answer(query, search_results)
    return render_template("index.html", answer=answer, query=query)

if __name__ == '__main__':
    app.run(debug=True)
