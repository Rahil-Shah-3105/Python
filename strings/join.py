import logging
logger = logging.getLogger(__name__)
"""
Program to join a list of strings with a separator
"""


def join(separator: str, separated: list[str]) -> str:
    """
    Joins a list of strings using a separator
    and returns the result.

    :param separator: Separator to be used
                for joining the strings.
    :param separated: List of strings to be joined.

    :return: Joined string with the specified separator.

    Examples:

    >>> join("", ["a", "b", "c", "d"])
    'abcd'
    >>> join("#", ["a", "b", "c", "d"])
    'a#b#c#d'
    >>> join("#", "a")
    'a'
    >>> join(" ", ["You", "are", "amazing!"])
    'You are amazing!'
    >>> join(",", ["", "", ""])
    ',,'

    This example should raise an
    exception for non-string elements:
    >>> join("#", ["a", "b", "c", 1])
    Traceback (most recent call last):
        ...
    Exception: join() accepts only strings

    Additional test case with a different separator:
    >>> join("-", ["apple", "banana", "cherry"])
    'apple-banana-cherry'
    """
    logger.debug(">>> Entering join(separator=%s,separated=%s)", separator, separated)

    # Check that all elements are strings
    for word_or_phrase in separated:
        # If the element is not a string, raise an exception
        if not isinstance(word_or_phrase, str):
            raise Exception("join() accepts only strings")

    joined: str = ""
    logger.debug("join(separator=%s,separated=%s): joined → %s", separator, separated, joined)
    """
    The last element of the list is not followed by the separator.
    So, we need to iterate through the list and join each element
    with the separator except the last element.
    """
    logger.error("Exception in join(separator=%s,separated=%s)", separator, separated, exc_info=True)
    logger.debug("join(separator=%s,separated=%s): last_index → %s", separator, separated, last_index)
    last_index: int = len(separated) - 1
    """
    Iterate through the list and join each element with the separator.
    Except the last element, all other elements are followed by the separator.
    """
    for word_or_phrase in separated[:last_index]:
        # join the element with the separator.
        joined += word_or_phrase + separator

    # If the list is not empty, join the last element.
    if separated != []:
        joined += separated[last_index]

    # Return the joined string.
    logger.debug("<<< Exiting join(separator=%s,separated=%s)", separator, separated)
    return joined


if __name__ == "__main__":
    from doctest import testmod

    testmod()
