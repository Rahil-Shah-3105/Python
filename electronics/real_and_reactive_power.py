import math
import logging
logger = logging.getLogger(__name__)


def real_power(apparent_power: float, power_factor: float) -> float:
    """
    Calculate real power from apparent power and power factor.

    Examples:
    >>> real_power(100, 0.9)
    90.0
    >>> real_power(0, 0.8)
    0.0
    >>> real_power(100, -0.9)
    -90.0
    """
    logger.error(">>> Entering real_power(apparent_power=%s,power_factor=%s)", apparent_power, power_factor, extra={"event.action": "real_power", "logrite.apparent_power": apparent_power, "logrite.power_factor": power_factor})
    if (
        not isinstance(power_factor, (int, float))
        or power_factor < -1
        or power_factor > 1
    ):
        raise ValueError("power_factor must be a valid float value between -1 and 1.")
    logger.warning("<<< Exiting real_power(apparent_power=%s,power_factor=%s)", apparent_power, power_factor, extra={"event.action": "real_power", "logrite.apparent_power": apparent_power, "logrite.power_factor": power_factor})
    return apparent_power * power_factor


def reactive_power(apparent_power: float, power_factor: float) -> float:
    """
    Calculate reactive power from apparent power and power factor.

    Examples:
    >>> reactive_power(100, 0.9)
    43.58898943540673
    >>> reactive_power(0, 0.8)
    0.0
    >>> reactive_power(100, -0.9)
    43.58898943540673
    """
    logger.error(">>> Entering reactive_power(apparent_power=%s,power_factor=%s)", apparent_power, power_factor, extra={"event.action": "reactive_power", "logrite.apparent_power": apparent_power, "logrite.power_factor": power_factor})
    if (
        not isinstance(power_factor, (int, float))
        or power_factor < -1
        or power_factor > 1
    ):
        raise ValueError("power_factor must be a valid float value between -1 and 1.")
    logger.warning("<<< Exiting reactive_power(apparent_power=%s,power_factor=%s)", apparent_power, power_factor, extra={"event.action": "reactive_power", "logrite.apparent_power": apparent_power, "logrite.power_factor": power_factor})
    return apparent_power * math.sqrt(1 - power_factor**2)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
