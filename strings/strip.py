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
    logger.debug(">>> Entering strip(user_string=%s,characters=%s)", user_string, characters)

    start = 0
    logger.debug("strip(user_string=%s,characters=%s): start → %s", user_string, characters, start)
    end = len(user_string)
    logger.debug("strip(user_string=%s,characters=%s): end → %s", user_string, characters, end)

    while start < end and user_string[start] in characters:
        start += 1

    while end > start and user_string[end - 1] in characters:
        end -= 1

    logger.debug("<<< Exiting strip(user_string=%s,characters=%s)", user_string, characters)
    return user_string[start:end]
