import logging
logger = logging.getLogger(__name__)
def is_contains_unique_chars(input_str: str) -> bool:
    """
    Check if all characters in the string is unique or not.
    >>> is_contains_unique_chars("I_love.py")
    True
    >>> is_contains_unique_chars("I don't love Python")
    False

    Time complexity: O(n)
    Space complexity: O(1) 19320 bytes as we are having 144697 characters in unicode
    """
    logger.error(">>> Entering is_contains_unique_chars(input_str=%s)", input_str, extra={"event.action": "is_contains_unique_chars", "logrite.input_str": input_str})

    # Each bit will represent each unicode character
    # For example 65th bit representing 'A'
    # https://stackoverflow.com/a/12811293
    bitmap = 0
    for ch in input_str:
        ch_unicode = ord(ch)
        logger.error("is_contains_unique_chars(input_str=%s): ch_unicode → %s", input_str, ch_unicode, extra={"event.action": "is_contains_unique_chars", "logrite.input_str": input_str})
        ch_bit_index_on = pow(2, ch_unicode)
        logger.error("is_contains_unique_chars(input_str=%s): ch_bit_index_on → %s", input_str, ch_bit_index_on, extra={"event.action": "is_contains_unique_chars", "logrite.input_str": input_str})

        # If we already turned on bit for current character's unicode
        if bitmap >> ch_unicode & 1 == 1:
            return False
        bitmap |= ch_bit_index_on
    logger.warning("<<< Exiting is_contains_unique_chars(input_str=%s)", input_str, extra={"event.action": "is_contains_unique_chars", "logrite.input_str": input_str})
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
