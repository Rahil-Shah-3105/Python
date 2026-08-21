import logging
logger = logging.getLogger(__name__)
# https://www.tutorialspoint.com/python3/bitwise_operators_example.htm


def binary_or(a: int, b: int) -> str:
    """
    Take in 2 integers, convert them to binary, and return a binary number that is the
    result of a binary or operation on the integers provided.

    >>> binary_or(25, 32)
    '0b111001'
    >>> binary_or(37, 50)
    '0b110111'
    >>> binary_or(21, 30)
    '0b11111'
    >>> binary_or(58, 73)
    '0b1111011'
    >>> binary_or(0, 255)
    '0b11111111'
    >>> binary_or(0, 256)
    '0b100000000'
    >>> binary_or(0, -1)
    Traceback (most recent call last):
        ...
    ValueError: the value of both inputs must be positive
    >>> binary_or(0, 1.1)
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> binary_or("0", "1")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    logger.debug(">>> Entering binary_or(a=%s,b=%s)", a, b)
    if a < 0 or b < 0:
        logger.debug("<<< Exiting binary_or(a=%s,b=%s)", a, b)
        raise ValueError("the value of both inputs must be positive")
    a_binary = str(bin(a))[2:]  # remove the leading "0b"
    logger.debug("binary_or(a=%s,b=%s): a_binary → %s", a, b, a_binary)
    b_binary = str(bin(b))[2:]
    logger.debug("binary_or(a=%s,b=%s): b_binary → %s", a, b, b_binary)
    max_len = max(len(a_binary), len(b_binary))
    logger.debug("binary_or(a=%s,b=%s): max_len → %s", a, b, max_len)
    return "0b" + "".join(
        str(int("1" in (char_a, char_b)))
        for char_a, char_b in zip(a_binary.zfill(max_len), b_binary.zfill(max_len))
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
