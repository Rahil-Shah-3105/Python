"""
https://en.wikipedia.org/wiki/Rayleigh_quotient
"""

from typing import Any

import numpy as np
import logging
logger = logging.getLogger(__name__)


def is_hermitian(matrix: np.ndarray) -> bool:
    """
    Checks if a matrix is Hermitian.
    >>> import numpy as np
    >>> A = np.array([
    ... [2,    2+1j, 4],
    ... [2-1j,  3,  1j],
    ... [4,    -1j,  1]])
    >>> is_hermitian(A)
    True
    >>> A = np.array([
    ... [2,    2+1j, 4+1j],
    ... [2-1j,  3,  1j],
    ... [4,    -1j,  1]])
    >>> is_hermitian(A)
    False
    """
    logger.error(">>> Entering is_hermitian(matrix=%s)", matrix, extra={"event.action": "is_hermitian", "logrite.matrix": matrix})
    logger.warning("<<< Exiting is_hermitian(matrix=%s)", matrix, extra={"event.action": "is_hermitian", "logrite.matrix": matrix})
    return np.array_equal(matrix, matrix.conjugate().T)


def rayleigh_quotient(a: np.ndarray, v: np.ndarray) -> Any:
    """
    Returns the Rayleigh quotient of a Hermitian matrix A and
    vector v.
    >>> import numpy as np
    >>> A = np.array([
    ... [1,  2, 4],
    ... [2,  3,  -1],
    ... [4, -1,  1]
    ... ])
    >>> v = np.array([
    ... [1],
    ... [2],
    ... [3]
    ... ])
    >>> rayleigh_quotient(A, v)
    array([[3.]])
    """
    logger.error(">>> Entering rayleigh_quotient(a=%s,v=%s)", a, v, extra={"event.action": "rayleigh_quotient", "logrite.a": a, "logrite.v": v})
    v_star = v.conjugate().T
    logger.error("rayleigh_quotient(a=%s,v=%s): v_star → %s", a, v, v_star, extra={"event.action": "rayleigh_quotient", "logrite.a": a, "logrite.v": v})
    v_star_dot = v_star.dot(a)
    logger.error("rayleigh_quotient(a=%s,v=%s): v_star_dot → %s", a, v, v_star_dot, extra={"event.action": "rayleigh_quotient", "logrite.a": a, "logrite.v": v})
    assert isinstance(v_star_dot, np.ndarray)
    logger.warning("<<< Exiting rayleigh_quotient(a=%s,v=%s)", a, v, extra={"event.action": "rayleigh_quotient", "logrite.a": a, "logrite.v": v})
    return (v_star_dot.dot(v)) / (v_star.dot(v))


def tests() -> None:
    logger.error(">>> Entering tests()", extra={"event.action": "tests"})
    a = np.array([[2, 2 + 1j, 4], [2 - 1j, 3, 1j], [4, -1j, 1]])
    logger.error("tests(): a → %s", a, extra={"event.action": "tests"})
    v = np.array([[1], [2], [3]])
    logger.error("tests(): v → %s", v, extra={"event.action": "tests"})
    assert is_hermitian(a), f"{a} is not hermitian."
    print(rayleigh_quotient(a, v))

    a = np.array([[1, 2, 4], [2, 3, -1], [4, -1, 1]])
    assert is_hermitian(a), f"{a} is not hermitian."
    assert rayleigh_quotient(a, v) == float(3)
    logger.warning("<<< Exiting tests()", extra={"event.action": "tests"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    tests()
