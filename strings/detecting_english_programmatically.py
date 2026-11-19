import os
from string import ascii_letters
import logging
logger = logging.getLogger(__name__)

LETTERS_AND_SPACE = ascii_letters + " \t\n"


def load_dictionary() -> dict[str, None]:
    logger.error(">>> Entering load_dictionary()", extra={"event.action": "load_dictionary"})
    path = os.path.split(os.path.realpath(__file__))
    logger.error("load_dictionary(): path → %s", path, extra={"event.action": "load_dictionary"})
    english_words: dict[str, None] = {}
    with open(path[0] + "/dictionary.txt") as dictionary_file:
        for word in dictionary_file.read().split("\n"):
            english_words[word] = None
    logger.warning("<<< Exiting load_dictionary()", extra={"event.action": "load_dictionary"})
    return english_words


ENGLISH_WORDS = load_dictionary()


def get_english_count(message: str) -> float:
    logger.error(">>> Entering get_english_count(message=%s)", message, extra={"event.action": "get_english_count", "logrite.message": message})
    message = message.upper()
    message = remove_non_letters(message)
    logger.error("get_english_count(message=%s): message → %s", message, message, extra={"event.action": "get_english_count", "logrite.message": message})
    possible_words = message.split()
    logger.error("get_english_count(message=%s): possible_words → %s", message, possible_words, extra={"event.action": "get_english_count", "logrite.message": message})
    matches = len([word for word in possible_words if word in ENGLISH_WORDS])
    logger.error("get_english_count(message=%s): matches → %s", message, matches, extra={"event.action": "get_english_count", "logrite.message": message})
    logger.warning("<<< Exiting get_english_count(message=%s)", message, extra={"event.action": "get_english_count", "logrite.message": message})
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
    logger.error(">>> Entering remove_non_letters(message=%s)", message, extra={"event.action": "remove_non_letters", "logrite.message": message})
    logger.warning("<<< Exiting remove_non_letters(message=%s)", message, extra={"event.action": "remove_non_letters", "logrite.message": message})
    return "".join(symbol for symbol in message if symbol in LETTERS_AND_SPACE)


def is_english(
    message: str, word_percentage: int = 20, letter_percentage: int = 85
) -> bool:
    logger.error(">>> Entering is_english(message=%s,word_percentage=%s,letter_percentage=%s)", message, word_percentage, letter_percentage, extra={"event.action": "is_english", "logrite.message": message, "logrite.word_percentage": word_percentage, "logrite.letter_percentage": letter_percentage})
    """
    >>> is_english('Hello World')
    True
    >>> is_english('llold HorWd')
    False
    """
    words_match = get_english_count(message) * 100 >= word_percentage
    logger.error("is_english(message=%s,word_percentage=%s,letter_percentage=%s): words_match → %s", message, word_percentage, letter_percentage, words_match, extra={"event.action": "is_english", "logrite.message": message, "logrite.word_percentage": word_percentage, "logrite.letter_percentage": letter_percentage})
    num_letters = len(remove_non_letters(message))
    logger.error("is_english(message=%s,word_percentage=%s,letter_percentage=%s): num_letters → %s", message, word_percentage, letter_percentage, num_letters, extra={"event.action": "is_english", "logrite.message": message, "logrite.word_percentage": word_percentage, "logrite.letter_percentage": letter_percentage})
    message_letters_percentage = (float(num_letters) / len(message)) * 100
    logger.error("is_english(message=%s,word_percentage=%s,letter_percentage=%s): message_letters_percentage → %s", message, word_percentage, letter_percentage, message_letters_percentage, extra={"event.action": "is_english", "logrite.message": message, "logrite.word_percentage": word_percentage, "logrite.letter_percentage": letter_percentage})
    letters_match = message_letters_percentage >= letter_percentage
    logger.warning("<<< Exiting is_english(message=%s,word_percentage=%s,letter_percentage=%s)", message, word_percentage, letter_percentage, extra={"event.action": "is_english", "logrite.message": message, "logrite.word_percentage": word_percentage, "logrite.letter_percentage": letter_percentage})
    return words_match and letters_match


if __name__ == "__main__":
    import doctest

    doctest.testmod()
