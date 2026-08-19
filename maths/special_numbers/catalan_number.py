import logging
logger = logging.getLogger(__name__)
"""

Calculate the nth Catalan number

Source:
    https://en.wikipedia.org/wiki/Catalan_number

"""


def catalan(number: int) -> int:
    """
    :param number: nth catalan number to calculate
    :return: the nth catalan number
    Note: A catalan number is only defined for positive integers

    >>> catalan(5)
    14
    >>> catalan(0)
    Traceback (most recent call last):
        ...
    ValueError: Input value of [number=0] must be > 0
    >>> catalan(-1)
    Traceback (most recent call last):
        ...
    ValueError: Input value of [number=-1] must be > 0
    >>> catalan(5.0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=5.0] must be an integer
    """
    logger.debug(">>> Entering catalan(number=%s)", number)

    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        logger.debug("catalan(number=%s): msg → %s", number, msg)
        raise TypeError(msg)

    if number < 1:
        msg = f"Input value of [number={number}] must be > 0"
        raise ValueError(msg)

    current_number = 1
    logger.debug("catalan(number=%s): current_number → %s", number, current_number)

    for i in range(1, number):
        current_number *= 4 * i - 2
        current_number //= i + 1

    logger.debug("<<< Exiting catalan(number=%s)", number)
    return current_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
