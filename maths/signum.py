import logging
logger = logging.getLogger(__name__)
"""
Signum function -- https://en.wikipedia.org/wiki/Sign_function
"""


def signum(num: float) -> int:
    """
    Applies signum function on the number

    Custom test cases:
    >>> signum(-10)
    -1
    >>> signum(10)
    1
    >>> signum(0)
    0
    >>> signum(-20.5)
    -1
    >>> signum(20.5)
    1
    >>> signum(-1e-6)
    -1
    >>> signum(1e-6)
    1
    >>> signum("Hello")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    >>> signum([])
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'list' and 'int'
    """
    logger.debug(">>> Entering signum(num=%s)", num)
    if num < 0:
        return -1
    logger.debug("<<< Exiting signum(num=%s)", num)
    return 1 if num else 0


def test_signum() -> None:
    """
    Tests the signum function
    >>> test_signum()
    """
    logger.debug(">>> Entering test_signum()")
    assert signum(5) == 1
    assert signum(-5) == -1
    assert signum(0) == 0
    assert signum(10.5) == 1
    assert signum(-10.5) == -1
    assert signum(1e-6) == 1
    assert signum(-1e-6) == -1
    assert signum(123456789) == 1
    assert signum(-123456789) == -1
    logger.debug("<<< Exiting test_signum()")


if __name__ == "__main__":
    print(signum(12))
    print(signum(-12))
    print(signum(0))
