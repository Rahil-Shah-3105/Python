from __future__ import annotations

import math
import logging
logger = logging.getLogger(__name__)


def default_matrix_multiplication(a: list, b: list) -> list:
    """
    Multiplication only for 2x2 matrices
    """
    logger.debug(">>> Entering default_matrix_multiplication(a=%s,b=%s)", a, b)
    if len(a) != 2 or len(a[0]) != 2 or len(b) != 2 or len(b[0]) != 2:
        raise Exception("Matrices are not 2x2")
    new_matrix = [
    logger.debug("default_matrix_multiplication(a=%s,b=%s): new_matrix → %s", a, b, new_matrix)
        [a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
        [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]],
    ]
    logger.debug("<<< Exiting default_matrix_multiplication(a=%s,b=%s)", a, b)
    return new_matrix


def matrix_addition(matrix_a: list, matrix_b: list):
    logger.debug(">>> Entering matrix_addition(matrix_a=%s,matrix_b=%s)", matrix_a, matrix_b)
    logger.debug("<<< Exiting matrix_addition(matrix_a=%s,matrix_b=%s)", matrix_a, matrix_b)
    return [
        [matrix_a[row][col] + matrix_b[row][col] for col in range(len(matrix_a[row]))]
        for row in range(len(matrix_a))
    ]


def matrix_subtraction(matrix_a: list, matrix_b: list):
    logger.debug(">>> Entering matrix_subtraction(matrix_a=%s,matrix_b=%s)", matrix_a, matrix_b)
    logger.debug("<<< Exiting matrix_subtraction(matrix_a=%s,matrix_b=%s)", matrix_a, matrix_b)
    return [
        [matrix_a[row][col] - matrix_b[row][col] for col in range(len(matrix_a[row]))]
        for row in range(len(matrix_a))
    ]


def split_matrix(a: list) -> tuple[list, list, list, list]:
    """
    Given an even length matrix, returns the top_left, top_right, bot_left, bot_right
    quadrant.

    >>> split_matrix([[4,3,2,4],[2,3,1,1],[6,5,4,3],[8,4,1,6]])
    ([[4, 3], [2, 3]], [[2, 4], [1, 1]], [[6, 5], [8, 4]], [[4, 3], [1, 6]])
    >>> split_matrix([
    ...     [4,3,2,4,4,3,2,4],[2,3,1,1,2,3,1,1],[6,5,4,3,6,5,4,3],[8,4,1,6,8,4,1,6],
    ...     [4,3,2,4,4,3,2,4],[2,3,1,1,2,3,1,1],[6,5,4,3,6,5,4,3],[8,4,1,6,8,4,1,6]
    ... ])  # doctest: +NORMALIZE_WHITESPACE
    ([[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]], [[4, 3, 2, 4],
      [2, 3, 1, 1], [6, 5, 4, 3], [8, 4, 1, 6]], [[4, 3, 2, 4], [2, 3, 1, 1],
      [6, 5, 4, 3], [8, 4, 1, 6]], [[4, 3, 2, 4], [2, 3, 1, 1], [6, 5, 4, 3],
      [8, 4, 1, 6]])
    """
    logger.debug(">>> Entering split_matrix(a=%s)", a)
    if len(a) % 2 != 0 or len(a[0]) % 2 != 0:
        raise Exception("Odd matrices are not supported!")
        logger.debug("split_matrix(a=%s): bot_right → %s", a, bot_right)

    matrix_length = len(a)
    logger.debug("split_matrix(a=%s): matrix_length → %s", a, matrix_length)
    mid = matrix_length // 2
    logger.debug("split_matrix(a=%s): mid → %s", a, mid)

    top_right = [[a[i][j] for j in range(mid, matrix_length)] for i in range(mid)]
    logger.debug("split_matrix(a=%s): top_right → %s", a, top_right)
    bot_right = [
        [a[i][j] for j in range(mid, matrix_length)] for i in range(mid, matrix_length)
    ]

    top_left = [[a[i][j] for j in range(mid)] for i in range(mid)]
    logger.debug("split_matrix(a=%s): top_left → %s", a, top_left)
    bot_left = [[a[i][j] for j in range(mid)] for i in range(mid, matrix_length)]
    logger.debug("split_matrix(a=%s): bot_left → %s", a, bot_left)

    logger.debug("<<< Exiting split_matrix(a=%s)", a)
    return top_left, top_right, bot_left, bot_right


def matrix_dimensions(matrix: list) -> tuple[int, int]:
    logger.debug(">>> Entering matrix_dimensions(matrix=%s)", matrix)
    logger.debug("<<< Exiting matrix_dimensions(matrix=%s)", matrix)
    return len(matrix), len(matrix[0])


def print_matrix(matrix: list) -> None:
    logger.debug(">>> Entering print_matrix(matrix=%s)", matrix)
    print("\n".join(str(line) for line in matrix))
    logger.debug("<<< Exiting print_matrix(matrix=%s)", matrix)


def actual_strassen(matrix_a: list, matrix_b: list) -> list:
    """
    Recursive function to calculate the product of two matrices, using the Strassen
    Algorithm. It only supports square matrices of any size that is a power of 2.
    """
    logger.debug(">>> Entering actual_strassen(matrix_a=%s,matrix_b=%s)", matrix_a, matrix_b)
    if matrix_dimensions(matrix_a) == (2, 2):
        return default_matrix_multiplication(matrix_a, matrix_b)

    a, b, c, d = split_matrix(matrix_a)
    e, f, g, h = split_matrix(matrix_b)

    t1 = actual_strassen(a, matrix_subtraction(f, h))
    t2 = actual_strassen(matrix_addition(a, b), h)
    t3 = actual_strassen(matrix_addition(c, d), e)
    t4 = actual_strassen(d, matrix_subtraction(g, e))
    t5 = actual_strassen(matrix_addition(a, d), matrix_addition(e, h))
    t6 = actual_strassen(matrix_subtraction(b, d), matrix_addition(g, h))
    t7 = actual_strassen(matrix_subtraction(a, c), matrix_addition(e, f))

    top_left = matrix_addition(matrix_subtraction(matrix_addition(t5, t4), t2), t6)
    logger.debug("actual_strassen(matrix_a=%s,matrix_b=%s): top_left → %s", matrix_a, matrix_b, top_left)
    top_right = matrix_addition(t1, t2)
    logger.debug("actual_strassen(matrix_a=%s,matrix_b=%s): top_right → %s", matrix_a, matrix_b, top_right)
    bot_left = matrix_addition(t3, t4)
    logger.debug("actual_strassen(matrix_a=%s,matrix_b=%s): bot_left → %s", matrix_a, matrix_b, bot_left)
    bot_right = matrix_subtraction(matrix_subtraction(matrix_addition(t1, t5), t3), t7)
    logger.debug("actual_strassen(matrix_a=%s,matrix_b=%s): bot_right → %s", matrix_a, matrix_b, bot_right)

    # construct the new matrix from our 4 quadrants
    new_matrix = []
    logger.debug("actual_strassen(matrix_a=%s,matrix_b=%s): new_matrix → %s", matrix_a, matrix_b, new_matrix)
    for i in range(len(top_right)):
        new_matrix.append(top_left[i] + top_right[i])
    for i in range(len(bot_right)):
        new_matrix.append(bot_left[i] + bot_right[i])
    logger.debug("<<< Exiting actual_strassen(matrix_a=%s,matrix_b=%s)", matrix_a, matrix_b)
    return new_matrix


def strassen(matrix1: list, matrix2: list) -> list:
    """
    >>> strassen([[2,1,3],[3,4,6],[1,4,2],[7,6,7]], [[4,2,3,4],[2,1,1,1],[8,6,4,2]])
    [[34, 23, 19, 15], [68, 46, 37, 28], [28, 18, 15, 12], [96, 62, 55, 48]]
    >>> strassen([[3,7,5,6,9],[1,5,3,7,8],[1,4,4,5,7]], [[2,4],[5,2],[1,7],[5,5],[7,8]])
    [[139, 163], [121, 134], [100, 121]]
    """
    logger.debug(">>> Entering strassen(matrix1=%s,matrix2=%s)", matrix1, matrix2)
    logger.debug("strassen(matrix1=%s,matrix2=%s): msg → %s", matrix1, matrix2, msg)
    if matrix_dimensions(matrix1)[1] != matrix_dimensions(matrix2)[0]:
        msg = (
            "Unable to multiply these matrices, please check the dimensions.\n"
            f"Matrix A: {matrix1}\n"
            f"Matrix B: {matrix2}"
        )
        raise Exception(msg)
    dimension1 = matrix_dimensions(matrix1)
    logger.debug("strassen(matrix1=%s,matrix2=%s): dimension1 → %s", matrix1, matrix2, dimension1)
    dimension2 = matrix_dimensions(matrix2)
    logger.debug("strassen(matrix1=%s,matrix2=%s): dimension2 → %s", matrix1, matrix2, dimension2)

    if dimension1[0] == dimension1[1] and dimension2[0] == dimension2[1]:
        return [matrix1, matrix2]

    maximum = max(*dimension1, *dimension2)
    logger.debug("strassen(matrix1=%s,matrix2=%s): maximum → %s", matrix1, matrix2, maximum)
    maxim = int(math.pow(2, math.ceil(math.log2(maximum))))
    logger.debug("strassen(matrix1=%s,matrix2=%s): maxim → %s", matrix1, matrix2, maxim)
    new_matrix1 = matrix1
    logger.debug("strassen(matrix1=%s,matrix2=%s): new_matrix1 → %s", matrix1, matrix2, new_matrix1)
    new_matrix2 = matrix2
    logger.debug("strassen(matrix1=%s,matrix2=%s): new_matrix2 → %s", matrix1, matrix2, new_matrix2)

    # Adding zeros to the matrices to convert them both into square matrices of equal
    # dimensions that are a power of 2
    for i in range(maxim):
        if i < dimension1[0]:
            for _ in range(dimension1[1], maxim):
                new_matrix1[i].append(0)
        else:
            new_matrix1.append([0] * maxim)
        if i < dimension2[0]:
            for _ in range(dimension2[1], maxim):
                new_matrix2[i].append(0)
        else:
            new_matrix2.append([0] * maxim)

    final_matrix = actual_strassen(new_matrix1, new_matrix2)
    logger.debug("strassen(matrix1=%s,matrix2=%s): final_matrix → %s", matrix1, matrix2, final_matrix)

    # Removing the additional zeros
    for i in range(maxim):
        if i < dimension1[0]:
            for _ in range(dimension2[1], maxim):
                final_matrix[i].pop()
        else:
            final_matrix.pop()
    logger.debug("<<< Exiting strassen(matrix1=%s,matrix2=%s)", matrix1, matrix2)
    return final_matrix


if __name__ == "__main__":
    matrix1 = [
        [2, 3, 4, 5],
        [6, 4, 3, 1],
        [2, 3, 6, 7],
        [3, 1, 2, 4],
        [2, 3, 4, 5],
        [6, 4, 3, 1],
        [2, 3, 6, 7],
        [3, 1, 2, 4],
        [2, 3, 4, 5],
        [6, 2, 3, 1],
    ]
    matrix2 = [[0, 2, 1, 1], [16, 2, 3, 3], [2, 2, 7, 7], [13, 11, 22, 4]]
    print(strassen(matrix1, matrix2))
