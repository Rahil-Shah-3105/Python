import logging
logger = logging.getLogger(__name__)
"""
Matrix-Based Game Script
=========================
This script implements a matrix-based game where players interact with a grid of
elements. The primary goals are to:
- Identify connected elements of the same type from a selected position.
- Remove those elements, adjust the matrix by simulating gravity, and reorganize empty
  columns.
- Calculate and display the score based on the number of elements removed in each move.

Functions:
-----------
1. `find_repeat`: Finds all connected elements of the same type.
2. `increment_score`: Calculates the score for a given move.
3. `move_x`: Simulates gravity in a column.
4. `move_y`: Reorganizes the matrix by shifting columns leftward when a column becomes
    empty.
5. `play`: Executes a single move, updating the matrix and returning the score.

Input Format:
--------------
1. Matrix size (`lines`): Integer specifying the size of the matrix (N x N).
2. Matrix content (`matrix`): Rows of the matrix, each consisting of characters.
3. Number of moves (`movs`): Integer indicating the number of moves.
4. List of moves (`movements`): A comma-separated string of coordinates for each move.

(0,0) position starts from first left column to last right, and below row to up row


Example Input:
---------------
4
RRBG
RBBG
YYGG
XYGG
2
0 1,1 1

Example (0,0) = X

Output:
--------
The script outputs the total score after processing all moves.

Usage:
-------
Run the script and provide the required inputs as prompted.

"""


def validate_matrix_size(size: int) -> None:
    """
    >>> validate_matrix_size(-1)
    Traceback (most recent call last):
        ...
    ValueError: Matrix size must be a positive integer.
    """
    logger.debug(">>> Entering validate_matrix_size(size=%s)", size)
    if not isinstance(size, int) or size <= 0:
        raise ValueError("Matrix size must be a positive integer.")
        logger.debug("<<< Exiting validate_matrix_size(size=%s)", size)


def validate_matrix_content(matrix: list[str], size: int) -> None:
    """
    Validates that the number of elements in the matrix matches the given size.

    >>> validate_matrix_content(['aaaa', 'aaaa', 'aaaa', 'aaaa'], 3)
    Traceback (most recent call last):
        ...
    ValueError: The matrix dont match with size.
    >>> validate_matrix_content(['aa%', 'aaa', 'aaa'], 3)
    Traceback (most recent call last):
        ...
    ValueError: Matrix rows can only contain letters and numbers.
    >>> validate_matrix_content(['aaa', 'aaa', 'aaaa'], 3)
    Traceback (most recent call last):
        ...
    ValueError: Each row in the matrix must have exactly 3 characters.
    """
    logger.debug(">>> Entering validate_matrix_content(matrix=%s,size=%s)", matrix, size)
    print(matrix)
    if len(matrix) != size:
        raise ValueError("The matrix dont match with size.")
    for row in matrix:
        if len(row) != size:
            msg = f"Each row in the matrix must have exactly {size} characters."
            logger.debug("validate_matrix_content(matrix=%s,size=%s): msg → %s", matrix, size, msg)
            raise ValueError(msg)
        if not all(char.isalnum() for char in row):
            raise ValueError("Matrix rows can only contain letters and numbers.")
            logger.debug("<<< Exiting validate_matrix_content(matrix=%s,size=%s)", matrix, size)


def validate_moves(moves: list[tuple[int, int]], size: int) -> None:
    """
    >>> validate_moves([(1, 2), (-1, 0)], 3)
    Traceback (most recent call last):
        ...
    ValueError: Move is out of bounds for a matrix.
    """
    logger.debug(">>> Entering validate_moves(moves=%s,size=%s)", moves, size)
    for move in moves:
        x, y = move
        if not (0 <= x < size and 0 <= y < size):
            raise ValueError("Move is out of bounds for a matrix.")
            logger.debug("<<< Exiting validate_moves(moves=%s,size=%s)", moves, size)


def parse_moves(input_str: str) -> list[tuple[int, int]]:
    """
    >>> parse_moves("0 1, 1 1")
    [(0, 1), (1, 1)]
    >>> parse_moves("0 1, 1 1, 2")
    Traceback (most recent call last):
        ...
    ValueError: Each move must have exactly two numbers.
    >>> parse_moves("0 1, 1 1, 2 4 5 6")
    Traceback (most recent call last):
        ...
    ValueError: Each move must have exactly two numbers.
    """
    logger.debug(">>> Entering parse_moves(input_str=%s)", input_str)
    moves = []
    logger.debug("parse_moves(input_str=%s): moves → %s", input_str, moves)
    for pair in input_str.split(","):
        parts = pair.strip().split()
        logger.debug("parse_moves(input_str=%s): parts → %s", input_str, parts)
        if len(parts) != 2:
            raise ValueError("Each move must have exactly two numbers.")
        x, y = map(int, parts)
        moves.append((x, y))
    logger.debug("<<< Exiting parse_moves(input_str=%s)", input_str)
    return moves


def find_repeat(
    matrix_g: list[list[str]], row: int, column: int, size: int
) -> set[tuple[int, int]]:
    """
    Finds all connected elements of the same type from a given position.

    >>> find_repeat([['A', 'B', 'A'], ['A', 'B', 'A'], ['A', 'A', 'A']], 0, 0, 3)
    {(1, 2), (2, 1), (0, 0), (2, 0), (0, 2), (2, 2), (1, 0)}
    >>> find_repeat([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']], 1, 1, 3)
    set()
    """

    column = size - 1 - column
    visited = set()
    repeated = set()

    if (color := matrix_g[column][row]) != "-":

        def dfs(row_n: int, column_n: int) -> None:
            logger.debug(">>> Entering dfs(row_n=%s,column_n=%s)", row_n, column_n)
            if row_n < 0 or row_n >= size or column_n < 0 or column_n >= size:
                return
            if (row_n, column_n) in visited:
                logger.debug("<<< Exiting dfs(row_n=%s,column_n=%s)", row_n, column_n)
                return
            visited.add((row_n, column_n))
            if matrix_g[row_n][column_n] == color:
                repeated.add((row_n, column_n))
                dfs(row_n - 1, column_n)
                dfs(row_n + 1, column_n)
                dfs(row_n, column_n - 1)
                dfs(row_n, column_n + 1)

        dfs(column, row)

    return repeated


def increment_score(count: int) -> int:
    """
    Calculates the score for a move based on the number of elements removed.

    >>> increment_score(3)
    6
    >>> increment_score(0)
    0
    """
    logger.debug(">>> Entering increment_score(count=%s)", count)
    logger.debug("<<< Exiting increment_score(count=%s)", count)
    return int(count * (count + 1) / 2)


def move_x(matrix_g: list[list[str]], column: int, size: int) -> list[list[str]]:
    """
    Simulates gravity in a specific column.

    >>> move_x([['-', 'A'], ['-', '-'], ['-', 'C']], 1, 2)
    [['-', '-'], ['-', 'A'], ['-', 'C']]
    """
    logger.debug(">>> Entering move_x(matrix_g=%s,column=%s,size=%s)", matrix_g, column, size)

    new_list = []
    logger.debug("move_x(matrix_g=%s,column=%s,size=%s): new_list → %s", matrix_g, column, size, new_list)

    for row in range(size):
        if matrix_g[row][column] != "-":
            new_list.append(matrix_g[row][column])
        else:
            new_list.insert(0, matrix_g[row][column])
    for row in range(size):
        matrix_g[row][column] = new_list[row]
    logger.debug("<<< Exiting move_x(matrix_g=%s,column=%s,size=%s)", matrix_g, column, size)
    return matrix_g


def move_y(matrix_g: list[list[str]], size: int) -> list[list[str]]:
    """
    Shifts all columns leftward when an entire column becomes empty.

    >>> move_y([['-', 'A'], ['-', '-'], ['-', 'C']], 2)
    [['A', '-'], ['-', '-'], ['-', 'C']]
    """
    logger.debug(">>> Entering move_y(matrix_g=%s,size=%s)", matrix_g, size)

    empty_columns = []
    logger.debug("move_y(matrix_g=%s,size=%s): empty_columns → %s", matrix_g, size, empty_columns)

    for column in range(size - 1, -1, -1):
        if all(matrix_g[row][column] == "-" for row in range(size)):
            empty_columns.append(column)

    for column in empty_columns:
        for col in range(column + 1, size):
            for row in range(size):
                matrix_g[row][col - 1] = matrix_g[row][col]
        for row in range(size):
            matrix_g[row][-1] = "-"

    logger.debug("<<< Exiting move_y(matrix_g=%s,size=%s)", matrix_g, size)
    return matrix_g


def play(
    matrix_g: list[list[str]], pos_x: int, pos_y: int, size: int
) -> tuple[list[list[str]], int]:
    """
    Processes a single move, updating the matrix and calculating the score.

    >>> play([['R', 'G'], ['R', 'G']], 0, 0, 2)
    ([['G', '-'], ['G', '-']], 3)
    """

    same_colors = find_repeat(matrix_g, pos_x, pos_y, size)

    if len(same_colors) != 0:
        for pos in same_colors:
            matrix_g[pos[0]][pos[1]] = "-"
        for column in range(size):
            matrix_g = move_x(matrix_g, column, size)

        matrix_g = move_y(matrix_g, size)

    return (matrix_g, increment_score(len(same_colors)))


def process_game(size: int, matrix: list[str], moves: list[tuple[int, int]]) -> int:
    """Processes the game logic for the given matrix and moves.

    Args:
        size (int): Size of the game board.
        matrix (List[str]): Initial game matrix.
        moves (List[Tuple[int, int]]): List of moves as (x, y) coordinates.

    Returns:
        int: The total score obtained.
    >>> process_game(3, ['aaa', 'bbb', 'ccc'], [(0, 0)])
    6
    """
    logger.debug(">>> Entering process_game(size=%s,matrix=%s,moves=%s)", size, matrix, moves)

    game_matrix = [list(row) for row in matrix]
    logger.debug("process_game(size=%s,matrix=%s,moves=%s): game_matrix → %s", size, matrix, moves, game_matrix)
    total_score = 0
    logger.debug("process_game(size=%s,matrix=%s,moves=%s): total_score → %s", size, matrix, moves, total_score)

    for move in moves:
        pos_x, pos_y = move
        game_matrix, score = play(game_matrix, pos_x, pos_y, size)
        total_score += score

    logger.debug("<<< Exiting process_game(size=%s,matrix=%s,moves=%s)", size, matrix, moves)
    return total_score


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    try:
        size = int(input("Enter the size of the matrix: "))
        validate_matrix_size(size)
        print(f"Enter the {size} rows of the matrix:")
        matrix = [input(f"Row {i + 1}: ") for i in range(size)]
        validate_matrix_content(matrix, size)
        moves_input = input("Enter the moves (e.g., '0 0, 1 1'): ")
        moves = parse_moves(moves_input)
        validate_moves(moves, size)
        score = process_game(size, matrix, moves)
        print(f"Total score: {score}")
    except ValueError as e:
        print(f"{e}")
