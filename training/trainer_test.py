import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the trained model and tokenizer
model_name = "results/final_model"  # Path to your saved model
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def ask_question(question):
    """
    Generates an answer from the trained model based on a given question.
    """
    input_text = f"Question: {question}"
    inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)
    
    # Generate response
    with torch.no_grad():
        outputs = model.generate(
    **inputs,
    max_length=256,
    do_sample=True,
    num_beams=5,
    repetition_penalty=2.0,
    early_stopping=True,
    temperature=0.7,
    top_p=0.9,
)

    # Decode the generated response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Test the model with sample questions
test_questions = [
    "What is the IMEx Ecosystem?",
    "What is Electrical Safety?",
    "What is Capital Planning?",
    "How does cybersecurity affect manufacturing?"
]

for question in test_questions:
    answer = ask_question(question)
    print(f"Q: {question}\nA: {answer}\n")
