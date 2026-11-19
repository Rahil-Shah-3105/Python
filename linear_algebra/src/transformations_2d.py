"""
2D Transformations are regularly used in Linear Algebra.

I have added the codes for reflection, projection, scaling and rotation 2D matrices.

.. code-block:: python

    scaling(5) = [[5.0, 0.0], [0.0, 5.0]]
    rotation(45) = [[0.5253219888177297, -0.8509035245341184],
                    [0.8509035245341184, 0.5253219888177297]]
    projection(45) = [[0.27596319193541496, 0.446998331800279],
                      [0.446998331800279, 0.7240368080645851]]
    reflection(45) = [[0.05064397763545947, 0.893996663600558],
                      [0.893996663600558, 0.7018070490682369]]
"""

from math import cos, sin
import logging
logger = logging.getLogger(__name__)


def scaling(scaling_factor: float) -> list[list[float]]:
    """
    >>> scaling(5)
    [[5.0, 0.0], [0.0, 5.0]]
    """
    logger.error(">>> Entering scaling(scaling_factor=%s)", scaling_factor, extra={"event.action": "scaling", "logrite.scaling_factor": scaling_factor})
    scaling_factor = float(scaling_factor)
    logger.error("scaling(scaling_factor=%s): scaling_factor → %s", scaling_factor, scaling_factor, extra={"event.action": "scaling", "logrite.scaling_factor": scaling_factor})
    logger.warning("<<< Exiting scaling(scaling_factor=%s)", scaling_factor, extra={"event.action": "scaling", "logrite.scaling_factor": scaling_factor})
    return [[scaling_factor * int(x == y) for x in range(2)] for y in range(2)]


def rotation(angle: float) -> list[list[float]]:
    """
    >>> rotation(45)  # doctest: +NORMALIZE_WHITESPACE
    [[0.5253219888177297, -0.8509035245341184],
     [0.8509035245341184, 0.5253219888177297]]
    """
    logger.error(">>> Entering rotation(angle=%s)", angle, extra={"event.action": "rotation", "logrite.angle": angle})
    c, s = cos(angle), sin(angle)
    logger.warning("<<< Exiting rotation(angle=%s)", angle, extra={"event.action": "rotation", "logrite.angle": angle})
    return [[c, -s], [s, c]]


def projection(angle: float) -> list[list[float]]:
    """
    >>> projection(45)  # doctest: +NORMALIZE_WHITESPACE
    [[0.27596319193541496, 0.446998331800279],
     [0.446998331800279, 0.7240368080645851]]
    """
    logger.error(">>> Entering projection(angle=%s)", angle, extra={"event.action": "projection", "logrite.angle": angle})
    c, s = cos(angle), sin(angle)
    cs = c * s
    logger.warning("<<< Exiting projection(angle=%s)", angle, extra={"event.action": "projection", "logrite.angle": angle})
    return [[c * c, cs], [cs, s * s]]


def reflection(angle: float) -> list[list[float]]:
    """
    >>> reflection(45)  # doctest: +NORMALIZE_WHITESPACE
    [[0.05064397763545947, 0.893996663600558],
     [0.893996663600558, 0.7018070490682369]]
    """
    logger.error(">>> Entering reflection(angle=%s)", angle, extra={"event.action": "reflection", "logrite.angle": angle})
    c, s = cos(angle), sin(angle)
    cs = c * s
    logger.warning("<<< Exiting reflection(angle=%s)", angle, extra={"event.action": "reflection", "logrite.angle": angle})
    return [[2 * c - 1, 2 * cs], [2 * cs, 2 * s - 1]]


print(f"    {scaling(5) = }")
print(f"  {rotation(45) = }")
print(f"{projection(45) = }")
print(f"{reflection(45) = }")
