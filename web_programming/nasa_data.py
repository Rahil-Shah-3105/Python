# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///

import httpx
import logging
logger = logging.getLogger(__name__)


def get_apod_data(api_key: str) -> dict:
    """
    Get the APOD(Astronomical Picture of the day) data
    Get your API Key from: https://api.nasa.gov/
    """
    logger.debug(">>> Entering get_apod_data(api_key=<redacted>)")
    logger.debug("get_apod_data(api_key=<redacted>): url → %s", url)
    logger.info("get_apod_data(api_key)=<redacted>: external service call took %s ms", int((time.time() - __log_start) * 1000))
    url = "https://api.nasa.gov/planetary/apod"
    logger.info("get_apod_data(api_key=<redacted>): url → %s", url)
    logger.debug("<<< Exiting get_apod_data(api_key=<redacted>)")
    return httpx.get(url, params={"api_key": api_key}, timeout=10).json()


def save_apod(api_key: str, path: str = ".") -> dict:
    apod_data = get_apod_data(api_key)
    logger.debug(">>> Entering save_apod(api_key=<redacted>,path=%s)", path)
    logger.debug("save_apod(api_key=<redacted>,path=%s): apod_data → %s", path, apod_data)
    img_url = apod_data["url"]
    logger.debug("save_apod(api_key=<redacted>,path=%s): img_url → %s", path, img_url)
    img_name = img_url.split("/")[-1]
    response = httpx.get(img_url, timeout=10)

    logger.debug("save_apod(api_key=<redacted>,path=%s): img_name → %s", path, img_name)
    with open(f"{path}/{img_name}", "wb+") as img_file:
        img_file.write(response.content)
    del response
    logger.info("save_apod(api_key,path)=<redacted>,%s: external service call took %s ms", path, int((time.time() - __log_start) * 1000))
    logger.debug("save_apod(api_key=<redacted>,path=%s): response → %s", path, response)
    logger.error("Exception in save_apod(api_key=<redacted>,path=%s)", path, exc_info=True)
    logger.debug("<<< Exiting save_apod(api_key=<redacted>,path=%s)", path)
    return apod_data


def get_archive_data(query: str) -> dict:
    """
    Get the data of a particular query from NASA archives
    """
    logger.debug(">>> Entering get_archive_data(query=%s)")
    logger.debug("get_archive_data(query=%s): url → %s", url)
    logger.info("get_archive_data(query)=%s: external service call took %s ms", int((time.time() - __log_start) * 1000))
    url = "https://images-api.nasa.gov/search"
    logger.info("get_archive_data(query=%s): url → %s", url)
    logger.debug("<<< Exiting get_archive_data(query=%s)")
    return httpx.get(url, params={"q": query}, timeout=10).json()


if __name__ == "__main__":
    print(save_apod("YOUR API KEY"))
    apollo_2011_items = get_archive_data("apollo 2011")["collection"]["items"]
    print(apollo_2011_items[0]["data"][0]["description"])
