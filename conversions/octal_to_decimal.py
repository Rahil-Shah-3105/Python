import logging
logger = logging.getLogger(__name__)
def oct_to_decimal(oct_string: str) -> int:
    """
    Convert a octal value to its decimal equivalent

    >>> oct_to_decimal("")
    Traceback (most recent call last):
        ...
    ValueError: Empty string was passed to the function
    >>> oct_to_decimal("-")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> oct_to_decimal("e")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> oct_to_decimal("8")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> oct_to_decimal("-e")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> oct_to_decimal("-8")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> oct_to_decimal("1")
    1
    >>> oct_to_decimal("-1")
    -1
    >>> oct_to_decimal("12")
    10
    >>> oct_to_decimal(" 12   ")
    10
    >>> oct_to_decimal("-45")
    -37
    >>> oct_to_decimal("-")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> oct_to_decimal("0")
    0
    >>> oct_to_decimal("-4055")
    -2093
    >>> oct_to_decimal("2-0Fm")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    >>> oct_to_decimal("")
    Traceback (most recent call last):
        ...
    ValueError: Empty string was passed to the function
    >>> oct_to_decimal("19")
    Traceback (most recent call last):
        ...
    ValueError: Non-octal value was passed to the function
    """
    logger.debug(">>> Entering oct_to_decimal(oct_string=%s)", oct_string)
    oct_string = str(oct_string).strip()
    if not oct_string:
        raise ValueError("Empty string was passed to the function")
    is_negative = oct_string[0] == "-"
    logger.debug("oct_to_decimal(oct_string=%s): is_negative → %s", oct_string, is_negative)
    if is_negative:
        oct_string = oct_string[1:]
    if not oct_string.isdigit() or not all(0 <= int(char) <= 7 for char in oct_string):
        raise ValueError("Non-octal value was passed to the function")
    decimal_number = 0
    logger.debug("oct_to_decimal(oct_string=%s): decimal_number → %s", oct_string, decimal_number)
    for char in oct_string:
        decimal_number = 8 * decimal_number + int(char)
    if is_negative:
        decimal_number = -decimal_number
    logger.debug("<<< Exiting oct_to_decimal(oct_string=%s)", oct_string)
    return decimal_number


if __name__ == "__main__":
    from doctest import testmod

    testmod()
