import logging
logger = logging.getLogger(__name__)
def reverse_words(sentence: str) -> str:
    """Reverse the order of words in a given string.

    Extra whitespace between words is ignored.

    >>> reverse_words("I love Python")
    'Python love I'
    >>> reverse_words("I     Love          Python")
    'Python Love I'
    """
    logger.debug(">>> Entering reverse_words(sentence=%s)", sentence)
    logger.debug("<<< Exiting reverse_words(sentence=%s)", sentence)
    return " ".join(sentence.split()[::-1])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
