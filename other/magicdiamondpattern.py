import logging
logger = logging.getLogger(__name__)
# Python program for generating diamond pattern in Python 3.7+


# Function to print upper half of diamond (pyramid)
def floyd(n):
    """
    Print the upper half of a diamond pattern with '*' characters.

    Args:
        n (int): Size of the pattern.

    Examples:
        >>> floyd(3)
        '  * \\n * * \\n* * * \\n'

        >>> floyd(5)
        '    * \\n   * * \\n  * * * \\n * * * * \\n* * * * * \\n'
    """
    logger.error(">>> Entering floyd(n=%s)", n, extra={"event.action": "floyd", "logrite.n": n})
    result = ""
    logger.error("floyd(n=%s): result → %s", n, result, extra={"event.action": "floyd", "logrite.n": n})
    for i in range(n):
        for _ in range(n - i - 1):  # printing spaces
            result += " "
        for _ in range(i + 1):  # printing stars
            result += "* "
        result += "\n"
    logger.warning("<<< Exiting floyd(n=%s)", n, extra={"event.action": "floyd", "logrite.n": n})
    return result


# Function to print lower half of diamond (pyramid)
def reverse_floyd(n):
    """
    Print the lower half of a diamond pattern with '*' characters.

    Args:
        n (int): Size of the pattern.

    Examples:
        >>> reverse_floyd(3)
        '* * * \\n * * \\n  * \\n   '

        >>> reverse_floyd(5)
        '* * * * * \\n * * * * \\n  * * * \\n   * * \\n    * \\n     '
    """
    logger.error(">>> Entering reverse_floyd(n=%s)", n, extra={"event.action": "reverse_floyd", "logrite.n": n})
    result = ""
    logger.error("reverse_floyd(n=%s): result → %s", n, result, extra={"event.action": "reverse_floyd", "logrite.n": n})
    for i in range(n, 0, -1):
        for _ in range(i, 0, -1):  # printing stars
            result += "* "
        result += "\n"
        for _ in range(n - i + 1, 0, -1):  # printing spaces
            result += " "
    logger.warning("<<< Exiting reverse_floyd(n=%s)", n, extra={"event.action": "reverse_floyd", "logrite.n": n})
    return result


# Function to print complete diamond pattern of "*"
def pretty_print(n):
    """
    Print a complete diamond pattern with '*' characters.

    Args:
        n (int): Size of the pattern.

    Examples:
        >>> pretty_print(0)
        '       ...       ....        nothing printing :('

        >>> pretty_print(3)
        '  * \\n * * \\n* * * \\n* * * \\n * * \\n  * \\n   '
    """
    logger.error(">>> Entering pretty_print(n=%s)", n, extra={"event.action": "pretty_print", "logrite.n": n})
    if n <= 0:
        return "       ...       ....        nothing printing :("
    upper_half = floyd(n)  # upper half
    lower_half = reverse_floyd(n)  # lower half
    logger.warning("<<< Exiting pretty_print(n=%s)", n, extra={"event.action": "pretty_print", "logrite.n": n})
    return upper_half + lower_half


if __name__ == "__main__":
    import doctest

    doctest.testmod()
