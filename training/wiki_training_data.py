import wikipedia

# Ensure we are using English
wikipedia.set_lang("en")

# Define the topics based on your keywords.
topics = [
    "International Molecular Exchange Consortium",
    "Integrated Facilities Program",
    "Compliance (medicine)",
    "Electrical Safety",
    "Life Cycle Asset Management",
    "Capital Planning",
    "OpU Engineering",
    "Environmental engineering",
    "Legacy Sites",
    "Business Operation",
    "Innovation",
    "Launch Excellence",
    "Network Strategy",
    "Business Development Engineering",  # Alternative for Bus.Dev Engineering
    "Capital Projects",
    "Data Tools for Making Medicines",
    "Utilities Optimization",
    "Compliance & Electrical Safety",
    "Net Zero Strategic Initiative",
    "Cybersecurity in Manufacturing"
]

# This dictionary will hold our new Q&A pairs.
training_data_wiki = {"input_text": [], "target_text": []}

for topic in topics:
    try:
        # Search for the topic on Wikipedia
        search_results = wikipedia.search(topic)
        if search_results:
            # Use the first result as the best match
            page_title = search_results[0]
            page = wikipedia.page(page_title)
            summary = page.summary

            # Create a Q&A pair
            question = f"Question: What is {topic}? Context: (Wikipedia article: '{page_title}')"
            answer = summary
            training_data_wiki["input_text"].append(question)
            training_data_wiki["target_text"].append(answer)
        else:
            print(f"No Wikipedia results found for topic: {topic}")
    except Exception as e:
        print(f"Error fetching topic '{topic}': {e}")

# Optionally, save the results to a JSON file.
import json
with open("wiki_training_data.json", "w", encoding="utf-8") as f:
    json.dump(training_data_wiki, f, indent=4)
