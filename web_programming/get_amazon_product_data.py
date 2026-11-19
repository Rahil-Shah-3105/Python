"""
This file provides a function which will take a product name as input from the user,
and fetch from Amazon information about products of this name or category.  The product
information will include title, URL, price, ratings, and the discount available.
"""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "httpx",
#     "pandas",
# ]
# ///

from itertools import zip_longest

import httpx
from bs4 import BeautifulSoup
from pandas import DataFrame
import time
import logging
logger = logging.getLogger(__name__)


def get_amazon_product_data(product: str = "laptop") -> DataFrame:
    """
    Take a product name or category as input and return product information from Amazon
    including title, URL, price, ratings, and the discount available.
    """
    logger.error(">>> Entering get_amazon_product_data(product=%s)", product, extra={"event.action": "get_amazon_product_data", "logrite.product": product})
    url = f"https://www.amazon.in/laptop/s?k={product}"
    logger.error("get_amazon_product_data(product=%s): url → %s", product, url, extra={"event.action": "get_amazon_product_data", "logrite.product": product})
    header = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
            "(KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36"
        ),
        "Accept-Language": "en-US, en;q=0.5",
    }
    __log_start = time.time()
    soup = BeautifulSoup(
        httpx.get(url, headers=header, timeout=10).text, features="lxml"
    )
    logger.error("get_amazon_product_data(product)=%s: external service call took %s ms", product, int((time.time() - __log_start) * 1000), extra={"event.action": "get_amazon_product_data", "event.category": "network", "logrite.product": product})
    # Initialize a Pandas dataframe with the column titles
    data_frame = DataFrame(
        columns=[
            "Product Title",
            "Product Link",
            "Current Price of the product",
            "Product Rating",
            "MRP of the product",
            "Discount",
        ]
    )
    logger.error("get_amazon_product_data(product=%s): data_frame → %s", product, data_frame, extra={"event.action": "get_amazon_product_data", "logrite.product": product})
    # Loop through each entry and store them in the dataframe
    for item, _ in zip_longest(
        soup.find_all(
            "div",
            attrs={"class": "s-result-item", "data-component-type": "s-search-result"},
        ),
        soup.find_all("div", attrs={"class": "a-row a-size-base a-color-base"}),
    ):
        try:
            product_title = item.h2.text
            product_link = "https://www.amazon.in/" + item.h2.a["href"]
            logger.error("get_amazon_product_data(product=%s): product_link → %s", product, product_link, extra={"event.action": "get_amazon_product_data", "logrite.product": product})
            logger.error("get_amazon_product_data(product=%s): attrs → %s", product, attrs, extra={"event.action": "get_amazon_product_data", "logrite.product": product})
            product_price = item.find("span", attrs={"class": "a-offscreen"}).text
            try:
                logger.error("get_amazon_product_data(product=%s): product_price → %s", product, product_price, extra={"event.action": "get_amazon_product_data", "logrite.product": product})
                product_rating = item.find("span", attrs={"class": "a-icon-alt"}).text
            except AttributeError:
                logger.error("Exception in get_amazon_product_data(product=%s)", product, exc_info=True, extra={"event.action": "get_amazon_product_data", "event.category": "process", "logrite.product": product})
                product_rating = "Not available"
                logger.error("get_amazon_product_data(product=%s): product_rating → %s", product, product_rating, extra={"event.action": "get_amazon_product_data", "logrite.product": product})
            try:
                product_mrp = (
                    "₹"
                    + item.find(
                        "span", attrs={"class": "a-price a-text-price"}
                    ).text.split("₹")[1]
                )
            except AttributeError:
                product_mrp = ""
                logger.error("get_amazon_product_data(product=%s): product_mrp → %s", product, product_mrp, extra={"event.action": "get_amazon_product_data", "logrite.product": product})
            try:
                discount = float(
                    (
                        (
                            float(product_mrp.strip("₹").replace(",", ""))
                            - float(product_price.strip("₹").replace(",", ""))
                        )
                        / float(product_mrp.strip("₹").replace(",", ""))
                    )
                    * 100
                )
            except ValueError:
                discount = float("nan")
        except AttributeError:
            continue
        data_frame.loc[str(len(data_frame.index))] = [
            product_title,
            product_link,
            product_price,
            product_rating,
            product_mrp,
            discount,
        ]
    data_frame.loc[
        data_frame["Current Price of the product"] > data_frame["MRP of the product"],
        "MRP of the product",
    ] = " "
    data_frame.loc[
        data_frame["Current Price of the product"] > data_frame["MRP of the product"],
        "Discount",
    ] = " "
    data_frame.index += 1
    logger.warning("<<< Exiting get_amazon_product_data(product=%s)", product, extra={"event.action": "get_amazon_product_data", "logrite.product": product})
    return data_frame


if __name__ == "__main__":
    product = "headphones"
    get_amazon_product_data(product).to_csv(f"Amazon Product Data for {product}.csv")
