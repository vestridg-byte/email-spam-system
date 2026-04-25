import re

SPAM_KEYWORDS = {
    "free", "winner", "won", "award", "prize", "reward", "claim",
    "urgent", "limited", "offer", "click", "verify", "confirm",
    "money", "cash", "credit", "loan", "refund",
    "inheritance", "beneficiary", "transfer", "donation"
}


def clean_text(text):
    """Clean text by converting it to lowercase and removing extra spaces."""
    if not isinstance(text, str):
        raise ValueError("Input text must be a string.")

    text = text.lower()
    text = re.sub(r"[^a-z0-9\s:/!.]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def count_urls(text):
    """Count URLs in a text string."""
    return len(re.findall(r"http[s]?://|www\.", text.lower()))


def count_exclamations(text):
    """Count exclamation marks in a text string."""
    return text.count("!")


def count_all_caps_words(text):
    """Count words written in all capital letters."""
    words = re.findall(r"\b[A-Z]{2,}\b", text)
    return len(words)


def count_spam_keywords(tokens):
    """Count how many tokens are found in the spam keyword set."""
    return sum(1 for token in tokens if token in SPAM_KEYWORDS)


def suspicious_sender(sender):
    """Return 1 if sender appears suspicious, otherwise 0."""
    sender = sender.lower()
    suspicious_words = [
        "promo", "offer", "winner", "lottery", "deal",
        "claim", "prize", "cash", "loan", "bonus"
    ]
    return 1 if any(word in sender for word in suspicious_words) else 0


def evaluate_predictions(actual, predicted):
    """Compute classification accuracy."""
    if len(actual) != len(predicted):
        raise ValueError("Actual and predicted lists must have the same length.")

    correct = sum(1 for a, p in zip(actual, predicted) if a == p)
    return correct / len(actual) if actual else 0.0
