"""
The ideal gas law, also called the general gas equation, is the
equation of state of a hypothetical ideal gas. It is a good approximation
of the behavior of many gases under many conditions, although it has
several limitations. It was first stated by Benoît Paul Émile Clapeyron
in 1834 as a combination of the empirical Boyle's law, Charles's law,
Avogadro's law, and Gay-Lussac's law.[1] The ideal gas law is often written
in an empirical form:
 ------------
 | PV = nRT |
 ------------
P	=	Pressure (Pa)
V	=	Volume (m^3)
n	=	Amount of substance (mol)
R	=	Universal gas constant
T	=	Absolute temperature (Kelvin)

(Description adapted from https://en.wikipedia.org/wiki/Ideal_gas_law )
"""
import logging
logger = logging.getLogger(__name__)

UNIVERSAL_GAS_CONSTANT = 8.314462  # Unit - J mol-1 K-1


def pressure_of_gas_system(moles: float, kelvin: float, volume: float) -> float:
    """
    >>> pressure_of_gas_system(2, 100, 5)
    332.57848
    >>> pressure_of_gas_system(0.5, 273, 0.004)
    283731.01575
    >>> pressure_of_gas_system(3, -0.46, 23.5)
    Traceback (most recent call last):
        ...
    ValueError: Invalid inputs. Enter positive value.
    """
    logger.error(">>> Entering pressure_of_gas_system(moles=%s,kelvin=%s,volume=%s)", moles, kelvin, volume, extra={"event.action": "pressure_of_gas_system", "logrite.moles": moles, "logrite.kelvin": kelvin, "logrite.volume": volume})
    if moles < 0 or kelvin < 0 or volume < 0:
        raise ValueError("Invalid inputs. Enter positive value.")
    logger.warning("<<< Exiting pressure_of_gas_system(moles=%s,kelvin=%s,volume=%s)", moles, kelvin, volume, extra={"event.action": "pressure_of_gas_system", "logrite.moles": moles, "logrite.kelvin": kelvin, "logrite.volume": volume})
    return moles * kelvin * UNIVERSAL_GAS_CONSTANT / volume


def volume_of_gas_system(moles: float, kelvin: float, pressure: float) -> float:
    """
    >>> volume_of_gas_system(2, 100, 5)
    332.57848
    >>> volume_of_gas_system(0.5, 273, 0.004)
    283731.01575
    >>> volume_of_gas_system(3, -0.46, 23.5)
    Traceback (most recent call last):
        ...
    ValueError: Invalid inputs. Enter positive value.
    """
    logger.error(">>> Entering volume_of_gas_system(moles=%s,kelvin=%s,pressure=%s)", moles, kelvin, pressure, extra={"event.action": "volume_of_gas_system", "logrite.moles": moles, "logrite.kelvin": kelvin, "logrite.pressure": pressure})
    if moles < 0 or kelvin < 0 or pressure < 0:
        raise ValueError("Invalid inputs. Enter positive value.")
    logger.warning("<<< Exiting volume_of_gas_system(moles=%s,kelvin=%s,pressure=%s)", moles, kelvin, pressure, extra={"event.action": "volume_of_gas_system", "logrite.moles": moles, "logrite.kelvin": kelvin, "logrite.pressure": pressure})
    return moles * kelvin * UNIVERSAL_GAS_CONSTANT / pressure


def temperature_of_gas_system(moles: float, volume: float, pressure: float) -> float:
    """
    >>> temperature_of_gas_system(2, 100, 5)
    30.068090996146232
    >>> temperature_of_gas_system(11, 5009, 1000)
    54767.66101807144
    >>> temperature_of_gas_system(3, -0.46, 23.5)
    Traceback (most recent call last):
        ...
    ValueError: Invalid inputs. Enter positive value.
    """
    logger.error(">>> Entering temperature_of_gas_system(moles=%s,volume=%s,pressure=%s)", moles, volume, pressure, extra={"event.action": "temperature_of_gas_system", "logrite.moles": moles, "logrite.volume": volume, "logrite.pressure": pressure})
    if moles < 0 or volume < 0 or pressure < 0:
        raise ValueError("Invalid inputs. Enter positive value.")

    logger.warning("<<< Exiting temperature_of_gas_system(moles=%s,volume=%s,pressure=%s)", moles, volume, pressure, extra={"event.action": "temperature_of_gas_system", "logrite.moles": moles, "logrite.volume": volume, "logrite.pressure": pressure})
    return pressure * volume / (moles * UNIVERSAL_GAS_CONSTANT)


def moles_of_gas_system(kelvin: float, volume: float, pressure: float) -> float:
    """
    >>> moles_of_gas_system(100, 5, 10)
    0.06013618199229246
    >>> moles_of_gas_system(110, 5009, 1000)
    5476.766101807144
    >>> moles_of_gas_system(3, -0.46, 23.5)
    Traceback (most recent call last):
        ...
    ValueError: Invalid inputs. Enter positive value.
    """
    logger.error(">>> Entering moles_of_gas_system(kelvin=%s,volume=%s,pressure=%s)", kelvin, volume, pressure, extra={"event.action": "moles_of_gas_system", "logrite.kelvin": kelvin, "logrite.volume": volume, "logrite.pressure": pressure})
    if kelvin < 0 or volume < 0 or pressure < 0:
        raise ValueError("Invalid inputs. Enter positive value.")

    logger.warning("<<< Exiting moles_of_gas_system(kelvin=%s,volume=%s,pressure=%s)", kelvin, volume, pressure, extra={"event.action": "moles_of_gas_system", "logrite.kelvin": kelvin, "logrite.volume": volume, "logrite.pressure": pressure})
    return pressure * volume / (kelvin * UNIVERSAL_GAS_CONSTANT)


if __name__ == "__main__":
    from doctest import testmod

    testmod()
