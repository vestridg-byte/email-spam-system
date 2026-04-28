import pandas as pd
from src.utils import clean_text, count_urls
from src.email_message import EmailMessage


class SpamFilter:
    """
    Rule-based spam filter using weighted scoring.
    """

    def __init__(self):
        self.spam_keywords = ["free", "money", "prize", "winner", "click"]
        self.messages = []
        self.df = None

    def load_data(self, filepath):
        """
        Loads dataset from CSV file.
        Raises FileNotFoundError if file missing.
        Raises ValueError if required columns missing.
        """
        try:
            df = pd.read_csv(filepath)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filepath}' not found.")

        required_columns = {"sender", "subject", "body", "label"}
        if not required_columns.issubset(df.columns):
            raise ValueError("Dataset missing required columns.")

        self.df = df
        return df

    def build_messages(self):
        """
        Builds EmailMessage objects from dataframe.
        """
        self.messages = []

        for _, row in self.df.iterrows():
            message = EmailMessage(
                sender=row["sender"],
                subject=row["subject"],
                body=row["body"],
                label=row["label"],
            )
            message.preprocess()
            self.messages.append(message)

    def calculate_risk_score(self, email):
        """
        Calculates spam risk score based on weighted rules.
        """
        text = email.full_text()
        cleaned_words = email.cleaned_words or clean_text(text)

        spam_keyword_count = sum(
            word in set(self.spam_keywords) for word in cleaned_words
        )

        url_count = count_urls(text)
        exclamation_count = text.count("!")
        all_caps_word_count = sum(word.isupper() for word in text.split())
        suspicious_sender_flag = 1 if "promo" in email.sender else 0

        score = (
            2 * spam_keyword_count
            + 3 * url_count
            + 1 * exclamation_count
            + 2 * all_caps_word_count
            + 2 * suspicious_sender_flag
        )

        return score

    def classify_score(self, score):
        """
        Classifies email based on score thresholds.
        """
        if score < 5:
            return "not spam"
        elif 5 <= score <= 9:
            return "suspicious"
        else:
            return "spam"

    def predict_all(self):
        """
        Predicts labels for all built messages.
        """
        predictions = []

        for index, message in enumerate(self.messages):
            score = self.calculate_risk_score(message)
            prediction = self.classify_score(score)

            predictions.append(
                {
                    "index": index,
                    "sender": message.sender,
                    "actual_label": message.label,
                    "prediction": prediction,
                    "score": score,
                }
            )

        return pd.DataFrame(predictions)