from decimal import Decimal, getcontext
from math import ceil, factorial
import logging
logger = logging.getLogger(__name__)


def pi(precision: int) -> str:
    """
    The Chudnovsky algorithm is a fast method for calculating the digits of PI,
    based on Ramanujan's PI formulae.

    https://en.wikipedia.org/wiki/Chudnovsky_algorithm

    PI = constant_term / ((multinomial_term * linear_term) / exponential_term)
        where constant_term = 426880 * sqrt(10005)

    The linear_term and the exponential_term can be defined iteratively as follows:
        L_k+1 = L_k + 545140134            where L_0 = 13591409
        X_k+1 = X_k * -262537412640768000  where X_0 = 1

    The multinomial_term is defined as follows:
        6k! / ((3k)! * (k!) ^ 3)
            where k is the k_th iteration.

    This algorithm correctly calculates around 14 digits of PI per iteration

    >>> pi(10)
    '3.14159265'
    >>> pi(100)
    '3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706'
    >>> pi('hello')
    Traceback (most recent call last):
        ...
    TypeError: Undefined for non-integers
    >>> pi(-1)
    Traceback (most recent call last):
        ...
    ValueError: Undefined for non-natural numbers
    """
    logger.debug(">>> Entering pi(precision=%s)", precision)
    logger.debug("pi(precision=%s): PI → %s", precision, PI)

    if not isinstance(precision, int):
        raise TypeError("Undefined for non-integers")
    elif precision < 1:
        raise ValueError("Undefined for non-natural numbers")

    getcontext().prec = precision
    num_iterations = ceil(precision / 14)
    logger.debug("pi(precision=%s): num_iterations → %s", precision, num_iterations)
    constant_term = 426880 * Decimal(10005).sqrt()
    logger.debug("pi(precision=%s): constant_term → %s", precision, constant_term)
    exponential_term = 1
    logger.debug("pi(precision=%s): exponential_term → %s", precision, exponential_term)
    linear_term = 13591409
    logger.debug("pi(precision=%s): linear_term → %s", precision, linear_term)
    partial_sum = Decimal(linear_term)
    logger.debug("pi(precision=%s): partial_sum → %s", precision, partial_sum)
    for k in range(1, num_iterations):
        multinomial_term = factorial(6 * k) // (factorial(3 * k) * factorial(k) ** 3)
        logger.debug("pi(precision=%s): multinomial_term → %s", precision, multinomial_term)
        linear_term += 545140134
        exponential_term *= -262537412640768000
        partial_sum += Decimal(multinomial_term * linear_term) / exponential_term
    logger.debug("<<< Exiting pi(precision=%s)", precision)
    return str(constant_term / partial_sum)[:-1]


if __name__ == "__main__":
    n = 50
    print(f"The first {n} digits of pi is: {pi(n)}")
