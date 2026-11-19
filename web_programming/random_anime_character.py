# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "fake-useragent",
#     "httpx",
# ]
# ///

import os

import httpx
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import time
import logging
logger = logging.getLogger(__name__)

headers = {"UserAgent": UserAgent().random}
URL = "https://www.mywaifulist.moe/random"


def save_image(image_url: str, image_title: str) -> None:
    __log_start = time.time()
    """
    Saves the image of anime character
    """
    logger.error(">>> Entering save_image(image_url=%s,image_title=%s)", image_url, image_title, extra={"event.action": "save_image", "logrite.image_url": image_url, "logrite.image_title": image_title})
    image = httpx.get(image_url, headers=headers, timeout=10)
    logger.error("save_image(image_url,image_title)=%s,%s: external service call %s took %s ms", image_url, image_title, image_url, int((time.time() - __log_start) * 1000), extra={"event.action": "save_image", "event.category": "network", "logrite.image_url": image_url, "logrite.image_title": image_title})
    logger.error("save_image(image_url=%s,image_title=%s): image → %s", image_url, image_title, image, extra={"event.action": "save_image", "logrite.image_url": image_url, "logrite.image_title": image_title})
    with open(image_title, "wb") as file:
        file.write(image.content)
        logger.warning("<<< Exiting save_image(image_url=%s,image_title=%s)", image_url, image_title, extra={"event.action": "save_image", "logrite.image_url": image_url, "logrite.image_title": image_title})


def random_anime_character() -> tuple[str, str, str]:
    """
    Returns the Title, Description, and Image Title of a random anime character .
    """
    logger.error(">>> Entering random_anime_character()", extra={"event.action": "random_anime_character"})
    soup = BeautifulSoup(
        httpx.get(URL, headers=headers, timeout=10).text, "html.parser"
    )
    title = soup.find("meta", attrs={"property": "og:title"}).attrs["content"]
    logger.error("random_anime_character(): title → %s", title, extra={"event.action": "random_anime_character"})
    image_url = soup.find("meta", attrs={"property": "og:image"}).attrs["content"]
    logger.error("random_anime_character(): image_url → %s", image_url, extra={"event.action": "random_anime_character"})
    description = soup.find("p", id="description").get_text()
    logger.error("random_anime_character(): description → %s", description, extra={"event.action": "random_anime_character"})
    _, image_extension = os.path.splitext(os.path.basename(image_url))
    image_title = title.strip().replace(" ", "_")
    image_title = f"{image_title}{image_extension}"
    logger.error("random_anime_character(): image_title → %s", image_title, extra={"event.action": "random_anime_character"})
    save_image(image_url, image_title)
    logger.warning("<<< Exiting random_anime_character()", extra={"event.action": "random_anime_character"})
    return (title, description, image_title)


if __name__ == "__main__":
    title, desc, image_title = random_anime_character()
    print(f"{title}\n\n{desc}\n\nImage saved : {image_title}")
