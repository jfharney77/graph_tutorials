"""Simple URL scraper

Provides `url_scraper(url: str) -> str` which fetches the given URL
and returns the page content (HTML) as a string.
"""
from typing import Any, List
import requests
from bs4 import BeautifulSoup, NavigableString, Tag


def url_scraper(url: str, timeout: float = 10.0) -> str:
    """Fetch `url` and return the response text.

    Raises requests.HTTPError on non-2xx responses and requests.RequestException
    for network-related errors.
    """
    headers = {"User-Agent": "Mozilla/5.0 (compatible; scraper/1.0)"}
    resp = requests.get(url, timeout=timeout, headers=headers)
    resp.raise_for_status()
    return resp.text


def find_compatibility2(html_content: str) -> List[str]:
    """Find all list items located between a header 'Compatibility' and the next
    header 'Reviews' in the provided HTML content.

    Returns a list of strings for each list item found (from any `ul` or `ol`).
    The search is case-insensitive for header text.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    products: List[str] = []

    # Find all header tags (h1..h6) and check for 'Compatibility'
    for level in range(1, 7):
        for header in soup.find_all(f"h{level}"):
            if header.get_text(strip=True).lower() == "compatibility":
                # Iterate forward in document order until a header with text 'Reviews'
                node = header.find_next()
                while node:
                    if isinstance(node, Tag):
                        # stop when we reach the Reviews header
                        if node.name and node.name.startswith("h") and node.get_text(strip=True).lower() == "reviews":
                            break

                        # when we find a list, collect its list items
                        if node.name in ("ul", "ol"):
                            for li in node.find_all("li"):
                                text = li.get_text(" ", strip=True)
                                if text:
                                    products.append(text)
                    node = node.find_next()

    return products


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python src/scraper.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        content = url_scraper(url)
        print(content)
        print('-' * 10)
        comp = find_compatibility2(content)
        print(comp)
        print('-' * 10)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        sys.exit(2)
