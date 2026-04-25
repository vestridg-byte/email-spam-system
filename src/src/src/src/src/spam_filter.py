import pandas as pd

from src.email_message import EmailMessage
from src.utils import (
    count_urls,
    count_exclamations,
    count_all_caps_words,
    count_spam_keywords,
    suspicious_sender,
)
from src.custom_exceptions import DatasetFileError, DatasetColumnError


class SpamFilter:
    """Loads email data, computes risk scores, and classifies emails."""

    REQUIRED_COLUMNS = {"sender", "subject", "body", "label"}

    def __init__(self, threshold_spam=10, threshold_suspicious=5):
        """Initialize thresholds and storage for the spam filter."""
        self.threshold_spam = threshold_spam
        self.threshold_suspicious = threshold_suspicious
        self.dataset = None
        self.messages = []

    def load_data(self, filepath):
        """Load the email dataset from a CSV file and validate columns."""
        try:
            df = pd.read_csv(filepath)
        except FileNotFoundError as exc:
            raise DatasetFileError(f"Dataset file not found: {filepath}") from exc

        if not self.REQUIRED_COLUMNS.issubset(df.columns):
            missing = self.REQUIRED_COLUMNS - set(df.columns)
            raise DatasetColumnError(f"Missing required columns: {missing}")

        self.dataset = df
        return df

    def build_messages(self):
        """Convert dataset rows into EmailMessage objects."""
        self.messages = []

        for _, row in self.dataset.iterrows():
            message = EmailMessage(
                row["sender"],
                row["subject"],
                row["body"],
                row["label"]
            )
            message.preprocess()
            self.messages.append(message)

    def calculate_risk_score(self, message):
        """Calculate a weighted risk score for an email message."""
        keyword_count = min(count_spam_keywords(message.tokens), 5)
        url_count = min(count_urls(message.cleaned_text), 3)
        exclamation_count = min(count_exclamations(message.body), 5)
        caps_count = min(count_all_caps_words(message.body), 3)
        sender_flag = suspicious_sender(message.sender)

        score = (
            2 * keyword_count
            + 3 * url_count
            + 1 * exclamation_count
            + 2 * caps_count
            + 2 * sender_flag
        )
        return score

    def classify_score(self, score):
        """Classify a score as not spam, suspicious, or spam."""
        if score >= self.threshold_spam:
            return "spam"
        if score >= self.threshold_suspicious:
            return "suspicious"
        return "not spam"

    def predict_all(self):
        """Predict classes and scores for all messages in the dataset."""
        results = []

        for message in self.messages:
            score = self.calculate_risk_score(message)
            prediction = self.classify_score(score)

            results.append({
                "sender": message.sender,
                "subject": message.subject,
                "actual_label": message.label,
                "risk_score": score,
                "prediction": prediction,
            })

        return pd.DataFrame(results)
