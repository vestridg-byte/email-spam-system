from src.email_message import EmailMessage
from src.spam_filter import SpamFilter


def test_spam_score_high():
    message = EmailMessage(
        sender="winner@promo-deals.com",
        subject="FREE PRIZE!!!",
        body="CLICK NOW!!! Visit http://spam.com to claim your money",
        label="spam"
    )
    message.preprocess()

    spam_filter = SpamFilter()
    score = spam_filter.calculate_risk_score(message)
    assert score >= 10


def test_classification_not_spam():
    spam_filter = SpamFilter()
    assert spam_filter.classify_score(2) == "not spam"
