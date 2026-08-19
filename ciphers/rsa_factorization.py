"""
An RSA prime factor algorithm.

The program can efficiently factor RSA prime number given the private key d and
public key e.

| Source: on page ``3`` of https://crypto.stanford.edu/~dabo/papers/RSA-survey.pdf
| More readable source: https://www.di-mgt.com.au/rsa_factorize_n.html

large number can take minutes to factor, therefore are not included in doctest.
"""

from __future__ import annotations

import math
import random
import logging
logger = logging.getLogger(__name__)


def rsafactor(d: int, e: int, n: int) -> list[int]:
    """
    This function returns the factors of N, where p*q=N

    Return: [p, q]

    We call N the RSA modulus, e the encryption exponent, and d the decryption exponent.
    The pair (N, e) is the public key. As its name suggests, it is public and is used to
    encrypt messages.
    The pair (N, d) is the secret key or private key and is known only to the recipient
    of encrypted messages.

    >>> rsafactor(3, 16971, 25777)
    [149, 173]
    >>> rsafactor(7331, 11, 27233)
    [113, 241]
    >>> rsafactor(4021, 13, 17711)
    [89, 199]
    """
    logger.debug(">>> Entering rsafactor(d=%s,e=%s,n=%s)", d, e, n)
    k = d * e - 1
    p = 0
    q = 0
    while p == 0:
        g = random.randint(2, n - 1)
        logger.debug("rsafactor(d=%s,e=%s,n=%s): g → %s", d, e, n, g)
        t = k
        while True:
            if t % 2 == 0:
                t = t // 2
                x = (g**t) % n
                logger.debug("rsafactor(d=%s,e=%s,n=%s): x → %s", d, e, n, x)
                y = math.gcd(x - 1, n)
                logger.debug("rsafactor(d=%s,e=%s,n=%s): y → %s", d, e, n, y)
                if x > 1 and y > 1:
                    p = y
                    q = n // y
                    break  # find the correct factors
            else:
                break  # t is not divisible by 2, break and choose another g
    logger.debug("<<< Exiting rsafactor(d=%s,e=%s,n=%s)", d, e, n)
    return sorted([p, q])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
