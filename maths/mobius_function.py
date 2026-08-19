"""
References: https://en.wikipedia.org/wiki/M%C3%B6bius_function
References: wikipedia:square free number
psf/black : True
ruff : True
"""

from maths.is_square_free import is_square_free
from maths.prime_factors import prime_factors
import logging
logger = logging.getLogger(__name__)


def mobius(n: int) -> int:
    """
    Mobius function
    >>> mobius(24)
    0
    >>> mobius(-1)
    1
    >>> mobius('asd')
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'str'
    >>> mobius(10**400)
    0
    >>> mobius(10**-400)
    1
    >>> mobius(-1424)
    1
    >>> mobius([1, '2', 2.0])
    Traceback (most recent call last):
        ...
    TypeError: '<=' not supported between instances of 'int' and 'list'
    """
    logger.debug(">>> Entering mobius(n=%s)", n)
    factors = prime_factors(n)
    logger.debug("mobius(n=%s): factors → %s", n, factors)
    if is_square_free(factors):
        return -1 if len(factors) % 2 else 1
    logger.debug("<<< Exiting mobius(n=%s)", n)
    return 0


if __name__ == "__main__":
    import doctest

    doctest.testmod()
