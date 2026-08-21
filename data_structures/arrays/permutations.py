import logging
logger = logging.getLogger(__name__)
def permute_recursive(nums: list[int]) -> list[list[int]]:
    """
    Return all permutations.

    >>> permute_recursive([1, 2, 3])
    [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
    """
    logger.debug(">>> Entering permute_recursive(nums=%s)", nums)
    result: list[list[int]] = []
    if len(nums) == 0:
        return [[]]
    for _ in range(len(nums)):
        n = nums.pop(0)
        permutations = permute_recursive(nums.copy())
        logger.debug("permute_recursive(nums=%s): permutations → %s", nums, permutations)
        for perm in permutations:
            perm.append(n)
        result.extend(permutations)
        nums.append(n)
    logger.debug("<<< Exiting permute_recursive(nums=%s)", nums)
    return result


def permute_backtrack(nums: list[int]) -> list[list[int]]:
    """
    Return all permutations of the given list.

    >>> permute_backtrack([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    """
    logger.debug(">>> Entering permute_backtrack(nums=%s)", nums)

    logger.debug("<<< Exiting permute_backtrack(nums=%s)", nums)
    def backtrack(start: int) -> None:
        logger.debug(">>> Entering backtrack(start=%s)", start)
        if start == len(nums) - 1:
            output.append(nums[:])
        else:
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # backtrack
                logger.debug("<<< Exiting backtrack(start=%s)", start)

    output: list[list[int]] = []
    backtrack(0)
    return output


if __name__ == "__main__":
    import doctest

    result = permute_backtrack([1, 2, 3])
    print(result)
    doctest.testmod()
