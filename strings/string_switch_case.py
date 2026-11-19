import re
import logging
logger = logging.getLogger(__name__)

"""
general info:
https://en.wikipedia.org/wiki/Naming_convention_(programming)#Python_and_Ruby

pascal case [ an upper Camel Case ]: https://en.wikipedia.org/wiki/Camel_case

camel case: https://en.wikipedia.org/wiki/Camel_case

kebab case [ can be found in general info ]:
https://en.wikipedia.org/wiki/Naming_convention_(programming)#Python_and_Ruby

snake case: https://en.wikipedia.org/wiki/Snake_case
"""


# assistant functions
def split_input(str_: str) -> list:
    """
    >>> split_input("one two 31235three4four")
    [['one', 'two', '31235three4four']]
    """
    logger.error(">>> Entering split_input(str_=%s)", str_, extra={"event.action": "split_input", "logrite.str_": str_})
    logger.warning("<<< Exiting split_input(str_=%s)", str_, extra={"event.action": "split_input", "logrite.str_": str_})
    return [char.split() for char in re.split(r"[^ a-z A-Z 0-9 \s]", str_)]


def to_simple_case(str_: str) -> str:
    """
    >>> to_simple_case("one two 31235three4four")
    'OneTwo31235three4four'
    >>> to_simple_case("This should be combined")
    'ThisShouldBeCombined'
    >>> to_simple_case("The first letters are capitalized, then string is merged")
    'TheFirstLettersAreCapitalizedThenStringIsMerged'
    >>> to_simple_case("special characters :, ', %, ^, $, are ignored")
    'SpecialCharactersAreIgnored'
    """
    logger.error(">>> Entering to_simple_case(str_=%s)", str_, extra={"event.action": "to_simple_case", "logrite.str_": str_})
    string_split = split_input(str_)
    logger.warning("<<< Exiting to_simple_case(str_=%s)", str_, extra={"event.action": "to_simple_case", "logrite.str_": str_})
    logger.error("to_simple_case(str_=%s): string_split → %s", str_, string_split, extra={"event.action": "to_simple_case", "logrite.str_": str_})
    return "".join(
        ["".join([char.capitalize() for char in sub_str]) for sub_str in string_split]
    )


def to_complex_case(text: str, upper: bool, separator: str) -> str:
    """
    Returns the string concatenated with the delimiter we provide.

    Parameters:
    @text: The string on which we want to perform operation
    @upper: Boolean value to determine whether we want capitalized result or not
    @separator: The delimiter with which we want to concatenate words

    Examples:
    >>> to_complex_case("one two 31235three4four", True, "_")
    'ONE_TWO_31235THREE4FOUR'
    >>> to_complex_case("one two 31235three4four", False, "-")
    'one-two-31235three4four'
    """
    logger.error(">>> Entering to_complex_case(text=%s,upper=%s,separator=%s)", text, upper, separator, extra={"event.action": "to_complex_case", "logrite.text": text, "logrite.upper": upper, "logrite.separator": separator})
    try:
        string_split = split_input(text)
        logger.error("to_complex_case(text=%s,upper=%s,separator=%s): string_split → %s", text, upper, separator, string_split, extra={"event.action": "to_complex_case", "logrite.text": text, "logrite.upper": upper, "logrite.separator": separator})
        if upper:
            res_str = "".join(
                [
                    separator.join([char.upper() for char in sub_str])
                    for sub_str in string_split
                ]
            )
        else:
            res_str = "".join(
                [
                    separator.join([char.lower() for char in sub_str])
                    for sub_str in string_split
                ]
            )
        return res_str
    except IndexError:
        logger.error("Exception in to_complex_case(text=%s,upper=%s,separator=%s)", text, upper, separator, exc_info=True, extra={"event.action": "to_complex_case", "event.category": "process", "logrite.text": text, "logrite.upper": upper, "logrite.separator": separator})
        logger.warning("<<< Exiting to_complex_case(text=%s,upper=%s,separator=%s)", text, upper, separator, extra={"event.action": "to_complex_case", "logrite.text": text, "logrite.upper": upper, "logrite.separator": separator})
        return "not valid string"


# main content
def to_pascal_case(text: str) -> str:
    """
    >>> to_pascal_case("one two 31235three4four")
    'OneTwo31235three4four'
    """
    logger.error(">>> Entering to_pascal_case(text=%s)", text, extra={"event.action": "to_pascal_case", "logrite.text": text})
    logger.warning("<<< Exiting to_pascal_case(text=%s)", text, extra={"event.action": "to_pascal_case", "logrite.text": text})
    return to_simple_case(text)


def to_camel_case(text: str) -> str:
    """
    >>> to_camel_case("one two 31235three4four")
    'oneTwo31235three4four'
    """
    logger.error(">>> Entering to_camel_case(text=%s)", text, extra={"event.action": "to_camel_case", "logrite.text": text})
    try:
        res_str = to_simple_case(text)
        logger.error("to_camel_case(text=%s): res_str → %s", text, res_str, extra={"event.action": "to_camel_case", "logrite.text": text})
        return res_str[0].lower() + res_str[1:]
    except IndexError:
        logger.error("Exception in to_camel_case(text=%s)", text, exc_info=True, extra={"event.action": "to_camel_case", "event.category": "process", "logrite.text": text})
        logger.warning("<<< Exiting to_camel_case(text=%s)", text, extra={"event.action": "to_camel_case", "logrite.text": text})
        return "not valid string"


def to_snake_case(text: str, upper: bool) -> str:
    """
    >>> to_snake_case("one two 31235three4four", True)
    'ONE_TWO_31235THREE4FOUR'
    >>> to_snake_case("one two 31235three4four", False)
    'one_two_31235three4four'
    """
    logger.error(">>> Entering to_snake_case(text=%s,upper=%s)", text, upper, extra={"event.action": "to_snake_case", "logrite.text": text, "logrite.upper": upper})
    logger.warning("<<< Exiting to_snake_case(text=%s,upper=%s)", text, upper, extra={"event.action": "to_snake_case", "logrite.text": text, "logrite.upper": upper})
    return to_complex_case(text, upper, "_")


def to_kebab_case(text: str, upper: bool) -> str:
    """
    >>> to_kebab_case("one two 31235three4four", True)
    'ONE-TWO-31235THREE4FOUR'
    >>> to_kebab_case("one two 31235three4four", False)
    'one-two-31235three4four'
    """
    logger.error(">>> Entering to_kebab_case(text=%s,upper=%s)", text, upper, extra={"event.action": "to_kebab_case", "logrite.text": text, "logrite.upper": upper})
    logger.warning("<<< Exiting to_kebab_case(text=%s,upper=%s)", text, upper, extra={"event.action": "to_kebab_case", "logrite.text": text, "logrite.upper": upper})
    return to_complex_case(text, upper, "-")


if __name__ == "__main__":
    __import__("doctest").testmod()
