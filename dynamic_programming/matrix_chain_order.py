import sys
import logging
logger = logging.getLogger(__name__)

"""
Dynamic Programming
Implementation of Matrix Chain Multiplication
Time Complexity: O(n^3)
Space Complexity: O(n^2)

Reference: https://en.wikipedia.org/wiki/Matrix_chain_multiplication
"""


def matrix_chain_order(array: list[int]) -> tuple[list[list[int]], list[list[int]]]:
    """
    >>> matrix_chain_order([10, 30, 5])
    ([[0, 0, 0], [0, 0, 1500], [0, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 0, 0]])
    """
    logger.debug(">>> Entering matrix_chain_order(array=%s)", array)
    n = len(array)
    logger.debug("matrix_chain_order(array=%s): n → %s", array, n)
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    logger.debug("matrix_chain_order(array=%s): matrix → %s", array, matrix)
    sol = [[0 for _ in range(n)] for _ in range(n)]
    logger.debug("matrix_chain_order(array=%s): sol → %s", array, sol)

    for chain_length in range(2, n):
        for a in range(1, n - chain_length + 1):
            b = a + chain_length - 1

            matrix[a][b] = sys.maxsize
            for c in range(a, b):
                cost = (
                    matrix[a][c] + matrix[c + 1][b] + array[a - 1] * array[c] * array[b]
                )
                if cost < matrix[a][b]:
                    matrix[a][b] = cost
                    sol[a][b] = c
    logger.debug("<<< Exiting matrix_chain_order(array=%s)", array)
    return matrix, sol


def print_optimal_solution(optimal_solution: list[list[int]], i: int, j: int):
    """
    Print order of matrix with Ai as Matrix.
    """
    logger.debug(">>> Entering print_optimal_solution(optimal_solution=%s,i=%s,j=%s)", optimal_solution, i, j)

    if i == j:
        print("A" + str(i), end=" ")
    else:
        print("(", end=" ")
        print_optimal_solution(optimal_solution, i, optimal_solution[i][j])
        print_optimal_solution(optimal_solution, optimal_solution[i][j] + 1, j)
        print(")", end=" ")
        logger.debug("<<< Exiting print_optimal_solution(optimal_solution=%s,i=%s,j=%s)", optimal_solution, i, j)


def main():
    """
    Size of matrix created from array [30, 35, 15, 5, 10, 20, 25] will be:
    30*35 35*15 15*5 5*10 10*20 20*25
    """
    logger.debug(">>> Entering main()")

    array = [30, 35, 15, 5, 10, 20, 25]
    logger.debug("main(): array → %s", array)
    n = len(array)
    logger.debug("main(): n → %s", n)

    matrix, optimal_solution = matrix_chain_order(array)

    print("No. of Operation required: " + str(matrix[1][n - 1]))
    print_optimal_solution(optimal_solution, 1, n - 1)
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    main()
