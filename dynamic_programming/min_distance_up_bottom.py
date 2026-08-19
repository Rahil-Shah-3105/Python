"""
Author  : Alexander Pantyukhin
Date    : October 14, 2022
This is an implementation of the up-bottom approach to find edit distance.
The implementation was tested on Leetcode: https://leetcode.com/problems/edit-distance/

Levinstein distance
Dynamic Programming: up -> down.
"""

import functools
import logging
logger = logging.getLogger(__name__)


def min_distance_up_bottom(word1: str, word2: str) -> int:
    """
    >>> min_distance_up_bottom("intention", "execution")
    5
    >>> min_distance_up_bottom("intention", "")
    9
    >>> min_distance_up_bottom("", "")
    0
    >>> min_distance_up_bottom("zooicoarchaeologist", "zoologist")
    10
    """
    logger.debug(">>> Entering min_distance_up_bottom(word1=%s,word2=%s)", word1, word2)
    len_word1 = len(word1)
    logger.debug("min_distance_up_bottom(word1=%s,word2=%s): len_word1 → %s", word1, word2, len_word1)
    len_word2 = len(word2)
    logger.debug("min_distance_up_bottom(word1=%s,word2=%s): len_word2 → %s", word1, word2, len_word2)

    @functools.cache
    def min_distance(index1: int, index2: int) -> int:
        logger.debug(">>> Entering min_distance(index1=%s,index2=%s)", index1, index2)
        # if first word index overflows - delete all from the second word
        if index1 >= len_word1:
            return len_word2 - index2
        # if second word index overflows - delete all from the first word
        if index2 >= len_word2:
            return len_word1 - index1
        diff = int(word1[index1] != word2[index2])  # current letters not identical
        logger.debug("<<< Exiting min_distance(index1=%s,index2=%s)", index1, index2)
        return min(
            1 + min_distance(index1 + 1, index2),
            1 + min_distance(index1, index2 + 1),
            diff + min_distance(index1 + 1, index2 + 1),
        )

    return min_distance(0, 0)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
