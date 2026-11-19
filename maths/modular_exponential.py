"""
Modular Exponential.
Modular exponentiation is a type of exponentiation performed over a modulus.
For more explanation, please check
https://en.wikipedia.org/wiki/Modular_exponentiation
"""
import logging
logger = logging.getLogger(__name__)

"""Calculate Modular Exponential."""


def modular_exponential(base: int, power: int, mod: int):
    """
    >>> modular_exponential(5, 0, 10)
    1
    >>> modular_exponential(2, 8, 7)
    4
    >>> modular_exponential(3, -2, 9)
    -1
    """
    logger.error(">>> Entering modular_exponential(base=%s,power=%s,mod=%s)", base, power, mod, extra={"event.action": "modular_exponential", "logrite.base": base, "logrite.power": power, "logrite.mod": mod})

    if power < 0:
        return -1
    base %= mod
    result = 1

    while power > 0:
        if power & 1:
            result = (result * base) % mod
        power = power >> 1
        base = (base * base) % mod

    logger.warning("<<< Exiting modular_exponential(base=%s,power=%s,mod=%s)", base, power, mod, extra={"event.action": "modular_exponential", "logrite.base": base, "logrite.power": power, "logrite.mod": mod})
    return result


def main():
    """Call Modular Exponential Function."""
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    print(modular_exponential(3, 200, 13))
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
