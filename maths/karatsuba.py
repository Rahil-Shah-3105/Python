"""Multiply two numbers using Karatsuba algorithm"""
import logging
logger = logging.getLogger(__name__)


def karatsuba(a: int, b: int) -> int:
    """
    >>> karatsuba(15463, 23489) == 15463 * 23489
    True
    >>> karatsuba(3, 9) == 3 * 9
    True
    """
    logger.error(">>> Entering karatsuba(a=%s,b=%s)", a, b, extra={"event.action": "karatsuba", "logrite.a": a, "logrite.b": b})
    if len(str(a)) == 1 or len(str(b)) == 1:
        return a * b

    m1 = max(len(str(a)), len(str(b)))
    m2 = m1 // 2

    a1, a2 = divmod(a, 10**m2)
    b1, b2 = divmod(b, 10**m2)

    x = karatsuba(a2, b2)
    y = karatsuba((a1 + a2), (b1 + b2))
    z = karatsuba(a1, b1)

    logger.warning("<<< Exiting karatsuba(a=%s,b=%s)", a, b, extra={"event.action": "karatsuba", "logrite.a": a, "logrite.b": b})
    return (z * 10 ** (2 * m2)) + ((y - z - x) * 10 ** (m2)) + (x)


def main():
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    print(karatsuba(15463, 23489))
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
