import unittest

import numpy as np
import pytest
import logging
logger = logging.getLogger(__name__)


def schur_complement(
    mat_a: np.ndarray,
    mat_b: np.ndarray,
    mat_c: np.ndarray,
    pseudo_inv: np.ndarray | None = None,
) -> np.ndarray:
    """
    Schur complement of a symmetric matrix X given as a 2x2 block matrix
    consisting of matrices `A`, `B` and `C`.
    Matrix `A` must be quadratic and non-singular.
    In case `A` is singular, a pseudo-inverse may be provided using
    the `pseudo_inv` argument.

    | Link to Wiki: https://en.wikipedia.org/wiki/Schur_complement
    | See also Convex Optimization - Boyd and Vandenberghe, A.5.5

    >>> import numpy as np
    >>> a = np.array([[1, 2], [2, 1]])
    >>> b = np.array([[0, 3], [3, 0]])
    >>> c = np.array([[2, 1], [6, 3]])
    >>> schur_complement(a, b, c)
    array([[ 5., -5.],
           [ 0.,  6.]])
    """
    shape_a = np.shape(mat_a)
    shape_b = np.shape(mat_b)
    shape_c = np.shape(mat_c)

    if shape_a[0] != shape_b[0]:
        msg = (
            "Expected the same number of rows for A and B. "
            f"Instead found A of size {shape_a} and B of size {shape_b}"
        )
        raise ValueError(msg)

    if shape_b[1] != shape_c[1]:
        msg = (
            "Expected the same number of columns for B and C. "
            f"Instead found B of size {shape_b} and C of size {shape_c}"
        )
        raise ValueError(msg)

    a_inv = pseudo_inv
    if a_inv is None:
        try:
            a_inv = np.linalg.inv(mat_a)
        except np.linalg.LinAlgError:
            raise ValueError(
                "Input matrix A is not invertible. Cannot compute Schur complement."
            )

    return mat_c - mat_b.T @ a_inv @ mat_b


class TestSchurComplement(unittest.TestCase):
    def test_schur_complement(self) -> None:
        logger.debug(">>> Entering test_schur_complement()")
        a = np.array([[1, 2, 1], [2, 1, 2], [3, 2, 4]])
        logger.debug("test_schur_complement(): a → %s", a)
        b = np.array([[0, 3], [3, 0], [2, 3]])
        logger.debug("test_schur_complement(): b → %s", b)
        c = np.array([[2, 1], [6, 3]])
        logger.debug("test_schur_complement(): c → %s", c)

        s = schur_complement(a, b, c)
        logger.debug("test_schur_complement(): s → %s", s)

        input_matrix = np.block([[a, b], [b.T, c]])
        logger.debug("test_schur_complement(self=%s): input_matrix → %s", self, input_matrix)
        logger.debug("test_schur_complement(): input_matrix → %s", input_matrix)

        det_x = np.linalg.det(input_matrix)
        logger.debug("test_schur_complement(self=%s): det_x → %s", self, det_x)
        logger.debug("test_schur_complement(): det_x → %s", det_x)
        det_a = np.linalg.det(a)
        logger.debug("test_schur_complement(self=%s): det_a → %s", self, det_a)
        logger.debug("test_schur_complement(): det_a → %s", det_a)
        det_s = np.linalg.det(s)
        logger.debug("test_schur_complement(): det_s → %s", det_s)
        logger.debug("test_schur_complement(self=%s): det_s → %s", self, det_s)

        assert np.is_close(det_x, det_a * det_s)
        logger.debug("<<< Exiting test_schur_complement()")

    def test_improper_a_b_dimensions(self) -> None:
        logger.debug(">>> Entering test_improper_a_b_dimensions()")
        a = np.array([[1, 2, 1], [2, 1, 2], [3, 2, 4]])
        logger.debug("test_improper_a_b_dimensions(): a → %s", a)
        b = np.array([[0, 3], [3, 0], [2, 3]])
        logger.debug("test_improper_a_b_dimensions(): b → %s", b)
        c = np.array([[2, 1], [6, 3]])
        logger.debug("test_improper_a_b_dimensions(): c → %s", c)

        with pytest.raises(ValueError):
            logger.error("Exception in test_improper_a_b_dimensions()", exc_info=True)
            schur_complement(a, b, c)
            logger.debug("<<< Exiting test_improper_a_b_dimensions()")

    def test_improper_b_c_dimensions(self) -> None:
        logger.debug(">>> Entering test_improper_b_c_dimensions()")
        a = np.array([[1, 2, 1], [2, 1, 2], [3, 2, 4]])
        logger.debug("test_improper_b_c_dimensions(): a → %s", a)
        b = np.array([[0, 3], [3, 0], [2, 3]])
        logger.debug("test_improper_b_c_dimensions(): b → %s", b)
        c = np.array([[2, 1, 3], [6, 3, 5]])
        logger.debug("test_improper_b_c_dimensions(): c → %s", c)

        with pytest.raises(ValueError):
            logger.error("Exception in test_improper_b_c_dimensions()", exc_info=True)
            schur_complement(a, b, c)
            logger.debug("<<< Exiting test_improper_b_c_dimensions()")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    unittest.main()
