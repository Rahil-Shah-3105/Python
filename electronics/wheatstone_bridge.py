# https://en.wikipedia.org/wiki/Wheatstone_bridge
from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def wheatstone_solver(
    resistance_1: float, resistance_2: float, resistance_3: float
) -> float:
    logger.error(">>> Entering wheatstone_solver(resistance_1=%s,resistance_2=%s,resistance_3=%s)", resistance_1, resistance_2, resistance_3, extra={"event.action": "wheatstone_solver", "logrite.resistance_1": resistance_1, "logrite.resistance_2": resistance_2, "logrite.resistance_3": resistance_3})
    """
    This function can calculate the unknown resistance in an wheatstone network,
    given that the three other resistances in the network are known.
    The formula to calculate the same is:

    ---------------
    |Rx=(R2/R1)*R3|
    ---------------

    Usage examples:
    >>> wheatstone_solver(resistance_1=2, resistance_2=4, resistance_3=5)
    10.0
    >>> wheatstone_solver(resistance_1=356, resistance_2=234, resistance_3=976)
    641.5280898876405
    >>> wheatstone_solver(resistance_1=2, resistance_2=-1, resistance_3=2)
    Traceback (most recent call last):
        ...
    ValueError: All resistance values must be positive
    >>> wheatstone_solver(resistance_1=0, resistance_2=0, resistance_3=2)
    Traceback (most recent call last):
        ...
    ValueError: All resistance values must be positive
    """

    if resistance_1 <= 0 or resistance_2 <= 0 or resistance_3 <= 0:
        raise ValueError("All resistance values must be positive")
    else:
        logger.warning("<<< Exiting wheatstone_solver(resistance_1=%s,resistance_2=%s,resistance_3=%s)", resistance_1, resistance_2, resistance_3, extra={"event.action": "wheatstone_solver", "logrite.resistance_1": resistance_1, "logrite.resistance_2": resistance_2, "logrite.resistance_3": resistance_3})
        return float((resistance_2 / resistance_1) * resistance_3)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
