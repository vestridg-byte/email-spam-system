from src.email_message import EmailMessage


def test_email_len_operator():
    email = EmailMessage(
        sender="test@test.com",
        subject="Hello",
        body="World",
        label="not spam"
    )
    assert len(email) == len("Hello World")


def test_email_equality_operator():
    email1 = EmailMessage("a@test.com", "Hi", "Body")
    email2 = EmailMessage("a@test.com", "Hi", "Different Body")
    email3 = EmailMessage("b@test.com", "Hi", "Body")

    assert email1 == email2
    assert email1 != email3