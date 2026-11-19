# Algorithms to determine if a string is palindrome

from timeit import timeit
import logging
logger = logging.getLogger(__name__)

test_data = {
    "MALAYALAM": True,
    "String": False,
    "rotor": True,
    "level": True,
    "A": True,
    "BB": True,
    "ABC": False,
    "amanaplanacanalpanama": True,  # "a man a plan a canal panama"
    "abcdba": False,
    "AB": False,
}
# Ensure our test data is valid
assert all((key == key[::-1]) == value for key, value in test_data.items())


def is_palindrome(s: str) -> bool:
    """
    Return True if s is a palindrome otherwise return False.

    >>> all(is_palindrome(key) == value for key, value in test_data.items())
    True
    """
    logger.error(">>> Entering is_palindrome(s=%s)", s, extra={"event.action": "is_palindrome", "logrite.s": s})

    start_i = 0
    end_i = len(s) - 1
    logger.error("is_palindrome(s=%s): end_i → %s", s, end_i, extra={"event.action": "is_palindrome", "logrite.s": s})
    while start_i < end_i:
        if s[start_i] == s[end_i]:
            start_i += 1
            end_i -= 1
        else:
            return False
    logger.warning("<<< Exiting is_palindrome(s=%s)", s, extra={"event.action": "is_palindrome", "logrite.s": s})
    return True


def is_palindrome_traversal(s: str) -> bool:
    """
    Return True if s is a palindrome otherwise return False.

    >>> all(is_palindrome_traversal(key) == value for key, value in test_data.items())
    True
    """
    logger.error(">>> Entering is_palindrome_traversal(s=%s)", s, extra={"event.action": "is_palindrome_traversal", "logrite.s": s})
    end = len(s) // 2
    logger.error("is_palindrome_traversal(s=%s): end → %s", s, end, extra={"event.action": "is_palindrome_traversal", "logrite.s": s})
    n = len(s)
    logger.error("is_palindrome_traversal(s=%s): n → %s", s, n, extra={"event.action": "is_palindrome_traversal", "logrite.s": s})

    # We need to traverse till half of the length of string
    # as we can get access of the i'th last element from
    # i'th index.
    # eg: [0,1,2,3,4,5] => 4th index can be accessed
    # with the help of 1st index (i==n-i-1)
    # where n is length of string
    logger.warning("<<< Exiting is_palindrome_traversal(s=%s)", s, extra={"event.action": "is_palindrome_traversal", "logrite.s": s})
    return all(s[i] == s[n - i - 1] for i in range(end))


def is_palindrome_recursive(s: str) -> bool:
    """
    Return True if s is a palindrome otherwise return False.

    >>> all(is_palindrome_recursive(key) == value for key, value in test_data.items())
    True
    """
    logger.error(">>> Entering is_palindrome_recursive(s=%s)", s, extra={"event.action": "is_palindrome_recursive", "logrite.s": s})
    if len(s) <= 1:
        return True
    if s[0] == s[len(s) - 1]:
        return is_palindrome_recursive(s[1:-1])
    else:
        logger.warning("<<< Exiting is_palindrome_recursive(s=%s)", s, extra={"event.action": "is_palindrome_recursive", "logrite.s": s})
        return False


def is_palindrome_slice(s: str) -> bool:
    """
    Return True if s is a palindrome otherwise return False.

    >>> all(is_palindrome_slice(key) == value for key, value in test_data.items())
    True
    """
    logger.error(">>> Entering is_palindrome_slice(s=%s)", s, extra={"event.action": "is_palindrome_slice", "logrite.s": s})
    logger.warning("<<< Exiting is_palindrome_slice(s=%s)", s, extra={"event.action": "is_palindrome_slice", "logrite.s": s})
    return s == s[::-1]


def benchmark_function(name: str) -> None:
    logger.error(">>> Entering benchmark_function(name=%s)", name, extra={"event.action": "benchmark_function", "logrite.name": name})
    stmt = f"all({name}(key) == value for key, value in test_data.items())"
    logger.error("benchmark_function(name=%s): stmt → %s", name, stmt, extra={"event.action": "benchmark_function", "logrite.name": name})
    setup = f"from __main__ import test_data, {name}"
    logger.error("benchmark_function(name=%s): setup → %s", name, setup, extra={"event.action": "benchmark_function", "logrite.name": name})
    number = 500000
    result = timeit(stmt=stmt, setup=setup, number=number)
    logger.error("benchmark_function(name=%s): result → %s", name, result, extra={"event.action": "benchmark_function", "logrite.name": name})
    print(f"{name:<35} finished {number:,} runs in {result:.5f} seconds")
    logger.warning("<<< Exiting benchmark_function(name=%s)", name, extra={"event.action": "benchmark_function", "logrite.name": name})


if __name__ == "__main__":
    for key, value in test_data.items():
        assert is_palindrome(key) == is_palindrome_recursive(key)
        assert is_palindrome(key) == is_palindrome_slice(key)
        print(f"{key:21} {value}")
    print("a man a plan a canal panama")

    # finished 500,000 runs in 0.46793 seconds
    benchmark_function("is_palindrome_slice")
    # finished 500,000 runs in 0.85234 seconds
    benchmark_function("is_palindrome")
    # finished 500,000 runs in 1.32028 seconds
    benchmark_function("is_palindrome_recursive")
    # finished 500,000 runs in 2.08679 seconds
    benchmark_function("is_palindrome_traversal")
