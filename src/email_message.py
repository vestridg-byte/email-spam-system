from src.utils import clean_text


class EmailMessage:
    """
    Represents a single email message.
    """

    def __init__(self, sender, subject, body, label=None):
        if not sender or not subject or not body:
            raise ValueError("Email must contain sender, subject, and body.")

        self.sender = sender
        self.subject = subject
        self.body = body
        self.label = label
        self.cleaned_words = None

    def full_text(self):
        """
        Returns combined subject and body text.
        """
        return f"{self.subject} {self.body}"

    def preprocess(self):
        """
        Cleans and tokenizes the email text.
        """
        self.cleaned_words = clean_text(self.full_text())
        return self.cleaned_words

    def __len__(self):
        """
        Returns total length of email text.
        """
        return len(self.full_text())

    def __eq__(self, other):
        """
        Compares two EmailMessage objects by sender and subject.
        """
        if not isinstance(other, EmailMessage):
            return False
        return self.sender == other.sender and self.subject == other.subject

    def __str__(self):
        return f"Email from {self.sender}: {self.subject}"