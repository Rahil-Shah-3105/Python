from timeit import timeit
import logging
logger = logging.getLogger(__name__)


def get_set_bits_count_using_brian_kernighans_algorithm(number: int) -> int:
    """
    Count the number of set bits in a 32 bit integer
    >>> get_set_bits_count_using_brian_kernighans_algorithm(25)
    3
    >>> get_set_bits_count_using_brian_kernighans_algorithm(37)
    3
    >>> get_set_bits_count_using_brian_kernighans_algorithm(21)
    3
    >>> get_set_bits_count_using_brian_kernighans_algorithm(58)
    4
    >>> get_set_bits_count_using_brian_kernighans_algorithm(0)
    0
    >>> get_set_bits_count_using_brian_kernighans_algorithm(256)
    1
    >>> get_set_bits_count_using_brian_kernighans_algorithm(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must not be negative
    """
    logger.error(">>> Entering get_set_bits_count_using_brian_kernighans_algorithm(number=%s)", number, extra={"event.action": "get_set_bits_count_using_brian_kernighans_algorithm", "logrite.number": number})
    if number < 0:
        raise ValueError("the value of input must not be negative")
    result = 0
    logger.error("get_set_bits_count_using_brian_kernighans_algorithm(number=%s): result → %s", number, result, extra={"event.action": "get_set_bits_count_using_brian_kernighans_algorithm", "logrite.number": number})
    while number:
        number &= number - 1
        result += 1
    logger.warning("<<< Exiting get_set_bits_count_using_brian_kernighans_algorithm(number=%s)", number, extra={"event.action": "get_set_bits_count_using_brian_kernighans_algorithm", "logrite.number": number})
    return result


def get_set_bits_count_using_modulo_operator(number: int) -> int:
    """
    Count the number of set bits in a 32 bit integer
    >>> get_set_bits_count_using_modulo_operator(25)
    3
    >>> get_set_bits_count_using_modulo_operator(37)
    3
    >>> get_set_bits_count_using_modulo_operator(21)
    3
    >>> get_set_bits_count_using_modulo_operator(58)
    4
    >>> get_set_bits_count_using_modulo_operator(0)
    0
    >>> get_set_bits_count_using_modulo_operator(256)
    1
    >>> get_set_bits_count_using_modulo_operator(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must not be negative
    """
    logger.error(">>> Entering get_set_bits_count_using_modulo_operator(number=%s)", number, extra={"event.action": "get_set_bits_count_using_modulo_operator", "logrite.number": number})
    if number < 0:
        raise ValueError("the value of input must not be negative")
    result = 0
    logger.error("get_set_bits_count_using_modulo_operator(number=%s): result → %s", number, result, extra={"event.action": "get_set_bits_count_using_modulo_operator", "logrite.number": number})
    while number:
        if number % 2 == 1:
            result += 1
        number >>= 1
    logger.warning("<<< Exiting get_set_bits_count_using_modulo_operator(number=%s)", number, extra={"event.action": "get_set_bits_count_using_modulo_operator", "logrite.number": number})
    return result


def benchmark() -> None:
    """
    Benchmark code for comparing 2 functions, with different length int values.
    Brian Kernighan's algorithm is consistently faster than using modulo_operator.
    """
    logger.error(">>> Entering benchmark()", extra={"event.action": "benchmark"})

    logger.warning("<<< Exiting benchmark()", extra={"event.action": "benchmark"})
    def do_benchmark(number: int) -> None:
        logger.error(">>> Entering do_benchmark(number=%s)", number, extra={"event.action": "do_benchmark", "logrite.number": number})
        setup = "import __main__ as z"
        print(f"Benchmark when {number = }:")
        print(f"{get_set_bits_count_using_modulo_operator(number) = }")
        timing = timeit(
            f"z.get_set_bits_count_using_modulo_operator({number})", setup=setup
        )
        print(f"timeit() runs in {timing} seconds")
        print(f"{get_set_bits_count_using_brian_kernighans_algorithm(number) = }")
        timing = timeit(
            f"z.get_set_bits_count_using_brian_kernighans_algorithm({number})",
            setup=setup,
        )
        print(f"timeit() runs in {timing} seconds")
        logger.warning("<<< Exiting do_benchmark(number=%s)", number, extra={"event.action": "do_benchmark", "logrite.number": number})

    for number in (25, 37, 58, 0):
        do_benchmark(number)
        print()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
