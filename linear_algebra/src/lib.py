"""
Created on Mon Feb 26 14:29:11 2018

@author: Christian Bender
@license: MIT-license

This module contains some useful classes and functions for dealing
with linear algebra in python.

Overview:

- class Vector
- function zero_vector(dimension)
- function unit_basis_vector(dimension, pos)
- function axpy(scalar, vector1, vector2)
- function random_vector(N, a, b)
- class Matrix
- function square_zero_matrix(N)
- function random_matrix(W, H, a, b)
"""

from __future__ import annotations

import math
import random
from collections.abc import Collection
from typing import overload
import logging
logger = logging.getLogger(__name__)


class Vector:
    """
    This class represents a vector of arbitrary size.
    You need to give the vector components.

    Overview of the methods:

        __init__(components: Collection[float] | None): init the vector
        __len__(): gets the size of the vector (number of components)
        __str__(): returns a string representation
        __add__(other: Vector): vector addition
        __sub__(other: Vector): vector subtraction
        __mul__(other: float): scalar multiplication
        __mul__(other: Vector): dot product
        copy(): copies this vector and returns it
        component(i): gets the i-th component (0-indexed)
        change_component(pos: int, value: float): changes specified component
        euclidean_length(): returns the euclidean length of the vector
        angle(other: Vector, deg: bool): returns the angle between two vectors
    """

    def __init__(self, components: Collection[float] | None = None) -> None:
        """
        input: components or nothing
        simple constructor for init the vector
        """
        logger.debug(">>> Entering __init__(components=%s)", components)
        if components is None:
            components = []
            logger.debug("<<< Exiting __init__(components=%s)", components)
        self.__components = list(components)
        logger.debug("__init__(components=%s): self.__components → %s", components, self.__components)
        logger.debug(">>> Entering __init__(matrix=%s,w=%s,h=%s)", matrix, w, h)
        logger.debug("<<< Exiting __init__(matrix=%s,w=%s,h=%s)", matrix, w, h)
        logger.debug("__init__(self=%s,matrix=%s,w=%s,h=%s): self.__matrix → %s", self, matrix, w, h, self.__matrix)
        logger.debug("__init__(self=%s,matrix=%s,w=%s,h=%s): self.__width → %s", self, matrix, w, h, self.__width)

    def __len__(self) -> int:
        """
        returns the size of the vector
        """
        logger.debug(">>> Entering __len__()")
        logger.debug("<<< Exiting __len__()")
        return len(self.__components)

    def __str__(self) -> str:
        """
        returns a string representation of the vector
        """
        logger.debug(">>> Entering __str__()")
        logger.debug("__str__(): ans → %s", ans)
        logger.debug("__str__(self=%s): ans → %s", self, ans)
        logger.debug("<<< Exiting __str__()")
        return "(" + ",".join(map(str, self.__components)) + ")"

    def __add__(self, other: Vector) -> Vector:
        """
        input: other vector
        assumes: other vector has the same size
        returns a new vector that represents the sum.
        """
        size = len(self)
        if size == len(other):
            result = [self.__components[i] + other.component(i) for i in range(size)]
            return Vector(result)
        else:
            logger.debug(">>> Entering __add__(other=%s)", other)
            logger.debug("__add__(self=%s,other=%s): matrix → %s", self, other, matrix)
            logger.debug("__add__(self=%s,other=%s): row → %s", self, other, row)
            logger.debug("<<< Exiting __add__(other=%s)", other)
            raise Exception("must have the same size")

    def __sub__(self, other: Vector) -> Vector:
        """
        input: other vector
        assumes: other vector has the same size
        returns a new vector that represents the difference.
        """
        size = len(self)
        if size == len(other):
            result = [self.__components[i] - other.component(i) for i in range(size)]
            return Vector(result)
        else:  # error case
            logger.debug(">>> Entering __sub__(other=%s)", other)
            logger.debug("__sub__(self=%s,other=%s): matrix → %s", self, other, matrix)
            logger.debug("__sub__(self=%s,other=%s): row → %s", self, other, row)
            logger.debug("<<< Exiting __sub__(other=%s)", other)
            raise Exception("must have the same size")

    def __eq__(self, other: object) -> bool:
        """
        performs the comparison between two vectors
        """
        logger.debug(">>> Entering __eq__(other=%s)", other)
        if not isinstance(other, Vector):
            return NotImplemented
        if len(self) != len(other):
            return False
        logger.debug("<<< Exiting __eq__(other=%s)", other)
        return all(self.component(i) == other.component(i) for i in range(len(self)))

    @overload
    def __mul__(self, other: float) -> Vector: ...

    @overload
    def __mul__(self, other: Vector) -> float: ...

    def __mul__(self, other: float | Vector) -> float | Vector:
        """
        mul implements the scalar multiplication
        and the dot-product
        """
        if isinstance(other, (float, int)):
            ans = [c * other for c in self.__components]
            return Vector(ans)
        elif isinstance(other, Vector) and len(self) == len(other):
            size = len(self)
            prods = [self.__components[i] * other.component(i) for i in range(size)]
            return sum(prods)
        else:  # error case
            logger.debug(">>> Entering __mul__(other=%s)", other)
            logger.debug("__mul__(other=%s): ans → %s", other, ans)
            logger.debug("__mul__(self=%s,other=%s): ans → %s", self, other, ans)
            logger.debug("__mul__(self=%s,other=%s): prods → %s", self, other, prods)
            logger.debug("__mul__(self=%s,other=%s): matrix → %s", self, other, matrix)
            logger.debug("<<< Exiting __mul__(other=%s)", other)
            raise Exception("invalid operand!")

    def copy(self) -> Vector:
        """
        copies this vector and returns it.
        """
        logger.debug(">>> Entering copy()")
        logger.debug("<<< Exiting copy()")
        return Vector(self.__components)

    def component(self, i: int) -> float:
        """
        input: index (0-indexed)
        output: the i-th component of the vector.
        """
        logger.debug(">>> Entering component(i=%s)", i)
        if isinstance(i, int) and -len(self.__components) <= i < len(self.__components):
            logger.debug("<<< Exiting component(i=%s)", i)
            return self.__components[i]
        else:
            logger.debug(">>> Entering component(x=%s,y=%s)", x, y)
            logger.debug("<<< Exiting component(x=%s,y=%s)", x, y)
            raise Exception("index out of range")

    def change_component(self, pos: int, value: float) -> None:
        """
        input: an index (pos) and a value
        changes the specified component (pos) with the
        'value'
        """
        logger.debug(">>> Entering change_component(pos=%s,value=%s)", pos, value)
        # precondition
        assert -len(self.__components) <= pos < len(self.__components)
        self.__components[pos] = value
        logger.debug("<<< Exiting change_component(pos=%s,value=%s)", pos, value)
        logger.debug(">>> Entering change_component(x=%s,y=%s,value=%s)", x, y, value)
        logger.debug("<<< Exiting change_component(x=%s,y=%s,value=%s)", x, y, value)

    def euclidean_length(self) -> float:
        """
        returns the euclidean length of the vector

        >>> Vector([2, 3, 4]).euclidean_length()
        5.385164807134504
        >>> Vector([1]).euclidean_length()
        1.0
        >>> Vector([0, -1, -2, -3, 4, 5, 6]).euclidean_length()
        9.539392014169456
        >>> Vector([]).euclidean_length()
        Traceback (most recent call last):
            ...
        Exception: Vector is empty
        """
        logger.debug(">>> Entering euclidean_length()")
        if len(self.__components) == 0:
            raise Exception("Vector is empty")
        squares = [c**2 for c in self.__components]
        logger.debug("euclidean_length(self=%s): squares → %s", self, squares)
        logger.debug("<<< Exiting euclidean_length()")
        return math.sqrt(sum(squares))

    def angle(self, other: Vector, deg: bool = False) -> float:
        """
        find angle between two Vector (self, Vector)

        >>> Vector([3, 4, -1]).angle(Vector([2, -1, 1]))
        1.4906464636572374
        >>> Vector([3, 4, -1]).angle(Vector([2, -1, 1]), deg = True)
        85.40775111366095
        >>> Vector([3, 4, -1]).angle(Vector([2, -1]))
        Traceback (most recent call last):
            ...
        Exception: invalid operand!
        """
        logger.debug(">>> Entering angle(other=%s,deg=%s)", other, deg)
        num = self * other
        logger.debug("angle(self=%s,other=%s,deg=%s): num → %s", self, other, deg, num)
        den = self.euclidean_length() * other.euclidean_length()
        logger.debug("angle(self=%s,other=%s,deg=%s): den → %s", self, other, deg, den)
        logger.debug("angle(other=%s,deg=%s): den → %s", other, deg, den)
        if deg:
            return math.degrees(math.acos(num / den))
        else:
            logger.debug("<<< Exiting angle(other=%s,deg=%s)", other, deg)
            return math.acos(num / den)


def zero_vector(dimension: int) -> Vector:
    """
    returns a zero-vector of size 'dimension'
    """
    logger.debug(">>> Entering zero_vector(dimension=%s)", dimension)
    # precondition
    assert isinstance(dimension, int)
    logger.debug("<<< Exiting zero_vector(dimension=%s)", dimension)
    return Vector([0] * dimension)


def unit_basis_vector(dimension: int, pos: int) -> Vector:
    """
    returns a unit basis vector with a One
    at index 'pos' (indexing at 0)
    """
    logger.debug(">>> Entering unit_basis_vector(dimension=%s,pos=%s)", dimension, pos)
    # precondition
    assert isinstance(dimension, int)
    assert isinstance(pos, int)
    ans = [0] * dimension
    logger.debug("unit_basis_vector(dimension=%s,pos=%s): ans → %s", dimension, pos, ans)
    ans[pos] = 1
    logger.debug("<<< Exiting unit_basis_vector(dimension=%s,pos=%s)", dimension, pos)
    return Vector(ans)


def axpy(scalar: float, x: Vector, y: Vector) -> Vector:
    """
    input: a 'scalar' and two vectors 'x' and 'y'
    output: a vector
    computes the axpy operation
    """
    logger.debug(">>> Entering axpy(scalar=%s,x=%s,y=%s)", scalar, x, y)
    # precondition
    assert isinstance(x, Vector)
    assert isinstance(y, Vector)
    assert isinstance(scalar, (int, float))
    logger.debug("<<< Exiting axpy(scalar=%s,x=%s,y=%s)", scalar, x, y)
    return x * scalar + y


def random_vector(n: int, a: int, b: int) -> Vector:
    """
    input: size (N) of the vector.
           random range (a,b)
    output: returns a random vector of size N, with
            random integer components between 'a' and 'b'.
    """
    logger.debug(">>> Entering random_vector(n=%s,a=%s,b=%s)", n, a, b)
    random.seed(None)
    ans = [random.randint(a, b) for _ in range(n)]
    logger.debug("random_vector(n=%s,a=%s,b=%s): ans → %s", n, a, b, ans)
    logger.debug("<<< Exiting random_vector(n=%s,a=%s,b=%s)", n, a, b)
    return Vector(ans)


class Matrix:
    """
    class: Matrix
    This class represents an arbitrary matrix.

    Overview of the methods:

        __init__():
        __str__(): returns a string representation
        __add__(other: Matrix): matrix addition
        __sub__(other: Matrix): matrix subtraction
        __mul__(other: float): scalar multiplication
        __mul__(other: Vector): vector multiplication
        height() : returns height
        width() : returns width
        component(x: int, y: int): returns specified component
        change_component(x: int, y: int, value: float): changes specified component
        minor(x: int, y: int): returns minor along (x, y)
        cofactor(x: int, y: int): returns cofactor along (x, y)
        determinant() : returns determinant
    """

    def __init__(self, matrix: list[list[float]], w: int, h: int) -> None:
        """
        simple constructor for initializing the matrix with components.
        """
        self.__matrix = matrix
        self.__width = w
        self.__height = h
        logger.debug("__init__(self=%s,matrix=%s,w=%s,h=%s): self.__height → %s", self, matrix, w, h, self.__height)

    def __str__(self) -> str:
        """
        returns a string representation of this matrix.
        """
        ans = ""
        for i in range(self.__height):
            ans += "|"
            for j in range(self.__width):
                if j < self.__width - 1:
                    ans += str(self.__matrix[i][j]) + ","
                else:
                    ans += str(self.__matrix[i][j]) + "|\n"
        return ans

    def __add__(self, other: Matrix) -> Matrix:
        """
        implements matrix addition.
        """
        logger.debug(">>> Entering __add__(other=%s)", other)
        if self.__width == other.width() and self.__height == other.height():
            matrix = []
            for i in range(self.__height):
                row = [
                    self.__matrix[i][j] + other.component(i, j)
                    for j in range(self.__width)
                ]
                matrix.append(row)
            return Matrix(matrix, self.__width, self.__height)
        else:
            raise Exception("matrix must have the same dimension!")

    def __sub__(self, other: Matrix) -> Matrix:
        """
        implements matrix subtraction.
        """
        logger.debug(">>> Entering __sub__(other=%s)", other)
        if self.__width == other.width() and self.__height == other.height():
            matrix = []
            for i in range(self.__height):
                row = [
                    self.__matrix[i][j] - other.component(i, j)
                    for j in range(self.__width)
                ]
                matrix.append(row)
            return Matrix(matrix, self.__width, self.__height)
        else:
            raise Exception("matrices must have the same dimension!")

    @overload
    def __mul__(self, other: float) -> Matrix: ...

    @overload
    def __mul__(self, other: Vector) -> Vector: ...

    def __mul__(self, other: float | Vector) -> Vector | Matrix:
        """
        implements the matrix-vector multiplication.
        implements the matrix-scalar multiplication
        """
        logger.debug(">>> Entering __mul__(other=%s)", other)
        if isinstance(other, Vector):  # matrix-vector
            if len(other) == self.__width:
                ans = zero_vector(self.__height)
                for i in range(self.__height):
                    prods = [
                        self.__matrix[i][j] * other.component(j)
                        for j in range(self.__width)
                    ]
                    ans.change_component(i, sum(prods))
                return ans
            else:
                raise Exception(
                    "vector must have the same size as the "
                    "number of columns of the matrix!"
                )
        elif isinstance(other, (int, float)):  # matrix-scalar
            matrix = [
                [self.__matrix[i][j] * other for j in range(self.__width)]
                for i in range(self.__height)
            ]
            return Matrix(matrix, self.__width, self.__height)
        return None

    def height(self) -> int:
        """
        getter for the height
        """
        logger.debug(">>> Entering height()")
        logger.debug("<<< Exiting height()")
        return self.__height

    def width(self) -> int:
        """
        getter for the width
        """
        logger.debug(">>> Entering width()")
        logger.debug("<<< Exiting width()")
        return self.__width

    def component(self, x: int, y: int) -> float:
        """
        returns the specified (x,y) component
        """
        if 0 <= x < self.__height and 0 <= y < self.__width:
            return self.__matrix[x][y]
        else:
            raise Exception("change_component: indices out of bounds")

    def change_component(self, x: int, y: int, value: float) -> None:
        """
        changes the x-y component of this matrix
        """
        if 0 <= x < self.__height and 0 <= y < self.__width:
            self.__matrix[x][y] = value
        else:
            raise Exception("change_component: indices out of bounds")

    def minor(self, x: int, y: int) -> float:
        """
        returns the minor along (x, y)
        """
        logger.debug(">>> Entering minor(x=%s,y=%s)", x, y)
        if self.__height != self.__width:
            raise Exception("Matrix is not square")
        minor = self.__matrix[:x] + self.__matrix[x + 1 :]
        logger.debug("minor(self=%s,x=%s,y=%s): minor → %s", self, x, y, minor)
        for i in range(len(minor)):
            minor[i] = minor[i][:y] + minor[i][y + 1 :]
        logger.debug("<<< Exiting minor(x=%s,y=%s)", x, y)
        return Matrix(minor, self.__width - 1, self.__height - 1).determinant()

    def cofactor(self, x: int, y: int) -> float:
        """
        returns the cofactor (signed minor) along (x, y)
        """
        logger.debug(">>> Entering cofactor(x=%s,y=%s)", x, y)
        if self.__height != self.__width:
            raise Exception("Matrix is not square")
        if 0 <= x < self.__height and 0 <= y < self.__width:
            logger.debug("<<< Exiting cofactor(x=%s,y=%s)", x, y)
            return (-1) ** (x + y) * self.minor(x, y)
        else:
            raise Exception("Indices out of bounds")

    def determinant(self) -> float:
        """
        returns the determinant of an nxn matrix using Laplace expansion
        """
        logger.debug(">>> Entering determinant()")
        if self.__height != self.__width:
            raise Exception("Matrix is not square")
        if self.__height < 1:
            raise Exception("Matrix has no element")
        elif self.__height == 1:
            return self.__matrix[0][0]
        elif self.__height == 2:
            return (
                self.__matrix[0][0] * self.__matrix[1][1]
                - self.__matrix[0][1] * self.__matrix[1][0]
            )
        else:
            cofactor_prods = [
                self.__matrix[0][y] * self.cofactor(0, y) for y in range(self.__width)
            ]
            logger.debug("<<< Exiting determinant()")
            return sum(cofactor_prods)


def square_zero_matrix(n: int) -> Matrix:
    """
    returns a square zero-matrix of dimension NxN
    """
    logger.debug(">>> Entering square_zero_matrix(n=%s)", n)
    ans: list[list[float]] = [[0] * n for _ in range(n)]
    logger.debug("<<< Exiting square_zero_matrix(n=%s)", n)
    return Matrix(ans, n, n)


def random_matrix(width: int, height: int, a: int, b: int) -> Matrix:
    """
    returns a random matrix WxH with integer components
    between 'a' and 'b'
    """
    logger.debug(">>> Entering random_matrix(width=%s,height=%s,a=%s,b=%s)", width, height, a, b)
    random.seed(None)
    matrix: list[list[float]] = [
        [random.randint(a, b) for _ in range(width)] for _ in range(height)
    ]
    logger.debug("<<< Exiting random_matrix(width=%s,height=%s,a=%s,b=%s)", width, height, a, b)
    return Matrix(matrix, width, height)
