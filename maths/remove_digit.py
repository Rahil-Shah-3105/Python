import logging
logger = logging.getLogger(__name__)
def remove_digit(num: int) -> int:
    """

    returns the biggest possible result
    that can be achieved by removing
    one digit from the given number

    >>> remove_digit(152)
    52
    >>> remove_digit(6385)
    685
    >>> remove_digit(-11)
    1
    >>> remove_digit(2222222)
    222222
    >>> remove_digit("2222222")
    Traceback (most recent call last):
    TypeError: only integers accepted as input
    >>> remove_digit("string input")
    Traceback (most recent call last):
    TypeError: only integers accepted as input
    """
    logger.debug(">>> Entering remove_digit(num=%s)", num)

    if not isinstance(num, int):
        raise TypeError("only integers accepted as input")
    else:
        num_str = str(abs(num))
        logger.debug("remove_digit(num=%s): num_str → %s", num, num_str)
        num_transpositions = [list(num_str) for char in range(len(num_str))]
        logger.debug("remove_digit(num=%s): num_transpositions → %s", num, num_transpositions)
        for index in range(len(num_str)):
            num_transpositions[index].pop(index)
            logger.debug("<<< Exiting remove_digit(num=%s)", num)
        return max(
            int("".join(list(transposition))) for transposition in num_transpositions
        )


if __name__ == "__main__":
    __import__("doctest").testmod()
