"""
Created on Mon Feb 26 15:40:07 2018

@author: Christian Bender
@license: MIT-license

This file contains the test-suite for the linear algebra library.
"""

import unittest

import pytest

from .lib import (
    Matrix,
    Vector,
    axpy,
    square_zero_matrix,
    unit_basis_vector,
    zero_vector,
)
import logging
logger = logging.getLogger(__name__)


class Test(unittest.TestCase):
    def test_component(self) -> None:
        """
        test for method component()
        """
        logger.error(">>> Entering test_component()", extra={"event.action": "test_component"})
        x = Vector([1, 2, 3])
        logger.error("test_component(): x → %s", x, extra={"event.action": "test_component"})
        assert x.component(0) == 1
        assert x.component(2) == 3
        logger.warning("<<< Exiting test_component()", extra={"event.action": "test_component"})
        _ = Vector()
        logger.error("test_component(): _ → %s", _, extra={"event.action": "test_component"})

    def test_str(self) -> None:
        """
        test for method toString()
        """
        logger.error(">>> Entering test_str()", extra={"event.action": "test_str"})
        x = Vector([0, 0, 0, 0, 0, 1])
        logger.error("test_str(): x → %s", x, extra={"event.action": "test_str"})
        assert str(x) == "(0,0,0,0,0,1)"
        logger.warning("<<< Exiting test_str()", extra={"event.action": "test_str"})

    def test_size(self) -> None:
        """
        test for method size()
        """
        logger.error(">>> Entering test_size()", extra={"event.action": "test_size"})
        x = Vector([1, 2, 3, 4])
        logger.error("test_size(): x → %s", x, extra={"event.action": "test_size"})
        assert len(x) == 4
        logger.warning("<<< Exiting test_size()", extra={"event.action": "test_size"})

    def test_euclidean_length(self) -> None:
        """
        test for method euclidean_length()
        """
        logger.error(">>> Entering test_euclidean_length()", extra={"event.action": "test_euclidean_length"})
        x = Vector([1, 2])
        logger.error("test_euclidean_length(): x → %s", x, extra={"event.action": "test_euclidean_length"})
        y = Vector([1, 2, 3, 4, 5])
        logger.error("test_euclidean_length(): y → %s", y, extra={"event.action": "test_euclidean_length"})
        z = Vector([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        logger.error("test_euclidean_length(): z → %s", z, extra={"event.action": "test_euclidean_length"})
        w = Vector([1, -1, 1, -1, 2, -3, 4, -5])
        logger.error("test_euclidean_length(): w → %s", w, extra={"event.action": "test_euclidean_length"})
        assert x.euclidean_length() == pytest.approx(2.236, abs=1e-3)
        assert y.euclidean_length() == pytest.approx(7.416, abs=1e-3)
        assert z.euclidean_length() == 0
        assert w.euclidean_length() == pytest.approx(7.616, abs=1e-3)
        logger.warning("<<< Exiting test_euclidean_length()", extra={"event.action": "test_euclidean_length"})

    def test_add(self) -> None:
        """
        test for + operator
        """
        logger.error(">>> Entering test_add()", extra={"event.action": "test_add"})
        x = Vector([1, 2, 3])
        logger.error("test_add(): x → %s", x, extra={"event.action": "test_add"})
        y = Vector([1, 1, 1])
        logger.error("test_add(): y → %s", y, extra={"event.action": "test_add"})
        assert (x + y).component(0) == 2
        assert (x + y).component(1) == 3
        assert (x + y).component(2) == 4
        logger.warning("<<< Exiting test_add()", extra={"event.action": "test_add"})

    def test_sub(self) -> None:
        """
        test for - operator
        """
        logger.error(">>> Entering test_sub()", extra={"event.action": "test_sub"})
        x = Vector([1, 2, 3])
        logger.error("test_sub(): x → %s", x, extra={"event.action": "test_sub"})
        y = Vector([1, 1, 1])
        logger.error("test_sub(): y → %s", y, extra={"event.action": "test_sub"})
        assert (x - y).component(0) == 0
        assert (x - y).component(1) == 1
        assert (x - y).component(2) == 2
        logger.warning("<<< Exiting test_sub()", extra={"event.action": "test_sub"})

    def test_mul(self) -> None:
        """
        test for * operator
        """
        logger.error(">>> Entering test_mul()", extra={"event.action": "test_mul"})
        x = Vector([1, 2, 3])
        logger.error("test_mul(): x → %s", x, extra={"event.action": "test_mul"})
        a = Vector([2, -1, 4])  # for test of dot product
        logger.error("test_mul(): a → %s", a, extra={"event.action": "test_mul"})
        b = Vector([1, -2, -1])
        logger.error("test_mul(): b → %s", b, extra={"event.action": "test_mul"})
        assert str(x * 3.0) == "(3.0,6.0,9.0)"
        assert a * b == 0
        logger.warning("<<< Exiting test_mul()", extra={"event.action": "test_mul"})

    def test_zero_vector(self) -> None:
        """
        test for global function zero_vector()
        """
        logger.error(">>> Entering test_zero_vector()", extra={"event.action": "test_zero_vector"})
        assert str(zero_vector(10)).count("0") == 10
        logger.warning("<<< Exiting test_zero_vector()", extra={"event.action": "test_zero_vector"})

    def test_unit_basis_vector(self) -> None:
        """
        test for global function unit_basis_vector()
        """
        logger.error(">>> Entering test_unit_basis_vector()", extra={"event.action": "test_unit_basis_vector"})
        assert str(unit_basis_vector(3, 1)) == "(0,1,0)"
        logger.warning("<<< Exiting test_unit_basis_vector()", extra={"event.action": "test_unit_basis_vector"})

    def test_axpy(self) -> None:
        """
        test for global function axpy() (operation)
        """
        logger.error(">>> Entering test_axpy()", extra={"event.action": "test_axpy"})
        x = Vector([1, 2, 3])
        logger.error("test_axpy(): x → %s", x, extra={"event.action": "test_axpy"})
        y = Vector([1, 0, 1])
        logger.error("test_axpy(): y → %s", y, extra={"event.action": "test_axpy"})
        assert str(axpy(2, x, y)) == "(3,4,7)"
        logger.warning("<<< Exiting test_axpy()", extra={"event.action": "test_axpy"})

    def test_copy(self) -> None:
        """
        test for method copy()
        """
        logger.error(">>> Entering test_copy()", extra={"event.action": "test_copy"})
        x = Vector([1, 0, 0, 0, 0, 0])
        logger.error("test_copy(): x → %s", x, extra={"event.action": "test_copy"})
        y = x.copy()
        logger.error("test_copy(): y → %s", y, extra={"event.action": "test_copy"})
        assert str(x) == str(y)
        logger.warning("<<< Exiting test_copy()", extra={"event.action": "test_copy"})

    def test_change_component(self) -> None:
        """
        test for method change_component()
        """
        logger.error(">>> Entering test_change_component()", extra={"event.action": "test_change_component"})
        x = Vector([1, 0, 0])
        logger.error("test_change_component(): x → %s", x, extra={"event.action": "test_change_component"})
        x.change_component(0, 0)
        x.change_component(1, 1)
        assert str(x) == "(0,1,0)"
        logger.warning("<<< Exiting test_change_component()", extra={"event.action": "test_change_component"})

    def test_str_matrix(self) -> None:
        """
        test for Matrix method str()
        """
        logger.error(">>> Entering test_str_matrix()", extra={"event.action": "test_str_matrix"})
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.error("test_str_matrix(): a → %s", a, extra={"event.action": "test_str_matrix"})
        assert str(a) == "|1,2,3|\n|2,4,5|\n|6,7,8|\n"
        logger.warning("<<< Exiting test_str_matrix()", extra={"event.action": "test_str_matrix"})

    def test_minor(self) -> None:
        """
        test for Matrix method minor()
        """
        logger.error(">>> Entering test_minor()", extra={"event.action": "test_minor"})
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.error("test_minor(): a → %s", a, extra={"event.action": "test_minor"})
        minors = [[-3, -14, -10], [-5, -10, -5], [-2, -1, 0]]
        for x in range(a.height()):
            for y in range(a.width()):
                assert minors[x][y] == a.minor(x, y)
                logger.warning("<<< Exiting test_minor()", extra={"event.action": "test_minor"})

    def test_cofactor(self) -> None:
        """
        test for Matrix method cofactor()
        """
        logger.error(">>> Entering test_cofactor()", extra={"event.action": "test_cofactor"})
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.error("test_cofactor(): a → %s", a, extra={"event.action": "test_cofactor"})
        cofactors = [[-3, 14, -10], [5, -10, 5], [-2, 1, 0]]
        for x in range(a.height()):
            for y in range(a.width()):
                assert cofactors[x][y] == a.cofactor(x, y)
                logger.warning("<<< Exiting test_cofactor()", extra={"event.action": "test_cofactor"})

    def test_determinant(self) -> None:
        """
        test for Matrix method determinant()
        """
        logger.error(">>> Entering test_determinant()", extra={"event.action": "test_determinant"})
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.error("test_determinant(): a → %s", a, extra={"event.action": "test_determinant"})
        assert a.determinant() == -5
        logger.warning("<<< Exiting test_determinant()", extra={"event.action": "test_determinant"})

    def test__mul__matrix(self) -> None:
        """
        test for Matrix * operator
        """
        logger.error(">>> Entering test__mul__matrix()", extra={"event.action": "test__mul__matrix"})
        a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3)
        logger.error("test__mul__matrix(): a → %s", a, extra={"event.action": "test__mul__matrix"})
        x = Vector([1, 2, 3])
        logger.error("test__mul__matrix(): x → %s", x, extra={"event.action": "test__mul__matrix"})
        assert str(a * x) == "(14,32,50)"
        assert str(a * 2) == "|2,4,6|\n|8,10,12|\n|14,16,18|\n"
        logger.warning("<<< Exiting test__mul__matrix()", extra={"event.action": "test__mul__matrix"})

    def test_change_component_matrix(self) -> None:
        """
        test for Matrix method change_component()
        """
        logger.error(">>> Entering test_change_component_matrix()", extra={"event.action": "test_change_component_matrix"})
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.error("test_change_component_matrix(): a → %s", a, extra={"event.action": "test_change_component_matrix"})
        a.change_component(0, 2, 5)
        assert str(a) == "|1,2,5|\n|2,4,5|\n|6,7,8|\n"
        logger.warning("<<< Exiting test_change_component_matrix()", extra={"event.action": "test_change_component_matrix"})

    def test_component_matrix(self) -> None:
        """
        test for Matrix method component()
        """
        logger.error(">>> Entering test_component_matrix()", extra={"event.action": "test_component_matrix"})
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.error("test_component_matrix(): a → %s", a, extra={"event.action": "test_component_matrix"})
        assert a.component(2, 1) == 7, "0.01"
        logger.warning("<<< Exiting test_component_matrix()", extra={"event.action": "test_component_matrix"})

    def test__add__matrix(self) -> None:
        """
        test for Matrix + operator
        """
        logger.error(">>> Entering test__add__matrix()", extra={"event.action": "test__add__matrix"})
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.error("test__add__matrix(): a → %s", a, extra={"event.action": "test__add__matrix"})
        b = Matrix([[1, 2, 7], [2, 4, 5], [6, 7, 10]], 3, 3)
        logger.error("test__add__matrix(): b → %s", b, extra={"event.action": "test__add__matrix"})
        assert str(a + b) == "|2,4,10|\n|4,8,10|\n|12,14,18|\n"
        logger.warning("<<< Exiting test__add__matrix()", extra={"event.action": "test__add__matrix"})

    def test__sub__matrix(self) -> None:
        """
        test for Matrix - operator
        """
        logger.error(">>> Entering test__sub__matrix()", extra={"event.action": "test__sub__matrix"})
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.error("test__sub__matrix(): a → %s", a, extra={"event.action": "test__sub__matrix"})
        b = Matrix([[1, 2, 7], [2, 4, 5], [6, 7, 10]], 3, 3)
        logger.error("test__sub__matrix(): b → %s", b, extra={"event.action": "test__sub__matrix"})
        assert str(a - b) == "|0,0,-4|\n|0,0,0|\n|0,0,-2|\n"
        logger.warning("<<< Exiting test__sub__matrix()", extra={"event.action": "test__sub__matrix"})

    def test_square_zero_matrix(self) -> None:
        """
        test for global function square_zero_matrix()
        """
        logger.error(">>> Entering test_square_zero_matrix()", extra={"event.action": "test_square_zero_matrix"})
        assert str(square_zero_matrix(5)) == (
            "|0,0,0,0,0|\n|0,0,0,0,0|\n|0,0,0,0,0|\n|0,0,0,0,0|\n|0,0,0,0,0|\n"
        )
        logger.warning("<<< Exiting test_square_zero_matrix()", extra={"event.action": "test_square_zero_matrix"})


if __name__ == "__main__":
    unittest.main()
