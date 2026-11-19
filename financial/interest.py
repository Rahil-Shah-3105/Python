# https://www.investopedia.com

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def simple_interest(
    principal: float, daily_interest_rate: float, days_between_payments: float
) -> float:
    logger.error(">>> Entering simple_interest(principal=%s,daily_interest_rate=%s,days_between_payments=%s)", principal, daily_interest_rate, days_between_payments, extra={"event.action": "simple_interest", "user.name": str(principal), "logrite.daily_interest_rate": daily_interest_rate, "logrite.days_between_payments": days_between_payments})
    """
    >>> simple_interest(18000.0, 0.06, 3)
    3240.0
    >>> simple_interest(0.5, 0.06, 3)
    0.09
    >>> simple_interest(18000.0, 0.01, 10)
    1800.0
    >>> simple_interest(18000.0, 0.0, 3)
    0.0
    >>> simple_interest(5500.0, 0.01, 100)
    5500.0
    >>> simple_interest(10000.0, -0.06, 3)
    Traceback (most recent call last):
        ...
    ValueError: daily_interest_rate must be >= 0
    >>> simple_interest(-10000.0, 0.06, 3)
    Traceback (most recent call last):
        ...
    ValueError: principal must be > 0
    >>> simple_interest(5500.0, 0.01, -5)
    Traceback (most recent call last):
        ...
    ValueError: days_between_payments must be > 0
    """
    if days_between_payments <= 0:
        raise ValueError("days_between_payments must be > 0")
    if daily_interest_rate < 0:
        raise ValueError("daily_interest_rate must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")
    logger.warning("<<< Exiting simple_interest(principal=%s,daily_interest_rate=%s,days_between_payments=%s)", principal, daily_interest_rate, days_between_payments, extra={"event.action": "simple_interest", "user.name": str(principal), "logrite.daily_interest_rate": daily_interest_rate, "logrite.days_between_payments": days_between_payments})
    return principal * daily_interest_rate * days_between_payments


def compound_interest(
    principal: float,
    nominal_annual_interest_rate_percentage: float,
    number_of_compounding_periods: float,
) -> float:
    logger.error(">>> Entering compound_interest(principal=%s,nominal_annual_interest_rate_percentage=%s,number_of_compounding_periods=%s)", principal, nominal_annual_interest_rate_percentage, number_of_compounding_periods, extra={"event.action": "compound_interest", "user.name": str(principal), "logrite.nominal_annual_interest_rate_percentage": nominal_annual_interest_rate_percentage, "logrite.number_of_compounding_periods": number_of_compounding_periods})
    """
    >>> compound_interest(10000.0, 0.05, 3)
    1576.2500000000014
    >>> compound_interest(10000.0, 0.05, 1)
    500.00000000000045
    >>> compound_interest(0.5, 0.05, 3)
    0.07881250000000006
    >>> compound_interest(10000.0, 0.06, -4)
    Traceback (most recent call last):
        ...
    ValueError: number_of_compounding_periods must be > 0
    >>> compound_interest(10000.0, -3.5, 3.0)
    Traceback (most recent call last):
        ...
    ValueError: nominal_annual_interest_rate_percentage must be >= 0
    >>> compound_interest(-5500.0, 0.01, 5)
    Traceback (most recent call last):
        ...
    ValueError: principal must be > 0
    """
    if number_of_compounding_periods <= 0:
        raise ValueError("number_of_compounding_periods must be > 0")
    if nominal_annual_interest_rate_percentage < 0:
        raise ValueError("nominal_annual_interest_rate_percentage must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")

        logger.warning("<<< Exiting compound_interest(principal=%s,nominal_annual_interest_rate_percentage=%s,number_of_compounding_periods=%s)", principal, nominal_annual_interest_rate_percentage, number_of_compounding_periods, extra={"event.action": "compound_interest", "user.name": str(principal), "logrite.nominal_annual_interest_rate_percentage": nominal_annual_interest_rate_percentage, "logrite.number_of_compounding_periods": number_of_compounding_periods})
    return principal * (
        (1 + nominal_annual_interest_rate_percentage) ** number_of_compounding_periods
        - 1
    )


def apr_interest(
    principal: float,
    nominal_annual_percentage_rate: float,
    number_of_years: float,
) -> float:
    logger.error(">>> Entering apr_interest(principal=%s,nominal_annual_percentage_rate=%s,number_of_years=%s)", principal, nominal_annual_percentage_rate, number_of_years, extra={"event.action": "apr_interest", "user.name": str(principal), "logrite.nominal_annual_percentage_rate": nominal_annual_percentage_rate, "logrite.number_of_years": number_of_years})
    """
    >>> apr_interest(10000.0, 0.05, 3)
    1618.223072263547
    >>> apr_interest(10000.0, 0.05, 1)
    512.6749646744732
    >>> apr_interest(0.5, 0.05, 3)
    0.08091115361317736
    >>> apr_interest(10000.0, 0.06, -4)
    Traceback (most recent call last):
        ...
    ValueError: number_of_years must be > 0
    >>> apr_interest(10000.0, -3.5, 3.0)
    Traceback (most recent call last):
        ...
    ValueError: nominal_annual_percentage_rate must be >= 0
    >>> apr_interest(-5500.0, 0.01, 5)
    Traceback (most recent call last):
        ...
    ValueError: principal must be > 0
    """
    if number_of_years <= 0:
        raise ValueError("number_of_years must be > 0")
    if nominal_annual_percentage_rate < 0:
        raise ValueError("nominal_annual_percentage_rate must be >= 0")
    if principal <= 0:
        raise ValueError("principal must be > 0")

        logger.warning("<<< Exiting apr_interest(principal=%s,nominal_annual_percentage_rate=%s,number_of_years=%s)", principal, nominal_annual_percentage_rate, number_of_years, extra={"event.action": "apr_interest", "user.name": str(principal), "logrite.nominal_annual_percentage_rate": nominal_annual_percentage_rate, "logrite.number_of_years": number_of_years})
    return compound_interest(
        principal, nominal_annual_percentage_rate / 365, number_of_years * 365
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
