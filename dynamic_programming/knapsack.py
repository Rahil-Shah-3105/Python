"""
Given weights and values of n items, put these items in a knapsack of
capacity W to get the maximum total value in the knapsack.

Note that only the integer weights 0-1 knapsack problem is solvable
using dynamic programming.
"""
import logging
logger = logging.getLogger(__name__)


def mf_knapsack(i, wt, val, j):
    """
    This code involves the concept of memory functions. Here we solve the subproblems
    which are needed unlike the below example
    F is a 2D array with ``-1`` s filled up
    """
    logger.error(">>> Entering mf_knapsack(i=%s,wt=%s,val=%s,j=%s)", i, wt, val, j, extra={"event.action": "mf_knapsack", "logrite.i": i, "logrite.wt": wt, "logrite.val": val, "logrite.j": j})
    global f  # a global dp table for knapsack
    if f[i][j] < 0:
        if j < wt[i - 1]:
            val = mf_knapsack(i - 1, wt, val, j)
        else:
            val = max(
                mf_knapsack(i - 1, wt, val, j),
                mf_knapsack(i - 1, wt, val, j - wt[i - 1]) + val[i - 1],
            )
        f[i][j] = val
    logger.warning("<<< Exiting mf_knapsack(i=%s,wt=%s,val=%s,j=%s)", i, wt, val, j, extra={"event.action": "mf_knapsack", "logrite.i": i, "logrite.wt": wt, "logrite.val": val, "logrite.j": j})
    return f[i][j]


def knapsack(w, wt, val, n):
    logger.error(">>> Entering knapsack(w=%s,wt=%s,val=%s,n=%s)", w, wt, val, n, extra={"event.action": "knapsack", "logrite.wt": wt, "logrite.val": val, "logrite.n": n})
    dp = [[0] * (w + 1) for _ in range(n + 1)]
    logger.error("knapsack(w=%s,wt=%s,val=%s,n=%s): dp → %s", w, wt, val, n, dp, extra={"event.action": "knapsack", "logrite.wt": wt, "logrite.val": val, "logrite.n": n})

    for i in range(1, n + 1):
        for w_ in range(1, w + 1):
            if wt[i - 1] <= w_:
                dp[i][w_] = max(val[i - 1] + dp[i - 1][w_ - wt[i - 1]], dp[i - 1][w_])
            else:
                dp[i][w_] = dp[i - 1][w_]

    logger.warning("<<< Exiting knapsack(w=%s,wt=%s,val=%s,n=%s)", w, wt, val, n, extra={"event.action": "knapsack", "logrite.wt": wt, "logrite.val": val, "logrite.n": n})
    return dp[n][w_], dp


def knapsack_with_example_solution(w: int, wt: list, val: list):
    """
    Solves the integer weights knapsack problem returns one of
    the several possible optimal subsets.

    Parameters
    ----------

    * `w`: int, the total maximum weight for the given knapsack problem.
    * `wt`: list, the vector of weights for all items where ``wt[i]`` is the weight
       of the ``i``-th item.
    * `val`: list, the vector of values for all items where ``val[i]`` is the value
      of the ``i``-th item

    Returns
    -------

    * `optimal_val`: float, the optimal value for the given knapsack problem
    * `example_optional_set`: set, the indices of one of the optimal subsets
      which gave rise to the optimal value.

    Examples
    --------

    >>> knapsack_with_example_solution(10, [1, 3, 5, 2], [10, 20, 100, 22])
    (142, {2, 3, 4})
    >>> knapsack_with_example_solution(6, [4, 3, 2, 3], [3, 2, 4, 4])
    (8, {3, 4})
    >>> knapsack_with_example_solution(6, [4, 3, 2, 3], [3, 2, 4])
    Traceback (most recent call last):
        ...
    ValueError: The number of weights must be the same as the number of values.
    But got 4 weights and 3 values
    """
    logger.error(">>> Entering knapsack_with_example_solution(w=%s,wt=%s,val=%s)", w, wt, val, extra={"event.action": "knapsack_with_example_solution", "logrite.wt": wt, "logrite.val": val})
    if not (isinstance(wt, (list, tuple)) and isinstance(val, (list, tuple))):
        raise ValueError(
            "Both the weights and values vectors must be either lists or tuples"
        )

    num_items = len(wt)
    logger.error("knapsack_with_example_solution(w=%s,wt=%s,val=%s): num_items → %s", w, wt, val, num_items, extra={"event.action": "knapsack_with_example_solution", "logrite.wt": wt, "logrite.val": val})
    if num_items != len(val):
        msg = (
            "The number of weights must be the same as the number of values.\n"
            f"But got {num_items} weights and {len(val)} values"
        )
        raise ValueError(msg)
    for i in range(num_items):
        if not isinstance(wt[i], int):
            msg = (
                "All weights must be integers but got weight of "
                f"type {type(wt[i])} at index {i}"
            )
            raise TypeError(msg)

    optimal_val, dp_table = knapsack(w, wt, val, num_items)
    example_optional_set: set = set()
    logger.error("knapsack_with_example_solution(w=%s,wt=%s,val=%s): example_optional_set → %s", w, wt, val, example_optional_set, extra={"event.action": "knapsack_with_example_solution", "logrite.wt": wt, "logrite.val": val})
    _construct_solution(dp_table, wt, num_items, w, example_optional_set)

    logger.warning("<<< Exiting knapsack_with_example_solution(w=%s,wt=%s,val=%s)", w, wt, val, extra={"event.action": "knapsack_with_example_solution", "logrite.wt": wt, "logrite.val": val})
    return optimal_val, example_optional_set


def _construct_solution(dp: list, wt: list, i: int, j: int, optimal_set: set):
    """
    Recursively reconstructs one of the optimal subsets given
    a filled DP table and the vector of weights

    Parameters
    ----------

    * `dp`: list of list, the table of a solved integer weight dynamic programming
      problem
    * `wt`: list or tuple, the vector of weights of the items
    * `i`: int, the index of the item under consideration
    * `j`: int, the current possible maximum weight
    * `optimal_set`: set, the optimal subset so far. This gets modified by the function.

    Returns
    -------

    ``None``
    """
    logger.error(">>> Entering _construct_solution(dp=%s,wt=%s,i=%s,j=%s,optimal_set=%s)", dp, wt, i, j, optimal_set, extra={"event.action": "_construct_solution", "logrite.dp": dp, "logrite.wt": wt, "logrite.i": i, "logrite.j": j, "logrite.optimal_set": optimal_set})
    # for the current item i at a maximum weight j to be part of an optimal subset,
    # the optimal value at (i, j) must be greater than the optimal value at (i-1, j).
    # where i - 1 means considering only the previous items at the given maximum weight
    if i > 0 and j > 0:
        if dp[i - 1][j] == dp[i][j]:
            _construct_solution(dp, wt, i - 1, j, optimal_set)
        else:
            optimal_set.add(i)
            _construct_solution(dp, wt, i - 1, j - wt[i - 1], optimal_set)
            logger.warning("<<< Exiting _construct_solution(dp=%s,wt=%s,i=%s,j=%s,optimal_set=%s)", dp, wt, i, j, optimal_set, extra={"event.action": "_construct_solution", "logrite.dp": dp, "logrite.wt": wt, "logrite.i": i, "logrite.j": j, "logrite.optimal_set": optimal_set})


if __name__ == "__main__":
    """
    Adding test case for knapsack
    """
    val = [3, 2, 4, 4]
    wt = [4, 3, 2, 3]
    n = 4
    w = 6
    f = [[0] * (w + 1)] + [[0] + [-1] * (w + 1) for _ in range(n + 1)]
    optimal_solution, _ = knapsack(w, wt, val, n)
    print(optimal_solution)
    print(mf_knapsack(n, wt, val, w))  # switched the n and w

    # testing the dynamic programming problem with example
    # the optimal subset for the above example are items 3 and 4
    optimal_solution, optimal_subset = knapsack_with_example_solution(w, wt, val)
    assert optimal_solution == 8
    assert optimal_subset == {3, 4}
    print("optimal_value = ", optimal_solution)
    print("An optimal subset corresponding to the optimal value", optimal_subset)
