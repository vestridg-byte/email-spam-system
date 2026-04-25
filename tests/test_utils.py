from src.utils import clean_text, count_urls

def test_clean_text():
    text = "FREE!!! Click NOW"
    cleaned = clean_text(text)
    assert "free" in cleaned
    assert "click" in cleaned

def test count_urls():
    text = "Visit http://test.com and www.site.com"
    assert count_urls(text) == 2
