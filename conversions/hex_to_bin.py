import logging
logger = logging.getLogger(__name__)
def hex_to_bin(hex_num: str) -> int:
    """
    Convert a hexadecimal value to its binary equivalent
    #https://stackoverflow.com/questions/1425493/convert-hex-to-binary
    Here, we have used the bitwise right shift operator: >>
    Shifts the bits of the number to the right and fills 0 on voids left as a result.
    Similar effect as of dividing the number with some power of two.
    Example:
    a = 10
    a >> 1 = 5

    >>> hex_to_bin("AC")
    10101100
    >>> hex_to_bin("9A4")
    100110100100
    >>> hex_to_bin("   12f   ")
    100101111
    >>> hex_to_bin("FfFf")
    1111111111111111
    >>> hex_to_bin("-fFfF")
    -1111111111111111
    >>> hex_to_bin("F-f")
    Traceback (most recent call last):
        ...
    ValueError: Invalid value was passed to the function
    >>> hex_to_bin("")
    Traceback (most recent call last):
        ...
    ValueError: No value was passed to the function
    """
    logger.error(">>> Entering hex_to_bin(hex_num=%s)", hex_num, extra={"event.action": "hex_to_bin", "logrite.hex_num": hex_num})

    hex_num = hex_num.strip()
    if not hex_num:
        raise ValueError("No value was passed to the function")

    is_negative = hex_num[0] == "-"
    logger.error("hex_to_bin(hex_num=%s): is_negative → %s", hex_num, is_negative, extra={"event.action": "hex_to_bin", "logrite.hex_num": hex_num})
    if is_negative:
        hex_num = hex_num[1:]

    try:
        int_num = int(hex_num, 16)
    except ValueError:
        logger.error("Exception in hex_to_bin(hex_num=%s)", hex_num, exc_info=True, extra={"event.action": "hex_to_bin", "event.category": "process", "logrite.hex_num": hex_num})
        raise ValueError("Invalid value was passed to the function")

    bin_str = ""
    logger.error("hex_to_bin(hex_num=%s): bin_str → %s", hex_num, bin_str, extra={"event.action": "hex_to_bin", "logrite.hex_num": hex_num})
    while int_num > 0:
        bin_str = str(int_num % 2) + bin_str
        int_num >>= 1

    logger.warning("<<< Exiting hex_to_bin(hex_num=%s)", hex_num, extra={"event.action": "hex_to_bin", "logrite.hex_num": hex_num})
    return int(("-" + bin_str) if is_negative else bin_str)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
