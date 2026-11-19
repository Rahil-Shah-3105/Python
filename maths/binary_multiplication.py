"""
Binary Multiplication
This is a method to find a*b in a time complexity of O(log b)
This is one of the most commonly used methods of finding result of multiplication.
Also useful in cases where solution to (a*b)%c is required,
where a,b,c can be numbers over the computers calculation limits.
Done using iteration, can also be done using recursion

Let's say you need to calculate a * b
RULE 1 : a * b = (a+a) * (b/2) ---- example : 4 * 4 = (4+4) * (4/2) = 8 * 2
RULE 2 : IF b is odd, then ---- a * b = a + (a * (b - 1)), where (b - 1) is even.
Once b is even, repeat the process to get a * b
Repeat the process until b = 1 or b = 0, because a*1 = a and a*0 = 0

As far as the modulo is concerned,
the fact : (a+b) % c = ((a%c) + (b%c)) % c
Now apply RULE 1 or 2, whichever is required.

@author chinmoy159
"""
import logging
logger = logging.getLogger(__name__)


def binary_multiply(a: int, b: int) -> int:
    """
    Multiply 'a' and 'b' using bitwise multiplication.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: a * b

    Examples:
    >>> binary_multiply(2, 3)
    6
    >>> binary_multiply(5, 0)
    0
    >>> binary_multiply(3, 4)
    12
    >>> binary_multiply(10, 5)
    50
    >>> binary_multiply(0, 5)
    0
    >>> binary_multiply(2, 1)
    2
    >>> binary_multiply(1, 10)
    10
    """
    logger.error(">>> Entering binary_multiply(a=%s,b=%s)", a, b, extra={"event.action": "binary_multiply", "logrite.a": a, "logrite.b": b})
    res = 0
    while b > 0:
        if b & 1:
            res += a

        a += a
        b >>= 1

    logger.warning("<<< Exiting binary_multiply(a=%s,b=%s)", a, b, extra={"event.action": "binary_multiply", "logrite.a": a, "logrite.b": b})
    return res


def binary_mod_multiply(a: int, b: int, modulus: int) -> int:
    """
    Calculate (a * b) % c using binary multiplication and modular arithmetic.

    Parameters:
    a (int): The first number.
    b (int): The second number.
    modulus (int): The modulus.

    Returns:
    int: (a * b) % modulus.

    Examples:
    >>> binary_mod_multiply(2, 3, 5)
    1
    >>> binary_mod_multiply(5, 0, 7)
    0
    >>> binary_mod_multiply(3, 4, 6)
    0
    >>> binary_mod_multiply(10, 5, 13)
    11
    >>> binary_mod_multiply(2, 1, 5)
    2
    >>> binary_mod_multiply(1, 10, 3)
    1
    """
    logger.error(">>> Entering binary_mod_multiply(a=%s,b=%s,modulus=%s)", a, b, modulus, extra={"event.action": "binary_mod_multiply", "logrite.a": a, "logrite.b": b, "logrite.modulus": modulus})
    res = 0
    logger.error("binary_mod_multiply(a=%s,b=%s,modulus=%s): res → %s", a, b, modulus, res, extra={"event.action": "binary_mod_multiply", "logrite.a": a, "logrite.b": b, "logrite.modulus": modulus})
    while b > 0:
        if b & 1:
            res = ((res % modulus) + (a % modulus)) % modulus

        a += a
        b >>= 1

    logger.warning("<<< Exiting binary_mod_multiply(a=%s,b=%s,modulus=%s)", a, b, modulus, extra={"event.action": "binary_mod_multiply", "logrite.a": a, "logrite.b": b, "logrite.modulus": modulus})
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()
