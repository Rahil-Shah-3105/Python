import logging
logger = logging.getLogger(__name__)
def chebyshev_distance(point_a: list[float], point_b: list[float]) -> float:
    """
    This function calculates the Chebyshev distance (also known as the
    Chessboard distance) between two n-dimensional points represented as lists.

    https://en.wikipedia.org/wiki/Chebyshev_distance

    >>> chebyshev_distance([1.0, 1.0], [2.0, 2.0])
    1.0
    >>> chebyshev_distance([1.0, 1.0, 9.0], [2.0, 2.0, -5.2])
    14.2
    >>> chebyshev_distance([1.0], [2.0, 2.0])
    Traceback (most recent call last):
        ...
    ValueError: Both points must have the same dimension.
    """
    logger.error(">>> Entering chebyshev_distance(point_a=%s,point_b=%s)", point_a, point_b, extra={"event.action": "chebyshev_distance", "logrite.point_a": point_a, "logrite.point_b": point_b})
    if len(point_a) != len(point_b):
        raise ValueError("Both points must have the same dimension.")

    logger.warning("<<< Exiting chebyshev_distance(point_a=%s,point_b=%s)", point_a, point_b, extra={"event.action": "chebyshev_distance", "logrite.point_a": point_a, "logrite.point_b": point_b})
    return max(abs(a - b) for a, b in zip(point_a, point_b))
