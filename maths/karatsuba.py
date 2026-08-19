import logging
logger = logging.getLogger(__name__)
"""Multiply two numbers using Karatsuba algorithm"""


def karatsuba(a: int, b: int) -> int:
    """
    >>> karatsuba(15463, 23489) == 15463 * 23489
    True
    >>> karatsuba(3, 9) == 3 * 9
    True
    """
    logger.debug(">>> Entering karatsuba(a=%s,b=%s)", a, b)
    if len(str(a)) == 1 or len(str(b)) == 1:
        return a * b

    m1 = max(len(str(a)), len(str(b)))
    m2 = m1 // 2

    a1, a2 = divmod(a, 10**m2)
    b1, b2 = divmod(b, 10**m2)

    x = karatsuba(a2, b2)
    y = karatsuba((a1 + a2), (b1 + b2))
    z = karatsuba(a1, b1)

    logger.debug("<<< Exiting karatsuba(a=%s,b=%s)", a, b)
    return (z * 10 ** (2 * m2)) + ((y - z - x) * 10 ** (m2)) + (x)


def main():
    logger.debug(">>> Entering main()")
    print(karatsuba(15463, 23489))
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    main()
