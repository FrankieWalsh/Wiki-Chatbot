# wiki_retriever.py
import wikipediaapi

def get_wikipedia_content(page_title):
    """
    Retrieve the full text of a Wikipedia page given its title.
    Returns the text if the page exists; otherwise, returns None.
    """
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent="WikiChatbot/1.0 (contact: frankie.walsh@outlook.com)", 
        language='en'
    )
    page = wiki_wiki.page(page_title)
    if page.exists():
        return page.text
    else:
        return None
