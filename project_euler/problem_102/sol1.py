"""
Three distinct points are plotted at random on a Cartesian plane,
for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas
triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text
file containing the coordinates of one thousand "random" triangles, find
the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the
example given above.
"""

from __future__ import annotations

from pathlib import Path
import logging
logger = logging.getLogger(__name__)


def vector_product(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    """
    Return the 2-d vector product of two vectors.
    >>> vector_product((1, 2), (-5, 0))
    10
    >>> vector_product((3, 1), (6, 10))
    24
    """
    logger.error(">>> Entering vector_product(point1=%s,point2=%s)", point1, point2, extra={"event.action": "vector_product", "logrite.point1": point1, "logrite.point2": point2})
    logger.warning("<<< Exiting vector_product(point1=%s,point2=%s)", point1, point2, extra={"event.action": "vector_product", "logrite.point1": point1, "logrite.point2": point2})
    return point1[0] * point2[1] - point1[1] * point2[0]


def contains_origin(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int) -> bool:
    """
    Check if the triangle given by the points A(x1, y1), B(x2, y2), C(x3, y3)
    contains the origin.
    >>> contains_origin(-340, 495, -153, -910, 835, -947)
    True
    >>> contains_origin(-175, 41, -421, -714, 574, -645)
    False
    """
    logger.error(">>> Entering contains_origin(x1=%s,y1=%s,x2=%s,y2=%s,x3=%s,y3=%s)", x1, y1, x2, y2, x3, y3, extra={"event.action": "contains_origin", "logrite.x1": x1, "logrite.y1": y1, "logrite.x2": x2, "logrite.y2": y2, "logrite.x3": x3, "logrite.y3": y3})
    point_a: tuple[int, int] = (x1, y1)
    point_a_to_b: tuple[int, int] = (x2 - x1, y2 - y1)
    point_a_to_c: tuple[int, int] = (x3 - x1, y3 - y1)
    a: float = -vector_product(point_a, point_a_to_b) / vector_product(
        point_a_to_c, point_a_to_b
    )
    logger.error("contains_origin(x1=%s,y1=%s,x2=%s,y2=%s,x3=%s,y3=%s): a → %s", x1, y1, x2, y2, x3, y3, a, extra={"event.action": "contains_origin", "logrite.x1": x1, "logrite.y1": y1, "logrite.x2": x2, "logrite.y2": y2, "logrite.x3": x3, "logrite.y3": y3})
    b: float = +vector_product(point_a, point_a_to_c) / vector_product(
        point_a_to_c, point_a_to_b
    )
    logger.error("contains_origin(x1=%s,y1=%s,x2=%s,y2=%s,x3=%s,y3=%s): b → %s", x1, y1, x2, y2, x3, y3, b, extra={"event.action": "contains_origin", "logrite.x1": x1, "logrite.y1": y1, "logrite.x2": x2, "logrite.y2": y2, "logrite.x3": x3, "logrite.y3": y3})

    logger.warning("<<< Exiting contains_origin(x1=%s,y1=%s,x2=%s,y2=%s,x3=%s,y3=%s)", x1, y1, x2, y2, x3, y3, extra={"event.action": "contains_origin", "logrite.x1": x1, "logrite.y1": y1, "logrite.x2": x2, "logrite.y2": y2, "logrite.x3": x3, "logrite.y3": y3})
    return a > 0 and b > 0 and a + b < 1


def solution(filename: str = "p102_triangles.txt") -> int:
    """
    Find the number of triangles whose interior contains the origin.
    >>> solution("test_triangles.txt")
    1
    """
    logger.error(">>> Entering solution(filename=%s)", filename, extra={"event.action": "solution", "logrite.filename": filename})
    data: str = Path(__file__).parent.joinpath(filename).read_text(encoding="utf-8")
    logger.error("solution(filename=%s): data → %s", filename, data, extra={"event.action": "solution", "logrite.filename": filename})

    triangles: list[list[int]] = []
    for line in data.strip().split("\n"):
        triangles.append([int(number) for number in line.split(",")])

    ret: int = 0
    triangle: list[int]

    for triangle in triangles:
        ret += contains_origin(*triangle)

    logger.warning("<<< Exiting solution(filename=%s)", filename, extra={"event.action": "solution", "logrite.filename": filename})
    return ret


if __name__ == "__main__":
    print(f"{solution() = }")
