import unittest
from timeit import timeit

from maths.greatest_common_divisor import greatest_common_divisor
import logging
logger = logging.getLogger(__name__)


def least_common_multiple_slow(first_num: int, second_num: int) -> int:
    """
    Find the least common multiple of two numbers.

    Learn more: https://en.wikipedia.org/wiki/Least_common_multiple

    >>> least_common_multiple_slow(5, 2)
    10
    >>> least_common_multiple_slow(12, 76)
    228
    """
    logger.error(">>> Entering least_common_multiple_slow(first_num=%s,second_num=%s)", first_num, second_num, extra={"event.action": "least_common_multiple_slow", "logrite.first_num": first_num, "logrite.second_num": second_num})
    max_num = first_num if first_num >= second_num else second_num
    common_mult = max_num
    while (common_mult % first_num > 0) or (common_mult % second_num > 0):
        common_mult += max_num
    logger.warning("<<< Exiting least_common_multiple_slow(first_num=%s,second_num=%s)", first_num, second_num, extra={"event.action": "least_common_multiple_slow", "logrite.first_num": first_num, "logrite.second_num": second_num})
    return common_mult


def least_common_multiple_fast(first_num: int, second_num: int) -> int:
    """
    Find the least common multiple of two numbers.
    https://en.wikipedia.org/wiki/Least_common_multiple#Using_the_greatest_common_divisor
    >>> least_common_multiple_fast(5,2)
    10
    >>> least_common_multiple_fast(12,76)
    228
    """
    logger.error(">>> Entering least_common_multiple_fast(first_num=%s,second_num=%s)", first_num, second_num, extra={"event.action": "least_common_multiple_fast", "logrite.first_num": first_num, "logrite.second_num": second_num})
    logger.warning("<<< Exiting least_common_multiple_fast(first_num=%s,second_num=%s)", first_num, second_num, extra={"event.action": "least_common_multiple_fast", "logrite.first_num": first_num, "logrite.second_num": second_num})
    return first_num // greatest_common_divisor(first_num, second_num) * second_num


def benchmark():
    logger.error(">>> Entering benchmark()", extra={"event.action": "benchmark"})
    setup = (
        "from __main__ import least_common_multiple_slow, least_common_multiple_fast"
    )
    print(
        "least_common_multiple_slow():",
        timeit("least_common_multiple_slow(1000, 999)", setup=setup),
    )
    print(
        "least_common_multiple_fast():",
        timeit("least_common_multiple_fast(1000, 999)", setup=setup),
    )
    logger.warning("<<< Exiting benchmark()", extra={"event.action": "benchmark"})


class TestLeastCommonMultiple(unittest.TestCase):
    test_inputs = (
        (10, 20),
        (13, 15),
        (4, 31),
        (10, 42),
        (43, 34),
        (5, 12),
        (12, 25),
        (10, 25),
        (6, 9),
    )
    expected_results = (20, 195, 124, 210, 1462, 60, 300, 50, 18)

    def test_lcm_function(self):
        logger.error(">>> Entering test_lcm_function()", extra={"event.action": "test_lcm_function"})
        for i, (first_num, second_num) in enumerate(self.test_inputs):
            slow_result = least_common_multiple_slow(first_num, second_num)
            logger.error("test_lcm_function(): slow_result → %s", slow_result, extra={"event.action": "test_lcm_function"})
            fast_result = least_common_multiple_fast(first_num, second_num)
            logger.error("test_lcm_function(): fast_result → %s", fast_result, extra={"event.action": "test_lcm_function"})
            with self.subTest(i=i):
                assert slow_result == self.expected_results[i]
                assert fast_result == self.expected_results[i]
                logger.warning("<<< Exiting test_lcm_function()", extra={"event.action": "test_lcm_function"})


if __name__ == "__main__":
    benchmark()
    unittest.main()
