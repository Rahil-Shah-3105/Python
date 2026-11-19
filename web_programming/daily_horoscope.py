# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "beautifulsoup4",
#     "httpx",
# ]
# ///

import httpx
from bs4 import BeautifulSoup
import time
import logging
logger = logging.getLogger(__name__)


def horoscope(zodiac_sign: int, day: str) -> str:
    logger.error(">>> Entering horoscope(zodiac_sign=%s,day=%s)", zodiac_sign, day, extra={"event.action": "horoscope", "logrite.zodiac_sign": zodiac_sign, "logrite.day": day})
    __log_start = time.time()
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    logger.error("horoscope(zodiac_sign,day)=%s,%s: external service call took %s ms", zodiac_sign, day, int((time.time() - __log_start) * 1000), extra={"event.action": "horoscope", "event.category": "network", "logrite.zodiac_sign": zodiac_sign, "logrite.day": day})
    soup = BeautifulSoup(httpx.get(url, timeout=10).content, "html.parser")
    logger.error("horoscope(zodiac_sign=%s,day=%s): soup → %s", zodiac_sign, day, soup, extra={"event.action": "horoscope", "logrite.zodiac_sign": zodiac_sign, "logrite.day": day})
    logger.warning("<<< Exiting horoscope(zodiac_sign=%s,day=%s)", zodiac_sign, day, extra={"event.action": "horoscope", "logrite.zodiac_sign": zodiac_sign, "logrite.day": day})
    return soup.find("div", class_="main-horoscope").p.text


if __name__ == "__main__":
    print("Daily Horoscope. \n")
    print(
        "enter your Zodiac sign number:\n",
        "1. Aries\n",
        "2. Taurus\n",
        "3. Gemini\n",
        "4. Cancer\n",
        "5. Leo\n",
        "6. Virgo\n",
        "7. Libra\n",
        "8. Scorpio\n",
        "9. Sagittarius\n",
        "10. Capricorn\n",
        "11. Aquarius\n",
        "12. Pisces\n",
    )
    zodiac_sign = int(input("number> ").strip())
    print("choose some day:\n", "yesterday\n", "today\n", "tomorrow\n")
    day = input("enter the day> ")
    horoscope_text = horoscope(zodiac_sign, day)
    print(horoscope_text)
