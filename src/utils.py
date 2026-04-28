import re

def clean_text(text):
    """
    Converts text to lowercase and removes punctuation.
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text.split()

def count_urls(text):
    """
    Counts occurrences of URLs in the text.
    """
    url_pattern = r'(http[s]?://\S+|www\.\S+)'
    return len(re.findall(url_pattern, text))