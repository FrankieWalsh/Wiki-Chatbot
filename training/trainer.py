import os
from transformers import T5Tokenizer, T5ForConditionalGeneration, Seq2SeqTrainer, Seq2SeqTrainingArguments
from datasets import Dataset
from training_data import training_data

# ---------- Optional: Adapter Tuning Setup (Requires the adapter-transformers package) ------------
# Uncomment and install adapter-transformers if you want to try adapter tuning.
#
# from transformers.adapters import AdapterConfig
# adapter_config = AdapterConfig.load("pfeiffer", reduction_factor=2)
# model.add_adapter("domain_adapter", config=adapter_config)
# model.train_adapter("domain_adapter")
# ------------------------------------------------------------------------------------------------

# Step 1. Load the tokenizer and model.
model_name = "google/flan-t5-base"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Step 2. Create the training dataset with expanded and refined examples.
dataset = Dataset.from_dict(training_data)

# Step 3. Preprocess the data: tokenize inputs and targets.
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

# Step 4. Set up training arguments with improved hyperparameters.
training_args = Seq2SeqTrainingArguments(
    output_dir="./results",
    num_train_epochs=10,
    per_device_train_batch_size=2,
    gradient_accumulation_steps=2,
    save_steps=50,
    logging_steps=10,
    do_train=True,
    evaluation_strategy="no",
    predict_with_generate=True,
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
