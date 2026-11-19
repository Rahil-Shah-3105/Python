import logging
logger = logging.getLogger(__name__)
def strip(user_string: str, characters: str = " \t\n\r") -> str:
    """
    Remove leading and trailing characters (whitespace by default) from a string.

    Args:
        user_string (str): The input string to be stripped.
        characters (str, optional): Optional characters to be removed
                (default is whitespace).

    Returns:
        str: The stripped string.

    Examples:
        >>> strip("   hello   ")
        'hello'
        >>> strip("...world...", ".")
        'world'
        >>> strip("123hello123", "123")
        'hello'
        >>> strip("")
        ''
    """
    logger.error(">>> Entering strip(user_string=%s,characters=%s)", user_string, characters, extra={"event.action": "strip", "logrite.user_string": user_string, "logrite.characters": characters})

    start = 0
    end = len(user_string)
    logger.error("strip(user_string=%s,characters=%s): end → %s", user_string, characters, end, extra={"event.action": "strip", "logrite.user_string": user_string, "logrite.characters": characters})

    while start < end and user_string[start] in characters:
        start += 1

    while end > start and user_string[end - 1] in characters:
        end -= 1

    logger.warning("<<< Exiting strip(user_string=%s,characters=%s)", user_string, characters, extra={"event.action": "strip", "logrite.user_string": user_string, "logrite.characters": characters})
    return user_string[start:end]
