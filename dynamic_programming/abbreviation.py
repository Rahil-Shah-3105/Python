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
import logging
logger = logging.getLogger(__name__)


def abbr(a: str, b: str) -> bool:
    """
    >>> abbr("daBcd", "ABC")
    True
    >>> abbr("dBcd", "ABC")
    False
    """
    logger.error(">>> Entering abbr(a=%s,b=%s)", a, b, extra={"event.action": "abbr", "logrite.a": a, "logrite.b": b})
    n = len(a)
    logger.error("abbr(a=%s,b=%s): n → %s", a, b, n, extra={"event.action": "abbr", "logrite.a": a, "logrite.b": b})
    m = len(b)
    logger.error("abbr(a=%s,b=%s): m → %s", a, b, m, extra={"event.action": "abbr", "logrite.a": a, "logrite.b": b})
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    logger.error("abbr(a=%s,b=%s): dp → %s", a, b, dp, extra={"event.action": "abbr", "logrite.a": a, "logrite.b": b})
    dp[0][0] = True
    for i in range(n):
        for j in range(m + 1):
            if dp[i][j]:
                if j < m and a[i].upper() == b[j]:
                    dp[i + 1][j + 1] = True
                if a[i].islower():
                    dp[i + 1][j] = True
    logger.warning("<<< Exiting abbr(a=%s,b=%s)", a, b, extra={"event.action": "abbr", "logrite.a": a, "logrite.b": b})
    return dp[n][m]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
