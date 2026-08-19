import logging
logger = logging.getLogger(__name__)
"""
Project Euler Problem 94: https://projecteuler.net/problem=94

It is easily proved that no equilateral triangle exists with integral length sides and
integral area. However, the almost equilateral triangle 5-5-6 has an area of 12 square
units.

We shall define an almost equilateral triangle to be a triangle for which two sides are
equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side
lengths and area and whose perimeters do not exceed one billion (1,000,000,000).
"""


def solution(max_perimeter: int = 10**9) -> int:
    """
    Returns the sum of the perimeters of all almost equilateral triangles with integral
    side lengths and area and whose perimeters do not exceed max_perimeter

    >>> solution(20)
    16
    """
    logger.debug(">>> Entering solution(max_perimeter=%s)", max_perimeter)

    prev_value = 1
    logger.debug("solution(max_perimeter=%s): prev_value → %s", max_perimeter, prev_value)
    value = 2
    logger.debug("solution(max_perimeter=%s): value → %s", max_perimeter, value)

    perimeters_sum = 0
    logger.debug("solution(max_perimeter=%s): perimeters_sum → %s", max_perimeter, perimeters_sum)
    i = 0
    perimeter = 0
    logger.debug("solution(max_perimeter=%s): perimeter → %s", max_perimeter, perimeter)
    while perimeter <= max_perimeter:
        perimeters_sum += perimeter

        prev_value += 2 * value
        value += prev_value

        perimeter = 2 * value + 2 if i % 2 == 0 else 2 * value - 2
        i += 1

    logger.debug("<<< Exiting solution(max_perimeter=%s)", max_perimeter)
    return perimeters_sum


if __name__ == "__main__":
    print(f"{solution() = }")
