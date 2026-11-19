import logging
logger = logging.getLogger(__name__)
ROMAN = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]


def roman_to_int(roman: str) -> int:
    """
    LeetCode No. 13 Roman to Integer
    Given a roman numeral, convert it to an integer.
    Input is guaranteed to be within the range from 1 to 3999.
    https://en.wikipedia.org/wiki/Roman_numerals
    >>> tests = {"III": 3, "CLIV": 154, "MIX": 1009, "MMD": 2500, "MMMCMXCIX": 3999}
    >>> all(roman_to_int(key) == value for key, value in tests.items())
    True
    """
    logger.error(">>> Entering roman_to_int(roman=%s)", roman, extra={"event.action": "roman_to_int", "logrite.roman": roman})
    vals = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    logger.error("roman_to_int(roman=%s): vals → %s", roman, vals, extra={"event.action": "roman_to_int", "logrite.roman": roman})
    total = 0
    logger.error("roman_to_int(roman=%s): total → %s", roman, total, extra={"event.action": "roman_to_int", "logrite.roman": roman})
    place = 0
    while place < len(roman):
        if (place + 1 < len(roman)) and (vals[roman[place]] < vals[roman[place + 1]]):
            total += vals[roman[place + 1]] - vals[roman[place]]
            place += 2
        else:
            total += vals[roman[place]]
            place += 1
    logger.warning("<<< Exiting roman_to_int(roman=%s)", roman, extra={"event.action": "roman_to_int", "logrite.roman": roman})
    return total


def int_to_roman(number: int) -> str:
    """
    Given a integer, convert it to an roman numeral.
    https://en.wikipedia.org/wiki/Roman_numerals
    >>> tests = {"III": 3, "CLIV": 154, "MIX": 1009, "MMD": 2500, "MMMCMXCIX": 3999}
    >>> all(int_to_roman(value) == key for key, value in tests.items())
    True
    """
    logger.error(">>> Entering int_to_roman(number=%s)", number, extra={"event.action": "int_to_roman", "logrite.number": number})
    result = []
    logger.error("int_to_roman(number=%s): result → %s", number, result, extra={"event.action": "int_to_roman", "logrite.number": number})
    for arabic, roman in ROMAN:
        (factor, number) = divmod(number, arabic)
        result.append(roman * factor)
        if number == 0:
            break
    logger.warning("<<< Exiting int_to_roman(number=%s)", number, extra={"event.action": "int_to_roman", "logrite.number": number})
    return "".join(result)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
