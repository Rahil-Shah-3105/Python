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
import logging
logger = logging.getLogger(__name__)


def get_imdb_top_250_movies(url: str = "") -> dict[str, float]:
    logger.debug(">>> Entering get_imdb_top_250_movies(url=%s)", url)
    url = url or "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    logger.debug("get_imdb_top_250_movies(url=%s): url → %s", url, url)
    soup = BeautifulSoup(httpx.get(url, timeout=10).text, "html.parser")
    titles = soup.find_all("h3", class_="ipc-title__text")
    logger.debug("get_imdb_top_250_movies(url=%s): soup → %s", url, soup)
    logger.debug("get_imdb_top_250_movies(url=%s): titles → %s", url, titles)
    ratings = soup.find_all("span", class_="ipc-rating-star--rating")
    return {
        title.a.text: float(rating.strong.text)
        for title, rating in zip(titles, ratings)
    }
    logger.debug("<<< Exiting get_imdb_top_250_movies(url=%s)", url)


def write_movies(filename: str = "IMDb_Top_250_Movies.csv") -> None:
    logger.debug(">>> Entering write_movies(filename=%s)", filename)
    movies = get_imdb_top_250_movies()
    logger.debug("write_movies(filename=%s): movies → %s", filename, movies)
    with open(filename, "w", newline="") as out_file:
        writer = csv.writer(out_file)
        logger.error("Exception in write_movies(filename=%s)", filename, exc_info=True)
        logger.debug("write_movies(filename=%s): writer → %s", filename, writer)
        writer.writerow(["Movie title", "IMDb rating"])
        for title, rating in movies.items():
            writer.writerow([title, rating])
            logger.debug("<<< Exiting write_movies(filename=%s)", filename)


if __name__ == "__main__":
    write_movies()
