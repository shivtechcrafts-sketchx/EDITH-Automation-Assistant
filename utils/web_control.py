import webbrowser
import urllib.parse


def search_google(query: str):
    """Open Google and search the query"""
    if not query.strip():
        return "No search query provided."
    
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={encoded_query}"
    webbrowser.open(url)
    return f"Searching Google for: {query}"


def search_youtube(query: str):
    """Open YouTube and search the query"""
    if not query.strip():
        return "No search query provided."
    
    encoded_query = urllib.parse.quote(query)
    url = f"https://www.youtube.com/results?search_query={encoded_query}"
    webbrowser.open(url)
    return f"Searching YouTube for: {query}"


def open_google():
    webbrowser.open("https://www.google.com")
    return "Opening Google"


def open_youtube():
    webbrowser.open("https://www.youtube.com")
    return "Opening YouTube"