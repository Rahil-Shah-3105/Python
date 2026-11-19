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


def get_apod_data(api_key: str) -> dict:
    """
    Get the APOD(Astronomical Picture of the day) data
    Get your API Key from: https://api.nasa.gov/
    """
    logger.error(">>> Entering get_apod_data(api_key=<redacted>)", extra={"event.action": "get_apod_data"})
    __log_start = time.time()
    url = "https://api.nasa.gov/planetary/apod"
    logger.warning("<<< Exiting get_apod_data(api_key=<redacted>)", extra={"event.action": "get_apod_data"})
    logger.error("get_apod_data(api_key=<redacted>): url → %s", url, extra={"event.action": "get_apod_data"})
    logger.error("get_apod_data(api_key)=<redacted>: external service call took %s ms", int((time.time() - __log_start) * 1000), extra={"event.action": "get_apod_data", "event.category": "network"})
    return httpx.get(url, params={"api_key": api_key}, timeout=10).json()


def save_apod(api_key: str, path: str = ".") -> dict:
    logger.error(">>> Entering save_apod(api_key=<redacted>,path=%s)", path, extra={"event.action": "save_apod", "logrite.path": path})
    apod_data = get_apod_data(api_key)
    logger.error("save_apod(api_key=<redacted>,path=%s): apod_data → %s", path, apod_data, extra={"event.action": "save_apod", "logrite.path": path})
    img_url = apod_data["url"]
    img_name = img_url.split("/")[-1]
    logger.error("save_apod(api_key=<redacted>,path=%s): img_url → %s", path, img_url, extra={"event.action": "save_apod", "logrite.path": path})
    logger.error("save_apod(api_key=<redacted>,path=%s): img_name → %s", path, img_name, extra={"event.action": "save_apod", "logrite.path": path})
    response = httpx.get(img_url, timeout=10)

    logger.error("save_apod(api_key=<redacted>,path=%s): response → %s", path, response, extra={"event.action": "save_apod", "logrite.path": path})
    with open(f"{path}/{img_name}", "wb+") as img_file:
        img_file.write(response.content)
    del response
    logger.warning("<<< Exiting save_apod(api_key=<redacted>,path=%s)", path, extra={"event.action": "save_apod", "logrite.path": path})
    return apod_data


def get_archive_data(query: str) -> dict:
    """
    Get the data of a particular query from NASA archives
    """
    logger.error(">>> Entering get_archive_data(query=%s)", extra={"event.action": "get_archive_data", "logrite.query": query})
    url = "https://images-api.nasa.gov/search"
    logger.warning("<<< Exiting get_archive_data(query=%s)", extra={"event.action": "get_archive_data", "logrite.query": query})
    logger.error("get_archive_data(query=%s): url → %s", url, extra={"event.action": "get_archive_data", "logrite.query": query})
    return httpx.get(url, params={"q": query}, timeout=10).json()


if __name__ == "__main__":
    print(save_apod("YOUR API KEY"))
    apollo_2011_items = get_archive_data("apollo 2011")["collection"]["items"]
    print(apollo_2011_items[0]["data"][0]["description"])
