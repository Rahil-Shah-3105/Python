import os
from string import ascii_letters
import logging
logger = logging.getLogger(__name__)

LETTERS_AND_SPACE = ascii_letters + " \t\n"


def load_dictionary() -> dict[str, None]:
    logger.debug(">>> Entering load_dictionary()")
    path = os.path.split(os.path.realpath(__file__))
    logger.debug("load_dictionary(): path → %s", path)
    english_words: dict[str, None] = {}
    with open(path[0] + "/dictionary.txt") as dictionary_file:
        logger.error("Exception in load_dictionary()", exc_info=True)
        for word in dictionary_file.read().split("\n"):
            english_words[word] = None
    logger.debug("<<< Exiting load_dictionary()")
    return english_words


ENGLISH_WORDS = load_dictionary()


def get_english_count(message: str) -> float:
    logger.debug(">>> Entering get_english_count(message=%s)", message)
    message = message.upper()
    message = remove_non_letters(message)
    logger.debug("get_english_count(message=%s): message → %s", message, message)
    possible_words = message.split()
    logger.debug("get_english_count(message=%s): possible_words → %s", message, possible_words)
    matches = len([word for word in possible_words if word in ENGLISH_WORDS])
    logger.debug("get_english_count(message=%s): matches → %s", message, matches)
    logger.debug("<<< Exiting get_english_count(message=%s)", message)
    return float(matches) / len(possible_words)


def remove_non_letters(message: str) -> str:
    """
    >>> remove_non_letters("Hi! how are you?")
    'Hi how are you'
    >>> remove_non_letters("P^y%t)h@o*n")
    'Python'
    >>> remove_non_letters("1+1=2")
    ''
    >>> remove_non_letters("www.google.com/")
    'wwwgooglecom'
    >>> remove_non_letters("")
    ''
    """
    logger.debug(">>> Entering remove_non_letters(message=%s)", message)
    logger.debug("<<< Exiting remove_non_letters(message=%s)", message)
    return "".join(symbol for symbol in message if symbol in LETTERS_AND_SPACE)


def is_english(
    message: str, word_percentage: int = 20, letter_percentage: int = 85
) -> bool:
    """
    >>> is_english('Hello World')
    True
    >>> is_english('llold HorWd')
    False
    """
    words_match = get_english_count(message) * 100 >= word_percentage
    num_letters = len(remove_non_letters(message))
    message_letters_percentage = (float(num_letters) / len(message)) * 100
    letters_match = message_letters_percentage >= letter_percentage
    return words_match and letters_match


if __name__ == "__main__":
    import doctest

    doctest.testmod()
