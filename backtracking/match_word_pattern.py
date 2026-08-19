import logging
logger = logging.getLogger(__name__)
def match_word_pattern(pattern: str, input_string: str) -> bool:
    """
    Determine if a given pattern matches a string using backtracking.

    pattern: The pattern to match.
    input_string: The string to match against the pattern.
    return: True if the pattern matches the string, False otherwise.

    >>> match_word_pattern("aba", "GraphTreesGraph")
    True

    >>> match_word_pattern("xyx", "PythonRubyPython")
    True

    >>> match_word_pattern("GG", "PythonJavaPython")
    False
    """
    logger.debug(">>> Entering match_word_pattern(pattern=%s,input_string=%s)", pattern, input_string)

    logger.debug("<<< Exiting match_word_pattern(pattern=%s,input_string=%s)", pattern, input_string)
    def backtrack(pattern_index: int, str_index: int) -> bool:
        """
        >>> backtrack(0, 0)
        True

        >>> backtrack(0, 1)
        True

        >>> backtrack(0, 4)
        False
        """
        logger.debug(">>> Entering backtrack(pattern_index=%s,str_index=%s)", pattern_index, str_index)
        if pattern_index == len(pattern) and str_index == len(input_string):
            return True
        if pattern_index == len(pattern) or str_index == len(input_string):
            return False
        char = pattern[pattern_index]
        logger.debug("backtrack(pattern_index=%s,str_index=%s): char → %s", pattern_index, str_index, char)
        if char in pattern_map:
            mapped_str = pattern_map[char]
            logger.debug("backtrack(pattern_index=%s,str_index=%s): mapped_str → %s", pattern_index, str_index, mapped_str)
            if input_string.startswith(mapped_str, str_index):
                return backtrack(pattern_index + 1, str_index + len(mapped_str))
            else:
                return False
        for end in range(str_index + 1, len(input_string) + 1):
            substr = input_string[str_index:end]
            logger.debug("backtrack(pattern_index=%s,str_index=%s): substr → %s", pattern_index, str_index, substr)
            if substr in str_map:
                continue
            pattern_map[char] = substr
            str_map[substr] = char
            if backtrack(pattern_index + 1, end):
                return True
            del pattern_map[char]
            del str_map[substr]
        logger.debug("<<< Exiting backtrack(pattern_index=%s,str_index=%s)", pattern_index, str_index)
        return False

    pattern_map: dict[str, str] = {}
    str_map: dict[str, str] = {}
    return backtrack(0, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
