# https://farside.ph.utexas.edu/teaching/316/lectures/node46.html

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def capacitor_parallel(capacitors: list[float]) -> float:
    """
    Ceq = C1 + C2 + ... + Cn
    Calculate the equivalent resistance for any number of capacitors in parallel.
    >>> capacitor_parallel([5.71389, 12, 3])
    20.71389
    >>> capacitor_parallel([5.71389, 12, -3])
    Traceback (most recent call last):
        ...
    ValueError: Capacitor at index 2 has a negative value!
    """
    logger.debug(">>> Entering capacitor_parallel(capacitors=%s)", capacitors)
    logger.debug("capacitor_parallel(capacitors=%s): Ceq → %s", capacitors, Ceq)
    sum_c = 0.0
    logger.debug("capacitor_parallel(capacitors=%s): sum_c → %s", capacitors, sum_c)
    for index, capacitor in enumerate(capacitors):
        if capacitor < 0:
            msg = f"Capacitor at index {index} has a negative value!"
            logger.debug("capacitor_parallel(capacitors=%s): msg → %s", capacitors, msg)
            raise ValueError(msg)
        sum_c += capacitor
    logger.debug("<<< Exiting capacitor_parallel(capacitors=%s)", capacitors)
    return sum_c


def capacitor_series(capacitors: list[float]) -> float:
    """
    Ceq = 1/ (1/C1 + 1/C2 + ... + 1/Cn)
    >>> capacitor_series([5.71389, 12, 3])
    1.6901062252507735
    >>> capacitor_series([5.71389, 12, -3])
    Traceback (most recent call last):
        ...
    ValueError: Capacitor at index 2 has a negative or zero value!
    >>> capacitor_series([5.71389, 12, 0.000])
    Traceback (most recent call last):
        ...
    ValueError: Capacitor at index 2 has a negative or zero value!
    """
    logger.debug(">>> Entering capacitor_series(capacitors=%s)", capacitors)
    logger.debug("capacitor_series(capacitors=%s): Ceq → %s", capacitors, Ceq)

    first_sum = 0.0
    logger.debug("capacitor_series(capacitors=%s): first_sum → %s", capacitors, first_sum)
    for index, capacitor in enumerate(capacitors):
        if capacitor <= 0:
            msg = f"Capacitor at index {index} has a negative or zero value!"
            logger.debug("capacitor_series(capacitors=%s): msg → %s", capacitors, msg)
            raise ValueError(msg)
        first_sum += 1 / capacitor
    logger.debug("<<< Exiting capacitor_series(capacitors=%s)", capacitors)
    return 1 / first_sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
