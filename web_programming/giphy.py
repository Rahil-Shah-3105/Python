#!/usr/bin/env python3

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///

import httpx
import logging
logger = logging.getLogger(__name__)

giphy_api_key = "YOUR API KEY"
# Can be fetched from https://developers.giphy.com/dashboard/


def get_gifs(query: str, api_key: str = giphy_api_key) -> list:
    """
    Get a list of URLs of GIFs based on a given query..
    """
    logger.debug(">>> Entering get_gifs(query=%s,api_key=<redacted>)")
    import time; __log_start = time.time()
    formatted_query = "+".join(query.split())
    logger.debug("get_gifs(query=%s,api_key=<redacted>): formatted_query → %s", formatted_query)
    url = f"https://api.giphy.com/v1/gifs/search?q={formatted_query}&api_key={api_key}"
    logger.debug("get_gifs(query=%s,api_key=<redacted>): url → %s", url)
    gifs = httpx.get(url, timeout=10).json()["data"]
    logger.info("get_gifs(query=%s,api_key=<redacted>): url → %s", url)
    logger.info("get_gifs(query,api_key)=%s,<redacted>: external service call took %s ms", int((time.time() - __log_start) * 1000))
    logger.debug("get_gifs(query=%s,api_key=<redacted>): gifs → %s", gifs)
    logger.debug("<<< Exiting get_gifs(query=%s,api_key=<redacted>)")
    return [gif["url"] for gif in gifs]


if __name__ == "__main__":
    print("\n".join(get_gifs("space ship")))
