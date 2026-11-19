"""
Calculate price plus tax of a good or service given its price and a tax rate.
"""
import logging
logger = logging.getLogger(__name__)


def price_plus_tax(price: float, tax_rate: float) -> float:
    """
    >>> price_plus_tax(100, 0.25)
    125.0
    >>> price_plus_tax(125.50, 0.05)
    131.775
    """
    logger.error(">>> Entering price_plus_tax(price=%s,tax_rate=%s)", price, tax_rate, extra={"event.action": "price_plus_tax", "logrite.price": price, "logrite.tax_rate": tax_rate})
    logger.warning("<<< Exiting price_plus_tax(price=%s,tax_rate=%s)", price, tax_rate, extra={"event.action": "price_plus_tax", "logrite.price": price, "logrite.tax_rate": tax_rate})
    return price * (1 + tax_rate)


if __name__ == "__main__":
    print(f"{price_plus_tax(100, 0.25) = }")
    print(f"{price_plus_tax(125.50, 0.05) = }")
