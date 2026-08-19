import logging
logger = logging.getLogger(__name__)
"""
https://www.hackerrank.com/challenges/abbr/problem
You can perform the following operation on some string, :

1. Capitalize zero or more of 's lowercase letters at some index i
   (i.e., make them uppercase).
2. Delete all of the remaining lowercase letters in .

Example:
a=daBcd and b="ABC"
daBcd -> capitalize a and c(dABCd) -> remove d (ABC)
"""


def abbr(a: str, b: str) -> bool:
    """
    >>> abbr("daBcd", "ABC")
    True
    >>> abbr("dBcd", "ABC")
    False
    """
    logger.debug(">>> Entering abbr(a=%s,b=%s)", a, b)
    n = len(a)
    logger.debug("abbr(a=%s,b=%s): n → %s", a, b, n)
    m = len(b)
    logger.debug("abbr(a=%s,b=%s): m → %s", a, b, m)
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    logger.debug("abbr(a=%s,b=%s): dp → %s", a, b, dp)
    dp[0][0] = True
    for i in range(n):
        for j in range(m + 1):
            if dp[i][j]:
                if j < m and a[i].upper() == b[j]:
                    dp[i + 1][j + 1] = True
                if a[i].islower():
                    dp[i + 1][j] = True
    logger.debug("<<< Exiting abbr(a=%s,b=%s)", a, b)
    return dp[n][m]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
