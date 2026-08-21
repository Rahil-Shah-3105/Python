import logging
logger = logging.getLogger(__name__)
def to_title_case(word: str) -> str:
    """
    Converts a string to capitalized case, preserving the input as is

    >>> to_title_case("Aakash")
    'Aakash'

    >>> to_title_case("aakash")
    'Aakash'

    >>> to_title_case("AAKASH")
    'Aakash'

    >>> to_title_case("aAkAsH")
    'Aakash'
    """
    logger.debug(">>> Entering to_title_case(word=%s)", word)

    """
    Convert the first character to uppercase if it's lowercase
    """
    if "a" <= word[0] <= "z":
        word = chr(ord(word[0]) - 32) + word[1:]
        logger.debug("to_title_case(word=%s): word → %s", word, word)

    """
    Convert the remaining characters to lowercase if they are uppercase
    """
    for i in range(1, len(word)):
        if "A" <= word[i] <= "Z":
            word = word[:i] + chr(ord(word[i]) + 32) + word[i + 1 :]

    logger.debug("<<< Exiting to_title_case(word=%s)", word)
    return word


def sentence_to_title_case(input_str: str) -> str:
    """
    Converts a string to title case, preserving the input as is

    >>> sentence_to_title_case("Aakash Giri")
    'Aakash Giri'

    >>> sentence_to_title_case("aakash giri")
    'Aakash Giri'

    >>> sentence_to_title_case("AAKASH GIRI")
    'Aakash Giri'

    >>> sentence_to_title_case("aAkAsH gIrI")
    'Aakash Giri'
    """
    logger.debug(">>> Entering sentence_to_title_case(input_str=%s)", input_str)

    logger.debug("<<< Exiting sentence_to_title_case(input_str=%s)", input_str)
    return " ".join(to_title_case(word) for word in input_str.split())


if __name__ == "__main__":
    from doctest import testmod

    testmod()
