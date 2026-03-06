from lxml import html
import re
from urllib.parse import urljoin


def extract_links(html_string: str, base_url: str) -> list[dict]:
    parser = html.HTMLParser(recover=True, encoding='utf-8')
    if not html_string:
        return []
    tree = html.fromstring(html_string, parser=parser)
    links = tree.xpath("//a[@href and @href != \"#\" and @href != \"\"]")

    unique_urls = set()
    for link in links:
        url = link.xpath("@href")[0]
        pattern = r"^https://[a-zA-Z0-9-]+\.[a-z]{2,}"
        if not re.match(pattern, url):
            url = urljoin(base_url, url)
            text = " ".join(link.text_content().split()
                            ) if link.text_content() else ""
        url_formed = (url, text)
        unique_urls.add(url_formed)

    linklist = [{"url": url_formed[0], "text": url_formed[1]}
                for url_formed in unique_urls]
    return linklist


def main():
    pass


if __name__ == "__main__":
    main()
