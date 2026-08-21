import logging
logger = logging.getLogger(__name__)
# Reference: https://www.geeksforgeeks.org/position-of-rightmost-set-bit/


def get_index_of_rightmost_set_bit(number: int) -> int:
    """
    Take in a positive integer 'number'.
    Returns the zero-based index of first set bit in that 'number' from right.
    Returns -1, If no set bit found.

    >>> get_index_of_rightmost_set_bit(0)
    -1
    >>> get_index_of_rightmost_set_bit(5)
    0
    >>> get_index_of_rightmost_set_bit(36)
    2
    >>> get_index_of_rightmost_set_bit(8)
    3
    >>> get_index_of_rightmost_set_bit(-18)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a non-negative integer
    >>> get_index_of_rightmost_set_bit('test')
    Traceback (most recent call last):
        ...
    ValueError: Input must be a non-negative integer
    >>> get_index_of_rightmost_set_bit(1.25)
    Traceback (most recent call last):
        ...
    ValueError: Input must be a non-negative integer
    """
    logger.debug(">>> Entering get_index_of_rightmost_set_bit(number=%s)", number)

    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")

    intermediate = number & ~(number - 1)
    logger.debug("get_index_of_rightmost_set_bit(number=%s): intermediate → %s", number, intermediate)
    index = 0
    logger.debug("get_index_of_rightmost_set_bit(number=%s): index → %s", number, index)
    while intermediate:
        intermediate >>= 1
        index += 1
    logger.debug("<<< Exiting get_index_of_rightmost_set_bit(number=%s)", number)
    return index - 1


if __name__ == "__main__":
    """
    Finding the index of rightmost set bit has some very peculiar use-cases,
    especially in finding missing or/and repeating numbers in a list of
    positive integers.
    """
    import doctest

    doctest.testmod(verbose=True)
