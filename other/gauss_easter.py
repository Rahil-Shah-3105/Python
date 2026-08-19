"""
https://en.wikipedia.org/wiki/Computus#Gauss'_Easter_algorithm
"""

import math
from datetime import UTC, datetime, timedelta
import logging
logger = logging.getLogger(__name__)


def gauss_easter(year: int) -> datetime:
    """
    Calculation Gregorian easter date for given year

    >>> gauss_easter(2007)
    datetime.datetime(2007, 4, 8, 0, 0, tzinfo=datetime.timezone.utc)

    >>> gauss_easter(2008)
    datetime.datetime(2008, 3, 23, 0, 0, tzinfo=datetime.timezone.utc)

    >>> gauss_easter(2020)
    datetime.datetime(2020, 4, 12, 0, 0, tzinfo=datetime.timezone.utc)

    >>> gauss_easter(2021)
    datetime.datetime(2021, 4, 4, 0, 0, tzinfo=datetime.timezone.utc)
    """
    logger.debug(">>> Entering gauss_easter(year=%s)", year)
    metonic_cycle = year % 19
    logger.debug("gauss_easter(year=%s): metonic_cycle → %s", year, metonic_cycle)
    julian_leap_year = year % 4
    logger.debug("gauss_easter(year=%s): julian_leap_year → %s", year, julian_leap_year)
    non_leap_year = year % 7
    logger.debug("gauss_easter(year=%s): non_leap_year → %s", year, non_leap_year)
    leap_day_inhibits = math.floor(year / 100)
    logger.debug("gauss_easter(year=%s): leap_day_inhibits → %s", year, leap_day_inhibits)
    lunar_orbit_correction = math.floor((13 + 8 * leap_day_inhibits) / 25)
    logger.debug("gauss_easter(year=%s): lunar_orbit_correction → %s", year, lunar_orbit_correction)
    leap_day_reinstall_number = leap_day_inhibits / 4
    logger.debug("gauss_easter(year=%s): leap_day_reinstall_number → %s", year, leap_day_reinstall_number)
    secular_moon_shift = (
        15 - lunar_orbit_correction + leap_day_inhibits - leap_day_reinstall_number
    ) % 30
    century_starting_point = (4 + leap_day_inhibits - leap_day_reinstall_number) % 7
    logger.debug("gauss_easter(year=%s): century_starting_point → %s", year, century_starting_point)

    # days to be added to March 21
    days_to_add = (19 * metonic_cycle + secular_moon_shift) % 30
    logger.debug("gauss_easter(year=%s): days_to_add → %s", year, days_to_add)

    # PHM -> Paschal Full Moon
    days_from_phm_to_sunday = (
        2 * julian_leap_year
        + 4 * non_leap_year
        + 6 * days_to_add
        + century_starting_point
    ) % 7

    if days_to_add == 29 and days_from_phm_to_sunday == 6:
        return datetime(year, 4, 19, tzinfo=UTC)
    elif days_to_add == 28 and days_from_phm_to_sunday == 6:
        logger.debug("gauss_easter(year=%s): days → %s", year, days)
        return datetime(year, 4, 18, tzinfo=UTC)
    else:
        logger.debug("<<< Exiting gauss_easter(year=%s)", year)
        return datetime(year, 3, 22, tzinfo=UTC) + timedelta(
            days=int(days_to_add + days_from_phm_to_sunday)
        )


if __name__ == "__main__":
    for year in (1994, 2000, 2010, 2021, 2023, 2032, 2100):
        tense = "will be" if year > datetime.now(tz=UTC).year else "was"
        print(f"Easter in {year} {tense} {gauss_easter(year)}")
