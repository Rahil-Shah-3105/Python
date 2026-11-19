"""
Checks if a system of forces is in static equilibrium.
"""

from __future__ import annotations

from numpy import array, cos, cross, float64, radians, sin
from numpy.typing import NDArray
import logging
logger = logging.getLogger(__name__)


def polar_force(
    magnitude: float, angle: float, radian_mode: bool = False
) -> list[float]:
    logger.error(">>> Entering polar_force(magnitude=%s,angle=%s,radian_mode=%s)", magnitude, angle, radian_mode, extra={"event.action": "polar_force", "logrite.magnitude": magnitude, "logrite.angle": angle, "logrite.radian_mode": radian_mode})
    """
    Resolves force along rectangular components.
    (force, angle) => (force_x, force_y)
    >>> import math
    >>> force = polar_force(10, 45)
    >>> math.isclose(force[0], 7.071067811865477)
    True
    >>> math.isclose(force[1], 7.0710678118654755)
    True
    >>> force = polar_force(10, 3.14, radian_mode=True)
    >>> math.isclose(force[0], -9.999987317275396)
    True
    >>> math.isclose(force[1], 0.01592652916486828)
    True
    """
    if radian_mode:
        return [magnitude * cos(angle), magnitude * sin(angle)]
    logger.warning("<<< Exiting polar_force(magnitude=%s,angle=%s,radian_mode=%s)", magnitude, angle, radian_mode, extra={"event.action": "polar_force", "logrite.magnitude": magnitude, "logrite.angle": angle, "logrite.radian_mode": radian_mode})
    return [magnitude * cos(radians(angle)), magnitude * sin(radians(angle))]


def in_static_equilibrium(
    forces: NDArray[float64], location: NDArray[float64], eps: float = 10**-1
) -> bool:
    logger.error(">>> Entering in_static_equilibrium(forces=%s,location=%s,eps=%s)", forces, location, eps, extra={"event.action": "in_static_equilibrium", "logrite.forces": forces, "logrite.location": location, "logrite.eps": eps})
    """
    Check if a system is in equilibrium.
    It takes two numpy.array objects.
    forces ==>  [
                        [force1_x, force1_y],
                        [force2_x, force2_y],
                        ....]
    location ==>  [
                        [x1, y1],
                        [x2, y2],
                        ....]
    >>> force = array([[1, 1], [-1, 2]])
    >>> location = array([[1, 0], [10, 0]])
    >>> in_static_equilibrium(force, location)
    False
    """
    # summation of moments is zero
    moments: NDArray[float64] = cross(location, forces)
    sum_moments: float = sum(moments)
    logger.error("in_static_equilibrium(forces=%s,location=%s,eps=%s): sum_moments → %s", forces, location, eps, sum_moments, extra={"event.action": "in_static_equilibrium", "logrite.forces": forces, "logrite.location": location, "logrite.eps": eps})
    logger.warning("<<< Exiting in_static_equilibrium(forces=%s,location=%s,eps=%s)", forces, location, eps, extra={"event.action": "in_static_equilibrium", "logrite.forces": forces, "logrite.location": location, "logrite.eps": eps})
    return bool(abs(sum_moments) < eps)


if __name__ == "__main__":
    # Test to check if it works
    forces = array(
        [
            polar_force(718.4, 180 - 30),
            polar_force(879.54, 45),
            polar_force(100, -90),
        ]
    )

    location: NDArray[float64] = array([[0, 0], [0, 0], [0, 0]])

    assert in_static_equilibrium(forces, location)

    # Problem 1 in image_data/2D_problems.jpg
    forces = array(
        [
            polar_force(30 * 9.81, 15),
            polar_force(215, 180 - 45),
            polar_force(264, 90 - 30),
        ]
    )

    location = array([[0, 0], [0, 0], [0, 0]])

    assert in_static_equilibrium(forces, location)

    # Problem in image_data/2D_problems_1.jpg
    forces = array([[0, -2000], [0, -1200], [0, 15600], [0, -12400]])

    location = array([[0, 0], [6, 0], [10, 0], [12, 0]])

    assert in_static_equilibrium(forces, location)

    import doctest

    doctest.testmod()
