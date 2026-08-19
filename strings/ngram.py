import logging
logger = logging.getLogger(__name__)
"""
https://en.wikipedia.org/wiki/N-gram
"""


def create_ngram(sentence: str, ngram_size: int) -> list[str]:
    """
    Create ngrams from a sentence

    >>> create_ngram("I am a sentence", 2)
    ['I ', ' a', 'am', 'm ', ' a', 'a ', ' s', 'se', 'en', 'nt', 'te', 'en', 'nc', 'ce']
    >>> create_ngram("I am an NLPer", 2)
    ['I ', ' a', 'am', 'm ', ' a', 'an', 'n ', ' N', 'NL', 'LP', 'Pe', 'er']
    >>> create_ngram("This is short", 50)
    []
    """
    logger.debug(">>> Entering create_ngram(sentence=%s,ngram_size=%s)", sentence, ngram_size)
    logger.debug("<<< Exiting create_ngram(sentence=%s,ngram_size=%s)", sentence, ngram_size)
    return [sentence[i : i + ngram_size] for i in range(len(sentence) - ngram_size + 1)]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
