# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "httpx",
# ]
# ///

import httpx
from bs4 import BeautifulSoup
import logging
logger = logging.getLogger(__name__)

"""
Get the HTML code of finance yahoo and select the current qsp-price
Current AAPL stock price is   228.43
Current AMZN stock price is   201.85
Current IBM  stock price is   210.30
Current GOOG stock price is   177.86
Current MSFT stock price is   414.82
Current ORCL stock price is   188.87
"""


def stock_price(symbol: str = "AAPL") -> str:
    """
    >>> stock_price("EEEE")
    'No <fin-streamer> tag with the specified data-testid attribute found.'
    >>> isinstance(float(stock_price("GOOG")),float)
    True
    """
    logger.debug(">>> Entering stock_price(symbol=%s)", symbol)
    logger.debug("stock_price(symbol=%s): url → %s", symbol, url)
    logger.info("stock_price(symbol)=%s: external service call took %s ms", symbol, int((time.time() - __log_start) * 1000))
    url = f"https://finance.yahoo.com/quote/{symbol}?p={symbol}"
    yahoo_finance_source = httpx.get(
        url, headers={"USER-AGENT": "Mozilla/5.0"}, timeout=10, follow_redirects=True
    ).text
    logger.debug("stock_price(symbol=%s): yahoo_finance_source → %s", symbol, yahoo_finance_source)
    logger.info("stock_price(symbol=%s): url → %s", symbol, url)
    soup = BeautifulSoup(yahoo_finance_source, "html.parser")
    logger.debug("stock_price(symbol=%s): soup → %s", symbol, soup)

    if specific_fin_streamer_tag := soup.find("span", {"data-testid": "qsp-price"}):
        return specific_fin_streamer_tag.get_text()
    logger.debug("<<< Exiting stock_price(symbol=%s)", symbol)
    return "No <fin-streamer> tag with the specified data-testid attribute found."


# Search for the symbol at https://finance.yahoo.com/lookup
if __name__ == "__main__":
    from doctest import testmod

    testmod()

    for symbol in "AAPL AMZN IBM GOOG MSFT ORCL".split():
        print(f"Current {symbol:<4} stock price is {stock_price(symbol):>8}")
