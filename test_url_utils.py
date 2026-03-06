import pytest

from url_utils import validate_url, normalize_url


@pytest.mark.parametrize("url, expected", [
    ("example.com", "https://example.com"),
    ("https://a.com", "https://a.com"),
])
def test_normalize_url_correct(url, expected):
    assert normalize_url(url) == expected


@pytest.mark.parametrize("url", [
    "  ",
    None
])
def test_normalize_url_exception(url):
    with pytest.raises(ValueError, match="Your URL is empty"):
        normalize_url(url)


@pytest.mark.parametrize("url, expected", [
    ("https://example.com", True),
    ("http://example.com/test/12test", True),

    ("ftp://files.com", False),
    ("https://localhost", False),
    ("https://127.0.0.1", False),
    ("https://127.0.0.1:8080", False),
    ("https://"+"abc"*1000+".com", False),
])
def test_validate_url(url, expected):
    is_valid, _ = validate_url(url)
    assert is_valid == expected
