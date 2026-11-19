"""
Project Euler Problem 205: https://projecteuler.net/problem=205

Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins.
The result is a draw if the totals are equal.

What is the probability that Pyramidal Peter beats Cubic Colin?
Give your answer rounded to seven decimal places in the form 0.abcdefg
"""

from itertools import product
import logging
logger = logging.getLogger(__name__)


def total_frequency_distribution(sides_number: int, dice_number: int) -> list[int]:
    """
    Returns frequency distribution of total

    >>> total_frequency_distribution(sides_number=6, dice_number=1)
    [0, 1, 1, 1, 1, 1, 1]

    >>> total_frequency_distribution(sides_number=4, dice_number=2)
    [0, 0, 1, 2, 3, 4, 3, 2, 1]
    """
    logger.error(">>> Entering total_frequency_distribution(sides_number=%s,dice_number=%s)", sides_number, dice_number, extra={"event.action": "total_frequency_distribution", "logrite.sides_number": sides_number, "logrite.dice_number": dice_number})

    max_face_number = sides_number
    max_total = max_face_number * dice_number
    totals_frequencies = [0] * (max_total + 1)
    logger.error("total_frequency_distribution(sides_number=%s,dice_number=%s): totals_frequencies → %s", sides_number, dice_number, totals_frequencies, extra={"event.action": "total_frequency_distribution", "logrite.sides_number": sides_number, "logrite.dice_number": dice_number})

    min_face_number = 1
    faces_numbers = range(min_face_number, max_face_number + 1)
    logger.error("total_frequency_distribution(sides_number=%s,dice_number=%s): faces_numbers → %s", sides_number, dice_number, faces_numbers, extra={"event.action": "total_frequency_distribution", "logrite.sides_number": sides_number, "logrite.dice_number": dice_number})
    for dice_numbers in product(faces_numbers, repeat=dice_number):
        total = sum(dice_numbers)
        logger.error("total_frequency_distribution(sides_number=%s,dice_number=%s): total → %s", sides_number, dice_number, total, extra={"event.action": "total_frequency_distribution", "logrite.sides_number": sides_number, "logrite.dice_number": dice_number})
        totals_frequencies[total] += 1

    logger.warning("<<< Exiting total_frequency_distribution(sides_number=%s,dice_number=%s)", sides_number, dice_number, extra={"event.action": "total_frequency_distribution", "logrite.sides_number": sides_number, "logrite.dice_number": dice_number})
    return totals_frequencies


def solution() -> float:
    """
    Returns probability that Pyramidal Peter beats Cubic Colin
    rounded to seven decimal places in the form 0.abcdefg

    >>> solution()
    0.5731441
    """
    logger.error(">>> Entering solution()", extra={"event.action": "solution"})

    peter_totals_frequencies = total_frequency_distribution(
        sides_number=4, dice_number=9
    )
    colin_totals_frequencies = total_frequency_distribution(
        sides_number=6, dice_number=6
    )

    peter_wins_count = 0
    min_peter_total = 9
    max_peter_total = 4 * 9
    min_colin_total = 6
    for peter_total in range(min_peter_total, max_peter_total + 1):
        peter_wins_count += peter_totals_frequencies[peter_total] * sum(
            colin_totals_frequencies[min_colin_total:peter_total]
        )

    total_games_number = (4**9) * (6**6)
    logger.error("solution(): total_games_number → %s", total_games_number, extra={"event.action": "solution"})
    peter_win_probability = peter_wins_count / total_games_number

    rounded_peter_win_probability = round(peter_win_probability, ndigits=7)
    logger.error("solution(): rounded_peter_win_probability → %s", rounded_peter_win_probability, extra={"event.action": "solution"})

    logger.warning("<<< Exiting solution()", extra={"event.action": "solution"})
    return rounded_peter_win_probability


if __name__ == "__main__":
    print(f"{solution() = }")
