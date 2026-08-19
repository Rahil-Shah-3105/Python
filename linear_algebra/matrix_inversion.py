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
    logger.debug(">>> Entering invert_matrix(matrix=%s)", matrix)
    np_matrix = np.array(matrix)
    logger.debug("invert_matrix(matrix=%s): np_matrix → %s", matrix, np_matrix)

    try:
        inv_matrix = np.linalg.inv(np_matrix)
        logger.debug("invert_matrix(matrix=%s): inv_matrix → %s", matrix, inv_matrix)
    except np.linalg.LinAlgError:
        logger.error("Exception in invert_matrix(matrix=%s)", matrix, exc_info=True)
        raise ValueError("Matrix is not invertible")

    logger.debug("<<< Exiting invert_matrix(matrix=%s)", matrix)
    return inv_matrix.tolist()


if __name__ == "__main__":
    mat = [[4.0, 7.0], [2.0, 6.0]]
    print("Original Matrix:")
    print(mat)
    print("Inverted Matrix:")
    print(invert_matrix(mat))
