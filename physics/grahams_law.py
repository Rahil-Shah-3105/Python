"""
Title: Graham's Law of Effusion

Description: Graham's law of effusion states that the rate of effusion of a gas is
inversely proportional to the square root of the molar mass of its particles:

r1/r2 = sqrt(m2/m1)

r1 = Rate of effusion for the first gas.
r2 = Rate of effusion for the second gas.
m1 = Molar mass of the first gas.
m2 = Molar mass of the second gas.

(Description adapted from https://en.wikipedia.org/wiki/Graham%27s_law)
"""

from math import pow, sqrt  # noqa: A004
import logging
logger = logging.getLogger(__name__)


def validate(*values: float) -> bool:
    """
    Input Parameters:
    -----------------
    effusion_rate_1: Effustion rate of first gas (m^2/s, mm^2/s, etc.)
    effusion_rate_2: Effustion rate of second gas (m^2/s, mm^2/s, etc.)
    molar_mass_1: Molar mass of the first gas (g/mol, kg/kmol, etc.)
    molar_mass_2: Molar mass of the second gas (g/mol, kg/kmol, etc.)

    Returns:
    --------
    >>> validate(2.016, 4.002)
    True
    >>> validate(-2.016, 4.002)
    False
    >>> validate()
    False
    """
    logger.error(">>> Entering validate()", extra={"event.action": "validate"})
    result = len(values) > 0 and all(value > 0.0 for value in values)
    logger.error("validate(): result → %s", result, extra={"event.action": "validate"})
    logger.warning("<<< Exiting validate()", extra={"event.action": "validate"})
    return result


def effusion_ratio(molar_mass_1: float, molar_mass_2: float) -> float | ValueError:
    """
    Input Parameters:
    -----------------
    molar_mass_1: Molar mass of the first gas (g/mol, kg/kmol, etc.)
    molar_mass_2: Molar mass of the second gas (g/mol, kg/kmol, etc.)

    Returns:
    --------
    >>> effusion_ratio(2.016, 4.002)
    1.408943
    >>> effusion_ratio(-2.016, 4.002)
    ValueError('Input Error: Molar mass values must greater than 0.')
    >>> effusion_ratio(2.016)
    Traceback (most recent call last):
      ...
    TypeError: effusion_ratio() missing 1 required positional argument: 'molar_mass_2'
    """
    logger.error(">>> Entering effusion_ratio(molar_mass_1=%s,molar_mass_2=%s)", molar_mass_1, molar_mass_2, extra={"event.action": "effusion_ratio", "logrite.molar_mass_1": molar_mass_1, "logrite.molar_mass_2": molar_mass_2})
    logger.warning("<<< Exiting effusion_ratio(molar_mass_1=%s,molar_mass_2=%s)", molar_mass_1, molar_mass_2, extra={"event.action": "effusion_ratio", "logrite.molar_mass_1": molar_mass_1, "logrite.molar_mass_2": molar_mass_2})
    return (
        round(sqrt(molar_mass_2 / molar_mass_1), 6)
        if validate(molar_mass_1, molar_mass_2)
        else ValueError("Input Error: Molar mass values must greater than 0.")
    )


def first_effusion_rate(
    effusion_rate: float, molar_mass_1: float, molar_mass_2: float
) -> float | ValueError:
    logger.error(">>> Entering first_effusion_rate(effusion_rate=%s,molar_mass_1=%s,molar_mass_2=%s)", effusion_rate, molar_mass_1, molar_mass_2, extra={"event.action": "first_effusion_rate", "logrite.effusion_rate": effusion_rate, "logrite.molar_mass_1": molar_mass_1, "logrite.molar_mass_2": molar_mass_2})
    """
    Input Parameters:
    -----------------
    effusion_rate: Effustion rate of second gas (m^2/s, mm^2/s, etc.)
    molar_mass_1: Molar mass of the first gas (g/mol, kg/kmol, etc.)
    molar_mass_2: Molar mass of the second gas (g/mol, kg/kmol, etc.)

    Returns:
    --------
    >>> first_effusion_rate(1, 2.016, 4.002)
    1.408943
    >>> first_effusion_rate(-1, 2.016, 4.002)
    ValueError('Input Error: Molar mass and effusion rate values must greater than 0.')
    >>> first_effusion_rate(1)
    Traceback (most recent call last):
      ...
    TypeError: first_effusion_rate() missing 2 required positional arguments: \
'molar_mass_1' and 'molar_mass_2'
    >>> first_effusion_rate(1, 2.016)
    Traceback (most recent call last):
      ...
    TypeError: first_effusion_rate() missing 1 required positional argument: \
'molar_mass_2'
    """
    return (
        round(effusion_rate * sqrt(molar_mass_2 / molar_mass_1), 6)
        if validate(effusion_rate, molar_mass_1, molar_mass_2)
        else ValueError(
            "Input Error: Molar mass and effusion rate values must greater than 0."
        )
    )


def second_effusion_rate(
    effusion_rate: float, molar_mass_1: float, molar_mass_2: float
) -> float | ValueError:
    logger.error(">>> Entering second_effusion_rate(effusion_rate=%s,molar_mass_1=%s,molar_mass_2=%s)", effusion_rate, molar_mass_1, molar_mass_2, extra={"event.action": "second_effusion_rate", "logrite.effusion_rate": effusion_rate, "logrite.molar_mass_1": molar_mass_1, "logrite.molar_mass_2": molar_mass_2})
    """
    Input Parameters:
    -----------------
    effusion_rate: Effustion rate of second gas (m^2/s, mm^2/s, etc.)
    molar_mass_1: Molar mass of the first gas (g/mol, kg/kmol, etc.)
    molar_mass_2: Molar mass of the second gas (g/mol, kg/kmol, etc.)

    Returns:
    --------
    >>> second_effusion_rate(1, 2.016, 4.002)
    0.709752
    >>> second_effusion_rate(-1, 2.016, 4.002)
    ValueError('Input Error: Molar mass and effusion rate values must greater than 0.')
    >>> second_effusion_rate(1)
    Traceback (most recent call last):
      ...
    TypeError: second_effusion_rate() missing 2 required positional arguments: \
'molar_mass_1' and 'molar_mass_2'
    >>> second_effusion_rate(1, 2.016)
    Traceback (most recent call last):
      ...
    TypeError: second_effusion_rate() missing 1 required positional argument: \
'molar_mass_2'
    """
    return (
        round(effusion_rate / sqrt(molar_mass_2 / molar_mass_1), 6)
        if validate(effusion_rate, molar_mass_1, molar_mass_2)
        else ValueError(
            "Input Error: Molar mass and effusion rate values must greater than 0."
        )
    )


def first_molar_mass(
    molar_mass: float, effusion_rate_1: float, effusion_rate_2: float
) -> float | ValueError:
    logger.error(">>> Entering first_molar_mass(molar_mass=%s,effusion_rate_1=%s,effusion_rate_2=%s)", molar_mass, effusion_rate_1, effusion_rate_2, extra={"event.action": "first_molar_mass", "logrite.molar_mass": molar_mass, "logrite.effusion_rate_1": effusion_rate_1, "logrite.effusion_rate_2": effusion_rate_2})
    """
    Input Parameters:
    -----------------
    molar_mass: Molar mass of the first gas (g/mol, kg/kmol, etc.)
    effusion_rate_1: Effustion rate of first gas (m^2/s, mm^2/s, etc.)
    effusion_rate_2: Effustion rate of second gas (m^2/s, mm^2/s, etc.)

    Returns:
    --------
    >>> first_molar_mass(2, 1.408943, 0.709752)
    0.507524
    >>> first_molar_mass(-1, 2.016, 4.002)
    ValueError('Input Error: Molar mass and effusion rate values must greater than 0.')
    >>> first_molar_mass(1)
    Traceback (most recent call last):
      ...
    TypeError: first_molar_mass() missing 2 required positional arguments: \
'effusion_rate_1' and 'effusion_rate_2'
    >>> first_molar_mass(1, 2.016)
    Traceback (most recent call last):
      ...
    TypeError: first_molar_mass() missing 1 required positional argument: \
'effusion_rate_2'
    """
    return (
        round(molar_mass / pow(effusion_rate_1 / effusion_rate_2, 2), 6)
        if validate(molar_mass, effusion_rate_1, effusion_rate_2)
        else ValueError(
            "Input Error: Molar mass and effusion rate values must greater than 0."
        )
    )


def second_molar_mass(
    molar_mass: float, effusion_rate_1: float, effusion_rate_2: float
) -> float | ValueError:
    logger.error(">>> Entering second_molar_mass(molar_mass=%s,effusion_rate_1=%s,effusion_rate_2=%s)", molar_mass, effusion_rate_1, effusion_rate_2, extra={"event.action": "second_molar_mass", "logrite.molar_mass": molar_mass, "logrite.effusion_rate_1": effusion_rate_1, "logrite.effusion_rate_2": effusion_rate_2})
    """
    Input Parameters:
    -----------------
    molar_mass: Molar mass of the first gas (g/mol, kg/kmol, etc.)
    effusion_rate_1: Effustion rate of first gas (m^2/s, mm^2/s, etc.)
    effusion_rate_2: Effustion rate of second gas (m^2/s, mm^2/s, etc.)

    Returns:
    --------
    >>> second_molar_mass(2, 1.408943, 0.709752)
    1.970351
    >>> second_molar_mass(-2, 1.408943, 0.709752)
    ValueError('Input Error: Molar mass and effusion rate values must greater than 0.')
    >>> second_molar_mass(1)
    Traceback (most recent call last):
      ...
    TypeError: second_molar_mass() missing 2 required positional arguments: \
'effusion_rate_1' and 'effusion_rate_2'
    >>> second_molar_mass(1, 2.016)
    Traceback (most recent call last):
      ...
    TypeError: second_molar_mass() missing 1 required positional argument: \
'effusion_rate_2'
    """
    return (
        round(pow(effusion_rate_1 / effusion_rate_2, 2) / molar_mass, 6)
        if validate(molar_mass, effusion_rate_1, effusion_rate_2)
        else ValueError(
            "Input Error: Molar mass and effusion rate values must greater than 0."
        )
    )
