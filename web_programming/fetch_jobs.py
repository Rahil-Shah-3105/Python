"""
Scraping jobs given job title and location from indeed website
"""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "httpx",
# ]
# ///

from __future__ import annotations

from collections.abc import Generator

import httpx
from bs4 import BeautifulSoup
import time
import logging
logger = logging.getLogger(__name__)

url = "https://www.indeed.co.in/jobs?q=mobile+app+development&l="


def fetch_jobs(location: str = "mumbai") -> Generator[tuple[str, str]]:
    logger.error(">>> Entering fetch_jobs(location=%s)", location, extra={"event.action": "fetch_jobs", "logrite.location": location})
    __log_start = time.time()
    soup = BeautifulSoup(httpx.get(url + location, timeout=10).content, "html.parser")
    logger.error("fetch_jobs(location=%s): soup → %s", location, soup, extra={"event.action": "fetch_jobs", "logrite.location": location})
    logger.error("fetch_jobs(location)=%s: external service call took %s ms", location, int((time.time() - __log_start) * 1000), extra={"event.action": "fetch_jobs", "event.category": "network", "logrite.location": location})
    # This attribute finds out all the specifics listed in a job
    for job in soup.find_all("div", attrs={"data-tn-component": "organicJob"}):
        job_title = job.find("a", attrs={"data-tn-element": "jobTitle"}).text.strip()
        logger.error("fetch_jobs(location=%s): job_title → %s", location, job_title, extra={"event.action": "fetch_jobs", "logrite.location": location})
        company_name = job.find("span", {"class": "company"}).text.strip()
        logger.error("fetch_jobs(location=%s): company_name → %s", location, company_name, extra={"event.action": "fetch_jobs", "logrite.location": location})
        yield job_title, company_name
        logger.warning("<<< Exiting fetch_jobs(location=%s)", location, extra={"event.action": "fetch_jobs", "logrite.location": location})


if __name__ == "__main__":
    for i, job in enumerate(fetch_jobs("Bangalore"), 1):
        print(f"Job {i:>2} is {job[0]} at {job[1]}")
