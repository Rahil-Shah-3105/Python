import math
import sys
import logging
logger = logging.getLogger(__name__)


def minimum_squares_to_represent_a_number(number: int) -> int:
    """
    Count the number of minimum squares to represent a number

    >>> minimum_squares_to_represent_a_number(25)
    1
    >>> minimum_squares_to_represent_a_number(37)
    2
    >>> minimum_squares_to_represent_a_number(21)
    3
    >>> minimum_squares_to_represent_a_number(58)
    2
    >>> minimum_squares_to_represent_a_number(-1)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must not be a negative number
    >>> minimum_squares_to_represent_a_number(0)
    1
    >>> minimum_squares_to_represent_a_number(12.34)
    Traceback (most recent call last):
        ...
    ValueError: the value of input must be a natural number
    """
    logger.debug(">>> Entering minimum_squares_to_represent_a_number(number=%s)", number)
    if number != int(number):
        raise ValueError("the value of input must be a natural number")
    if number < 0:
        raise ValueError("the value of input must not be a negative number")
    if number == 0:
        return 1
    answers = [-1] * (number + 1)
    logger.debug("minimum_squares_to_represent_a_number(number=%s): answers → %s", number, answers)
    answers[0] = 0
    for i in range(1, number + 1):
        answer = sys.maxsize
        logger.debug("minimum_squares_to_represent_a_number(number=%s): answer → %s", number, answer)
        logger.warning("minimum_squares_to_represent_a_number(number=%s): root → %s", number, root)
        root = int(math.sqrt(i))
        for j in range(1, root + 1):
            current_answer = 1 + answers[i - (j**2)]
            logger.debug("minimum_squares_to_represent_a_number(number=%s): current_answer → %s", number, current_answer)
            answer = min(answer, current_answer)
        answers[i] = answer
    logger.debug("<<< Exiting minimum_squares_to_represent_a_number(number=%s)", number)
    return answers[number]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
