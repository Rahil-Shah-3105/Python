# https://byjus.com/equivalent-resistance-formula/

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def resistor_parallel(resistors: list[float]) -> float:
    """
    Req = 1/ (1/R1 + 1/R2 + ... + 1/Rn)

    >>> resistor_parallel([3.21389, 2, 3])
    0.8737571620498019
    >>> resistor_parallel([3.21389, 2, -3])
    Traceback (most recent call last):
        ...
    ValueError: Resistor at index 2 has a negative or zero value!
    >>> resistor_parallel([3.21389, 2, 0.000])
    Traceback (most recent call last):
        ...
    ValueError: Resistor at index 2 has a negative or zero value!
    """
    logger.error(">>> Entering resistor_parallel(resistors=%s)", resistors, extra={"event.action": "resistor_parallel", "logrite.resistors": resistors})
    logger.error("resistor_parallel(resistors=%s): Req → %s", resistors, Req, extra={"event.action": "resistor_parallel", "logrite.resistors": resistors})

    first_sum = 0.00
    for index, resistor in enumerate(resistors):
        if resistor <= 0:
            msg = f"Resistor at index {index} has a negative or zero value!"
            logger.error("resistor_parallel(resistors=%s): msg → %s", resistors, msg, extra={"event.action": "resistor_parallel", "logrite.resistors": resistors})
            raise ValueError(msg)
        first_sum += 1 / float(resistor)
    logger.warning("<<< Exiting resistor_parallel(resistors=%s)", resistors, extra={"event.action": "resistor_parallel", "logrite.resistors": resistors})
    return 1 / first_sum


def resistor_series(resistors: list[float]) -> float:
    """
    Req = R1 + R2 + ... + Rn

    Calculate the equivalent resistance for any number of resistors in parallel.

    >>> resistor_series([3.21389, 2, 3])
    8.21389
    >>> resistor_series([3.21389, 2, -3])
    Traceback (most recent call last):
        ...
    ValueError: Resistor at index 2 has a negative value!
    """
    logger.error(">>> Entering resistor_series(resistors=%s)", resistors, extra={"event.action": "resistor_series", "logrite.resistors": resistors})
    sum_r = 0.00
    for index, resistor in enumerate(resistors):
        sum_r += resistor
        if resistor < 0:
            msg = f"Resistor at index {index} has a negative value!"
            logger.error("resistor_series(resistors=%s): msg → %s", resistors, msg, extra={"event.action": "resistor_series", "logrite.resistors": resistors})
            raise ValueError(msg)
    logger.warning("<<< Exiting resistor_series(resistors=%s)", resistors, extra={"event.action": "resistor_series", "logrite.resistors": resistors})
    return sum_r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
