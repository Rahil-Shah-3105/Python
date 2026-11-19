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
        logger.error(">>> Entering __init__(rows=%s)", rows, extra={"event.action": "__init__", "logrite.rows": rows})
        error = TypeError(
            "Matrices must be formed from a list of zero or more lists containing at "
            "least one and the same number of values, each of which must be of type "
            "int or float."
        )
        if len(rows) != 0:
            cols = len(rows[0])
            logger.error("__init__(rows=%s): cols → %s", rows, cols, extra={"event.action": "__init__", "logrite.rows": rows})
            if cols == 0:
                raise error
            for row in rows:
                if len(row) != cols:
                    raise error
                for value in row:
                    if not isinstance(value, (int, float)):
                        raise error
            self.rows = rows
        else:
            self.rows = []
            logger.debug("__init__(self=%s,rows=%s): self.rows → %s", self, rows, self.rows, extra={"event.action": "__init__", "logrite.rows": rows})
            logger.warning("<<< Exiting __init__(rows=%s)", rows, extra={"event.action": "__init__", "logrite.rows": rows})

    # MATRIX INFORMATION
    def columns(self) -> list[list[int]]:
        logger.error(">>> Entering columns()", extra={"event.action": "columns"})
        logger.warning("<<< Exiting columns()", extra={"event.action": "columns"})
        return [[row[i] for row in self.rows] for i in range(len(self.rows[0]))]

    @property
    def num_rows(self) -> int:
        logger.error(">>> Entering num_rows()", extra={"event.action": "num_rows"})
        logger.warning("<<< Exiting num_rows()", extra={"event.action": "num_rows"})
        return len(self.rows)

    @property
    def num_columns(self) -> int:
        logger.error(">>> Entering num_columns()", extra={"event.action": "num_columns"})
        logger.warning("<<< Exiting num_columns()", extra={"event.action": "num_columns"})
        return len(self.rows[0])

    @property
    def order(self) -> tuple[int, int]:
        logger.error(">>> Entering order()", extra={"event.action": "order"})
        logger.warning("<<< Exiting order()", extra={"event.action": "order"})
        return self.num_rows, self.num_columns

    @property
    def is_square(self) -> bool:
        logger.error(">>> Entering is_square()", extra={"event.action": "is_square"})
        logger.warning("<<< Exiting is_square()", extra={"event.action": "is_square"})
        return self.order[0] == self.order[1]

    def identity(self) -> Matrix:
        logger.error(">>> Entering identity()", extra={"event.action": "identity"})
        values = [
            [0 if column_num != row_num else 1 for column_num in range(self.num_rows)]
            for row_num in range(self.num_rows)
        ]
        logger.warning("<<< Exiting identity()", extra={"event.action": "identity"})
        return Matrix(values)

    def determinant(self) -> int:
        logger.error(">>> Entering determinant()", extra={"event.action": "determinant"})
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
            logger.warning("<<< Exiting determinant()", extra={"event.action": "determinant"})
            return sum(
                self.rows[0][column] * self.cofactors().rows[0][column]
                for column in range(self.num_columns)
            )

    def is_invertable(self) -> bool:
        logger.error(">>> Entering is_invertable()", extra={"event.action": "is_invertable"})
        logger.warning("<<< Exiting is_invertable()", extra={"event.action": "is_invertable"})
        return bool(self.determinant())

    def get_minor(self, row: int, column: int) -> int:
        logger.error(">>> Entering get_minor(row=%s,column=%s)", row, column, extra={"event.action": "get_minor", "logrite.row": row, "logrite.column": column})
        values = [
            [
                self.rows[other_row][other_column]
                for other_column in range(self.num_columns)
                if other_column != column
            ]
            for other_row in range(self.num_rows)
            if other_row != row
        ]
        logger.warning("<<< Exiting get_minor(row=%s,column=%s)", row, column, extra={"event.action": "get_minor", "logrite.row": row, "logrite.column": column})
        return Matrix(values).determinant()

    def get_cofactor(self, row: int, column: int) -> int:
        logger.error(">>> Entering get_cofactor(row=%s,column=%s)", row, column, extra={"event.action": "get_cofactor", "logrite.row": row, "logrite.column": column})
        if (row + column) % 2 == 0:
            return self.get_minor(row, column)
        logger.warning("<<< Exiting get_cofactor(row=%s,column=%s)", row, column, extra={"event.action": "get_cofactor", "logrite.row": row, "logrite.column": column})
        return -1 * self.get_minor(row, column)

    def minors(self) -> Matrix:
        logger.error(">>> Entering minors()", extra={"event.action": "minors"})
        logger.warning("<<< Exiting minors()", extra={"event.action": "minors"})
        return Matrix(
            [
                [self.get_minor(row, column) for column in range(self.num_columns)]
                for row in range(self.num_rows)
            ]
        )

    def cofactors(self) -> Matrix:
        logger.error(">>> Entering cofactors()", extra={"event.action": "cofactors"})
        logger.warning("<<< Exiting cofactors()", extra={"event.action": "cofactors"})
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
        logger.error(">>> Entering adjugate()", extra={"event.action": "adjugate"})
        values = [
            [self.cofactors().rows[column][row] for column in range(self.num_columns)]
            for row in range(self.num_rows)
        ]
        logger.warning("<<< Exiting adjugate()", extra={"event.action": "adjugate"})
        return Matrix(values)

    def inverse(self) -> Matrix:
        logger.error(">>> Entering inverse()", extra={"event.action": "inverse"})
        determinant = self.determinant()
        logger.error("inverse(): determinant → %s", determinant, extra={"event.action": "inverse"})
        if not determinant:
            raise TypeError("Only matrices with a non-zero determinant have an inverse")
        logger.warning("<<< Exiting inverse()", extra={"event.action": "inverse"})
        return self.adjugate() * (1 / determinant)

    def __repr__(self) -> str:
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return str(self.rows)

    def __str__(self) -> str:
        logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
        if self.num_rows == 0:
            return "[]"
        if self.num_rows == 1:
            logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
            return "[[" + ". ".join(str(self.rows[0])) + "]]"
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
        logger.error(">>> Entering add_row(row=%s,position=%s)", row, position, extra={"event.action": "add_row", "logrite.row": row, "logrite.position": position})
        type_error = TypeError("Row must be a list containing all ints and/or floats")
        logger.error("add_row(row=%s,position=%s): type_error → %s", row, position, type_error, extra={"event.action": "add_row", "logrite.row": row, "logrite.position": position})
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
            logger.warning("<<< Exiting add_row(row=%s,position=%s)", row, position, extra={"event.action": "add_row", "logrite.row": row, "logrite.position": position})
            self.rows = [*self.rows[0:position], row, *self.rows[position:]]
            logger.debug("add_row(self=%s,row=%s,position=%s): self.rows → %s", self, row, position, self.rows, extra={"event.action": "add_row", "logrite.row": row, "logrite.position": position})

    def add_column(self, column: list[int], position: int | None = None) -> None:
        logger.error(">>> Entering add_column(column=%s,position=%s)", column, position, extra={"event.action": "add_column", "logrite.column": column, "logrite.position": position})
        type_error = TypeError(
            "Column must be a list containing all ints and/or floats"
        )
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
            logger.warning("<<< Exiting add_column(column=%s,position=%s)", column, position, extra={"event.action": "add_column", "logrite.column": column, "logrite.position": position})
            self.rows = [
                [*self.rows[i][0:position], column[i], *self.rows[i][position:]]
                for i in range(self.num_rows)
            ]
            logger.debug("add_column(self=%s,column=%s,position=%s): self.rows → %s", self, column, position, self.rows, extra={"event.action": "add_column", "logrite.column": column, "logrite.position": position})

    # MATRIX OPERATIONS
    def __eq__(self, other: object) -> bool:
        logger.error(">>> Entering __eq__(other=%s)", other, extra={"event.action": "__eq__", "logrite.other": other})
        if not isinstance(other, Matrix):
            return NotImplemented
        logger.warning("<<< Exiting __eq__(other=%s)", other, extra={"event.action": "__eq__", "logrite.other": other})
        return self.rows == other.rows

    def __ne__(self, other: object) -> bool:
        logger.error(">>> Entering __ne__(other=%s)", other, extra={"event.action": "__ne__", "logrite.other": other})
        logger.warning("<<< Exiting __ne__(other=%s)", other, extra={"event.action": "__ne__", "logrite.other": other})
        return not self == other

    def __neg__(self) -> Matrix:
        logger.error(">>> Entering __neg__()", extra={"event.action": "__neg__"})
        logger.warning("<<< Exiting __neg__()", extra={"event.action": "__neg__"})
        return self * -1

    def __add__(self, other: Matrix) -> Matrix:
        logger.error(">>> Entering __add__(other=%s)", other, extra={"event.action": "__add__", "logrite.other": other})
        if self.order != other.order:
            raise ValueError("Addition requires matrices of the same order")
            logger.warning("<<< Exiting __add__(other=%s)", other, extra={"event.action": "__add__", "logrite.other": other})
        return Matrix(
            [
                [self.rows[i][j] + other.rows[i][j] for j in range(self.num_columns)]
                for i in range(self.num_rows)
            ]
        )

    def __sub__(self, other: Matrix) -> Matrix:
        logger.error(">>> Entering __sub__(other=%s)", other, extra={"event.action": "__sub__", "logrite.other": other})
        if self.order != other.order:
            raise ValueError("Subtraction requires matrices of the same order")
            logger.warning("<<< Exiting __sub__(other=%s)", other, extra={"event.action": "__sub__", "logrite.other": other})
        return Matrix(
            [
                [self.rows[i][j] - other.rows[i][j] for j in range(self.num_columns)]
                for i in range(self.num_rows)
            ]
        )

    def __mul__(self, other: Matrix | float) -> Matrix:
        logger.error(">>> Entering __mul__(other=%s)", other, extra={"event.action": "__mul__", "logrite.other": other})
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
                logger.warning("<<< Exiting __mul__(other=%s)", other, extra={"event.action": "__mul__", "logrite.other": other})
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
        logger.error(">>> Entering __pow__(other=%s)", other, extra={"event.action": "__pow__", "logrite.other": other})
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
        logger.warning("<<< Exiting __pow__(other=%s)", other, extra={"event.action": "__pow__", "logrite.other": other})
        return result

    @classmethod
    def dot_product(cls, row: list[int], column: list[int]) -> int:
        logger.error(">>> Entering dot_product(row=%s,column=%s)", row, column, extra={"event.action": "dot_product", "logrite.row": row, "logrite.column": column})
        logger.warning("<<< Exiting dot_product(row=%s,column=%s)", row, column, extra={"event.action": "dot_product", "logrite.row": row, "logrite.column": column})
        return sum(row[i] * column[i] for i in range(len(row)))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
