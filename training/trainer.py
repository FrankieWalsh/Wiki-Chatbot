import os
from transformers import T5Tokenizer, T5ForConditionalGeneration, Seq2SeqTrainer, Seq2SeqTrainingArguments
from datasets import Dataset

# Step 1. Load the tokenizer and model.
model_name = "google/flan-t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Step 2. Tiny example dataset.
data = {
    "input_text": [
        "Question: What is a yacht? Context: A yacht is a luxurious boat often used for recreation.",
        "Question: What is the capital of France? Context: France is a country in Western Europe."
    ],
    "target_text": [
        "A yacht is a large, luxurious boat used primarily for pleasure and recreation.",
        "The capital of France is Paris."
    ]
}

# Create a Hugging Face Dataset from the dictionary.
dataset = Dataset.from_dict(data)

# Step 3. Preprocess the data: tokenize inputs and targets.
def preprocess_function(examples):
    # Tokenize the input text (prompt) and target text (answer).
    model_inputs = tokenizer(examples["input_text"], max_length=512, truncation=True, padding="max_length")
    # Tokenize the target texts. The tokenizer will add the special tokens needed for generation.
    labels = tokenizer(examples["target_text"], max_length=128, truncation=True, padding="max_length")
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_dataset = dataset.map(preprocess_function, batched=True)
tokenized_dataset = tokenized_dataset.remove_columns(["input_text", "target_text"])

# Step 4. Set up training arguments.
training_args = Seq2SeqTrainingArguments(
    output_dir="./results",         # where to save model predictions and checkpoints
    num_train_epochs=3,             # number of epochs for training
    per_device_train_batch_size=2,  # adjust based on your GPU/CPU memory
    save_steps=10,                  # save checkpoint every 10 steps (for this demo, steps will be few)
    logging_steps=5,
    do_train=True,
    evaluation_strategy="no",       # not evaluating on a separate dataset in this simple demo
    remove_unused_columns=True,
)

# Step 5. Initialize the trainer.
trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
)

# Step 6. Start training.
trainer.train()

# Save the final model.
model.save_pretrained(os.path.join(training_args.output_dir, "final_model"))
tokenizer.save_pretrained(os.path.join(training_args.output_dir, "final_model"))
