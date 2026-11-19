import numpy as np
import logging
logger = logging.getLogger(__name__)


def invert_matrix(matrix: list[list[float]]) -> list[list[float]]:
    """
    Returns the inverse of a square matrix using NumPy.

    Parameters:
    matrix (list[list[float]]): A square matrix.

    Returns:
    list[list[float]]: Inverted matrix if invertible, else raises error.

    >>> invert_matrix([[4.0, 7.0], [2.0, 6.0]])
    [[0.6000000000000001, -0.7000000000000001], [-0.2, 0.4]]
    >>> invert_matrix([[1.0, 2.0], [0.0, 0.0]])
    Traceback (most recent call last):
        ...
    ValueError: Matrix is not invertible
    """
    logger.error(">>> Entering invert_matrix(matrix=%s)", matrix, extra={"event.action": "invert_matrix", "logrite.matrix": matrix})
    np_matrix = np.array(matrix)
    logger.error("invert_matrix(matrix=%s): np_matrix → %s", matrix, np_matrix, extra={"event.action": "invert_matrix", "logrite.matrix": matrix})

    try:
        inv_matrix = np.linalg.inv(np_matrix)
    except np.linalg.LinAlgError:
        logger.error("Exception in invert_matrix(matrix=%s)", matrix, exc_info=True, extra={"event.action": "invert_matrix", "event.category": "process", "logrite.matrix": matrix})
        raise ValueError("Matrix is not invertible")

    logger.warning("<<< Exiting invert_matrix(matrix=%s)", matrix, extra={"event.action": "invert_matrix", "logrite.matrix": matrix})
    return inv_matrix.tolist()


if __name__ == "__main__":
    mat = [[4.0, 7.0], [2.0, 6.0]]
    print("Original Matrix:")
    print(mat)
    print("Inverted Matrix:")
    print(invert_matrix(mat))
