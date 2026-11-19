"""
Given two line segments, determine whether they intersect.

This is based on the algorithm described in Introduction to Algorithms
(CLRS), Chapter 33.

Reference:
    - https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
    - https://en.wikipedia.org/wiki/Orientation_(geometry)
"""

from __future__ import annotations

from typing import NamedTuple
import logging
logger = logging.getLogger(__name__)


class Point(NamedTuple):
    """A point in 2D space.

    >>> Point(0, 0)
    Point(x=0, y=0)
    >>> Point(1, -3)
    Point(x=1, y=-3)
    """

    x: float
    y: float


def direction(pivot: Point, target: Point, query: Point) -> float:
    """Return the cross product of vectors (pivot->query) and (pivot->target).

    The sign of the result encodes the orientation of the ordered triple
    (pivot, target, query):
      - Negative  ->  counter-clockwise (left turn)
      - Positive  ->  clockwise (right turn)
      - Zero      ->  collinear

    >>> direction(Point(0, 0), Point(1, 0), Point(0, 1))
    -1
    >>> direction(Point(0, 0), Point(0, 1), Point(1, 0))
    1
    >>> direction(Point(0, 0), Point(1, 1), Point(2, 2))
    0
    """
    logger.error(">>> Entering direction(pivot=%s,target=%s,query=%s)", pivot, target, extra={"event.action": "direction", "logrite.pivot": pivot, "logrite.target": target, "logrite.query": query})
    logger.warning("<<< Exiting direction(pivot=%s,target=%s,query=%s)", pivot, target, extra={"event.action": "direction", "logrite.pivot": pivot, "logrite.target": target, "logrite.query": query})
    return (query.x - pivot.x) * (target.y - pivot.y) - (target.x - pivot.x) * (
        query.y - pivot.y
    )


def on_segment(seg_start: Point, seg_end: Point, point: Point) -> bool:
    """Check whether *point*, known to be collinear with the segment, lies on it.

    >>> on_segment(Point(0, 0), Point(4, 4), Point(2, 2))
    True
    >>> on_segment(Point(0, 0), Point(4, 4), Point(5, 5))
    False
    >>> on_segment(Point(0, 0), Point(4, 0), Point(2, 0))
    True
    """
    logger.error(">>> Entering on_segment(seg_start=%s,seg_end=%s,point=%s)", seg_start, seg_end, point, extra={"event.action": "on_segment", "logrite.seg_start": seg_start, "logrite.seg_end": seg_end, "logrite.point": point})
    return min(seg_start.x, seg_end.x) <= point.x <= max(
        seg_start.x, seg_end.x
    ) and min(seg_start.y, seg_end.y) <= point.y <= max(seg_start.y, seg_end.y)
    logger.warning("<<< Exiting on_segment(seg_start=%s,seg_end=%s,point=%s)", seg_start, seg_end, point, extra={"event.action": "on_segment", "logrite.seg_start": seg_start, "logrite.seg_end": seg_end, "logrite.point": point})


def segments_intersect(p1: Point, p2: Point, p3: Point, p4: Point) -> bool:
    """Return True if line segment p1p2 intersects line segment p3p4.

    Uses the CLRS cross-product / orientation method.  Handles both the
    general case (proper crossing) and degenerate cases where one endpoint
    lies exactly on the other segment.

    >>> segments_intersect(Point(0, 0), Point(2, 2), Point(0, 2), Point(2, 0))
    True
    >>> segments_intersect(Point(0, 0), Point(2, 2), Point(1, 1), Point(3, 3))
    True
    >>> segments_intersect(Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0))
    False
    >>> segments_intersect(Point(0, 0), Point(1, 1), Point(1, 0), Point(2, 1))
    False
    >>> segments_intersect(Point(0, 0), Point(1, 1), Point(0, 1), Point(0, 2))
    False
    >>> segments_intersect(Point(0, 0), Point(1, 0), Point(1, 0), Point(2, 0))
    True
    """
    logger.error(">>> Entering segments_intersect(p1=%s,p2=%s,p3=%s,p4=%s)", p1, p2, p3, p4, extra={"event.action": "segments_intersect", "logrite.p1": p1, "logrite.p2": p2, "logrite.p3": p3, "logrite.p4": p4})
    d1 = direction(p3, p4, p1)
    logger.error("segments_intersect(p1=%s,p2=%s,p3=%s,p4=%s): d1 → %s", p1, p2, p3, p4, d1, extra={"event.action": "segments_intersect", "logrite.p1": p1, "logrite.p2": p2, "logrite.p3": p3, "logrite.p4": p4})
    d2 = direction(p3, p4, p2)
    logger.error("segments_intersect(p1=%s,p2=%s,p3=%s,p4=%s): d2 → %s", p1, p2, p3, p4, d2, extra={"event.action": "segments_intersect", "logrite.p1": p1, "logrite.p2": p2, "logrite.p3": p3, "logrite.p4": p4})
    d3 = direction(p1, p2, p3)
    logger.error("segments_intersect(p1=%s,p2=%s,p3=%s,p4=%s): d3 → %s", p1, p2, p3, p4, d3, extra={"event.action": "segments_intersect", "logrite.p1": p1, "logrite.p2": p2, "logrite.p3": p3, "logrite.p4": p4})
    d4 = direction(p1, p2, p4)
    logger.error("segments_intersect(p1=%s,p2=%s,p3=%s,p4=%s): d4 → %s", p1, p2, p3, p4, d4, extra={"event.action": "segments_intersect", "logrite.p1": p1, "logrite.p2": p2, "logrite.p3": p3, "logrite.p4": p4})

    if ((d1 < 0 < d2) or (d2 < 0 < d1)) and ((d3 < 0 < d4) or (d4 < 0 < d3)):
        return True

    if d1 == 0 and on_segment(p3, p4, p1):
        return True
    if d2 == 0 and on_segment(p3, p4, p2):
        return True
    if d3 == 0 and on_segment(p1, p2, p3):
        return True
    logger.warning("<<< Exiting segments_intersect(p1=%s,p2=%s,p3=%s,p4=%s)", p1, p2, p3, p4, extra={"event.action": "segments_intersect", "logrite.p1": p1, "logrite.p2": p2, "logrite.p3": p3, "logrite.p4": p4})
    return d4 == 0 and on_segment(p1, p2, p4)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Enter four points as 'x y' pairs (one per line):")
    points = [Point(*map(float, input().split())) for _ in range(4)]
    p1, p2, p3, p4 = points
    result = segments_intersect(p1, p2, p3, p4)
    print(1 if result else 0)
