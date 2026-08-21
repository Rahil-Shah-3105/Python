from sys import maxsize
import logging
logger = logging.getLogger(__name__)


def array_equalization(vector: list[int], step_size: int) -> int:
    """
    This algorithm equalizes all elements of the input vector
    to a common value, by making the minimal number of
    "updates" under the constraint of a step size (step_size).

    >>> array_equalization([1, 1, 6, 2, 4, 6, 5, 1, 7, 2, 2, 1, 7, 2, 2], 4)
    4
    >>> array_equalization([22, 81, 88, 71, 22, 81, 632, 81, 81, 22, 92], 2)
    5
    >>> array_equalization([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 5)
    0
    >>> array_equalization([22, 22, 22, 33, 33, 33], 2)
    2
    >>> array_equalization([1, 2, 3], 0)
    Traceback (most recent call last):
    ValueError: Step size must be positive and non-zero.
    >>> array_equalization([1, 2, 3], -1)
    Traceback (most recent call last):
    ValueError: Step size must be positive and non-zero.
    >>> array_equalization([1, 2, 3], 0.5)
    Traceback (most recent call last):
    ValueError: Step size must be an integer.
    >>> array_equalization([1, 2, 3], maxsize)
    1
    """
    logger.debug(">>> Entering array_equalization(vector=%s,step_size=%s)", vector, step_size)
    if step_size <= 0:
        raise ValueError("Step size must be positive and non-zero.")
    if not isinstance(step_size, int):
        raise ValueError("Step size must be an integer.")

    unique_elements = set(vector)
    logger.debug("array_equalization(vector=%s,step_size=%s): unique_elements → %s", vector, step_size, unique_elements)
    min_updates = maxsize
    logger.debug("array_equalization(vector=%s,step_size=%s): min_updates → %s", vector, step_size, min_updates)

    for element in unique_elements:
        elem_index = 0
        logger.debug("array_equalization(vector=%s,step_size=%s): elem_index → %s", vector, step_size, elem_index)
        updates = 0
        logger.debug("array_equalization(vector=%s,step_size=%s): updates → %s", vector, step_size, updates)
        while elem_index < len(vector):
            if vector[elem_index] != element:
                updates += 1
                elem_index += step_size
            else:
                elem_index += 1
        min_updates = min(min_updates, updates)

    logger.debug("<<< Exiting array_equalization(vector=%s,step_size=%s)", vector, step_size)
    return min_updates


if __name__ == "__main__":
    from doctest import testmod

    testmod()
