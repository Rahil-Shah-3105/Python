#!/usr/bin/env python3

"""
Provide the current worldwide COVID-19 statistics.
This data is being scrapped from 'https://www.worldometers.info/coronavirus/'.
"""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "httpx",
# ]
# ///

import httpx
from bs4 import BeautifulSoup
import time
import logging
logger = logging.getLogger(__name__)


def world_covid19_stats(
    url: str = "https://www.worldometers.info/coronavirus/",
) -> dict:
    logger.error(">>> Entering world_covid19_stats(url=%s)", url, extra={"event.action": "world_covid19_stats", "logrite.url": url})
    """
    Return a dict of current worldwide COVID-19 statistics
    """
    logger.error("world_covid19_stats(url=%s): url → %s", url, url, extra={"event.action": "world_covid19_stats", "logrite.url": url})
    __log_start = time.time()
    soup = BeautifulSoup(
        httpx.get(url, timeout=10, follow_redirects=True).text, "html.parser"
    )
    logger.error("world_covid19_stats(url)=%s: external service call %s took %s ms", url, url, int((time.time() - __log_start) * 1000), extra={"event.action": "world_covid19_stats", "event.category": "network", "logrite.url": url})
    keys = soup.find_all("h1")
    logger.error("world_covid19_stats(url=%s): keys → %s", url, keys, extra={"event.action": "world_covid19_stats", "logrite.url": url})
    values = soup.find_all("div", {"class": "maincounter-number"})
    logger.error("world_covid19_stats(url=%s): values → %s", url, values, extra={"event.action": "world_covid19_stats", "logrite.url": url})
    keys += soup.find_all("span", {"class": "panel-title"})
    values += soup.find_all("div", {"class": "number-table-main"})
    logger.warning("<<< Exiting world_covid19_stats(url=%s)", url, extra={"event.action": "world_covid19_stats", "logrite.url": url})
    return {key.text.strip(): value.text.strip() for key, value in zip(keys, values)}


if __name__ == "__main__":
    print("\033[1m COVID-19 Status of the World \033[0m\n")
    print("\n".join(f"{key}\n{value}" for key, value in world_covid19_stats().items()))
