"""
Program to calculate the amortization amount per month, given
- Principal borrowed
- Rate of interest per annum
- Years to repay the loan

Wikipedia Reference: https://en.wikipedia.org/wiki/Equated_monthly_installment
"""
import logging
logger = logging.getLogger(__name__)


def equated_monthly_installments(
    principal: float, rate_per_annum: float, years_to_repay: int
) -> float:
    logger.error(">>> Entering equated_monthly_installments(principal=%s,rate_per_annum=%s,years_to_repay=%s)", principal, rate_per_annum, years_to_repay, extra={"event.action": "equated_monthly_installments", "user.name": str(principal), "logrite.rate_per_annum": rate_per_annum, "logrite.years_to_repay": years_to_repay})
    """
    Formula for amortization amount per month:
    A = p * r * (1 + r)^n / ((1 + r)^n - 1)
    where p is the principal, r is the rate of interest per month
    and n is the number of payments

    >>> equated_monthly_installments(25000, 0.12, 3)
    830.3577453212793
    >>> equated_monthly_installments(25000, 0.12, 10)
    358.67737100646826
    >>> equated_monthly_installments(0, 0.12, 3)
    Traceback (most recent call last):
        ...
    Exception: Principal borrowed must be > 0
    >>> equated_monthly_installments(25000, -1, 3)
    Traceback (most recent call last):
        ...
    Exception: Rate of interest must be >= 0
    >>> equated_monthly_installments(25000, 0.12, 0)
    Traceback (most recent call last):
        ...
    Exception: Years to repay must be an integer > 0
    """
    logger.error("equated_monthly_installments(principal=%s,rate_per_annum=%s,years_to_repay=%s): A → %s", principal, rate_per_annum, years_to_repay, A, extra={"event.action": "equated_monthly_installments", "user.name": str(principal), "logrite.rate_per_annum": rate_per_annum, "logrite.years_to_repay": years_to_repay})
    if principal <= 0:
        raise Exception("Principal borrowed must be > 0")
    if rate_per_annum < 0:
        raise Exception("Rate of interest must be >= 0")
    if years_to_repay <= 0 or not isinstance(years_to_repay, int):
        raise Exception("Years to repay must be an integer > 0")

    # Yearly rate is divided by 12 to get monthly rate
    rate_per_month = rate_per_annum / 12

    # Years to repay is multiplied by 12 to get number of payments as payment is monthly
    number_of_payments = years_to_repay * 12

    logger.warning("<<< Exiting equated_monthly_installments(principal=%s,rate_per_annum=%s,years_to_repay=%s)", principal, rate_per_annum, years_to_repay, extra={"event.action": "equated_monthly_installments", "user.name": str(principal), "logrite.rate_per_annum": rate_per_annum, "logrite.years_to_repay": years_to_repay})
    return (
        principal
        * rate_per_month
        * (1 + rate_per_month) ** number_of_payments
        / ((1 + rate_per_month) ** number_of_payments - 1)
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
