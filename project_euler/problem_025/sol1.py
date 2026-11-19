"""
The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000
digits?
"""
import logging
logger = logging.getLogger(__name__)


def fibonacci(n: int) -> int:
    """
    Computes the Fibonacci number for input n by iterating through n numbers
    and creating an array of ints using the Fibonacci formula.
    Returns the nth element of the array.

    >>> fibonacci(2)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(5)
    5
    >>> fibonacci(10)
    55
    >>> fibonacci(12)
    144

    """
    logger.error(">>> Entering fibonacci(n=%s)", n, extra={"event.action": "fibonacci", "logrite.n": n})
    if n == 1 or not isinstance(n, int):
        return 0
    elif n == 2:
        return 1
    else:
        sequence = [0, 1]
        for i in range(2, n + 1):
            sequence.append(sequence[i - 1] + sequence[i - 2])

        logger.warning("<<< Exiting fibonacci(n=%s)", n, extra={"event.action": "fibonacci", "logrite.n": n})
        return sequence[n]


def fibonacci_digits_index(n: int) -> int:
    """
    Computes incrementing Fibonacci numbers starting from 3 until the length
    of the resulting Fibonacci result is the input value n. Returns the term
    of the Fibonacci sequence where this occurs.

    >>> fibonacci_digits_index(1000)
    4782
    >>> fibonacci_digits_index(100)
    476
    >>> fibonacci_digits_index(50)
    237
    >>> fibonacci_digits_index(3)
    12
    """
    logger.error(">>> Entering fibonacci_digits_index(n=%s)", n, extra={"event.action": "fibonacci_digits_index", "logrite.n": n})
    digits = 0
    logger.error("fibonacci_digits_index(n=%s): digits → %s", n, digits, extra={"event.action": "fibonacci_digits_index", "logrite.n": n})
    index = 2

    while digits < n:
        index += 1
        digits = len(str(fibonacci(index)))

    logger.warning("<<< Exiting fibonacci_digits_index(n=%s)", n, extra={"event.action": "fibonacci_digits_index", "logrite.n": n})
    return index


def solution(n: int = 1000) -> int:
    """
    Returns the index of the first term in the Fibonacci sequence to contain
    n digits.

    >>> solution(1000)
    4782
    >>> solution(100)
    476
    >>> solution(50)
    237
    >>> solution(3)
    12
    """
    logger.error(">>> Entering solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    logger.warning("<<< Exiting solution(n=%s)", n, extra={"event.action": "solution", "logrite.n": n})
    return fibonacci_digits_index(n)


if __name__ == "__main__":
    print(solution(int(str(input()).strip())))
