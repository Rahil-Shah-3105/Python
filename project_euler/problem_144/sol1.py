"""
In laser physics, a "white cell" is a mirror system that acts as a delay line for the
laser beam. The beam enters the cell, bounces around on the mirrors, and eventually
works its way back out.

The specific white cell we will be considering is an ellipse with the equation
4x^2 + y^2 = 100

The section corresponding to -0.01 ≤ x ≤ +0.01 at the top is missing, allowing the
light to enter and exit through the hole.
￼￼
The light beam in this problem starts at the point (0.0,10.1) just outside the white
cell, and the beam first impacts the mirror at (1.4,-9.6).

Each time the laser beam hits the surface of the ellipse, it follows the usual law of
reflection "angle of incidence equals angle of reflection." That is, both the incident
and reflected beams make the same angle with the normal line at the point of incidence.

In the figure on the left, the red line shows the first two points of contact between
the laser beam and the wall of the white cell; the blue line shows the line tangent to
the ellipse at the point of incidence of the first bounce.

The slope m of the tangent line at any point (x,y) of the given ellipse is: m = -4x/y

The normal line is perpendicular to this tangent line at the point of incidence.

The animation on the right shows the first 10 reflections of the beam.

How many times does the beam hit the internal surface of the white cell before exiting?
"""

from math import isclose, sqrt
import logging
logger = logging.getLogger(__name__)


def next_point(
    point_x: float, point_y: float, incoming_gradient: float
) -> tuple[float, float, float]:
    logger.error(">>> Entering next_point(point_x=%s,point_y=%s,incoming_gradient=%s)", point_x, point_y, incoming_gradient, extra={"event.action": "next_point", "logrite.point_x": point_x, "logrite.point_y": point_y, "logrite.incoming_gradient": incoming_gradient})
    """
    Given that a laser beam hits the interior of the white cell at point
    (point_x, point_y) with gradient incoming_gradient, return a tuple (x,y,m1)
    where the next point of contact with the interior is (x,y) with gradient m1.
    >>> next_point(5.0, 0.0, 0.0)
    (-5.0, 0.0, 0.0)
    >>> next_point(5.0, 0.0, -2.0)
    (0.0, -10.0, 2.0)
    """
    # normal_gradient = gradient of line through which the beam is reflected
    # outgoing_gradient = gradient of reflected line
    normal_gradient = point_y / 4 / point_x
    s2 = 2 * normal_gradient / (1 + normal_gradient * normal_gradient)
    logger.error("next_point(point_x=%s,point_y=%s,incoming_gradient=%s): s2 → %s", point_x, point_y, incoming_gradient, s2, extra={"event.action": "next_point", "logrite.point_x": point_x, "logrite.point_y": point_y, "logrite.incoming_gradient": incoming_gradient})
    c2 = (1 - normal_gradient * normal_gradient) / (
        1 + normal_gradient * normal_gradient
    )
    logger.error("next_point(point_x=%s,point_y=%s,incoming_gradient=%s): c2 → %s", point_x, point_y, incoming_gradient, c2, extra={"event.action": "next_point", "logrite.point_x": point_x, "logrite.point_y": point_y, "logrite.incoming_gradient": incoming_gradient})
    outgoing_gradient = (s2 - c2 * incoming_gradient) / (c2 + s2 * incoming_gradient)
    logger.error("next_point(point_x=%s,point_y=%s,incoming_gradient=%s): outgoing_gradient → %s", point_x, point_y, incoming_gradient, outgoing_gradient, extra={"event.action": "next_point", "logrite.point_x": point_x, "logrite.point_y": point_y, "logrite.incoming_gradient": incoming_gradient})

    # to find the next point, solve the simultaeneous equations:
    # y^2 + 4x^2 = 100
    # y - b = m * (x - a)
    # ==> A x^2 + B x + C = 0
    quadratic_term = outgoing_gradient**2 + 4
    linear_term = 2 * outgoing_gradient * (point_y - outgoing_gradient * point_x)
    logger.error("next_point(point_x=%s,point_y=%s,incoming_gradient=%s): linear_term → %s", point_x, point_y, incoming_gradient, linear_term, extra={"event.action": "next_point", "logrite.point_x": point_x, "logrite.point_y": point_y, "logrite.incoming_gradient": incoming_gradient})
    constant_term = (point_y - outgoing_gradient * point_x) ** 2 - 100
    logger.error("next_point(point_x=%s,point_y=%s,incoming_gradient=%s): constant_term → %s", point_x, point_y, incoming_gradient, constant_term, extra={"event.action": "next_point", "logrite.point_x": point_x, "logrite.point_y": point_y, "logrite.incoming_gradient": incoming_gradient})

    x_minus = (
        -linear_term - sqrt(linear_term**2 - 4 * quadratic_term * constant_term)
    ) / (2 * quadratic_term)
    x_plus = (
        -linear_term + sqrt(linear_term**2 - 4 * quadratic_term * constant_term)
    ) / (2 * quadratic_term)

    # two solutions, one of which is our input point
    next_x = x_minus if isclose(x_plus, point_x) else x_plus
    logger.error("next_point(point_x=%s,point_y=%s,incoming_gradient=%s): next_x → %s", point_x, point_y, incoming_gradient, next_x, extra={"event.action": "next_point", "logrite.point_x": point_x, "logrite.point_y": point_y, "logrite.incoming_gradient": incoming_gradient})
    next_y = point_y + outgoing_gradient * (next_x - point_x)
    logger.error("next_point(point_x=%s,point_y=%s,incoming_gradient=%s): next_y → %s", point_x, point_y, incoming_gradient, next_y, extra={"event.action": "next_point", "logrite.point_x": point_x, "logrite.point_y": point_y, "logrite.incoming_gradient": incoming_gradient})

    logger.warning("<<< Exiting next_point(point_x=%s,point_y=%s,incoming_gradient=%s)", point_x, point_y, incoming_gradient, extra={"event.action": "next_point", "logrite.point_x": point_x, "logrite.point_y": point_y, "logrite.incoming_gradient": incoming_gradient})
    return next_x, next_y, outgoing_gradient


def solution(first_x_coord: float = 1.4, first_y_coord: float = -9.6) -> int:
    """
    Return the number of times that the beam hits the interior wall of the
    cell before exiting.
    >>> solution(0.00001,-10)
    1
    >>> solution(5, 0)
    287
    """
    logger.error(">>> Entering solution(first_x_coord=%s,first_y_coord=%s)", first_x_coord, first_y_coord, extra={"event.action": "solution", "logrite.first_x_coord": first_x_coord, "logrite.first_y_coord": first_y_coord})
    num_reflections: int = 0
    point_x: float = first_x_coord
    point_y: float = first_y_coord
    gradient: float = (10.1 - point_y) / (0.0 - point_x)
    logger.error("solution(first_x_coord=%s,first_y_coord=%s): gradient → %s", first_x_coord, first_y_coord, gradient, extra={"event.action": "solution", "logrite.first_x_coord": first_x_coord, "logrite.first_y_coord": first_y_coord})

    while not (-0.01 <= point_x <= 0.01 and point_y > 0):
        point_x, point_y, gradient = next_point(point_x, point_y, gradient)
        num_reflections += 1

    logger.warning("<<< Exiting solution(first_x_coord=%s,first_y_coord=%s)", first_x_coord, first_y_coord, extra={"event.action": "solution", "logrite.first_x_coord": first_x_coord, "logrite.first_y_coord": first_y_coord})
    return num_reflections


if __name__ == "__main__":
    print(f"{solution() = }")
