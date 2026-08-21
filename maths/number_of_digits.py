import math
from timeit import timeit
import logging
logger = logging.getLogger(__name__)


def num_digits(n: int) -> int:
    """
    Find the number of digits in a number.

    >>> num_digits(12345)
    5
    >>> num_digits(123)
    3
    >>> num_digits(0)
    1
    >>> num_digits(-1)
    1
    >>> num_digits(-123456)
    6
    >>> num_digits('123')  # Raises a TypeError for non-integer input
    Traceback (most recent call last):
        ...
    TypeError: Input must be an integer
    """
    logger.debug(">>> Entering num_digits(n=%s)", n)

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    digits = 0
    logger.debug("num_digits(n=%s): digits → %s", n, digits)
    n = abs(n)
    while True:
        n = n // 10
        digits += 1
        if n == 0:
            break
    logger.debug("<<< Exiting num_digits(n=%s)", n)
    return digits


def num_digits_fast(n: int) -> int:
    """
    Find the number of digits in a number.
    abs() is used as logarithm for negative numbers is not defined.

    >>> num_digits_fast(12345)
    5
    >>> num_digits_fast(123)
    3
    >>> num_digits_fast(0)
    1
    >>> num_digits_fast(-1)
    1
    >>> num_digits_fast(-123456)
    6
    >>> num_digits('123')  # Raises a TypeError for non-integer input
    Traceback (most recent call last):
        ...
    TypeError: Input must be an integer
    """
    logger.debug(">>> Entering num_digits_fast(n=%s)", n)

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    logger.debug("<<< Exiting num_digits_fast(n=%s)", n)
    return 1 if n == 0 else math.floor(math.log(abs(n), 10) + 1)


def num_digits_faster(n: int) -> int:
    """
    Find the number of digits in a number.
    abs() is used for negative numbers

    >>> num_digits_faster(12345)
    5
    >>> num_digits_faster(123)
    3
    >>> num_digits_faster(0)
    1
    >>> num_digits_faster(-1)
    1
    >>> num_digits_faster(-123456)
    6
    >>> num_digits('123')  # Raises a TypeError for non-integer input
    Traceback (most recent call last):
        ...
    TypeError: Input must be an integer
    """
    logger.debug(">>> Entering num_digits_faster(n=%s)", n)

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    logger.debug("<<< Exiting num_digits_faster(n=%s)", n)
    return len(str(abs(n)))


def benchmark() -> None:
    """
    Benchmark multiple functions, with three different length int values.
    """
    logger.debug(">>> Entering benchmark()")
    from collections.abc import Callable
    logger.debug("<<< Exiting benchmark()")

    def benchmark_a_function(func: Callable, value: int) -> None:
        logger.debug(">>> Entering benchmark_a_function(func=%s,value=%s)", func, value)
        call = f"{func.__name__}({value})"
        logger.debug("benchmark_a_function(func=%s,value=%s): call → %s", func, value, call)
        timing = timeit(f"__main__.{call}", setup="import __main__")
        print(f"{call}: {func(value)} -- {timing} seconds")
        logger.debug("benchmark_a_function(func=%s,value=%s): timing → %s", func, value, timing)
        logger.debug("<<< Exiting benchmark_a_function(func=%s,value=%s)", func, value)

    for value in (262144, 1125899906842624, 1267650600228229401496703205376):
        for func in (num_digits, num_digits_fast, num_digits_faster):
            benchmark_a_function(func, value)
        print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
