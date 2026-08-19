from __future__ import annotations

from typing import Any
import logging
logger = logging.getLogger(__name__)


class Matrix:
    """
    <class Matrix>
    Matrix structure.
    """

    def __init__(self, row: int, column: int, default_value: float = 0) -> None:
        """
        <method Matrix.__init__>
        Initialize matrix with given size and default value.
        Example:
        >>> a = Matrix(2, 3, 1)
        >>> a
        Matrix consist of 2 rows and 3 columns
        [1, 1, 1]
        [1, 1, 1]
        """
        logger.debug(">>> Entering __init__(row=%s,column=%s,default_value=%s)", row, column, default_value)

        self.row, self.column = row, column
        logger.debug("<<< Exiting __init__(row=%s,column=%s,default_value=%s)", row, column, default_value)
        self.array = [[default_value for _ in range(column)] for _ in range(row)]
        logger.debug("__init__(row=%s,column=%s,default_value=%s): self.array → %s", row, column, default_value, self.array)

    def __str__(self) -> str:
        """
        <method Matrix.__str__>
        Return string representation of this matrix.
        """
        logger.debug(">>> Entering __str__()")

        # Prefix
        s = f"Matrix consist of {self.row} rows and {self.column} columns\n"
        logger.debug("__str__(): s → %s", s)
        logger.debug("__str__(): max_element_length → %s", max_element_length)
        logger.debug("__str__(self=%s): max_element_length → %s", self, max_element_length)
        logger.debug("__str__(): string_format_identifier → %s", string_format_identifier)

        logger.debug("<<< Exiting __str__()")
        # Make string identifier
        max_element_length = 0
        for row_vector in self.array:
            for obj in row_vector:
                max_element_length = max(max_element_length, len(str(obj)))
        string_format_identifier = f"%{max_element_length}s"
        logger.debug("__str__(self=%s): string_format_identifier → %s", self, string_format_identifier)

        # Make string and return
        def single_line(row_vector: list[float]) -> str:
            logger.debug(">>> Entering single_line(row_vector=%s)", row_vector)
            nonlocal string_format_identifier
            line = "["
            logger.debug("single_line(row_vector=%s): line → %s", row_vector, line)
            line += ", ".join(string_format_identifier % (obj,) for obj in row_vector)
            line += "]"
            logger.debug("<<< Exiting single_line(row_vector=%s)", row_vector)
            return line

        s += "\n".join(single_line(row_vector) for row_vector in self.array)
        return s

    def __repr__(self) -> str:
        logger.debug(">>> Entering __repr__()")
        logger.debug("<<< Exiting __repr__()")
        return str(self)

    def validate_indices(self, loc: tuple[int, int]) -> bool:
        """
        <method Matrix.validate_indicies>
        Check if given indices are valid to pick element from matrix.
        Example:
        >>> a = Matrix(2, 6, 0)
        >>> a.validate_indices((2, 7))
        False
        >>> a.validate_indices((0, 0))
        True
        """
        logger.debug(">>> Entering validate_indices(loc=%s)", loc)
        if not (isinstance(loc, (list, tuple)) and len(loc) == 2):  # noqa: SIM114
            return False
        elif not (0 <= loc[0] < self.row and 0 <= loc[1] < self.column):
            return False
        else:
            logger.debug("<<< Exiting validate_indices(loc=%s)", loc)
            return True

    def __getitem__(self, loc: tuple[int, int]) -> Any:
        """
        <method Matrix.__getitem__>
        Return array[row][column] where loc = (row, column).
        Example:
        >>> a = Matrix(3, 2, 7)
        >>> a[1, 0]
        7
        """
        logger.debug(">>> Entering __getitem__(loc=%s)", loc)
        assert self.validate_indices(loc)
        logger.debug("<<< Exiting __getitem__(loc=%s)", loc)
        return self.array[loc[0]][loc[1]]

    def __setitem__(self, loc: tuple[int, int], value: float) -> None:
        """
        <method Matrix.__setitem__>
        Set array[row][column] = value where loc = (row, column).
        Example:
        >>> a = Matrix(2, 3, 1)
        >>> a[1, 2] = 51
        >>> a
        Matrix consist of 2 rows and 3 columns
        [ 1,  1,  1]
        [ 1,  1, 51]
        """
        logger.debug(">>> Entering __setitem__(loc=%s,value=%s)", loc, value)
        assert self.validate_indices(loc)
        self.array[loc[0]][loc[1]] = value
        logger.debug("<<< Exiting __setitem__(loc=%s,value=%s)", loc, value)

    def __add__(self, another: Matrix) -> Matrix:
        """
        <method Matrix.__add__>
        Return self + another.
        Example:
        >>> a = Matrix(2, 1, -4)
        >>> b = Matrix(2, 1, 3)
        >>> a+b
        Matrix consist of 2 rows and 1 columns
        [-1]
        [-1]
        """
        logger.debug(">>> Entering __add__(another=%s)", another)

        # Validation
        assert isinstance(another, Matrix)
        assert self.row == another.row
        assert self.column == another.column

        # Add
        result = Matrix(self.row, self.column)
        logger.debug("__add__(another=%s): result → %s", another, result)
        for r in range(self.row):
            for c in range(self.column):
                result[r, c] = self[r, c] + another[r, c]
        logger.debug("<<< Exiting __add__(another=%s)", another)
        return result

    def __neg__(self) -> Matrix:
        """
        <method Matrix.__neg__>
        Return -self.
        Example:
        >>> a = Matrix(2, 2, 3)
        >>> a[0, 1] = a[1, 0] = -2
        >>> -a
        Matrix consist of 2 rows and 2 columns
        [-3,  2]
        [ 2, -3]
        """
        logger.debug(">>> Entering __neg__()")

        result = Matrix(self.row, self.column)
        logger.debug("__neg__(): result → %s", result)
        for r in range(self.row):
            for c in range(self.column):
                result[r, c] = -self[r, c]
        logger.debug("<<< Exiting __neg__()")
        return result

    def __sub__(self, another: Matrix) -> Matrix:
        logger.debug(">>> Entering __sub__(another=%s)", another)
        logger.debug("<<< Exiting __sub__(another=%s)", another)
        return self + (-another)

    def __mul__(self, another: float | Matrix) -> Matrix:
        """
        <method Matrix.__mul__>
        Return self * another.
        Example:
        >>> a = Matrix(2, 3, 1)
        >>> a[0,2] = a[1,2] = 3
        >>> a * -2
        Matrix consist of 2 rows and 3 columns
        [-2, -2, -6]
        [-2, -2, -6]
        """
        logger.debug(">>> Entering __mul__(another=%s)", another)

        if isinstance(another, (int, float)):  # Scalar multiplication
            result = Matrix(self.row, self.column)
            logger.debug("__mul__(another=%s): result → %s", another, result)
            for r in range(self.row):
                for c in range(self.column):
                    result[r, c] = self[r, c] * another
            return result
        elif isinstance(another, Matrix):  # Matrix multiplication
            assert self.column == another.row
            result = Matrix(self.row, another.column)
            for r in range(self.row):
                for c in range(another.column):
                    for i in range(self.column):
                        result[r, c] += self[r, i] * another[i, c]
            logger.debug("<<< Exiting __mul__(another=%s)", another)
            return result
        else:
            msg = f"Unsupported type given for another ({type(another)})"
            logger.debug("__mul__(self=%s,another=%s): msg → %s", self, another, msg)
            raise TypeError(msg)

    def transpose(self) -> Matrix:
        """
        <method Matrix.transpose>
        Return self^T.
        Example:
        >>> a = Matrix(2, 3)
        >>> for r in range(2):
        ...     for c in range(3):
        ...             a[r,c] = r*c
        ...
        >>> a.transpose()
        Matrix consist of 3 rows and 2 columns
        [0, 0]
        [0, 1]
        [0, 2]
        """
        logger.debug(">>> Entering transpose()")

        result = Matrix(self.column, self.row)
        logger.debug("transpose(): result → %s", result)
        for r in range(self.row):
            for c in range(self.column):
                result[c, r] = self[r, c]
        logger.debug("<<< Exiting transpose()")
        return result

    def sherman_morrison(self, u: Matrix, v: Matrix) -> Any:
        """
        <method Matrix.sherman_morrison>
        Apply Sherman-Morrison formula in O(n^2).
        To learn this formula, please look this:
        https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula
        This method returns (A + uv^T)^(-1) where A^(-1) is self. Returns None if it's
        impossible to calculate.
        Warning: This method doesn't check if self is invertible.
            Make sure self is invertible before execute this method.
        Example:
        >>> ainv = Matrix(3, 3, 0)
        >>> for i in range(3): ainv[i,i] = 1
        ...
        >>> u = Matrix(3, 1, 0)
        >>> u[0,0], u[1,0], u[2,0] = 1, 2, -3
        >>> v = Matrix(3, 1, 0)
        >>> v[0,0], v[1,0], v[2,0] = 4, -2, 5
        >>> ainv.sherman_morrison(u, v)
        Matrix consist of 3 rows and 3 columns
        [  1.2857142857142856, -0.14285714285714285,   0.3571428571428571]
        [  0.5714285714285714,   0.7142857142857143,   0.7142857142857142]
        [ -0.8571428571428571,  0.42857142857142855,  -0.0714285714285714]
        """
        logger.debug(">>> Entering sherman_morrison(u=%s,v=%s)", u, v)

        # Size validation
        assert isinstance(u, Matrix)
        assert isinstance(v, Matrix)
        assert self.row == self.column == u.row == v.row  # u, v should be column vector
        assert u.column == v.column == 1  # u, v should be column vector

        # Calculate
        v_t = v.transpose()
        logger.debug("sherman_morrison(self=%s,u=%s,v=%s): v_t → %s", self, u, v, v_t)
        logger.debug("sherman_morrison(u=%s,v=%s): v_t → %s", u, v, v_t)
        numerator_factor = (v_t * self * u)[0, 0] + 1
        logger.debug("sherman_morrison(u=%s,v=%s): numerator_factor → %s", u, v, numerator_factor)
        if numerator_factor == 0:
            return None  # It's not invertible
        logger.debug("<<< Exiting sherman_morrison(u=%s,v=%s)", u, v)
        return self - ((self * u) * (v_t * self) * (1.0 / numerator_factor))


# Testing
if __name__ == "__main__":

    def test1() -> None:
        logger.debug(">>> Entering test1()")
        # a^(-1)
        ainv = Matrix(3, 3, 0)
        logger.debug("test1(): ainv → %s", ainv)
        for i in range(3):
            ainv[i, i] = 1
        print(f"a^(-1) is {ainv}")
        # u, v
        u = Matrix(3, 1, 0)
        logger.debug("test1(): u → %s", u)
        u[0, 0], u[1, 0], u[2, 0] = 1, 2, -3
        v = Matrix(3, 1, 0)
        logger.debug("test1(): v → %s", v)
        v[0, 0], v[1, 0], v[2, 0] = 4, -2, 5
        print(f"u is {u}")
        print(f"v is {v}")
        print(f"uv^T is {u * v.transpose()}")
        # Sherman Morrison
        print(f"(a + uv^T)^(-1) is {ainv.sherman_morrison(u, v)}")
        logger.debug("<<< Exiting test1()")

    def test2() -> None:
        logger.debug(">>> Entering test2()")
        import doctest

        doctest.testmod()
        logger.debug("<<< Exiting test2()")

    test2()
