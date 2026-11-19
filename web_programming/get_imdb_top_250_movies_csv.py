# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "httpx",
# ]
# ///

from __future__ import annotations

import csv

import httpx
from bs4 import BeautifulSoup
import time
import logging
logger = logging.getLogger(__name__)


def get_imdb_top_250_movies(url: str = "") -> dict[str, float]:
    logger.error(">>> Entering get_imdb_top_250_movies(url=%s)", url, extra={"event.action": "get_imdb_top_250_movies", "logrite.url": url})
    __log_start = time.time()
    url = url or "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    logger.error("get_imdb_top_250_movies(url=%s): url → %s", url, url, extra={"event.action": "get_imdb_top_250_movies", "logrite.url": url})
    soup = BeautifulSoup(httpx.get(url, timeout=10).text, "html.parser")
    logger.error("get_imdb_top_250_movies(url=%s): soup → %s", url, soup, extra={"event.action": "get_imdb_top_250_movies", "logrite.url": url})
    titles = soup.find_all("h3", class_="ipc-title__text")
    logger.error("get_imdb_top_250_movies(url)=%s: external service call %s took %s ms", url, url, int((time.time() - __log_start) * 1000), extra={"event.action": "get_imdb_top_250_movies", "event.category": "network", "logrite.url": url})
    logger.error("get_imdb_top_250_movies(url=%s): titles → %s", url, titles, extra={"event.action": "get_imdb_top_250_movies", "logrite.url": url})
    ratings = soup.find_all("span", class_="ipc-rating-star--rating")
    return {
        title.a.text: float(rating.strong.text)
        for title, rating in zip(titles, ratings)
    }
    logger.warning("<<< Exiting get_imdb_top_250_movies(url=%s)", url, extra={"event.action": "get_imdb_top_250_movies", "logrite.url": url})
    logger.error("get_imdb_top_250_movies(url=%s): ratings → %s", url, ratings, extra={"event.action": "get_imdb_top_250_movies", "logrite.url": url})


def write_movies(filename: str = "IMDb_Top_250_Movies.csv") -> None:
    logger.error(">>> Entering write_movies(filename=%s)", filename, extra={"event.action": "write_movies", "logrite.filename": filename})
    movies = get_imdb_top_250_movies()
    logger.error("write_movies(filename=%s): movies → %s", filename, movies, extra={"event.action": "write_movies", "logrite.filename": filename})
    with open(filename, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        logger.error("write_movies(filename=%s): writer → %s", filename, writer, extra={"event.action": "write_movies", "logrite.filename": filename})
        writer.writerow(["Movie title", "IMDb rating"])
        for title, rating in movies.items():
            writer.writerow([title, rating])
            logger.warning("<<< Exiting write_movies(filename=%s)", filename, extra={"event.action": "write_movies", "logrite.filename": filename})


if __name__ == "__main__":
    write_movies()
