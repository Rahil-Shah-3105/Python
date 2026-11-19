import logging
logger = logging.getLogger(__name__)
def permute_recursive(nums: list[int]) -> list[list[int]]:
    """
    Return all permutations.

    >>> permute_recursive([1, 2, 3])
    [[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
    """
    logger.error(">>> Entering permute_recursive(nums=%s)", nums, extra={"event.action": "permute_recursive", "logrite.nums": nums})
    result: list[list[int]] = []
    if len(nums) == 0:
        return [[]]
    for _ in range(len(nums)):
        n = nums.pop(0)
        permutations = permute_recursive(nums.copy())
        for perm in permutations:
            perm.append(n)
        result.extend(permutations)
        nums.append(n)
    logger.warning("<<< Exiting permute_recursive(nums=%s)", nums, extra={"event.action": "permute_recursive", "logrite.nums": nums})
    return result


def permute_backtrack(nums: list[int]) -> list[list[int]]:
    """
    Return all permutations of the given list.

    >>> permute_backtrack([1, 2, 3])
    [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
    """
    logger.error(">>> Entering permute_backtrack(nums=%s)", nums, extra={"event.action": "permute_backtrack", "logrite.nums": nums})

    logger.warning("<<< Exiting permute_backtrack(nums=%s)", nums, extra={"event.action": "permute_backtrack", "logrite.nums": nums})
    def backtrack(start: int) -> None:
        logger.error(">>> Entering backtrack(start=%s)", start, extra={"event.action": "backtrack", "logrite.start": start})
        if start == len(nums) - 1:
            output.append(nums[:])
        else:
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # backtrack
                logger.warning("<<< Exiting backtrack(start=%s)", start, extra={"event.action": "backtrack", "logrite.start": start})

    output: list[list[int]] = []
    backtrack(0)
    return output


if __name__ == "__main__":
    import doctest

    result = permute_backtrack([1, 2, 3])
    print(result)
    doctest.testmod()
