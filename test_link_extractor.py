import pytest

from link_extractor import extract_links


@pytest.mark.parametrize("html_string, base_url, expected", [
    # пустые href, относительная ссылка превращается в абсолютную
    ('<div><a href="one">One</a></div><a href="#"></a><a href=""></a>', 'https://example.com',
     [{"url": "https://example.com/one", "text": "One"}]),

    # битый html
    ('<a href="/page">Link</a><div>Unclosed', 'https://example.com',
     [{"url": "https://example.com/page", "text": "Link"}]),

    # дубликаты отфильтрованы
    ('<div><a href="one">One</a></div><a href="one">One</a><a href=""></a>', 'https://example.com',
     [{"url": "https://example.com/one", "text": "One"}]),

    # пустой html
    ('', 'https://example.com',
     []),
])
def test_extract_links(html_string, base_url, expected):
    assert extract_links(html_string, base_url) == expected
