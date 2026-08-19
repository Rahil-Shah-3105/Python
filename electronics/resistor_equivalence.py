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
    logger.debug(">>> Entering resistor_parallel(resistors=%s)", resistors)
    logger.debug("resistor_parallel(resistors=%s): Req → %s", resistors, Req)

    first_sum = 0.00
    logger.debug("resistor_parallel(resistors=%s): first_sum → %s", resistors, first_sum)
    for index, resistor in enumerate(resistors):
        if resistor <= 0:
            msg = f"Resistor at index {index} has a negative or zero value!"
            logger.debug("resistor_parallel(resistors=%s): msg → %s", resistors, msg)
            raise ValueError(msg)
        first_sum += 1 / float(resistor)
    logger.debug("<<< Exiting resistor_parallel(resistors=%s)", resistors)
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
    logger.debug(">>> Entering resistor_series(resistors=%s)", resistors)
    logger.debug("resistor_series(resistors=%s): Req → %s", resistors, Req)
    sum_r = 0.00
    logger.debug("resistor_series(resistors=%s): sum_r → %s", resistors, sum_r)
    for index, resistor in enumerate(resistors):
        sum_r += resistor
        if resistor < 0:
            msg = f"Resistor at index {index} has a negative value!"
            logger.debug("resistor_series(resistors=%s): msg → %s", resistors, msg)
            raise ValueError(msg)
    logger.debug("<<< Exiting resistor_series(resistors=%s)", resistors)
    return sum_r


if __name__ == "__main__":
    import doctest

    doctest.testmod()
