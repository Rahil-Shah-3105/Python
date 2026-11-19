import logging
logger = logging.getLogger(__name__)
def remove_duplicates(sentence: str) -> str:
    """
    Remove duplicates from sentence
    >>> remove_duplicates("Python is great and Java is also great")
    'Java Python also and great is'
    >>> remove_duplicates("Python   is      great and Java is also great")
    'Java Python also and great is'
    """
    logger.error(">>> Entering remove_duplicates(sentence=%s)", sentence, extra={"event.action": "remove_duplicates", "logrite.sentence": sentence})
    logger.warning("<<< Exiting remove_duplicates(sentence=%s)", sentence, extra={"event.action": "remove_duplicates", "logrite.sentence": sentence})
    return " ".join(sorted(set(sentence.split())))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
