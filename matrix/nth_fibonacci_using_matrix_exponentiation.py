import logging
logger = logging.getLogger(__name__)
"""
Implementation of finding nth fibonacci number using matrix exponentiation.
Time Complexity is about O(log(n)*8), where 8 is the complexity of matrix
multiplication of size 2 by 2.
And on the other hand complexity of bruteforce solution is O(n).
As we know
    f[n] = f[n-1] + f[n-1]
Converting to matrix,
    [f(n),f(n-1)] = [[1,1],[1,0]] * [f(n-1),f(n-2)]
->  [f(n),f(n-1)] = [[1,1],[1,0]]^2 * [f(n-2),f(n-3)]
    ...
    ...
->  [f(n),f(n-1)] = [[1,1],[1,0]]^(n-1) * [f(1),f(0)]
So we just need the n times multiplication of the matrix [1,1],[1,0]].
We can decrease the n times multiplication by following the divide and conquer approach.
"""


def multiply(matrix_a: list[list[int]], matrix_b: list[list[int]]) -> list[list[int]]:
    logger.debug(">>> Entering multiply(matrix_a=%s,matrix_b=%s)", matrix_a, matrix_b)
    matrix_c = []
    logger.debug("multiply(matrix_a=%s,matrix_b=%s): matrix_c → %s", matrix_a, matrix_b, matrix_c)
    n = len(matrix_a)
    logger.debug("multiply(matrix_a=%s,matrix_b=%s): n → %s", matrix_a, matrix_b, n)
    for i in range(n):
        list_1 = []
        logger.debug("multiply(matrix_a=%s,matrix_b=%s): list_1 → %s", matrix_a, matrix_b, list_1)
        for j in range(n):
            val = 0
            logger.debug("multiply(matrix_a=%s,matrix_b=%s): val → %s", matrix_a, matrix_b, val)
            for k in range(n):
                val = val + matrix_a[i][k] * matrix_b[k][j]
            list_1.append(val)
        matrix_c.append(list_1)
    logger.debug("<<< Exiting multiply(matrix_a=%s,matrix_b=%s)", matrix_a, matrix_b)
    return matrix_c


def identity(n: int) -> list[list[int]]:
    logger.debug(">>> Entering identity(n=%s)", n)
    logger.debug("<<< Exiting identity(n=%s)", n)
    return [[int(row == column) for column in range(n)] for row in range(n)]


def nth_fibonacci_matrix(n: int) -> int:
    """
    >>> nth_fibonacci_matrix(100)
    354224848179261915075
    >>> nth_fibonacci_matrix(-100)
    -100
    """
    logger.debug(">>> Entering nth_fibonacci_matrix(n=%s)", n)
    if n <= 1:
        return n
    res_matrix = identity(2)
    logger.debug("nth_fibonacci_matrix(n=%s): res_matrix → %s", n, res_matrix)
    fibonacci_matrix = [[1, 1], [1, 0]]
    logger.debug("nth_fibonacci_matrix(n=%s): fibonacci_matrix → %s", n, fibonacci_matrix)
    n = n - 1
    while n > 0:
        if n % 2 == 1:
            res_matrix = multiply(res_matrix, fibonacci_matrix)
        fibonacci_matrix = multiply(fibonacci_matrix, fibonacci_matrix)
        n = int(n / 2)
    logger.debug("<<< Exiting nth_fibonacci_matrix(n=%s)", n)
    return res_matrix[0][0]


def nth_fibonacci_bruteforce(n: int) -> int:
    """
    >>> nth_fibonacci_bruteforce(100)
    354224848179261915075
    >>> nth_fibonacci_bruteforce(-100)
    -100
    """
    logger.debug(">>> Entering nth_fibonacci_bruteforce(n=%s)", n)
    if n <= 1:
        return n
    fib0 = 0
    logger.debug("nth_fibonacci_bruteforce(n=%s): fib0 → %s", n, fib0)
    fib1 = 1
    logger.debug("nth_fibonacci_bruteforce(n=%s): fib1 → %s", n, fib1)
    for _ in range(2, n + 1):
        fib0, fib1 = fib1, fib0 + fib1
    logger.debug("<<< Exiting nth_fibonacci_bruteforce(n=%s)", n)
    return fib1


def main() -> None:
    logger.debug(">>> Entering main()")
    for ordinal in "0th 1st 2nd 3rd 10th 100th 1000th".split():
        n = int("".join(c for c in ordinal if c in "0123456789"))  # 1000th --> 1000
        logger.debug("main(): n → %s", n)
        print(
            f"{ordinal} fibonacci number using matrix exponentiation is "
            f"{nth_fibonacci_matrix(n)} and using bruteforce is "
            f"{nth_fibonacci_bruteforce(n)}\n"
        )
    # from timeit import timeit
    # print(timeit("nth_fibonacci_matrix(1000000)",
    #              "from main import nth_fibonacci_matrix", number=5))
    # print(timeit("nth_fibonacci_bruteforce(1000000)",
    #              "from main import nth_fibonacci_bruteforce", number=5))
    # 2.3342058970001744
    logger.debug("<<< Exiting main()")
    # 57.256506615000035


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
