import logging
logger = logging.getLogger(__name__)
"""
Given a string s, partition s such that every substring of the
partition is a palindrome.
Find the minimum cuts needed for a palindrome partitioning of s.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
For other explanations refer to: https://www.youtube.com/watch?v=_H8V5hJUGd0
"""


def find_minimum_partitions(string: str) -> int:
    """
    Returns the minimum cuts needed for a palindrome partitioning of string

    >>> find_minimum_partitions("aab")
    1
    >>> find_minimum_partitions("aaa")
    0
    >>> find_minimum_partitions("ababbbabbababa")
    3
    """
    logger.debug(">>> Entering find_minimum_partitions(string=%s)", string)
    length = len(string)
    logger.debug("find_minimum_partitions(string=%s): length → %s", string, length)
    cut = [0] * length
    logger.debug("find_minimum_partitions(string=%s): cut → %s", string, cut)
    is_palindromic = [[False for i in range(length)] for j in range(length)]
    logger.debug("find_minimum_partitions(string=%s): is_palindromic → %s", string, is_palindromic)
    for i, c in enumerate(string):
        mincut = i
        logger.debug("find_minimum_partitions(string=%s): mincut → %s", string, mincut)
        for j in range(i + 1):
            if c == string[j] and (i - j < 2 or is_palindromic[j + 1][i - 1]):
                is_palindromic[j][i] = True
                mincut = min(mincut, 0 if j == 0 else (cut[j - 1] + 1))
        cut[i] = mincut
    logger.debug("<<< Exiting find_minimum_partitions(string=%s)", string)
    return cut[length - 1]


if __name__ == "__main__":
    s = input("Enter the string: ").strip()
    ans = find_minimum_partitions(s)
    print(f"Minimum number of partitions required for the '{s}' is {ans}")
