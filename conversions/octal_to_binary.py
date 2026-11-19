"""
* Author: Bama Charan Chhandogi (https://github.com/BamaCharanChhandogi)
* Description: Convert a Octal number to Binary.

References for better understanding:
https://en.wikipedia.org/wiki/Binary_number
https://en.wikipedia.org/wiki/Octal
"""
import logging
logger = logging.getLogger(__name__)


def octal_to_binary(octal_number: str) -> str:
    """
    Convert an Octal number to Binary.

    >>> octal_to_binary("17")
    '001111'
    >>> octal_to_binary("7")
    '111'
    >>> octal_to_binary("Av")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> octal_to_binary("@#")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> octal_to_binary("")
    Traceback (most recent call last):
        ...
    ValueError: Empty string was passed to the function
    """
    logger.error(">>> Entering octal_to_binary(octal_number=%s)", octal_number, extra={"event.action": "octal_to_binary", "logrite.octal_number": octal_number})
    if not octal_number:
        raise ValueError("Empty string was passed to the function")

    binary_number = ""
    logger.error("octal_to_binary(octal_number=%s): binary_number → %s", octal_number, binary_number, extra={"event.action": "octal_to_binary", "logrite.octal_number": octal_number})
    octal_digits = "01234567"
    logger.error("octal_to_binary(octal_number=%s): octal_digits → %s", octal_number, octal_digits, extra={"event.action": "octal_to_binary", "logrite.octal_number": octal_number})
    for digit in octal_number:
        if digit not in octal_digits:
            raise ValueError("Non-octal value was passed to the function")

        binary_digit = ""
        logger.error("octal_to_binary(octal_number=%s): binary_digit → %s", octal_number, binary_digit, extra={"event.action": "octal_to_binary", "logrite.octal_number": octal_number})
        value = int(digit)
        logger.error("octal_to_binary(octal_number=%s): value → %s", octal_number, value, extra={"event.action": "octal_to_binary", "logrite.octal_number": octal_number})
        for _ in range(3):
            binary_digit = str(value % 2) + binary_digit
            value //= 2
        binary_number += binary_digit

    logger.warning("<<< Exiting octal_to_binary(octal_number=%s)", octal_number, extra={"event.action": "octal_to_binary", "logrite.octal_number": octal_number})
    return binary_number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
