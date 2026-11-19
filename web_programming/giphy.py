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
    logger.error(">>> Entering get_gifs(query=%s,api_key=<redacted>)", extra={"event.action": "get_gifs", "logrite.query": query})
    formatted_query = "+".join(query.split())
    logger.warning("<<< Exiting get_gifs(query=%s,api_key=<redacted>)", query, extra={"event.action": "get_gifs", "logrite.query": query})
    logger.error("get_gifs(query=%s,api_key=<redacted>): formatted_query → %s", query, formatted_query, extra={"event.action": "get_gifs", "logrite.query": query})
    url = f"https://api.giphy.com/v1/gifs/search?q={formatted_query}&api_key={api_key}"
    gifs = httpx.get(url, timeout=10).json()["data"]
    logger.error("get_gifs(query=%s,api_key=<redacted>): url → %s", query, url, extra={"event.action": "get_gifs", "logrite.query": query})
    logger.error("get_gifs(query=%s,api_key=<redacted>): gifs → %s", query, gifs, extra={"event.action": "get_gifs", "logrite.query": query})
    return [gif["url"] for gif in gifs]


if __name__ == "__main__":
    print("\n".join(get_gifs("space ship")))
