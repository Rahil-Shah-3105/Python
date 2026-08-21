import logging
logger = logging.getLogger(__name__)
"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number,
134217728=89, is a ninth power.
How many n-digit positive integers exist which are also an nth power?
"""

"""
The maximum base can be 9 because all n-digit numbers < 10^n.
Now 9**23 has 22 digits so the maximum power can be 22.
Using these conclusions, we will calculate the result.
"""


def solution(max_base: int = 10, max_power: int = 22) -> int:
    """
    Returns the count of all n-digit numbers which are nth power
    >>> solution(10, 22)
    49
    >>> solution(0, 0)
    0
    >>> solution(1, 1)
    0
    >>> solution(-1, -1)
    0
    """
    logger.debug(">>> Entering solution(max_base=%s,max_power=%s)", max_base, max_power)
    bases = range(1, max_base)
    logger.debug("solution(max_base=%s,max_power=%s): bases → %s", max_base, max_power, bases)
    logger.debug("<<< Exiting solution(max_base=%s,max_power=%s)", max_base, max_power)
    powers = range(1, max_power)
    logger.debug("solution(max_base=%s,max_power=%s): powers → %s", max_base, max_power, powers)
    return sum(
        1 for power in powers for base in bases if len(str(base**power)) == power
    )


if __name__ == "__main__":
    print(f"{solution(10, 22) = }")
