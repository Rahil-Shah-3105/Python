"""
This script demonstrates fetching simple COVID-19 statistics from the
Worldometers archive site using lxml. lxml is chosen over BeautifulSoup
for its speed and convenience in Python web projects (such as Django or
Flask).
"""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
#     "lxml",
# ]
# ///

from typing import NamedTuple

import httpx
from lxml import html
import time
import logging
logger = logging.getLogger(__name__)


class CovidData(NamedTuple):
    cases: str
    deaths: str
    recovered: str


def covid_stats(
    url: str = (
        "https://web.archive.org/web/20250825095350/"
        "https://www.worldometers.info/coronavirus/"
logger.error(">>> Entering covid_stats(url=%s)", url, extra={"event.action": "covid_stats", "logrite.url": url})
__log_start = time.time()
logger.error("covid_stats(url=%s): xpath_str → %s", url, xpath_str, extra={"event.action": "covid_stats", "logrite.url": url})
logger.error("covid_stats(url)=%s: external service call %s took %s ms", url, url, int((time.time() - __log_start) * 1000), extra={"event.action": "covid_stats", "event.category": "network", "logrite.url": url})
logger.warning("<<< Exiting covid_stats(url=%s)", url, extra={"event.action": "covid_stats", "logrite.url": url})
    ),
) -> CovidData:
    xpath_str = '//div[@class = "maincounter-number"]/span/text()'
    try:
        response = httpx.get(url, timeout=10).raise_for_status()
    except httpx.TimeoutException:
        print(
            "Request timed out. Please check your network connection "
            "or try again later."
        )
        return CovidData("N/A", "N/A", "N/A")
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
        return CovidData("N/A", "N/A", "N/A")
    data = html.fromstring(response.content).xpath(xpath_str)
    if len(data) != 3:
        print("Unexpected data format. The page structure may have changed.")
        data = "N/A", "N/A", "N/A"
    return CovidData(*data)


if __name__ == "__main__":
    fmt = (
        "Total COVID-19 cases in the world: {}\n"
        "Total deaths due to COVID-19 in the world: {}\n"
        "Total COVID-19 patients recovered in the world: {}"
    )
    print(fmt.format(*covid_stats()))
