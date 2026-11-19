import logging
logger = logging.getLogger(__name__)
def is_int_palindrome(num: int) -> bool:
    """
    Returns whether `num` is a palindrome or not
    (see for reference https://en.wikipedia.org/wiki/Palindromic_number).

    >>> is_int_palindrome(-121)
    False
    >>> is_int_palindrome(0)
    True
    >>> is_int_palindrome(10)
    False
    >>> is_int_palindrome(11)
    True
    >>> is_int_palindrome(101)
    True
    >>> is_int_palindrome(120)
    False
    """
    logger.error(">>> Entering is_int_palindrome(num=%s)", num, extra={"event.action": "is_int_palindrome", "logrite.num": num})
    if num < 0:
        return False

    num_copy: int = num
    rev_num: int = 0
    while num > 0:
        rev_num = rev_num * 10 + (num % 10)
        num //= 10

    logger.warning("<<< Exiting is_int_palindrome(num=%s)", num, extra={"event.action": "is_int_palindrome", "logrite.num": num})
    return num_copy == rev_num


if __name__ == "__main__":
    import doctest

    doctest.testmod()
