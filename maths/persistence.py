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
    logger.error(">>> Entering multiplicative_persistence(num=%s)", num, extra={"event.action": "multiplicative_persistence", "logrite.num": num})

    if not isinstance(num, int):
        raise ValueError("multiplicative_persistence() only accepts integral values")
    if num < 0:
        raise ValueError("multiplicative_persistence() does not accept negative values")

    steps = 0
    num_string = str(num)
    logger.error("multiplicative_persistence(num=%s): num_string → %s", num, num_string, extra={"event.action": "multiplicative_persistence", "logrite.num": num})

    while len(num_string) != 1:
        numbers = [int(i) for i in num_string]
        logger.error("multiplicative_persistence(num=%s): numbers → %s", num, numbers, extra={"event.action": "multiplicative_persistence", "logrite.num": num})

        total = 1
        logger.error("multiplicative_persistence(num=%s): total → %s", num, total, extra={"event.action": "multiplicative_persistence", "logrite.num": num})
        for i in range(len(numbers)):
            total *= numbers[i]

        num_string = str(total)

        steps += 1
    logger.warning("<<< Exiting multiplicative_persistence(num=%s)", num, extra={"event.action": "multiplicative_persistence", "logrite.num": num})
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
    logger.error(">>> Entering additive_persistence(num=%s)", num, extra={"event.action": "additive_persistence", "logrite.num": num})

    if not isinstance(num, int):
        raise ValueError("additive_persistence() only accepts integral values")
    if num < 0:
        raise ValueError("additive_persistence() does not accept negative values")

    steps = 0
    num_string = str(num)
    logger.error("additive_persistence(num=%s): num_string → %s", num, num_string, extra={"event.action": "additive_persistence", "logrite.num": num})

    while len(num_string) != 1:
        numbers = [int(i) for i in num_string]
        logger.error("additive_persistence(num=%s): numbers → %s", num, numbers, extra={"event.action": "additive_persistence", "logrite.num": num})

        total = 0
        logger.error("additive_persistence(num=%s): total → %s", num, total, extra={"event.action": "additive_persistence", "logrite.num": num})
        for i in range(len(numbers)):
            total += numbers[i]

        num_string = str(total)

        steps += 1
    logger.warning("<<< Exiting additive_persistence(num=%s)", num, extra={"event.action": "additive_persistence", "logrite.num": num})
    return steps


if __name__ == "__main__":
    import doctest

    doctest.testmod()
