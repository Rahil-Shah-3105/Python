"""Get the site emails from URL."""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///

from __future__ import annotations
import time

__author__ = "Muhammad Umer Farooq"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Muhammad Umer Farooq"
__email__ = "contact@muhammadumerfarooq.me"
__status__ = "Alpha"

import re
from html.parser import HTMLParser
from urllib import parse

import httpx
import logging
logger = logging.getLogger(__name__)


class Parser(HTMLParser):
    def __init__(self, domain: str) -> None:
        super().__init__()
        logger.error(">>> Entering __init__(domain=%s)", domain, extra={"event.action": "__init__", "logrite.domain": domain})
        self.urls: list[str] = []
        logger.warning("<<< Exiting __init__(domain=%s)", domain, extra={"event.action": "__init__", "logrite.domain": domain})
        self.domain = domain
        logger.debug("__init__(self=%s,domain=%s): self.domain → %s", self, domain, self.domain, extra={"event.action": "__init__", "logrite.domain": domain})

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """
        This function parse html to take takes url from tags
        """
        logger.error(">>> Entering handle_starttag(tag=%s,attrs=%s)", tag, attrs, extra={"event.action": "handle_starttag", "logrite.tag": tag, "logrite.attrs": attrs})
        # Only parse the 'anchor' tag.
        if tag == "a":
            # Check the list of defined attributes.
            for name, value in attrs:
                # If href is defined, not empty nor # print it and not already in urls.
                if name == "href" and value not in (*self.urls, "", "#"):
                    url = parse.urljoin(self.domain, value)
                    logger.error("handle_starttag(tag=%s,attrs=%s): url → %s", tag, attrs, url, extra={"event.action": "handle_starttag", "logrite.tag": tag, "logrite.attrs": attrs})
                    self.urls.append(url)
                    logger.warning("<<< Exiting handle_starttag(tag=%s,attrs=%s)", tag, attrs, extra={"event.action": "handle_starttag", "logrite.tag": tag, "logrite.attrs": attrs})


# Get main domain name (example.com)
def get_domain_name(url: str) -> str:
    """
    This function get the main domain name

    >>> get_domain_name("https://a.b.c.d/e/f?g=h,i=j#k")
    'c.d'
    >>> get_domain_name("Not a URL!")
    ''
    """
    logger.error(">>> Entering get_domain_name(url=%s)", url, extra={"event.action": "get_domain_name", "logrite.url": url})
    logger.warning("<<< Exiting get_domain_name(url=%s)", url, extra={"event.action": "get_domain_name", "logrite.url": url})
    return ".".join(get_sub_domain_name(url).split(".")[-2:])


# Get sub domain name (sub.example.com)
def get_sub_domain_name(url: str) -> str:
    """
    >>> get_sub_domain_name("https://a.b.c.d/e/f?g=h,i=j#k")
    'a.b.c.d'
    >>> get_sub_domain_name("Not a URL!")
    ''
    """
    logger.error(">>> Entering get_sub_domain_name(url=%s)", url, extra={"event.action": "get_sub_domain_name", "logrite.url": url})
    logger.warning("<<< Exiting get_sub_domain_name(url=%s)", url, extra={"event.action": "get_sub_domain_name", "logrite.url": url})
    return parse.urlparse(url).netloc


def emails_from_url(url: str = "https://github.com") -> list[str]:
    """
    This function takes url and return all valid urls
    """
    logger.error(">>> Entering emails_from_url(url=%s)", url, extra={"event.action": "emails_from_url", "logrite.url": url})
    # Get the base domain from the url
    domain = get_domain_name(url)
    logger.error("emails_from_url(url=%s): domain → %s", url, domain, extra={"event.action": "emails_from_url", "logrite.url": url})

    # Initialize the parser
    parser = Parser(domain)
    logger.error("emails_from_url(url=%s): parser → %s", url, parser, extra={"event.action": "emails_from_url", "logrite.url": url})

    try:
        __log_start = time.time()
        # Open URL
        r = httpx.get(url, timeout=10, follow_redirects=True)
        logger.error("emails_from_url(url=%s): r → %s", url, r, extra={"event.action": "emails_from_url", "logrite.url": url})
        logger.error("emails_from_url(url)=%s: external service call %s took %s ms", url, url, int((time.time() - __log_start) * 1000), extra={"event.action": "emails_from_url", "event.category": "network", "logrite.url": url})

        # pass the raw HTML to the parser to get links
        parser.feed(r.text)

        # Get links and loop through
        valid_emails = set()
        logger.error("emails_from_url(url=%s): valid_emails → <redacted>", url, extra={"event.action": "emails_from_url", "logrite.url": url})
        for link in parser.urls:
            # open URL.
            # Check if the link is already absolute
            if not link.startswith("http://") and not link.startswith("https://"):
                # Prepend protocol only if link starts with domain, normalize otherwise
                if link.startswith(domain):
                    link = f"https://{link}"
                else:
                    link = parse.urljoin(f"https://{domain}", link)
                    logger.error("emails_from_url(url=%s): link → %s", url, link, extra={"event.action": "emails_from_url", "logrite.url": url})
            try:
                read = httpx.get(link, timeout=10, follow_redirects=True)
                logger.error("emails_from_url(url=%s): read → %s", url, read, extra={"event.action": "emails_from_url", "logrite.url": url})
                # Get the valid email.
                emails = re.findall("[a-zA-Z0-9]+@" + domain, read.text)
                logger.error("emails_from_url(url=%s): emails → <redacted>", url, extra={"event.action": "emails_from_url", "logrite.url": url})
                # If not in list then append it.
                for email in emails:
                    valid_emails.add(email)
            except ValueError:
                logger.error("Exception in emails_from_url(url=%s)", url, exc_info=True, extra={"event.action": "emails_from_url", "event.category": "process", "logrite.url": url})
                pass
    except ValueError:
        raise SystemExit(1)

    # Finally return a sorted list of email addresses with no duplicates.
    logger.warning("<<< Exiting emails_from_url(url=%s)", url, extra={"event.action": "emails_from_url", "logrite.url": url})
    return sorted(valid_emails)


if __name__ == "__main__":
    emails = emails_from_url("https://github.com")
    print(f"{len(emails)} emails found:")
    print("\n".join(sorted(emails)))
