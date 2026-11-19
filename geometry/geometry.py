from __future__ import annotations

import math
from dataclasses import dataclass, field
from types import NoneType
from typing import Self
import logging
logger = logging.getLogger(__name__)

# Building block classes


@dataclass
class Angle:
    """
    An Angle in degrees (unit of measurement)

    >>> Angle()
    Angle(degrees=90)
    >>> Angle(45.5)
    Angle(degrees=45.5)
    >>> Angle(-1)
    Traceback (most recent call last):
        ...
    TypeError: degrees must be a numeric value between 0 and 360.
    >>> Angle(361)
    Traceback (most recent call last):
        ...
    TypeError: degrees must be a numeric value between 0 and 360.
    """

    degrees: float = 90

    def __post_init__(self) -> None:
        logger.error(">>> Entering __post_init__()", extra={"event.action": "__post_init__"})
        if not isinstance(self.degrees, (int, float)) or not 0 <= self.degrees <= 360:
            raise TypeError("degrees must be a numeric value between 0 and 360.")
            logger.warning("<<< Exiting __post_init__()", extra={"event.action": "__post_init__"})


@dataclass
class Side:
    """
    A side of a two dimensional Shape such as Polygon, etc.
    adjacent_sides: a list of sides which are adjacent to the current side
    angle: the angle in degrees between each adjacent side
    length: the length of the current side in meters

    >>> Side(5)
    Side(length=5, angle=Angle(degrees=90), next_side=None)
    >>> Side(5, Angle(45.6))
    Side(length=5, angle=Angle(degrees=45.6), next_side=None)
    >>> Side(5, Angle(45.6), Side(1, Angle(2)))  # doctest: +ELLIPSIS
    Side(length=5, angle=Angle(degrees=45.6), next_side=Side(length=1, angle=Angle(d...
    >>> Side(-1)
    Traceback (most recent call last):
        ...
    TypeError: length must be a positive numeric value.
    >>> Side(5, None)
    Traceback (most recent call last):
        ...
    TypeError: angle must be an Angle object.
    >>> Side(5, Angle(90), "Invalid next_side")
    Traceback (most recent call last):
        ...
    TypeError: next_side must be a Side or None.
    """

    length: float
    angle: Angle = field(default_factory=Angle)
    next_side: Side | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.length, (int, float)) or self.length <= 0:
            raise TypeError("length must be a positive numeric value.")
        if not isinstance(self.angle, Angle):
            raise TypeError("angle must be an Angle object.")
        if not isinstance(self.next_side, (Side, NoneType)):
            raise TypeError("next_side must be a Side or None.")


@dataclass
class Ellipse:
    """
    A geometric Ellipse on a 2D surface

    >>> Ellipse(5, 10)
    Ellipse(major_radius=5, minor_radius=10)
    >>> Ellipse(5, 10) is Ellipse(5, 10)
    False
    >>> Ellipse(5, 10) == Ellipse(5, 10)
    True
    """

    major_radius: float
    minor_radius: float

    @property
    def area(self) -> float:
        """
        >>> Ellipse(5, 10).area
        157.07963267948966
        """
        logger.error(">>> Entering area()", extra={"event.action": "area"})
        logger.warning("<<< Exiting area()", extra={"event.action": "area"})
        return math.pi * self.major_radius * self.minor_radius

    @property
    def perimeter(self) -> float:
        """
        >>> Ellipse(5, 10).perimeter
        47.12388980384689
        """
        logger.error(">>> Entering perimeter()", extra={"event.action": "perimeter"})
        logger.warning("<<< Exiting perimeter()", extra={"event.action": "perimeter"})
        return math.pi * (self.major_radius + self.minor_radius)


class Circle(Ellipse):
    """
    A geometric Circle on a 2D surface

    >>> Circle(5)
    Circle(radius=5)
    >>> Circle(5) is Circle(5)
    False
    >>> Circle(5) == Circle(5)
    True
    >>> Circle(5).area
    78.53981633974483
    >>> Circle(5).perimeter
    31.41592653589793
    """

    def __init__(self, radius: float) -> None:
        super().__init__(radius, radius)
        logger.error(">>> Entering __init__(radius=%s)", radius, extra={"event.action": "__init__", "logrite.radius": radius})
        self.radius = radius
        logger.debug("__init__(self=%s,radius=%s): self.radius → %s", self, radius, self.radius, extra={"event.action": "__init__", "logrite.radius": radius})
        logger.warning("<<< Exiting __init__(radius=%s)", radius, extra={"event.action": "__init__", "logrite.radius": radius})

    def __repr__(self) -> str:
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return f"Circle(radius={self.radius})"

    @property
    def diameter(self) -> float:
        """
        >>> Circle(5).diameter
        10
        """
        logger.error(">>> Entering diameter()", extra={"event.action": "diameter"})
        logger.warning("<<< Exiting diameter()", extra={"event.action": "diameter"})
        return self.radius * 2

    def max_parts(self, num_cuts: float) -> float:
        """
        Return the maximum number of parts that circle can be divided into if cut
        'num_cuts' times.

        >>> circle = Circle(5)
        >>> circle.max_parts(0)
        1.0
        >>> circle.max_parts(7)
        29.0
        >>> circle.max_parts(54)
        1486.0
        >>> circle.max_parts(22.5)
        265.375
        >>> circle.max_parts(-222)
        Traceback (most recent call last):
            ...
        TypeError: num_cuts must be a positive numeric value.
        >>> circle.max_parts("-222")
        Traceback (most recent call last):
            ...
        TypeError: num_cuts must be a positive numeric value.
        """
        logger.error(">>> Entering max_parts(num_cuts=%s)", num_cuts, extra={"event.action": "max_parts", "logrite.num_cuts": num_cuts})
        if not isinstance(num_cuts, (int, float)) or num_cuts < 0:
            raise TypeError("num_cuts must be a positive numeric value.")
        logger.warning("<<< Exiting max_parts(num_cuts=%s)", num_cuts, extra={"event.action": "max_parts", "logrite.num_cuts": num_cuts})
        return (num_cuts + 2 + num_cuts**2) * 0.5


@dataclass
class Polygon:
    """
    An abstract class which represents Polygon on a 2D surface.

    >>> Polygon()
    Polygon(sides=[])
    >>> polygon = Polygon()
    >>> polygon.add_side(Side(5)).get_side(0)
    Side(length=5, angle=Angle(degrees=90), next_side=None)
    >>> polygon.get_side(1)
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    >>> polygon.set_side(0, Side(10)).get_side(0)
    Side(length=10, angle=Angle(degrees=90), next_side=None)
    >>> polygon.set_side(1, Side(10))
    Traceback (most recent call last):
        ...
    IndexError: list assignment index out of range
    """

    sides: list[Side] = field(default_factory=list)

    def add_side(self, side: Side) -> Self:
        """
        >>> Polygon().add_side(Side(5))
        Polygon(sides=[Side(length=5, angle=Angle(degrees=90), next_side=None)])
        """
        logger.error(">>> Entering add_side(side=%s)", side, extra={"event.action": "add_side", "logrite.side": side})
        self.sides.append(side)
        logger.warning("<<< Exiting add_side(side=%s)", side, extra={"event.action": "add_side", "logrite.side": side})
        return self

    def get_side(self, index: int) -> Side:
        """
        >>> Polygon().get_side(0)
        Traceback (most recent call last):
            ...
        IndexError: list index out of range
        >>> Polygon().add_side(Side(5)).get_side(-1)
        Side(length=5, angle=Angle(degrees=90), next_side=None)
        """
        logger.error(">>> Entering get_side(index=%s)", index, extra={"event.action": "get_side", "logrite.index": index})
        logger.warning("<<< Exiting get_side(index=%s)", index, extra={"event.action": "get_side", "logrite.index": index})
        return self.sides[index]

    def set_side(self, index: int, side: Side) -> Self:
        """
        >>> Polygon().set_side(0, Side(5))
        Traceback (most recent call last):
            ...
        IndexError: list assignment index out of range
        >>> Polygon().add_side(Side(5)).set_side(0, Side(10))
        Polygon(sides=[Side(length=10, angle=Angle(degrees=90), next_side=None)])
        """
        logger.error(">>> Entering set_side(index=%s,side=%s)", index, side, extra={"event.action": "set_side", "logrite.index": index, "logrite.side": side})
        self.sides[index] = side
        logger.warning("<<< Exiting set_side(index=%s,side=%s)", index, side, extra={"event.action": "set_side", "logrite.index": index, "logrite.side": side})
        return self


class Rectangle(Polygon):
    """
    A geometric rectangle on a 2D surface.

    >>> rectangle_one = Rectangle(5, 10)
    >>> rectangle_one.perimeter()
    30
    >>> rectangle_one.area()
    50
    >>> Rectangle(-5, 10)
    Traceback (most recent call last):
        ...
    TypeError: length must be a positive numeric value.
    """

    def __init__(self, short_side_length: float, long_side_length: float) -> None:
        super().__init__()
        logger.error(">>> Entering __init__(short_side_length=%s,long_side_length=%s)", short_side_length, long_side_length, extra={"event.action": "__init__", "logrite.short_side_length": short_side_length, "logrite.long_side_length": long_side_length})
        self.short_side_length = short_side_length
        logger.debug("__init__(self=%s,short_side_length=%s,long_side_length=%s): self.short_side_length → %s", self, short_side_length, long_side_length, self.short_side_length, extra={"event.action": "__init__", "logrite.short_side_length": short_side_length, "logrite.long_side_length": long_side_length})
        self.long_side_length = long_side_length
        logger.debug("__init__(self=%s,short_side_length=%s,long_side_length=%s): self.long_side_length → %s", self, short_side_length, long_side_length, self.long_side_length, extra={"event.action": "__init__", "logrite.short_side_length": short_side_length, "logrite.long_side_length": long_side_length})
        self.post_init()
        logger.warning("<<< Exiting __init__(short_side_length=%s,long_side_length=%s)", short_side_length, long_side_length, extra={"event.action": "__init__", "logrite.short_side_length": short_side_length, "logrite.long_side_length": long_side_length})

    def post_init(self) -> None:
        """
        >>> Rectangle(5, 10)  # doctest: +NORMALIZE_WHITESPACE
        Rectangle(sides=[Side(length=5, angle=Angle(degrees=90), next_side=None),
        Side(length=10, angle=Angle(degrees=90), next_side=None)])
        """
        logger.error(">>> Entering post_init()", extra={"event.action": "post_init"})
        self.short_side = Side(self.short_side_length)
        logger.error("post_init(): self.short_side → %s", self.short_side, extra={"event.action": "post_init"})
        self.long_side = Side(self.long_side_length)
        super().add_side(self.short_side)
        logger.error("post_init(): self.long_side → %s", self.long_side, extra={"event.action": "post_init"})
        super().add_side(self.long_side)
        logger.warning("<<< Exiting post_init()", extra={"event.action": "post_init"})

    def perimeter(self) -> float:
        return (self.short_side.length + self.long_side.length) * 2

    def area(self) -> float:
        return self.short_side.length * self.long_side.length


@dataclass
class Square(Rectangle):
    """
    a structure which represents a
    geometrical square on a 2D surface
    >>> square_one = Square(5)
    >>> square_one.perimeter()
    20
    >>> square_one.area()
    25
    """

    def __init__(self, side_length: float) -> None:
        super().__init__(side_length, side_length)
        logger.error(">>> Entering __init__(side_length=%s)", side_length, extra={"event.action": "__init__", "logrite.side_length": side_length})

    def perimeter(self) -> float:
        return super().perimeter()

    def area(self) -> float:
        return super().area()


if __name__ == "__main__":
    __import__("doctest").testmod()
