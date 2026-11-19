"""
Heap's (iterative) algorithm returns the list of all permutations possible from a list.
It minimizes movement by generating each permutation from the previous one
by swapping only two elements.
More information:
https://en.wikipedia.org/wiki/Heap%27s_algorithm.
"""
import logging
logger = logging.getLogger(__name__)


def heaps(arr: list) -> list:
    """
    Pure python implementation of the iterative Heap's algorithm,
    returning all permutations of a list.
    >>> heaps([])
    [()]
    >>> heaps([0])
    [(0,)]
    >>> heaps([-1, 1])
    [(-1, 1), (1, -1)]
    >>> heaps([1, 2, 3])
    [(1, 2, 3), (2, 1, 3), (3, 1, 2), (1, 3, 2), (2, 3, 1), (3, 2, 1)]
    >>> from itertools import permutations
    >>> sorted(heaps([1,2,3])) == sorted(permutations([1,2,3]))
    True
    >>> all(sorted(heaps(x)) == sorted(permutations(x))
    ...     for x in ([], [0], [-1, 1], [1, 2, 3]))
    True
    """
    logger.error(">>> Entering heaps(arr=%s)", arr, extra={"event.action": "heaps", "logrite.arr": arr})

    if len(arr) <= 1:
        logger.warning("<<< Exiting heaps(arr=%s)", arr, extra={"event.action": "heaps", "logrite.arr": arr})
        return [tuple(arr)]

    res = []

    def generate(n: int, arr: list):
        logger.error(">>> Entering generate(n=%s,arr=%s)", n, arr, extra={"event.action": "generate", "logrite.n": n, "logrite.arr": arr})
        c = [0] * n
        res.append(tuple(arr))

        i = 0
        while i < n:
            if c[i] < i:
                if i % 2 == 0:
                    arr[0], arr[i] = arr[i], arr[0]
                else:
                    arr[c[i]], arr[i] = arr[i], arr[c[i]]
                res.append(tuple(arr))
                c[i] += 1
                i = 0
            else:
                c[i] = 0
                i += 1
                logger.warning("<<< Exiting generate(n=%s,arr=%s)", n, arr, extra={"event.action": "generate", "logrite.n": n, "logrite.arr": arr})

    generate(len(arr), arr)
    return res


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    arr = [int(item) for item in user_input.split(",")]
    print(heaps(arr))
