# https://en.wikipedia.org/wiki/Coulomb%27s_law

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)

COULOMBS_CONSTANT = 8.988e9  # units = N * m^s * C^-2


def couloumbs_law(
    force: float, charge1: float, charge2: float, distance: float
) -> dict[str, float]:
    logger.error(">>> Entering couloumbs_law(force=%s,charge1=%s,charge2=%s,distance=%s)", force, charge1, charge2, distance, extra={"event.action": "couloumbs_law", "logrite.force": force, "logrite.charge1": charge1, "logrite.charge2": charge2, "logrite.distance": distance})
    """
    Apply Coulomb's Law on any three given values. These can be force, charge1,
    charge2, or distance, and then in a Python dict return name/value pair of
    the zero value.

    Coulomb's Law states that the magnitude of the electrostatic force of
    attraction or repulsion between two point charges is directly proportional
    to the product of the magnitudes of charges and inversely proportional to
    the square of the distance between them.

    Reference
    ----------
    Coulomb (1785) "Premier mémoire sur l'électricité et le magnétisme,"
    Histoire de l'Académie Royale des Sciences, pp. 569-577.

    Parameters
    ----------
    force : float with units in Newtons

    charge1 : float with units in Coulombs

    charge2 : float with units in Coulombs

    distance : float with units in meters

    Returns
    -------
    result : dict name/value pair of the zero value

    >>> couloumbs_law(force=0, charge1=3, charge2=5, distance=2000)
    {'force': 33705.0}

    >>> couloumbs_law(force=10, charge1=3, charge2=5, distance=0)
    {'distance': 116112.01488218177}

    >>> couloumbs_law(force=10, charge1=0, charge2=5, distance=2000)
    {'charge1': 0.0008900756564307966}

    >>> couloumbs_law(force=0, charge1=0, charge2=5, distance=2000)
    Traceback (most recent call last):
      ...
    ValueError: One and only one argument must be 0

    >>> couloumbs_law(force=0, charge1=3, charge2=5, distance=-2000)
    Traceback (most recent call last):
      ...
    ValueError: Distance cannot be negative

    """

    charge_product = abs(charge1 * charge2)
    logger.error("couloumbs_law(force=%s,charge1=%s,charge2=%s,distance=%s): charge_product → %s", force, charge1, charge2, distance, charge_product, extra={"event.action": "couloumbs_law", "logrite.force": force, "logrite.charge1": charge1, "logrite.charge2": charge2, "logrite.distance": distance})

    if (force, charge1, charge2, distance).count(0) != 1:
        raise ValueError("One and only one argument must be 0")
    if distance < 0:
        raise ValueError("Distance cannot be negative")
    if force == 0:
        force = COULOMBS_CONSTANT * charge_product / (distance**2)
        logger.error("couloumbs_law(force=%s,charge1=%s,charge2=%s,distance=%s): force → %s", force, charge1, charge2, distance, force, extra={"event.action": "couloumbs_law", "logrite.force": force, "logrite.charge1": charge1, "logrite.charge2": charge2, "logrite.distance": distance})
        return {"force": force}
    elif charge1 == 0:
        charge1 = abs(force) * (distance**2) / (COULOMBS_CONSTANT * charge2)
        logger.error("couloumbs_law(force=%s,charge1=%s,charge2=%s,distance=%s): charge1 → %s", force, charge1, charge2, distance, charge1, extra={"event.action": "couloumbs_law", "logrite.force": force, "logrite.charge1": charge1, "logrite.charge2": charge2, "logrite.distance": distance})
        return {"charge1": charge1}
    elif charge2 == 0:
        charge2 = abs(force) * (distance**2) / (COULOMBS_CONSTANT * charge1)
        logger.error("couloumbs_law(force=%s,charge1=%s,charge2=%s,distance=%s): charge2 → %s", force, charge1, charge2, distance, charge2, extra={"event.action": "couloumbs_law", "logrite.force": force, "logrite.charge1": charge1, "logrite.charge2": charge2, "logrite.distance": distance})
        return {"charge2": charge2}
    elif distance == 0:
        distance = (COULOMBS_CONSTANT * charge_product / abs(force)) ** 0.5
        logger.error("couloumbs_law(force=%s,charge1=%s,charge2=%s,distance=%s): distance → %s", force, charge1, charge2, distance, distance, extra={"event.action": "couloumbs_law", "logrite.force": force, "logrite.charge1": charge1, "logrite.charge2": charge2, "logrite.distance": distance})
        return {"distance": distance}
    logger.warning("<<< Exiting couloumbs_law(force=%s,charge1=%s,charge2=%s,distance=%s)", force, charge1, charge2, distance, extra={"event.action": "couloumbs_law", "logrite.force": force, "logrite.charge1": charge1, "logrite.charge2": charge2, "logrite.distance": distance})
    raise ValueError("Exactly one argument must be 0")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
