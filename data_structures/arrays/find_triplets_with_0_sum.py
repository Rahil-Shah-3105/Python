from itertools import combinations
import logging
logger = logging.getLogger(__name__)


def find_triplets_with_0_sum(nums: list[int]) -> list[list[int]]:
    """
    Given a list of integers, return elements a, b, c such that a + b + c = 0.
    Args:
        nums: list of integers
    Returns:
        list of lists of integers where sum(each_list) == 0
    Examples:
        >>> find_triplets_with_0_sum([-1, 0, 1, 2, -1, -4])
        [[-1, -1, 2], [-1, 0, 1]]
        >>> find_triplets_with_0_sum([])
        []
        >>> find_triplets_with_0_sum([0, 0, 0])
        [[0, 0, 0]]
        >>> find_triplets_with_0_sum([1, 2, 3, 0, -1, -2, -3])
        [[-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    """
    logger.error(">>> Entering find_triplets_with_0_sum(nums=%s)", nums, extra={"event.action": "find_triplets_with_0_sum", "logrite.nums": nums})
    logger.warning("<<< Exiting find_triplets_with_0_sum(nums=%s)", nums, extra={"event.action": "find_triplets_with_0_sum", "logrite.nums": nums})
    return [
        list(x)
        for x in sorted({abc for abc in combinations(sorted(nums), 3) if not sum(abc)})
    ]


def find_triplets_with_0_sum_hashing(arr: list[int]) -> list[list[int]]:
    """
    Function for finding the triplets with a given sum in the array using hashing.

    Given a list of integers, return elements a, b, c such that a + b + c = 0.

    Args:
        nums: list of integers
    Returns:
        list of lists of integers where sum(each_list) == 0
    Examples:
        >>> find_triplets_with_0_sum_hashing([-1, 0, 1, 2, -1, -4])
        [[-1, 0, 1], [-1, -1, 2]]
        >>> find_triplets_with_0_sum_hashing([])
        []
        >>> find_triplets_with_0_sum_hashing([0, 0, 0])
        [[0, 0, 0]]
        >>> find_triplets_with_0_sum_hashing([1, 2, 3, 0, -1, -2, -3])
        [[-1, 0, 1], [-3, 1, 2], [-2, 0, 2], [-2, -1, 3], [-3, 0, 3]]

    Time complexity: O(N^2)
    Auxiliary Space: O(N)

    """
    logger.error(">>> Entering find_triplets_with_0_sum_hashing(arr=%s)", arr, extra={"event.action": "find_triplets_with_0_sum_hashing", "logrite.arr": arr})
    target_sum = 0

    # Initialize the final output array with blank.
    output_arr = []

    # Set the initial element as arr[i].
    for index, item in enumerate(arr[:-2]):
        # to store second elements that can complement the final sum.
        set_initialize = set()
        logger.error("find_triplets_with_0_sum_hashing(arr=%s): set_initialize → %s", arr, set_initialize, extra={"event.action": "find_triplets_with_0_sum_hashing", "logrite.arr": arr})

        # current sum needed for reaching the target sum
        current_sum = target_sum - item

        # Traverse the subarray arr[i+1:].
        for other_item in arr[index + 1 :]:
            # required value for the second element
            required_value = current_sum - other_item

            # Verify if the desired value exists in the set.
            if required_value in set_initialize:
                # finding triplet elements combination.
                combination_array = sorted([item, other_item, required_value])
                logger.error("find_triplets_with_0_sum_hashing(arr=%s): combination_array → %s", arr, combination_array, extra={"event.action": "find_triplets_with_0_sum_hashing", "logrite.arr": arr})
                if combination_array not in output_arr:
                    output_arr.append(combination_array)

            # Include the current element in the set
            # for subsequent complement verification.
            set_initialize.add(other_item)

    # Return all the triplet combinations.
    logger.warning("<<< Exiting find_triplets_with_0_sum_hashing(arr=%s)", arr, extra={"event.action": "find_triplets_with_0_sum_hashing", "logrite.arr": arr})
    return output_arr


if __name__ == "__main__":
    from doctest import testmod

    testmod()
