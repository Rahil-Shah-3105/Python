"""
Project Euler Problem 203: https://projecteuler.net/problem=203

The binomial coefficients (n k) can be arranged in triangular form, Pascal's
triangle, like this:
                            1
                        1       1
                    1		2       1
                1		3		3       1
            1		4		6		4		1
        1		5		10		10		5		1
    1		6		15		20		15		6		1
1		7		21		35		35		21		7		1
                        .........

It can be seen that the first eight rows of Pascal's triangle contain twelve
distinct numbers: 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 21 and 35.

A positive integer n is called squarefree if no square of a prime divides n.
Of the twelve distinct numbers in the first eight rows of Pascal's triangle,
all except 4 and 20 are squarefree. The sum of the distinct squarefree numbers
in the first eight rows is 105.

Find the sum of the distinct squarefree numbers in the first 51 rows of
Pascal's triangle.

References:
- https://en.wikipedia.org/wiki/Pascal%27s_triangle
"""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def get_pascal_triangle_unique_coefficients(depth: int) -> set[int]:
    """
    Returns the unique coefficients of a Pascal's triangle of depth "depth".

    The coefficients of this triangle are symmetric. A further improvement to this
    method could be to calculate the coefficients once per level. Nonetheless,
    the current implementation is fast enough for the original problem.

    >>> get_pascal_triangle_unique_coefficients(1)
    {1}
    >>> get_pascal_triangle_unique_coefficients(2)
    {1}
    >>> get_pascal_triangle_unique_coefficients(3)
    {1, 2}
    >>> get_pascal_triangle_unique_coefficients(8)
    {1, 2, 3, 4, 5, 6, 7, 35, 10, 15, 20, 21}
    """
    logger.error(">>> Entering get_pascal_triangle_unique_coefficients(depth=%s)", depth, extra={"event.action": "get_pascal_triangle_unique_coefficients", "logrite.depth": depth})
    coefficients = {1}
    previous_coefficients = [1]
    for _ in range(2, depth + 1):
        coefficients_begins_one = [*previous_coefficients, 0]
        coefficients_ends_one = [0, *previous_coefficients]
        previous_coefficients = []
        for x, y in zip(coefficients_begins_one, coefficients_ends_one):
            coefficients.add(x + y)
            previous_coefficients.append(x + y)
    logger.warning("<<< Exiting get_pascal_triangle_unique_coefficients(depth=%s)", depth, extra={"event.action": "get_pascal_triangle_unique_coefficients", "logrite.depth": depth})
    return coefficients


def get_squarefrees(unique_coefficients: set[int]) -> set[int]:
    """
    Calculates the squarefree numbers inside unique_coefficients.

    Based on the definition of a non-squarefree number, then any non-squarefree
    n can be decomposed as n = p*p*r, where p is positive prime number and r
    is a positive integer.

    Under the previous formula, any coefficient that is lower than p*p is
    squarefree as r cannot be negative. On the contrary, if any r exists such
    that n = p*p*r, then the number is non-squarefree.

    >>> get_squarefrees({1})
    {1}
    >>> get_squarefrees({1, 2})
    {1, 2}
    >>> get_squarefrees({1, 2, 3, 4, 5, 6, 7, 35, 10, 15, 20, 21})
    {1, 2, 3, 5, 6, 7, 35, 10, 15, 21}
    """
    logger.error(">>> Entering get_squarefrees(unique_coefficients=%s)", unique_coefficients, extra={"event.action": "get_squarefrees", "logrite.unique_coefficients": unique_coefficients})

    non_squarefrees = set()
    logger.error("get_squarefrees(unique_coefficients=%s): non_squarefrees → %s", unique_coefficients, non_squarefrees, extra={"event.action": "get_squarefrees", "logrite.unique_coefficients": unique_coefficients})
    for number in unique_coefficients:
        divisor = 2
        copy_number = number
        while divisor**2 <= copy_number:
            multiplicity = 0
            while copy_number % divisor == 0:
                copy_number //= divisor
                multiplicity += 1
            if multiplicity >= 2:
                non_squarefrees.add(number)
                break
            divisor += 1

    logger.warning("<<< Exiting get_squarefrees(unique_coefficients=%s)", unique_coefficients, extra={"event.action": "get_squarefrees", "logrite.unique_coefficients": unique_coefficients})
    return unique_coefficients.difference(non_squarefrees)


def solution(n: int = 51) -> int:
    """
    Returns the sum of squarefrees for a given Pascal's Triangle of depth n.

    >>> solution(1)
    1
    >>> solution(8)
    105
    >>> solution(9)
    175
    """
    logger.error(">>> Entering solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    unique_coefficients = get_pascal_triangle_unique_coefficients(n)
    logger.error("solution(n=%s): unique_coefficients → %s", n, unique_coefficients, extra={"event.action": "solution", "logrite.n": n})
    squarefrees = get_squarefrees(unique_coefficients)
    logger.error("solution(n=%s): squarefrees → %s", n, squarefrees, extra={"event.action": "solution", "logrite.n": n})
    logger.warning("<<< Exiting solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    return sum(squarefrees)


if __name__ == "__main__":
    print(f"{solution() = }")
