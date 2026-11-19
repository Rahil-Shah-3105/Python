import logging
logger = logging.getLogger(__name__)
def kth_permutation(k, n):
    """
    Finds k'th lexicographic permutation (in increasing order) of
    0,1,2,...n-1 in O(n^2) time.

    Examples:
    First permutation is always 0,1,2,...n
    >>> kth_permutation(0,5)
    [0, 1, 2, 3, 4]

    The order of permutation of 0,1,2,3 is [0,1,2,3], [0,1,3,2], [0,2,1,3],
    [0,2,3,1], [0,3,1,2], [0,3,2,1], [1,0,2,3], [1,0,3,2], [1,2,0,3],
    [1,2,3,0], [1,3,0,2]
    >>> kth_permutation(10,4)
    [1, 3, 0, 2]
    """
    logger.error(">>> Entering kth_permutation(k=%s,n=%s)", k, n, extra={"event.action": "kth_permutation", "logrite.k": k, "logrite.n": n})
    # Factorails from 1! to (n-1)!
    factorials = [1]
    for i in range(2, n):
        factorials.append(factorials[-1] * i)
    assert 0 <= k < factorials[-1] * n, "k out of bounds"

    permutation = []
    elements = list(range(n))
    logger.error("kth_permutation(k=%s,n=%s): elements → %s", k, n, elements, extra={"event.action": "kth_permutation", "logrite.k": k, "logrite.n": n})

    # Find permutation
    while factorials:
        factorial = factorials.pop()
        logger.error("kth_permutation(k=%s,n=%s): factorial → %s", k, n, factorial, extra={"event.action": "kth_permutation", "logrite.k": k, "logrite.n": n})
        number, k = divmod(k, factorial)
        permutation.append(elements[number])
        elements.remove(elements[number])
    permutation.append(elements[0])

    logger.warning("<<< Exiting kth_permutation(k=%s,n=%s)", k, n, extra={"event.action": "kth_permutation", "logrite.k": k, "logrite.n": n})
    return permutation


if __name__ == "__main__":
    import doctest

    doctest.testmod()
