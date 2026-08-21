from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def largest_divisible_subset(items: list[int]) -> list[int]:
    """
    Algorithm to find the biggest subset in the given array such that for any 2 elements
    x and y in the subset, either x divides y or y divides x.
    >>> largest_divisible_subset([1, 16, 7, 8, 4])
    [16, 8, 4, 1]
    >>> largest_divisible_subset([1, 2, 3])
    [2, 1]
    >>> largest_divisible_subset([-1, -2, -3])
    [-3]
    >>> largest_divisible_subset([1, 2, 4, 8])
    [8, 4, 2, 1]
    >>> largest_divisible_subset((1, 2, 4, 8))
    [8, 4, 2, 1]
    >>> largest_divisible_subset([1, 1, 1])
    [1, 1, 1]
    >>> largest_divisible_subset([0, 0, 0])
    [0, 0, 0]
    >>> largest_divisible_subset([-1, -1, -1])
    [-1, -1, -1]
    >>> largest_divisible_subset([])
    []
    """
    logger.debug(">>> Entering largest_divisible_subset(items=%s)", items)
    # Sort the array in ascending order as the sequence does not matter we only have to
    # pick up a subset.
    items = sorted(items)
    logger.debug("largest_divisible_subset(items=%s): items → %s", items, items)

    number_of_items = len(items)
    logger.debug("largest_divisible_subset(items=%s): number_of_items → %s", items, number_of_items)

    # Initialize memo with 1s and hash with increasing numbers
    memo = [1] * number_of_items
    logger.debug("largest_divisible_subset(items=%s): memo → %s", items, memo)
    hash_array = list(range(number_of_items))
    logger.debug("largest_divisible_subset(items=%s): hash_array → %s", items, hash_array)

    # Iterate through the array
    for i, item in enumerate(items):
        for prev_index in range(i):
            if ((items[prev_index] != 0 and item % items[prev_index]) == 0) and (
                (1 + memo[prev_index]) > memo[i]
            ):
                memo[i] = 1 + memo[prev_index]
                hash_array[i] = prev_index

    ans = -1
    logger.debug("largest_divisible_subset(items=%s): ans → %s", items, ans)
    last_index = -1

    # Find the maximum length and its corresponding index
    for i, memo_item in enumerate(memo):
        if memo_item > ans:
            ans = memo_item
            last_index = i

    # Reconstruct the divisible subset
    if last_index == -1:
        return []
    result = [items[last_index]]
    while hash_array[last_index] != last_index:
        last_index = hash_array[last_index]
        result.append(items[last_index])

    logger.debug("<<< Exiting largest_divisible_subset(items=%s)", items)
    return result


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    items = [1, 16, 7, 8, 4]
    print(
        f"The longest divisible subset of {items} is {largest_divisible_subset(items)}."
    )
