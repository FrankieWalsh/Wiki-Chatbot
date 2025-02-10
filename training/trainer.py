import os
from transformers import T5Tokenizer, T5ForConditionalGeneration, Seq2SeqTrainer, Seq2SeqTrainingArguments
from datasets import Dataset
from training_data import training_data  # Your manual data
from wiki_training_data import training_data_wiki  # Wikipedia-based data

# Merge your training data.
merged_training_data = {
    "input_text": training_data["input_text"] + training_data_wiki["input_text"],
    "target_text": training_data["target_text"] + training_data_wiki["target_text"],
}
dataset = Dataset.from_dict(merged_training_data)

# Step 1. Load the tokenizer and model.
model_name = "google/flan-t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# ---------- PEFT / LoRA Adapter Tuning Setup ------------
from peft import LoraConfig, get_peft_model

# Create a LoRA configuration for sequence-to-sequence fine-tuning.
lora_config = LoraConfig(
    task_type="SEQ_2_SEQ_LM",
    inference_mode=False,  # Set to True for inference; False for training.
    r=8,                   # Rank of the low-rank decomposition.
    lora_alpha=32,         # Scaling parameter.
    lora_dropout=0.1       # Dropout probability.
)

# Wrap your model with the PEFT model using the LoRA configuration.
model = get_peft_model(model, lora_config)
# ---------------------------------------------------------

# Step 2. Preprocess the data: tokenize inputs and targets.
def preprocess_function(examples):
    model_inputs = tokenizer(
        examples["input_text"],
        max_length=512,
        truncation=True,
        padding="max_length"
    )
    labels = tokenizer(
        examples["target_text"],
        max_length=128,
        truncation=True,
        padding="max_length"
    )
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_dataset = dataset.map(preprocess_function, batched=True)
tokenized_dataset = tokenized_dataset.remove_columns(["input_text", "target_text"])

# Step 3. Set up training arguments.
training_args = Seq2SeqTrainingArguments(
    output_dir="./results_peft",
    num_train_epochs=14,
    per_device_train_batch_size=4,
    gradient_accumulation_steps=1,
    save_steps=50,
    logging_steps=10,
    do_train=True,
    evaluation_strategy="no",
    predict_with_generate=True,
)

# Step 4. Initialize the trainer.
trainer = Seq2SeqTrainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
    tokenizer=tokenizer,
)

# Step 5. Start training.
trainer.train()

# Save the final model (including the adapter).
model.save_pretrained(os.path.join(training_args.output_dir, "final_model"))
tokenizer.save_pretrained(os.path.join(training_args.output_dir, "final_model"))
