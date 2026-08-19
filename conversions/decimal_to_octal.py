"""Convert a Decimal Number to an Octal Number."""

import math
import logging
logger = logging.getLogger(__name__)

# Modified from:
# https://github.com/TheAlgorithms/Javascript/blob/master/Conversions/DecimalToOctal.js


def decimal_to_octal(num: int) -> str:
    """Convert a Decimal Number to an Octal Number.

    >>> all(decimal_to_octal(i) == oct(i) for i
    ...     in (0, 2, 8, 64, 65, 216, 255, 256, 512))
    True
    """
    logger.debug(">>> Entering decimal_to_octal(num=%s)", num)
    octal = 0
    logger.debug("decimal_to_octal(num=%s): octal → %s", num, octal)
    counter = 0
    logger.debug("decimal_to_octal(num=%s): counter → %s", num, counter)
    while num > 0:
        remainder = num % 8
        logger.debug("decimal_to_octal(num=%s): remainder → %s", num, remainder)
        octal = octal + (remainder * math.floor(math.pow(10, counter)))
        counter += 1
        num = math.floor(num / 8)  # basically /= 8 without remainder if any
        logger.debug("decimal_to_octal(num=%s): num → %s", num, num)
        # This formatting removes trailing '.0' from `octal`.
    logger.debug("<<< Exiting decimal_to_octal(num=%s)", num)
    return f"0o{int(octal)}"


def main() -> None:
    """Print octal equivalents of decimal numbers."""
    logger.debug(">>> Entering main()")
    print("\n2 in octal is:")
    print(decimal_to_octal(2))  # = 2
    print("\n8 in octal is:")
    print(decimal_to_octal(8))  # = 10
    print("\n65 in octal is:")
    print(decimal_to_octal(65))  # = 101
    print("\n216 in octal is:")
    print(decimal_to_octal(216))  # = 330
    print("\n512 in octal is:")
    print(decimal_to_octal(512))  # = 1000
    print("\n")
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    main()
