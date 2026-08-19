# An OOP approach to representing and manipulating matrices

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


class Matrix:
    """
    Matrix object generated from a 2D array where each element is an array representing
    a row.
    Rows can contain type int or float.
    Common operations and information available.
    >>> rows = [
    ...     [1, 2, 3],
    ...     [4, 5, 6],
    ...     [7, 8, 9]
    ... ]
    >>> matrix = Matrix(rows)
    >>> print(matrix)
    [[1. 2. 3.]
     [4. 5. 6.]
     [7. 8. 9.]]

    Matrix rows and columns are available as 2D arrays
    >>> matrix.rows
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> matrix.columns()
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    Order is returned as a tuple
    >>> matrix.order
    (3, 3)

    Squareness and invertability are represented as bool
    >>> matrix.is_square
    True
    >>> matrix.is_invertable()
    False

    Identity, Minors, Cofactors and Adjugate are returned as Matrices.  Inverse can be
    a Matrix or Nonetype
    >>> print(matrix.identity())
    [[1. 0. 0.]
     [0. 1. 0.]
     [0. 0. 1.]]
    >>> print(matrix.minors())
    [[-3. -6. -3.]
     [-6. -12. -6.]
     [-3. -6. -3.]]
    >>> print(matrix.cofactors())
    [[-3. 6. -3.]
     [6. -12. 6.]
     [-3. 6. -3.]]
    >>>  # won't be apparent due to the nature of the cofactor matrix
    >>> print(matrix.adjugate())
    [[-3. 6. -3.]
     [6. -12. 6.]
     [-3. 6. -3.]]
    >>> matrix.inverse()
    Traceback (most recent call last):
        ...
    TypeError: Only matrices with a non-zero determinant have an inverse

    Determinant is an int, float, or Nonetype
    >>> matrix.determinant()
    0

    Negation, scalar multiplication, addition, subtraction, multiplication and
    exponentiation are available and all return a Matrix
    >>> print(-matrix)
    [[-1. -2. -3.]
     [-4. -5. -6.]
     [-7. -8. -9.]]
    >>> matrix2 = matrix * 3
    >>> print(matrix2)
    [[3. 6. 9.]
     [12. 15. 18.]
     [21. 24. 27.]]
    >>> print(matrix + matrix2)
    [[4. 8. 12.]
     [16. 20. 24.]
     [28. 32. 36.]]
    >>> print(matrix - matrix2)
    [[-2. -4. -6.]
     [-8. -10. -12.]
     [-14. -16. -18.]]
    >>> print(matrix ** 3)
    [[468. 576. 684.]
     [1062. 1305. 1548.]
     [1656. 2034. 2412.]]

    Matrices can also be modified
    >>> matrix.add_row([10, 11, 12])
    >>> print(matrix)
    [[1. 2. 3.]
     [4. 5. 6.]
     [7. 8. 9.]
     [10. 11. 12.]]
    >>> matrix2.add_column([8, 16, 32])
    >>> print(matrix2)
    [[3. 6. 9. 8.]
     [12. 15. 18. 16.]
     [21. 24. 27. 32.]]
    >>> print(matrix *  matrix2)
    [[90. 108. 126. 136.]
     [198. 243. 288. 304.]
     [306. 378. 450. 472.]
     [414. 513. 612. 640.]]
    """

    def __init__(self, rows: list[list[int]]):
        logger.debug(">>> Entering __init__(rows=%s)", rows)
        error = TypeError(
            "Matrices must be formed from a list of zero or more lists containing at "
            "least one and the same number of values, each of which must be of type "
            "int or float."
        )
        logger.debug("__init__(self=%s,rows=%s): error → %s", self, rows, error)
        if len(rows) != 0:
            cols = len(rows[0])
            logger.debug("__init__(rows=%s): cols → %s", rows, cols)
            if cols == 0:
                raise error
            for row in rows:
                if len(row) != cols:
                    raise error
                for value in row:
                    if not isinstance(value, (int, float)):
                        raise error
            self.rows = rows
            logger.debug("__init__(self=%s,rows=%s): self.rows → %s", self, rows, self.rows)
        else:
            logger.debug("<<< Exiting __init__(rows=%s)", rows)
            self.rows = []

    # MATRIX INFORMATION
    def columns(self) -> list[list[int]]:
        logger.debug(">>> Entering columns()")
        logger.debug("<<< Exiting columns()")
        return [[row[i] for row in self.rows] for i in range(len(self.rows[0]))]

    @property
    def num_rows(self) -> int:
        logger.debug(">>> Entering num_rows()")
        logger.debug("<<< Exiting num_rows()")
        return len(self.rows)

    @property
    def num_columns(self) -> int:
        logger.debug(">>> Entering num_columns()")
        logger.debug("<<< Exiting num_columns()")
        return len(self.rows[0])

    @property
    def order(self) -> tuple[int, int]:
        logger.debug(">>> Entering order()")
        logger.debug("<<< Exiting order()")
        return self.num_rows, self.num_columns

    @property
    def is_square(self) -> bool:
        logger.debug(">>> Entering is_square()")
        logger.debug("<<< Exiting is_square()")
        logger.debug("identity(self=%s): values → %s", self, values)
        return self.order[0] == self.order[1]

    def identity(self) -> Matrix:
        logger.debug(">>> Entering identity()")
        values = [
            [0 if column_num != row_num else 1 for column_num in range(self.num_rows)]
            for row_num in range(self.num_rows)
        ]
        logger.debug("<<< Exiting identity()")
        return Matrix(values)

    def determinant(self) -> int:
        logger.debug(">>> Entering determinant()")
        if not self.is_square:
            return 0
        if self.order == (0, 0):
            return 1
        if self.order == (1, 1):
            return int(self.rows[0][0])
        if self.order == (2, 2):
            return int(
                (self.rows[0][0] * self.rows[1][1])
                - (self.rows[0][1] * self.rows[1][0])
            )
        else:
            logger.debug("<<< Exiting determinant()")
            return sum(
                self.rows[0][column] * self.cofactors().rows[0][column]
                for column in range(self.num_columns)
            )

    def is_invertable(self) -> bool:
        logger.debug(">>> Entering is_invertable()")
        logger.debug("<<< Exiting is_invertable()")
        logger.debug("get_minor(self=%s,row=%s,column=%s): values → %s", self, row, column, values)
        return bool(self.determinant())

    def get_minor(self, row: int, column: int) -> int:
        logger.debug(">>> Entering get_minor(row=%s,column=%s)", row, column)
        values = [
            [
                self.rows[other_row][other_column]
                for other_column in range(self.num_columns)
                if other_column != column
            ]
            for other_row in range(self.num_rows)
            if other_row != row
        ]
        logger.debug("<<< Exiting get_minor(row=%s,column=%s)", row, column)
        return Matrix(values).determinant()

    def get_cofactor(self, row: int, column: int) -> int:
        logger.debug(">>> Entering get_cofactor(row=%s,column=%s)", row, column)
        if (row + column) % 2 == 0:
            return self.get_minor(row, column)
        logger.debug("<<< Exiting get_cofactor(row=%s,column=%s)", row, column)
        return -1 * self.get_minor(row, column)

    def minors(self) -> Matrix:
        logger.debug(">>> Entering minors()")
        logger.debug("<<< Exiting minors()")
        return Matrix(
            [
                [self.get_minor(row, column) for column in range(self.num_columns)]
                for row in range(self.num_rows)
            ]
        )

    def cofactors(self) -> Matrix:
        logger.debug(">>> Entering cofactors()")
        logger.debug("<<< Exiting cofactors()")
        return Matrix(
            [
                [
                    self.minors().rows[row][column]
                    if (row + column) % 2 == 0
                    else self.minors().rows[row][column] * -1
                    for column in range(self.minors().num_columns)
                ]
                for row in range(self.minors().num_rows)
            ]
        )

    def adjugate(self) -> Matrix:
        logger.debug(">>> Entering adjugate()")
        values = [
            [self.cofactors().rows[column][row] for column in range(self.num_columns)]
            for row in range(self.num_rows)
        ]
        logger.debug("adjugate(self=%s): values → %s", self, values)
        logger.debug("<<< Exiting adjugate()")
        return Matrix(values)

    def inverse(self) -> Matrix:
        logger.debug(">>> Entering inverse()")
        determinant = self.determinant()
        logger.debug("inverse(): determinant → %s", determinant)
        logger.debug("inverse(self=%s): determinant → %s", self, determinant)
        if not determinant:
            raise TypeError("Only matrices with a non-zero determinant have an inverse")
        logger.debug("<<< Exiting inverse()")
        return self.adjugate() * (1 / determinant)

    def __repr__(self) -> str:
        logger.debug(">>> Entering __repr__()")
        logger.debug("<<< Exiting __repr__()")
        return str(self.rows)

    def __str__(self) -> str:
        logger.debug(">>> Entering __str__()")
        if self.num_rows == 0:
            return "[]"
        if self.num_rows == 1:
            return "[[" + ". ".join(str(self.rows[0])) + "]]"
        logger.debug("<<< Exiting __str__()")
        return (
            "["
            + "\n ".join(
                [
                    "[" + ". ".join([str(value) for value in row]) + ".]"
                    for row in self.rows
                ]
            )
            + "]"
        )

    # MATRIX MANIPULATION
    def add_row(self, row: list[int], position: int | None = None) -> None:
        logger.debug(">>> Entering add_row(row=%s,position=%s)", row, position)
        type_error = TypeError("Row must be a list containing all ints and/or floats")
        logger.debug("add_row(row=%s,position=%s): type_error → %s", row, position, type_error)
        logger.debug("add_row(self=%s,row=%s,position=%s): type_error → %s", self, row, position, type_error)
        if not isinstance(row, list):
            raise type_error
        for value in row:
            if not isinstance(value, (int, float)):
                raise type_error
        if len(row) != self.num_columns:
            raise ValueError(
                "Row must be equal in length to the other rows in the matrix"
            )
        if position is None:
            self.rows.append(row)
        else:
            logger.debug("<<< Exiting add_row(row=%s,position=%s)", row, position)
            self.rows = [*self.rows[0:position], row, *self.rows[position:]]
            logger.debug("add_row(self=%s,row=%s,position=%s): self.rows → %s", self, row, position, self.rows)

    def add_column(self, column: list[int], position: int | None = None) -> None:
        logger.debug(">>> Entering add_column(column=%s,position=%s)", column, position)
        type_error = TypeError(
            "Column must be a list containing all ints and/or floats"
        )
        logger.debug("add_column(self=%s,column=%s,position=%s): type_error → %s", self, column, position, type_error)
        if not isinstance(column, list):
            raise type_error
        for value in column:
            if not isinstance(value, (int, float)):
                raise type_error
        if len(column) != self.num_rows:
            raise ValueError(
                "Column must be equal in length to the other columns in the matrix"
            )
        if position is None:
            self.rows = [self.rows[i] + [column[i]] for i in range(self.num_rows)]
        else:
            self.rows = [
                [*self.rows[i][0:position], column[i], *self.rows[i][position:]]
                for i in range(self.num_rows)
            ]
            logger.debug("<<< Exiting add_column(column=%s,position=%s)", column, position)

    # MATRIX OPERATIONS
    def __eq__(self, other: object) -> bool:
        logger.debug(">>> Entering __eq__(other=%s)", other)
        if not isinstance(other, Matrix):
            return NotImplemented
        logger.debug("<<< Exiting __eq__(other=%s)", other)
        return self.rows == other.rows

    def __ne__(self, other: object) -> bool:
        logger.debug(">>> Entering __ne__(other=%s)", other)
        logger.debug("<<< Exiting __ne__(other=%s)", other)
        return not self == other

    def __neg__(self) -> Matrix:
        logger.debug(">>> Entering __neg__()")
        logger.debug("<<< Exiting __neg__()")
        return self * -1

    def __add__(self, other: Matrix) -> Matrix:
        logger.debug(">>> Entering __add__(other=%s)", other)
        if self.order != other.order:
            raise ValueError("Addition requires matrices of the same order")
            logger.debug("<<< Exiting __add__(other=%s)", other)
        return Matrix(
            [
                [self.rows[i][j] + other.rows[i][j] for j in range(self.num_columns)]
                for i in range(self.num_rows)
            ]
        )

    def __sub__(self, other: Matrix) -> Matrix:
        logger.debug(">>> Entering __sub__(other=%s)", other)
        if self.order != other.order:
            raise ValueError("Subtraction requires matrices of the same order")
            logger.debug("<<< Exiting __sub__(other=%s)", other)
        return Matrix(
            [
                [self.rows[i][j] - other.rows[i][j] for j in range(self.num_columns)]
                for i in range(self.num_rows)
            ]
        )

    def __mul__(self, other: Matrix | float) -> Matrix:
        logger.debug(">>> Entering __mul__(other=%s)", other)
        if isinstance(other, (int, float)):
            return Matrix(
                [[int(element * other) for element in row] for row in self.rows]
            )
        elif isinstance(other, Matrix):
            if self.num_columns != other.num_rows:
                raise ValueError(
                    "The number of columns in the first matrix must "
                    "be equal to the number of rows in the second"
                )
            return Matrix(
                [
                    [Matrix.dot_product(row, column) for column in other.columns()]
                    for row in self.rows
                ]
            )
        else:
            raise TypeError(
                "A Matrix can only be multiplied by an int, float, or another matrix"
            )

    def __pow__(self, other: int) -> Matrix:
        logger.debug(">>> Entering __pow__(other=%s)", other)
        if not isinstance(other, int):
            raise TypeError("A Matrix can only be raised to the power of an int")
        if not self.is_square:
            raise ValueError("Only square matrices can be raised to a power")
        if other == 0:
            return self.identity()
        if other < 0:
            if self.is_invertable():
                return self.inverse() ** (-other)
            raise ValueError(
                "Only invertable matrices can be raised to a negative power"
            )
        result = self
        for _ in range(other - 1):
            result *= self
        logger.debug("<<< Exiting __pow__(other=%s)", other)
        return result

    @classmethod
    def dot_product(cls, row: list[int], column: list[int]) -> int:
        logger.debug(">>> Entering dot_product(row=%s,column=%s)", row, column)
        logger.debug("<<< Exiting dot_product(row=%s,column=%s)", row, column)
        return sum(row[i] * column[i] for i in range(len(row)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
