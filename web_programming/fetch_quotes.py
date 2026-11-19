"""
This file fetches quotes from the " ZenQuotes API ".
It does not require any API key as it uses free tier.

For more details and premium features visit:
    https://zenquotes.io/
"""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///

import pprint

import httpx
import time
import logging
logger = logging.getLogger(__name__)

API_ENDPOINT_URL = "https://zenquotes.io/api"


def quote_of_the_day() -> list:
    logger.error(">>> Entering quote_of_the_day()", extra={"event.action": "quote_of_the_day"})
    __log_start = time.time()
    logger.warning("<<< Exiting quote_of_the_day()", extra={"event.action": "quote_of_the_day"})
    logger.error("quote_of_the_day()=: external service call took %s ms", int((time.time() - __log_start) * 1000), extra={"event.action": "quote_of_the_day", "event.category": "network"})
    return httpx.get(API_ENDPOINT_URL + "/today", timeout=10).json()


def random_quotes() -> list:
    logger.error(">>> Entering random_quotes()", extra={"event.action": "random_quotes"})
    __log_start = time.time()
    logger.warning("<<< Exiting random_quotes()", extra={"event.action": "random_quotes"})
    logger.error("random_quotes()=: external service call took %s ms", int((time.time() - __log_start) * 1000), extra={"event.action": "random_quotes", "event.category": "network"})
    return httpx.get(API_ENDPOINT_URL + "/random", timeout=10).json()


if __name__ == "__main__":
    """
    response object has all the info with the quote
    To retrieve the actual quote access the response.json() object as below
    response.json() is a list of json object
        response.json()[0]['q'] = actual quote.
        response.json()[0]['a'] = author name.
        response.json()[0]['h'] = in html format.
    """
    response = random_quotes()
    pprint.pprint(response)
