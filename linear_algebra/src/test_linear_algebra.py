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
        logger.debug(">>> Entering test_component()")
        x = Vector([1, 2, 3])
        logger.debug("test_component(): x → %s", x)
        assert x.component(0) == 1
        assert x.component(2) == 3
        logger.debug("<<< Exiting test_component()")
        _ = Vector()
        logger.debug("test_component(): _ → %s", _)

    def test_str(self) -> None:
        """
        test for method toString()
        """
        logger.debug(">>> Entering test_str()")
        x = Vector([0, 0, 0, 0, 0, 1])
        logger.debug("test_str(): x → %s", x)
        assert str(x) == "(0,0,0,0,0,1)"
        logger.debug("<<< Exiting test_str()")

    def test_size(self) -> None:
        """
        test for method size()
        """
        logger.debug(">>> Entering test_size()")
        x = Vector([1, 2, 3, 4])
        logger.debug("test_size(): x → %s", x)
        assert len(x) == 4
        logger.debug("<<< Exiting test_size()")

    def test_euclidean_length(self) -> None:
        """
        test for method euclidean_length()
        """
        logger.debug(">>> Entering test_euclidean_length()")
        x = Vector([1, 2])
        logger.debug("test_euclidean_length(): x → %s", x)
        y = Vector([1, 2, 3, 4, 5])
        logger.debug("test_euclidean_length(): y → %s", y)
        z = Vector([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        logger.debug("test_euclidean_length(): z → %s", z)
        w = Vector([1, -1, 1, -1, 2, -3, 4, -5])
        logger.debug("test_euclidean_length(): w → %s", w)
        assert x.euclidean_length() == pytest.approx(2.236, abs=1e-3)
        assert y.euclidean_length() == pytest.approx(7.416, abs=1e-3)
        assert z.euclidean_length() == 0
        assert w.euclidean_length() == pytest.approx(7.616, abs=1e-3)
        logger.debug("<<< Exiting test_euclidean_length()")

    def test_add(self) -> None:
        """
        test for + operator
        """
        logger.debug(">>> Entering test_add()")
        x = Vector([1, 2, 3])
        logger.debug("test_add(): x → %s", x)
        y = Vector([1, 1, 1])
        logger.debug("test_add(): y → %s", y)
        assert (x + y).component(0) == 2
        assert (x + y).component(1) == 3
        assert (x + y).component(2) == 4
        logger.debug("<<< Exiting test_add()")

    def test_sub(self) -> None:
        """
        test for - operator
        """
        logger.debug(">>> Entering test_sub()")
        x = Vector([1, 2, 3])
        logger.debug("test_sub(): x → %s", x)
        y = Vector([1, 1, 1])
        logger.debug("test_sub(): y → %s", y)
        assert (x - y).component(0) == 0
        assert (x - y).component(1) == 1
        assert (x - y).component(2) == 2
        logger.debug("<<< Exiting test_sub()")

    def test_mul(self) -> None:
        """
        test for * operator
        """
        logger.debug(">>> Entering test_mul()")
        x = Vector([1, 2, 3])
        logger.debug("test_mul(): x → %s", x)
        a = Vector([2, -1, 4])  # for test of dot product
        logger.debug("test_mul(): a → %s", a)
        b = Vector([1, -2, -1])
        logger.debug("test_mul(): b → %s", b)
        assert str(x * 3.0) == "(3.0,6.0,9.0)"
        assert a * b == 0
        logger.debug("<<< Exiting test_mul()")

    def test_zero_vector(self) -> None:
        """
        test for global function zero_vector()
        """
        logger.debug(">>> Entering test_zero_vector()")
        assert str(zero_vector(10)).count("0") == 10
        logger.debug("<<< Exiting test_zero_vector()")

    def test_unit_basis_vector(self) -> None:
        """
        test for global function unit_basis_vector()
        """
        logger.debug(">>> Entering test_unit_basis_vector()")
        assert str(unit_basis_vector(3, 1)) == "(0,1,0)"
        logger.debug("<<< Exiting test_unit_basis_vector()")

    def test_axpy(self) -> None:
        """
        test for global function axpy() (operation)
        """
        logger.debug(">>> Entering test_axpy()")
        x = Vector([1, 2, 3])
        logger.debug("test_axpy(): x → %s", x)
        y = Vector([1, 0, 1])
        logger.debug("test_axpy(): y → %s", y)
        assert str(axpy(2, x, y)) == "(3,4,7)"
        logger.debug("<<< Exiting test_axpy()")

    def test_copy(self) -> None:
        """
        test for method copy()
        """
        logger.debug(">>> Entering test_copy()")
        x = Vector([1, 0, 0, 0, 0, 0])
        logger.debug("test_copy(): x → %s", x)
        y = x.copy()
        logger.debug("test_copy(): y → %s", y)
        assert str(x) == str(y)
        logger.debug("<<< Exiting test_copy()")

    def test_change_component(self) -> None:
        """
        test for method change_component()
        """
        logger.debug(">>> Entering test_change_component()")
        x = Vector([1, 0, 0])
        logger.debug("test_change_component(): x → %s", x)
        x.change_component(0, 0)
        x.change_component(1, 1)
        assert str(x) == "(0,1,0)"
        logger.debug("<<< Exiting test_change_component()")

    def test_str_matrix(self) -> None:
        """
        test for Matrix method str()
        """
        logger.debug(">>> Entering test_str_matrix()")
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.debug("test_str_matrix(): a → %s", a)
        assert str(a) == "|1,2,3|\n|2,4,5|\n|6,7,8|\n"
        logger.debug("<<< Exiting test_str_matrix()")

    def test_minor(self) -> None:
        """
        test for Matrix method minor()
        """
        logger.debug(">>> Entering test_minor()")
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.debug("test_minor(): a → %s", a)
        minors = [[-3, -14, -10], [-5, -10, -5], [-2, -1, 0]]
        logger.debug("test_minor(self=%s): minors → %s", self, minors)
        for x in range(a.height()):
            for y in range(a.width()):
                assert minors[x][y] == a.minor(x, y)
                logger.debug("<<< Exiting test_minor()")

    def test_cofactor(self) -> None:
        """
        test for Matrix method cofactor()
        """
        logger.debug(">>> Entering test_cofactor()")
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.debug("test_cofactor(): a → %s", a)
        cofactors = [[-3, 14, -10], [5, -10, 5], [-2, 1, 0]]
        logger.debug("test_cofactor(self=%s): cofactors → %s", self, cofactors)
        for x in range(a.height()):
            for y in range(a.width()):
                assert cofactors[x][y] == a.cofactor(x, y)
                logger.debug("<<< Exiting test_cofactor()")

    def test_determinant(self) -> None:
        """
        test for Matrix method determinant()
        """
        logger.debug(">>> Entering test_determinant()")
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.debug("test_determinant(): a → %s", a)
        assert a.determinant() == -5
        logger.debug("<<< Exiting test_determinant()")

    def test__mul__matrix(self) -> None:
        """
        test for Matrix * operator
        """
        logger.debug(">>> Entering test__mul__matrix()")
        a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 3)
        logger.debug("test__mul__matrix(): a → %s", a)
        x = Vector([1, 2, 3])
        logger.debug("test__mul__matrix(): x → %s", x)
        assert str(a * x) == "(14,32,50)"
        assert str(a * 2) == "|2,4,6|\n|8,10,12|\n|14,16,18|\n"
        logger.debug("<<< Exiting test__mul__matrix()")

    def test_change_component_matrix(self) -> None:
        """
        test for Matrix method change_component()
        """
        logger.debug(">>> Entering test_change_component_matrix()")
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.debug("test_change_component_matrix(): a → %s", a)
        a.change_component(0, 2, 5)
        assert str(a) == "|1,2,5|\n|2,4,5|\n|6,7,8|\n"
        logger.debug("<<< Exiting test_change_component_matrix()")

    def test_component_matrix(self) -> None:
        """
        test for Matrix method component()
        """
        logger.debug(">>> Entering test_component_matrix()")
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.debug("test_component_matrix(): a → %s", a)
        assert a.component(2, 1) == 7, "0.01"
        logger.debug("<<< Exiting test_component_matrix()")

    def test__add__matrix(self) -> None:
        """
        test for Matrix + operator
        """
        logger.debug(">>> Entering test__add__matrix()")
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.debug("test__add__matrix(): a → %s", a)
        b = Matrix([[1, 2, 7], [2, 4, 5], [6, 7, 10]], 3, 3)
        logger.debug("test__add__matrix(): b → %s", b)
        assert str(a + b) == "|2,4,10|\n|4,8,10|\n|12,14,18|\n"
        logger.debug("<<< Exiting test__add__matrix()")

    def test__sub__matrix(self) -> None:
        """
        test for Matrix - operator
        """
        logger.debug(">>> Entering test__sub__matrix()")
        a = Matrix([[1, 2, 3], [2, 4, 5], [6, 7, 8]], 3, 3)
        logger.debug("test__sub__matrix(): a → %s", a)
        b = Matrix([[1, 2, 7], [2, 4, 5], [6, 7, 10]], 3, 3)
        logger.debug("test__sub__matrix(): b → %s", b)
        assert str(a - b) == "|0,0,-4|\n|0,0,0|\n|0,0,-2|\n"
        logger.debug("<<< Exiting test__sub__matrix()")

    def test_square_zero_matrix(self) -> None:
        """
        test for global function square_zero_matrix()
        """
        logger.debug(">>> Entering test_square_zero_matrix()")
        assert str(square_zero_matrix(5)) == (
            "|0,0,0,0,0|\n|0,0,0,0,0|\n|0,0,0,0,0|\n|0,0,0,0,0|\n|0,0,0,0,0|\n"
        )
        logger.debug("<<< Exiting test_square_zero_matrix()")


if __name__ == "__main__":
    unittest.main()
