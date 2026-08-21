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
import logging
logger = logging.getLogger(__name__)

headers = {"UserAgent": UserAgent().random}
URL = "https://www.mywaifulist.moe/random"


def save_image(image_url: str, image_title: str) -> None:
    """
    Saves the image of anime character
    """
    logger.debug(">>> Entering save_image(image_url=%s,image_title=%s)", image_url, image_title)
    logger.info("save_image(image_url,image_title)=%s,%s: external service call %s took %s ms", image_url, image_title, image_url, int((time.time() - __log_start) * 1000))
    image = httpx.get(image_url, headers=headers, timeout=10)
    logger.debug("save_image(image_url=%s,image_title=%s): image → %s", image_url, image_title, image)
    with open(image_title, "wb") as file:
        file.write(image.content)
        logger.error("Exception in save_image(image_url=%s,image_title=%s)", image_url, image_title, exc_info=True)

        logger.debug("<<< Exiting save_image(image_url=%s,image_title=%s)", image_url, image_title)

def random_anime_character() -> tuple[str, str, str]:
    """
    Returns the Title, Description, and Image Title of a random anime character .
    """
    logger.debug(">>> Entering random_anime_character()")
    logger.info("random_anime_character()=: external service call took %s ms", int((time.time() - __log_start) * 1000))
    soup = BeautifulSoup(
        httpx.get(URL, headers=headers, timeout=10).text, "html.parser"
    )
    title = soup.find("meta", attrs={"property": "og:title"}).attrs["content"]
    logger.debug("random_anime_character(): title → %s", title)
    image_url = soup.find("meta", attrs={"property": "og:image"}).attrs["content"]
    logger.debug("random_anime_character(): image_url → %s", image_url)
    description = soup.find("p", id="description").get_text()
    _, image_extension = os.path.splitext(os.path.basename(image_url))
    logger.debug("random_anime_character(): description → %s", description)
    image_title = title.strip().replace(" ", "_")
    image_title = f"{image_title}{image_extension}"
    logger.debug("random_anime_character(): image_title → %s", image_title)
    save_image(image_url, image_title)
    logger.debug("<<< Exiting random_anime_character()")
    return (title, description, image_title)


if __name__ == "__main__":
    title, desc, image_title = random_anime_character()
    print(f"{title}\n\n{desc}\n\nImage saved : {image_title}")
