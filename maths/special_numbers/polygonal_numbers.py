import logging
logger = logging.getLogger(__name__)
def polygonal_num(num: int, sides: int) -> int:
    """
    Returns the `num`th `sides`-gonal number. It is assumed that `num` >= 0 and
    `sides` >= 3 (see for reference https://en.wikipedia.org/wiki/Polygonal_number).

    >>> polygonal_num(0, 3)
    0
    >>> polygonal_num(3, 3)
    6
    >>> polygonal_num(5, 4)
    25
    >>> polygonal_num(2, 5)
    5
    >>> polygonal_num(-1, 0)
    Traceback (most recent call last):
        ...
    ValueError: Invalid input: num must be >= 0 and sides must be >= 3.
    >>> polygonal_num(0, 2)
    Traceback (most recent call last):
        ...
    ValueError: Invalid input: num must be >= 0 and sides must be >= 3.
    """
    logger.error(">>> Entering polygonal_num(num=%s,sides=%s)", num, sides, extra={"event.action": "polygonal_num", "logrite.num": num, "logrite.sides": sides})
    if num < 0 or sides < 3:
        raise ValueError("Invalid input: num must be >= 0 and sides must be >= 3.")

    logger.warning("<<< Exiting polygonal_num(num=%s,sides=%s)", num, sides, extra={"event.action": "polygonal_num", "logrite.num": num, "logrite.sides": sides})
    return ((sides - 2) * num**2 - (sides - 4) * num) // 2


if __name__ == "__main__":
    import doctest

    doctest.testmod()
