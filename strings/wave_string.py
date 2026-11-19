import logging
logger = logging.getLogger(__name__)
def wave(txt: str) -> list:
    """
    Returns a so called 'wave' of a given string
    >>> wave('cat')
    ['Cat', 'cAt', 'caT']
    >>> wave('one')
    ['One', 'oNe', 'onE']
    >>> wave('book')
    ['Book', 'bOok', 'boOk', 'booK']
    """
    logger.error(">>> Entering wave(txt=%s)", txt, extra={"event.action": "wave", "logrite.txt": txt})

    logger.warning("<<< Exiting wave(txt=%s)", txt, extra={"event.action": "wave", "logrite.txt": txt})
    return [
        txt[:a] + txt[a].upper() + txt[a + 1 :]
        for a in range(len(txt))
        if txt[a].isalpha()
    ]


if __name__ == "__main__":
    __import__("doctest").testmod()
