"""Get the site emails from URL."""
from __future__ import annotations

import re
from html.parser import HTMLParser
from urllib import parse

import requests
from typing import Set, List

__author__ = "Muhammad Umer Farooq"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Muhammad Umer Farooq"
__email__ = "contact@muhammadumerfarooq.me"
__status__ = "Alpha"


class Parser(HTMLParser):
    def __init__(self, domain: str) -> None:
        super().__init__()
        self.urls: list[str] = []
        self.domain = domain

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """
        This function parse html to take takes url from tags
        """
        # Only parse the 'anchor' tag.
        if tag == "a":
            # Check the list of defined attributes.
            for name, value in attrs:
                # If href is defined, and not empty nor # print it.
                if name == "href" and value != "#" and value != "":
                    # If not already in urls.
                    if value not in self.urls:
                        url = parse.urljoin(self.domain, value)
                        self.urls.append(url)


# Get main domain name (example.com)
def get_domain_name(url: str) -> str:
    """
    This function get the main domain name

    >>> get_domain_name("https://a.b.c.d/e/f?g=h,i=j#k")
    'c.d'
    >>> get_domain_name("Not a URL!")
    ''
    """
    return ".".join(get_sub_domain_name(url).split(".")[-2:])


# Get sub domain name (sub.example.com)
def get_sub_domain_name(url: str) -> str:
    """
    >>> get_sub_domain_name("https://a.b.c.d/e/f?g=h,i=j#k")
    'a.b.c.d'
    >>> get_sub_domain_name("Not a URL!")
    ''
    """
    return parse.urlparse(url).netloc


def emails_from_url(url: str = "https://github.com") -> List[str]:
    """
    Extracts all valid email addresses from a given url and all of its accessible subpages
    that belong to the same domain.

    Args:
    url (str): The url to extract the email addresses from.
              If not provided, 'https://github.com' is used by default.

    Raises:
    SystemExit: If the passed URL is not valid.

    Returns:
    list[str]: A list of valid email addresses found, sorted in lexicographical order.
              The return list contains no duplicates.
    """
    # Get the base domain from the url
    domain = get_domain_name(url)

    # Initialize the parser
    parser = Parser(domain)

    # retrieve and parse the HTML content
    try:
        parser_content = requests.get(url).text
        parser.feed(parser_content)
    except ValueError:
        raise SystemExit(1)

    # Extract emails from the pages
    valid_emails = set()
    for link in parser.urls:
        emails = get_page_emails(link, domain)
        valid_emails.update(emails)

    return sorted(valid_emails)


if __name__ == "__main__":
    emails = emails_from_url("https://github.com")
    print(f"{len(emails)} emails found:")
    print("\n".join(sorted(emails)))



def get_page_emails(link: str, domain: str) -> Set[str]:
    """
    Extracts valid email addresses from a given webpage.

    Args:
    link (str): The url of the webpage.
    domain (str): The domain name.

    Returns:
    set[str]: A set of valid email addresses found on the webpage.
    """
    try:
        page_content = requests.get(link).text
    except ValueError:
        return set()

    return extract_emails(page_content, domain)


def extract_emails(content: str, domain: str) -> Set[str]:
    """
    Extracts valid email addresses from a text content.

    Args:
    content (str): The text(content of a webpage) to extract the email addresses from.
    domain (str): The domain name.

    Returns:
    set[str]: A set of valid email addresses found in the content.
    """
    emails = re.findall("[a-zA-Z0-9]+@" + domain, content)
    return set(emails)
