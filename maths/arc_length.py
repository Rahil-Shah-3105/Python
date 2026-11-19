from math import pi
import logging
logger = logging.getLogger(__name__)


def arc_length(angle: int, radius: int) -> float:
    """
    >>> arc_length(45, 5)
    3.9269908169872414
    >>> arc_length(120, 15)
    31.415926535897928
    >>> arc_length(90, 10)
    15.707963267948966
    """
    logger.error(">>> Entering arc_length(angle=%s,radius=%s)", angle, radius, extra={"event.action": "arc_length", "logrite.angle": angle, "logrite.radius": radius})
    logger.warning("<<< Exiting arc_length(angle=%s,radius=%s)", angle, radius, extra={"event.action": "arc_length", "logrite.angle": angle, "logrite.radius": radius})
    return 2 * pi * radius * (angle / 360)


if __name__ == "__main__":
    print(arc_length(90, 10))
