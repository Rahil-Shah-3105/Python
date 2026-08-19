"""
Project Euler Problem 89: https://projecteuler.net/problem=89

For a number written in Roman numerals to be considered valid there are basic rules
which must be followed. Even though the rules allow some numbers to be expressed in
more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number
sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example
is considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one
thousand numbers written in valid, but not necessarily minimal, Roman numerals; see
About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four
consecutive identical units.
"""

import os
import logging
logger = logging.getLogger(__name__)

SYMBOLS = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def parse_roman_numerals(numerals: str) -> int:
    """
    Converts a string of roman numerals to an integer.
    e.g.
    >>> parse_roman_numerals("LXXXIX")
    89
    >>> parse_roman_numerals("IIII")
    4
    """
    logger.debug(">>> Entering parse_roman_numerals(numerals=%s)", numerals)

    total_value = 0
    logger.debug("parse_roman_numerals(numerals=%s): total_value → %s", numerals, total_value)

    index = 0
    logger.debug("parse_roman_numerals(numerals=%s): index → %s", numerals, index)
    while index < len(numerals) - 1:
        current_value = SYMBOLS[numerals[index]]
        logger.debug("parse_roman_numerals(numerals=%s): current_value → %s", numerals, current_value)
        next_value = SYMBOLS[numerals[index + 1]]
        logger.debug("parse_roman_numerals(numerals=%s): next_value → %s", numerals, next_value)
        if current_value < next_value:
            total_value -= current_value
        else:
            total_value += current_value
        index += 1
    total_value += SYMBOLS[numerals[index]]

    logger.debug("<<< Exiting parse_roman_numerals(numerals=%s)", numerals)
    return total_value


def generate_roman_numerals(num: int) -> str:
    """
    Generates a string of roman numerals for a given integer.
    e.g.
    >>> generate_roman_numerals(89)
    'LXXXIX'
    >>> generate_roman_numerals(4)
    'IV'
    """
    logger.debug(">>> Entering generate_roman_numerals(num=%s)", num)

    numerals = ""
    logger.debug("generate_roman_numerals(num=%s): numerals → %s", num, numerals)

    m_count = num // 1000
    logger.debug("generate_roman_numerals(num=%s): m_count → %s", num, m_count)
    numerals += m_count * "M"
    num %= 1000

    c_count = num // 100
    if c_count == 9:
        numerals += "CM"
        c_count -= 9
    elif c_count == 4:
        numerals += "CD"
        c_count -= 4
    if c_count >= 5:
        numerals += "D"
        c_count -= 5
    numerals += c_count * "C"
    num %= 100

    x_count = num // 10
    if x_count == 9:
        numerals += "XC"
        x_count -= 9
    elif x_count == 4:
        numerals += "XL"
        x_count -= 4
    if x_count >= 5:
        numerals += "L"
        x_count -= 5
    numerals += x_count * "X"
    num %= 10

    if num == 9:
        numerals += "IX"
        num -= 9
    elif num == 4:
        numerals += "IV"
        num -= 4
    if num >= 5:
        numerals += "V"
        num -= 5
    numerals += num * "I"

    logger.debug("<<< Exiting generate_roman_numerals(num=%s)", num)
    return numerals


def solution(roman_numerals_filename: str = "/p089_roman.txt") -> int:
    """
    Calculates and returns the answer to project euler problem 89.

    >>> solution("/numeralcleanup_test.txt")
    16
    """
    logger.debug(">>> Entering solution(roman_numerals_filename=%s)", roman_numerals_filename)

    savings = 0
    logger.debug("solution(roman_numerals_filename=%s): savings → %s", roman_numerals_filename, savings)

    with open(os.path.dirname(__file__) + roman_numerals_filename) as file1:
        logger.error("Exception in solution(roman_numerals_filename=%s)", roman_numerals_filename, exc_info=True)
        lines = file1.readlines()
        logger.debug("solution(roman_numerals_filename=%s): lines → %s", roman_numerals_filename, lines)

    for line in lines:
        original = line.strip()
        logger.debug("solution(roman_numerals_filename=%s): original → %s", roman_numerals_filename, original)
        num = parse_roman_numerals(original)
        logger.debug("solution(roman_numerals_filename=%s): num → %s", roman_numerals_filename, num)
        shortened = generate_roman_numerals(num)
        logger.debug("solution(roman_numerals_filename=%s): shortened → %s", roman_numerals_filename, shortened)
        savings += len(original) - len(shortened)

    logger.debug("<<< Exiting solution(roman_numerals_filename=%s)", roman_numerals_filename)
    return savings


if __name__ == "__main__":
    print(f"{solution() = }")
