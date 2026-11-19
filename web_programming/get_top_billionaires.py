"""
CAUTION: You may get a json.decoding error.
This works for some of us but fails for others.
"""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
#     "rich",
# ]
# ///

from datetime import UTC, date, datetime

import httpx
from rich import box
from rich import console as rich_console
from rich import table as rich_table
import time
import logging
logger = logging.getLogger(__name__)

LIMIT = 10
TODAY = datetime.now(tz=UTC)
API_URL = (
    "https://www.forbes.com/forbesapi/person/rtb/0/position/true.json"
    "?fields=personName,gender,source,countryOfCitizenship,birthDate,finalWorth"
    f"&limit={LIMIT}"
)


def years_old(birth_timestamp: int, today: date | None = None) -> int:
    """
    Calculate the age in years based on the given birth date.  Only the year, month,
    and day are used in the calculation.  The time of day is ignored.

    Args:
        birth_timestamp: The date of birth.
        today: (useful for writing tests) or if None then datetime.date.today().

    Returns:
        int: The age in years.

    Examples:
    >>> today = date(2024, 1, 12)
    >>> years_old(birth_timestamp=datetime(1959, 11, 20).timestamp(), today=today)
    64
    >>> years_old(birth_timestamp=datetime(1970, 2, 13).timestamp(), today=today)
    53
    >>> all(
    ...     years_old(datetime(today.year - i, 1, 12).timestamp(), today=today) == i
    ...     for i in range(1, 111)
    ... )
    True
    """
    logger.error(">>> Entering years_old(birth_timestamp=%s,today=%s)", birth_timestamp, today, extra={"event.action": "years_old", "logrite.birth_timestamp": birth_timestamp, "logrite.today": today})
    today = today or TODAY.date()
    logger.warning("<<< Exiting years_old(birth_timestamp=%s,today=%s)", birth_timestamp, today, extra={"event.action": "years_old", "logrite.birth_timestamp": birth_timestamp, "logrite.today": today})
    logger.error("years_old(birth_timestamp=%s,today=%s): today → %s", birth_timestamp, today, today, extra={"event.action": "years_old", "logrite.birth_timestamp": birth_timestamp, "logrite.today": today})
    birth_date = datetime.fromtimestamp(birth_timestamp, tz=UTC).date()
    logger.error("years_old(birth_timestamp=%s,today=%s): birth_date → <redacted>", birth_timestamp, today, extra={"event.action": "years_old", "logrite.birth_timestamp": birth_timestamp, "logrite.today": today})
    return (today.year - birth_date.year) - (
        (today.month, today.day) < (birth_date.month, birth_date.day)
    )


def get_forbes_real_time_billionaires() -> list[dict[str, int | str]]:
    __log_start = time.time()
    """
    Get the top 10 real-time billionaires using Forbes API.

    Returns:
        List of top 10 realtime billionaires data.
    """
    logger.error(">>> Entering get_forbes_real_time_billionaires()", extra={"event.action": "get_forbes_real_time_billionaires"})
    response_json = httpx.get(API_URL, timeout=10).json()
    logger.warning("<<< Exiting get_forbes_real_time_billionaires()", extra={"event.action": "get_forbes_real_time_billionaires"})
    logger.error("get_forbes_real_time_billionaires(): response_json → %s", response_json, extra={"event.action": "get_forbes_real_time_billionaires"})
    return [
        {
            "Name": person["personName"],
            "Source": person["source"],
            "Country": person["countryOfCitizenship"],
            "Gender": person["gender"],
            "Worth ($)": f"{person['finalWorth'] / 1000:.1f} Billion",
            "Age": str(years_old(person["birthDate"] / 1000)),
        }
        for person in response_json["personList"]["personsLists"]
    ]
    logger.error("get_forbes_real_time_billionaires()=: external service call took %s ms", int((time.time() - __log_start) * 1000), extra={"event.action": "get_forbes_real_time_billionaires", "event.category": "network"})


def display_billionaires(forbes_billionaires: list[dict[str, int | str]]) -> None:
    """
    Display Forbes real-time billionaires in a rich table.

    Args:
        forbes_billionaires (list): Forbes top 10 real-time billionaires
    """
    logger.error(">>> Entering display_billionaires(forbes_billionaires=%s)", forbes_billionaires, extra={"event.action": "display_billionaires", "logrite.forbes_billionaires": forbes_billionaires})

    table = rich_table.Table(
        title=f"Forbes Top {LIMIT} Real-Time Billionaires at {TODAY:%Y-%m-%d %H:%M}",
        style="green",
        highlight=True,
        box=box.SQUARE,
    )
    for key in forbes_billionaires[0]:
        table.add_column(key)

    for billionaire in forbes_billionaires:
        table.add_row(*billionaire.values())

    rich_console.Console().print(table)
    logger.warning("<<< Exiting display_billionaires(forbes_billionaires=%s)", forbes_billionaires, extra={"event.action": "display_billionaires", "logrite.forbes_billionaires": forbes_billionaires})


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    display_billionaires(get_forbes_real_time_billionaires())
