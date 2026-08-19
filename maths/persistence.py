import logging
logger = logging.getLogger(__name__)
def multiplicative_persistence(num: int) -> int:
    """
    Return the persistence of a given number.

    https://en.wikipedia.org/wiki/Persistence_of_a_number

    >>> multiplicative_persistence(217)
    2
    >>> multiplicative_persistence(-1)
    Traceback (most recent call last):
        ...
    ValueError: multiplicative_persistence() does not accept negative values
    >>> multiplicative_persistence("long number")
    Traceback (most recent call last):
        ...
    ValueError: multiplicative_persistence() only accepts integral values
    """
    logger.debug(">>> Entering multiplicative_persistence(num=%s)", num)

    if not isinstance(num, int):
        raise ValueError("multiplicative_persistence() only accepts integral values")
    if num < 0:
        raise ValueError("multiplicative_persistence() does not accept negative values")

    steps = 0
    logger.debug("multiplicative_persistence(num=%s): steps → %s", num, steps)
    num_string = str(num)
    logger.debug("multiplicative_persistence(num=%s): num_string → %s", num, num_string)

    while len(num_string) != 1:
        numbers = [int(i) for i in num_string]
        logger.debug("multiplicative_persistence(num=%s): numbers → %s", num, numbers)

        total = 1
        logger.debug("multiplicative_persistence(num=%s): total → %s", num, total)
        for i in range(len(numbers)):
            total *= numbers[i]

        num_string = str(total)

        steps += 1
    logger.debug("<<< Exiting multiplicative_persistence(num=%s)", num)
    return steps


def additive_persistence(num: int) -> int:
    """
    Return the persistence of a given number.

    https://en.wikipedia.org/wiki/Persistence_of_a_number

    >>> additive_persistence(199)
    3
    >>> additive_persistence(-1)
    Traceback (most recent call last):
        ...
    ValueError: additive_persistence() does not accept negative values
    >>> additive_persistence("long number")
    Traceback (most recent call last):
        ...
    ValueError: additive_persistence() only accepts integral values
    """
    logger.debug(">>> Entering additive_persistence(num=%s)", num)

    if not isinstance(num, int):
        raise ValueError("additive_persistence() only accepts integral values")
    if num < 0:
        raise ValueError("additive_persistence() does not accept negative values")

    steps = 0
    logger.debug("additive_persistence(num=%s): steps → %s", num, steps)
    num_string = str(num)
    logger.debug("additive_persistence(num=%s): num_string → %s", num, num_string)

    while len(num_string) != 1:
        numbers = [int(i) for i in num_string]
        logger.debug("additive_persistence(num=%s): numbers → %s", num, numbers)

        total = 0
        logger.debug("additive_persistence(num=%s): total → %s", num, total)
        for i in range(len(numbers)):
            total += numbers[i]

        num_string = str(total)

        steps += 1
    logger.debug("<<< Exiting additive_persistence(num=%s)", num)
    return steps


if __name__ == "__main__":
    import doctest

    doctest.testmod()
