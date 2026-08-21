"""
Get CO2 emission data from the UK CarbonIntensity API
"""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
# ]
# ///

from datetime import date

import httpx
import logging
logger = logging.getLogger(__name__)

BASE_URL = "https://api.carbonintensity.org.uk/intensity"


# Emission in the last half hour
def fetch_last_half_hour() -> str:
    logger.debug(">>> Entering fetch_last_half_hour()")
    import time; __log_start = time.time()
    last_half_hour = httpx.get(BASE_URL, timeout=10).json()["data"][0]
    logger.info("fetch_last_half_hour()=: external service call took %s ms", int((time.time() - __log_start) * 1000))
    logger.debug("fetch_last_half_hour(): last_half_hour → %s", last_half_hour)
    logger.debug("<<< Exiting fetch_last_half_hour()")
    return last_half_hour["intensity"]["actual"]


# Emissions in a specific date range
def fetch_from_to(start, end) -> list:
    logger.debug(">>> Entering fetch_from_to(start=%s,end=%s)", start, end)
    import time; __log_start = time.time()
    logger.debug("<<< Exiting fetch_from_to(start=%s,end=%s)", start, end)
    logger.info("fetch_from_to(start,end)=%s,%s: external service call took %s ms", start, end, int((time.time() - __log_start) * 1000))
    return httpx.get(f"{BASE_URL}/{start}/{end}", timeout=10).json()["data"]


if __name__ == "__main__":
    for entry in fetch_from_to(start=date(2020, 10, 1), end=date(2020, 10, 3)):
        print("from {from} to {to}: {intensity[actual]}".format(**entry))
    print(f"{fetch_last_half_hour() = }")
