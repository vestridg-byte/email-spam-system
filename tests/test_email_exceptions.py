import pytest
from src.email_message import EmailMessage


def test_empty_email_raises_value_error():
    with pytest.raises(ValueError):
        EmailMessage(sender="", subject="Hi", body="Hello")