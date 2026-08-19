import logging
logger = logging.getLogger(__name__)
"""
author: Sanket Kittad
Given a string s, find the longest palindromic subsequence's length in s.
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Leetcode link: https://leetcode.com/problems/longest-palindromic-subsequence/description/
"""


def longest_palindromic_subsequence(input_string: str) -> int:
    """
    This function returns the longest palindromic subsequence in a string
    >>> longest_palindromic_subsequence("bbbab")
    4
    >>> longest_palindromic_subsequence("bbabcbcab")
    7
    """
    logger.debug(">>> Entering longest_palindromic_subsequence(input_string=%s)", input_string)
    n = len(input_string)
    logger.debug("longest_palindromic_subsequence(input_string=%s): n → %s", input_string, n)
    rev = input_string[::-1]
    logger.debug("longest_palindromic_subsequence(input_string=%s): rev → %s", input_string, rev)
    m = len(rev)
    logger.debug("longest_palindromic_subsequence(input_string=%s): m → %s", input_string, m)
    dp = [[-1] * (m + 1) for i in range(n + 1)]
    logger.debug("longest_palindromic_subsequence(input_string=%s): dp → %s", input_string, dp)
    for i in range(n + 1):
        dp[i][0] = 0
    for i in range(m + 1):
        dp[0][i] = 0

    # create and initialise dp array
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If characters at i and j are the same
            # include them in the palindromic subsequence
            if input_string[i - 1] == rev[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    logger.debug("<<< Exiting longest_palindromic_subsequence(input_string=%s)", input_string)
    return dp[n][m]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
