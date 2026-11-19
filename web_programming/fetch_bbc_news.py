# Created by sarathkaul on 12/11/19

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///

import httpx
import time
import logging
logger = logging.getLogger(__name__)

_NEWS_API = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey="


def fetch_bbc_news(bbc_news_api_key: str) -> None:
    logger.error(">>> Entering fetch_bbc_news(bbc_news_api_key=<redacted>)", extra={"event.action": "fetch_bbc_news"})
    __log_start = time.time()
    # fetching a list of articles in json format
    bbc_news_page = httpx.get(_NEWS_API + bbc_news_api_key, timeout=10).json()
    logger.error("fetch_bbc_news(bbc_news_api_key=<redacted>): bbc_news_page → %s", bbc_news_page, extra={"event.action": "fetch_bbc_news"})
    logger.error("fetch_bbc_news(bbc_news_api_key)=<redacted>: external service call took %s ms", int((time.time() - __log_start) * 1000), extra={"event.action": "fetch_bbc_news", "event.category": "network"})
    # each article in the list is a dict
    for i, article in enumerate(bbc_news_page["articles"], 1):
        print(f"{i}.) {article['title']}")
        logger.warning("<<< Exiting fetch_bbc_news(bbc_news_api_key=<redacted>)", extra={"event.action": "fetch_bbc_news"})


if __name__ == "__main__":
    fetch_bbc_news(bbc_news_api_key="<Your BBC News API key goes here>")
