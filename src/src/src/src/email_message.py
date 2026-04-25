from src.utils import clean_text


class EmailMessage:
    """Represents a single email message and its processed content."""

    def __init__(self, sender, subject, body, label="unknown"):
        """Initialize an EmailMessage object with basic email fields."""
        self.sender = sender
        self.subject = subject
        self.body = body
        self.label = label
        self.cleaned_text = ""
        self.tokens = []

    def preprocess(self):
        """Clean and tokenize the combined subject and body text."""
        combined_text = f"{self.subject} {self.body}"
        self.cleaned_text = clean_text(combined_text)
        self.tokens = self.cleaned_text.split()

    def __str__(self):
        """Return a readable summary of the email."""
        return f"Email from {self.sender} | Subject: {self.subject} | Label: {self.label}"

    def __len__(self):
        """Return the number of processed tokens in the email."""
        return len(self.tokens)
