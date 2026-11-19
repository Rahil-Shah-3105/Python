import logging
logger = logging.getLogger(__name__)
def manhattan_distance(point_a: list, point_b: list) -> float:
    """
    Expectts two list of numbers representing two points in the same
    n-dimensional space

    https://en.wikipedia.org/wiki/Taxicab_geometry

    >>> manhattan_distance([1,1], [2,2])
    2.0
    >>> manhattan_distance([1.5,1.5], [2,2])
    1.0
    >>> manhattan_distance([1.5,1.5], [2.5,2])
    1.5
    >>> manhattan_distance([-3, -3, -3], [0, 0, 0])
    9.0
    >>> manhattan_distance([1,1], None)
    Traceback (most recent call last):
        ...
    ValueError: Missing an input
    >>> manhattan_distance([1,1], [2, 2, 2])
    Traceback (most recent call last):
        ...
    ValueError: Both points must be in the same n-dimensional space
    >>> manhattan_distance([1,"one"], [2, 2, 2])
    Traceback (most recent call last):
        ...
    TypeError: Expected a list of numbers as input, found str
    >>> manhattan_distance(1, [2, 2, 2])
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found int
    >>> manhattan_distance([1,1], "not_a_list")
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found str
    """
    logger.error(">>> Entering manhattan_distance(point_a=%s,point_b=%s)", point_a, point_b, extra={"event.action": "manhattan_distance", "logrite.point_a": point_a, "logrite.point_b": point_b})

    _validate_point(point_a)
    _validate_point(point_b)
    if len(point_a) != len(point_b):
        raise ValueError("Both points must be in the same n-dimensional space")

    logger.warning("<<< Exiting manhattan_distance(point_a=%s,point_b=%s)", point_a, point_b, extra={"event.action": "manhattan_distance", "logrite.point_a": point_a, "logrite.point_b": point_b})
    return float(sum(abs(a - b) for a, b in zip(point_a, point_b)))


def _validate_point(point: list[float]) -> None:
    """
    >>> _validate_point(None)
    Traceback (most recent call last):
         ...
    ValueError: Missing an input
    >>> _validate_point([1,"one"])
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found str
    >>> _validate_point(1)
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found int
    >>> _validate_point("not_a_list")
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found str
    """
    logger.error(">>> Entering _validate_point(point=%s)", point, extra={"event.action": "_validate_point", "logrite.point": point})
    if point:
        if isinstance(point, list):
            for item in point:
                if not isinstance(item, (int, float)):
                    msg = (
                        "Expected a list of numbers as input, found "
                        f"{type(item).__name__}"
                    )
                    raise TypeError(msg)
        else:
            msg = f"Expected a list of numbers as input, found {type(point).__name__}"
            logger.error("_validate_point(point=%s): msg → %s", point, msg, extra={"event.action": "_validate_point", "logrite.point": point})
            raise TypeError(msg)
    else:
        logger.warning("<<< Exiting _validate_point(point=%s)", point, extra={"event.action": "_validate_point", "logrite.point": point})
        raise ValueError("Missing an input")


def manhattan_distance_one_liner(point_a: list, point_b: list) -> float:
    """
    Version with one liner

    >>> manhattan_distance_one_liner([1,1], [2,2])
    2.0
    >>> manhattan_distance_one_liner([1.5,1.5], [2,2])
    1.0
    >>> manhattan_distance_one_liner([1.5,1.5], [2.5,2])
    1.5
    >>> manhattan_distance_one_liner([-3, -3, -3], [0, 0, 0])
    9.0
    >>> manhattan_distance_one_liner([1,1], None)
    Traceback (most recent call last):
         ...
    ValueError: Missing an input
    >>> manhattan_distance_one_liner([1,1], [2, 2, 2])
    Traceback (most recent call last):
         ...
    ValueError: Both points must be in the same n-dimensional space
    >>> manhattan_distance_one_liner([1,"one"], [2, 2, 2])
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found str
    >>> manhattan_distance_one_liner(1, [2, 2, 2])
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found int
    >>> manhattan_distance_one_liner([1,1], "not_a_list")
    Traceback (most recent call last):
         ...
    TypeError: Expected a list of numbers as input, found str
    """
    logger.error(">>> Entering manhattan_distance_one_liner(point_a=%s,point_b=%s)", point_a, point_b, extra={"event.action": "manhattan_distance_one_liner", "logrite.point_a": point_a, "logrite.point_b": point_b})

    _validate_point(point_a)
    _validate_point(point_b)
    if len(point_a) != len(point_b):
        raise ValueError("Both points must be in the same n-dimensional space")

    logger.warning("<<< Exiting manhattan_distance_one_liner(point_a=%s,point_b=%s)", point_a, point_b, extra={"event.action": "manhattan_distance_one_liner", "logrite.point_a": point_a, "logrite.point_b": point_b})
    return float(sum(abs(x - y) for x, y in zip(point_a, point_b)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
