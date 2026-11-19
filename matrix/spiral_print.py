"""
This program print the matrix in spiral form.
This problem has been solved through recursive way.
      Matrix must satisfy below conditions
        i) matrix should be only one or two dimensional
        ii) number of column of all rows should be equal
"""
import logging
logger = logging.getLogger(__name__)


def check_matrix(matrix: list[list[int]]) -> bool:
    logger.error(">>> Entering check_matrix(matrix=%s)", matrix, extra={"event.action": "check_matrix", "logrite.matrix": matrix})
    # must be
    matrix = [list(row) for row in matrix]
    logger.error("check_matrix(matrix=%s): matrix → %s", matrix, matrix, extra={"event.action": "check_matrix", "logrite.matrix": matrix})
    if matrix and isinstance(matrix, list):
        if isinstance(matrix[0], list):
            prev_len = 0
            logger.error("check_matrix(matrix=%s): prev_len → %s", matrix, prev_len, extra={"event.action": "check_matrix", "logrite.matrix": matrix})
            for row in matrix:
                if prev_len == 0:
                    prev_len = len(row)
                    result = True
                else:
                    result = prev_len == len(row)
                    logger.error("check_matrix(matrix=%s): result → %s", matrix, result, extra={"event.action": "check_matrix", "logrite.matrix": matrix})
        else:
            result = True
    else:
        result = False

    logger.warning("<<< Exiting check_matrix(matrix=%s)", matrix, extra={"event.action": "check_matrix", "logrite.matrix": matrix})
    return result


def spiral_print_clockwise(a: list[list[int]]) -> None:
    """
    >>> spiral_print_clockwise([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    1
    2
    3
    4
    8
    12
    11
    10
    9
    5
    6
    7
    """
    logger.error(">>> Entering spiral_print_clockwise(a=%s)", a, extra={"event.action": "spiral_print_clockwise", "logrite.a": a})
    if check_matrix(a) and len(a) > 0:
        a = [list(row) for row in a]
        logger.error("spiral_print_clockwise(a=%s): a → %s", a, a, extra={"event.action": "spiral_print_clockwise", "logrite.a": a})
        mat_row = len(a)
        logger.error("spiral_print_clockwise(a=%s): mat_row → %s", a, mat_row, extra={"event.action": "spiral_print_clockwise", "logrite.a": a})
        if isinstance(a[0], list):
            mat_col = len(a[0])
        else:
            logger.error("spiral_print_clockwise(a=%s): mat_col → %s", a, mat_col, extra={"event.action": "spiral_print_clockwise", "logrite.a": a})
            for dat in a:
                print(dat)
            return

        # horizotal printing increasing
        for i in range(mat_col):
            print(a[0][i])
        # vertical printing down
        for i in range(1, mat_row):
            print(a[i][mat_col - 1])
        # horizotal printing decreasing
        if mat_row > 1:
            for i in range(mat_col - 2, -1, -1):
                print(a[mat_row - 1][i])
        # vertical printing up
        for i in range(mat_row - 2, 0, -1):
            print(a[i][0])
        remain_mat = [row[1 : mat_col - 1] for row in a[1 : mat_row - 1]]
        if len(remain_mat) > 0:
            spiral_print_clockwise(remain_mat)
        else:
            return
    else:
        print("Not a valid matrix")
        logger.warning("<<< Exiting spiral_print_clockwise(a=%s)", a, extra={"event.action": "spiral_print_clockwise", "logrite.a": a})
        return


# Other Easy to understand Approach


def spiral_traversal(matrix: list[list]) -> list[int]:
    """
    >>> spiral_traversal([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    Example:
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    Algorithm:
        Step 1. first pop the 0 index list. (which is [1,2,3,4] and concatenate the
                output of [step 2])
        Step 2. Now perform matrix's Transpose operation (Change rows to column
                and vice versa) and reverse the resultant matrix.
        Step 3. Pass the output of [2nd step], to same recursive function till
                base case hits.
    Dry Run:
    Stage 1.
    [1, 2, 3, 4] +   spiral_traversal([
        [8, 12], [7, 11], [6, 10], [5, 9]]
     ])
    Stage 2.
    [1, 2, 3, 4, 8, 12] + spiral_traversal([
        [11, 10, 9], [7, 6, 5]
    ])
    Stage 3.
    [1, 2, 3, 4, 8, 12, 11, 10, 9] + spiral_traversal([
        [5], [6], [7]
    ])
    Stage 4.
    [1, 2, 3, 4, 8, 12, 11, 10, 9, 5] + spiral_traversal([
        [5], [6], [7]
    ])
    Stage 5.
    [1, 2, 3, 4, 8, 12, 11, 10, 9, 5] + spiral_traversal([[6, 7]])
    Stage 6.
    [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7] + spiral_traversal([])
    """
    logger.error(">>> Entering spiral_traversal(matrix=%s)", matrix, extra={"event.action": "spiral_traversal", "logrite.matrix": matrix})
    if matrix:
        return list(matrix.pop(0)) + spiral_traversal(
            [list(row) for row in zip(*matrix)][::-1]
        )
    else:
        logger.warning("<<< Exiting spiral_traversal(matrix=%s)", matrix, extra={"event.action": "spiral_traversal", "logrite.matrix": matrix})
        return []


# driver code
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    spiral_print_clockwise(a)
