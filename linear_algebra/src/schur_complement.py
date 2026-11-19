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
    logger.error(">>> Entering schur_complement(mat_a=%s,mat_b=%s,mat_c=%s,pseudo_inv=%s)", mat_a, mat_b, mat_c, pseudo_inv, extra={"event.action": "schur_complement", "logrite.mat_a": mat_a, "logrite.mat_b": mat_b, "logrite.mat_c": mat_c, "logrite.pseudo_inv": pseudo_inv})
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
    logger.error("schur_complement(mat_a=%s,mat_b=%s,mat_c=%s,pseudo_inv=%s): shape_a → %s", mat_a, mat_b, mat_c, pseudo_inv, shape_a, extra={"event.action": "schur_complement", "logrite.mat_a": mat_a, "logrite.mat_b": mat_b, "logrite.mat_c": mat_c, "logrite.pseudo_inv": pseudo_inv})
    shape_b = np.shape(mat_b)
    logger.error("schur_complement(mat_a=%s,mat_b=%s,mat_c=%s,pseudo_inv=%s): shape_b → %s", mat_a, mat_b, mat_c, pseudo_inv, shape_b, extra={"event.action": "schur_complement", "logrite.mat_a": mat_a, "logrite.mat_b": mat_b, "logrite.mat_c": mat_c, "logrite.pseudo_inv": pseudo_inv})
    shape_c = np.shape(mat_c)
    logger.error("schur_complement(mat_a=%s,mat_b=%s,mat_c=%s,pseudo_inv=%s): shape_c → %s", mat_a, mat_b, mat_c, pseudo_inv, shape_c, extra={"event.action": "schur_complement", "logrite.mat_a": mat_a, "logrite.mat_b": mat_b, "logrite.mat_c": mat_c, "logrite.pseudo_inv": pseudo_inv})

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
    logger.error("schur_complement(mat_a=%s,mat_b=%s,mat_c=%s,pseudo_inv=%s): a_inv → %s", mat_a, mat_b, mat_c, pseudo_inv, a_inv, extra={"event.action": "schur_complement", "logrite.mat_a": mat_a, "logrite.mat_b": mat_b, "logrite.mat_c": mat_c, "logrite.pseudo_inv": pseudo_inv})
    if a_inv is None:
        try:
            a_inv = np.linalg.inv(mat_a)
        except np.linalg.LinAlgError:
            logger.error("Exception in schur_complement(mat_a=%s,mat_b=%s,mat_c=%s,pseudo_inv=%s)", mat_a, mat_b, mat_c, pseudo_inv, exc_info=True, extra={"event.action": "schur_complement", "event.category": "process", "logrite.mat_a": mat_a, "logrite.mat_b": mat_b, "logrite.mat_c": mat_c, "logrite.pseudo_inv": pseudo_inv})
            raise ValueError(
                "Input matrix A is not invertible. Cannot compute Schur complement."
            )

    logger.warning("<<< Exiting schur_complement(mat_a=%s,mat_b=%s,mat_c=%s,pseudo_inv=%s)", mat_a, mat_b, mat_c, pseudo_inv, extra={"event.action": "schur_complement", "logrite.mat_a": mat_a, "logrite.mat_b": mat_b, "logrite.mat_c": mat_c, "logrite.pseudo_inv": pseudo_inv})
    return mat_c - mat_b.T @ a_inv @ mat_b


class TestSchurComplement(unittest.TestCase):
    def test_schur_complement(self) -> None:
        logger.error(">>> Entering test_schur_complement()", extra={"event.action": "test_schur_complement"})
        a = np.array([[1, 2, 1], [2, 1, 2], [3, 2, 4]])
        logger.error("test_schur_complement(): a → %s", a, extra={"event.action": "test_schur_complement"})
        b = np.array([[0, 3], [3, 0], [2, 3]])
        logger.error("test_schur_complement(): b → %s", b, extra={"event.action": "test_schur_complement"})
        c = np.array([[2, 1], [6, 3]])
        logger.error("test_schur_complement(): c → %s", c, extra={"event.action": "test_schur_complement"})

        s = schur_complement(a, b, c)
        logger.error("test_schur_complement(): s → %s", s, extra={"event.action": "test_schur_complement"})

        input_matrix = np.block([[a, b], [b.T, c]])
        logger.error("test_schur_complement(): input_matrix → %s", input_matrix, extra={"event.action": "test_schur_complement"})

        det_x = np.linalg.det(input_matrix)
        logger.error("test_schur_complement(): det_x → %s", det_x, extra={"event.action": "test_schur_complement"})
        det_a = np.linalg.det(a)
        logger.error("test_schur_complement(): det_a → %s", det_a, extra={"event.action": "test_schur_complement"})
        det_s = np.linalg.det(s)
        logger.error("test_schur_complement(): det_s → %s", det_s, extra={"event.action": "test_schur_complement"})

        assert np.is_close(det_x, det_a * det_s)
        logger.warning("<<< Exiting test_schur_complement()", extra={"event.action": "test_schur_complement"})

    def test_improper_a_b_dimensions(self) -> None:
        logger.error(">>> Entering test_improper_a_b_dimensions()", extra={"event.action": "test_improper_a_b_dimensions"})
        a = np.array([[1, 2, 1], [2, 1, 2], [3, 2, 4]])
        logger.error("test_improper_a_b_dimensions(): a → %s", a, extra={"event.action": "test_improper_a_b_dimensions"})
        b = np.array([[0, 3], [3, 0], [2, 3]])
        logger.error("test_improper_a_b_dimensions(): b → %s", b, extra={"event.action": "test_improper_a_b_dimensions"})
        c = np.array([[2, 1], [6, 3]])
        logger.error("test_improper_a_b_dimensions(): c → %s", c, extra={"event.action": "test_improper_a_b_dimensions"})

        with pytest.raises(ValueError):
            schur_complement(a, b, c)
            logger.warning("<<< Exiting test_improper_a_b_dimensions()", extra={"event.action": "test_improper_a_b_dimensions"})

    def test_improper_b_c_dimensions(self) -> None:
        logger.error(">>> Entering test_improper_b_c_dimensions()", extra={"event.action": "test_improper_b_c_dimensions"})
        a = np.array([[1, 2, 1], [2, 1, 2], [3, 2, 4]])
        logger.error("test_improper_b_c_dimensions(): a → %s", a, extra={"event.action": "test_improper_b_c_dimensions"})
        b = np.array([[0, 3], [3, 0], [2, 3]])
        logger.error("test_improper_b_c_dimensions(): b → %s", b, extra={"event.action": "test_improper_b_c_dimensions"})
        c = np.array([[2, 1, 3], [6, 3, 5]])
        logger.error("test_improper_b_c_dimensions(): c → %s", c, extra={"event.action": "test_improper_b_c_dimensions"})

        with pytest.raises(ValueError):
            schur_complement(a, b, c)
            logger.warning("<<< Exiting test_improper_b_c_dimensions()", extra={"event.action": "test_improper_b_c_dimensions"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    unittest.main()
