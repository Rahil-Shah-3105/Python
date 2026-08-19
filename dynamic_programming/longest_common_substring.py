import logging
logger = logging.getLogger(__name__)
"""
Longest Common Substring Problem Statement:
    Given two sequences, find the
    longest common substring present in both of them. A substring is
    necessarily continuous.

Example:
    ``abcdef`` and ``xabded`` have two longest common substrings, ``ab`` or ``de``.
    Therefore, algorithm should return any one of them.
"""


def longest_common_substring(text1: str, text2: str) -> str:
    """
    Finds the longest common substring between two strings.

    >>> longest_common_substring("", "")
    ''
    >>> longest_common_substring("a","")
    ''
    >>> longest_common_substring("", "a")
    ''
    >>> longest_common_substring("a", "a")
    'a'
    >>> longest_common_substring("abcdef", "bcd")
    'bcd'
    >>> longest_common_substring("abcdef", "xabded")
    'ab'
    >>> longest_common_substring("GeeksforGeeks", "GeeksQuiz")
    'Geeks'
    >>> longest_common_substring("abcdxyz", "xyzabcd")
    'abcd'
    >>> longest_common_substring("zxabcdezy", "yzabcdezx")
    'abcdez'
    >>> longest_common_substring("OldSite:GeeksforGeeks.org", "NewSite:GeeksQuiz.com")
    'Site:Geeks'
    >>> longest_common_substring(1, 1)
    Traceback (most recent call last):
        ...
    ValueError: longest_common_substring() takes two strings for inputs
    """
    logger.debug(">>> Entering longest_common_substring(text1=%s,text2=%s)", text1, text2)

    if not (isinstance(text1, str) and isinstance(text2, str)):
        raise ValueError("longest_common_substring() takes two strings for inputs")

    if not text1 or not text2:
        return ""

    text1_length = len(text1)
    logger.debug("longest_common_substring(text1=%s,text2=%s): text1_length → %s", text1, text2, text1_length)
    text2_length = len(text2)
    logger.debug("longest_common_substring(text1=%s,text2=%s): text2_length → %s", text1, text2, text2_length)

    dp = [[0] * (text2_length + 1) for _ in range(text1_length + 1)]
    end_pos = 0
    logger.debug("longest_common_substring(text1=%s,text2=%s): end_pos → %s", text1, text2, end_pos)
    max_length = 0
    logger.debug("longest_common_substring(text1=%s,text2=%s): max_length → %s", text1, text2, max_length)

    for i in range(1, text1_length + 1):
        for j in range(1, text2_length + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                if dp[i][j] > max_length:
                    end_pos = i
                    max_length = dp[i][j]

    logger.debug("<<< Exiting longest_common_substring(text1=%s,text2=%s)", text1, text2)
    return text1[end_pos - max_length : end_pos]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
