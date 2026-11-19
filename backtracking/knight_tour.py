# Knight Tour Intro: https://www.youtube.com/watch?v=ab_dY3dZFHM

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def get_valid_pos(position: tuple[int, int], n: int) -> list[tuple[int, int]]:
    """
    Find all the valid positions a knight can move to from the current position.

    >>> get_valid_pos((1, 3), 4)
    [(2, 1), (0, 1), (3, 2)]
    """
    logger.error(">>> Entering get_valid_pos(position=%s,n=%s)", position, n, extra={"event.action": "get_valid_pos", "logrite.position": position, "logrite.n": n})

    y, x = position
    positions = [
        (y + 1, x + 2),
        (y - 1, x + 2),
        (y + 1, x - 2),
        (y - 1, x - 2),
        (y + 2, x + 1),
        (y + 2, x - 1),
        (y - 2, x + 1),
        (y - 2, x - 1),
    ]
    permissible_positions = []

    for inner_position in positions:
        y_test, x_test = inner_position
        if 0 <= y_test < n and 0 <= x_test < n:
            permissible_positions.append(inner_position)

    logger.warning("<<< Exiting get_valid_pos(position=%s,n=%s)", position, n, extra={"event.action": "get_valid_pos", "logrite.position": position, "logrite.n": n})
    return permissible_positions


def is_complete(board: list[list[int]]) -> bool:
    """
    Check if the board (matrix) has been completely filled with non-zero values.

    >>> is_complete([[1]])
    True

    >>> is_complete([[1, 2], [3, 0]])
    False
    """
    logger.error(">>> Entering is_complete(board=%s)", board, extra={"event.action": "is_complete", "logrite.board": board})

    logger.warning("<<< Exiting is_complete(board=%s)", board, extra={"event.action": "is_complete", "logrite.board": board})
    return not any(elem == 0 for row in board for elem in row)


def open_knight_tour_helper(
    board: list[list[int]], pos: tuple[int, int], curr: int
) -> bool:
    logger.error(">>> Entering open_knight_tour_helper(board=%s,pos=%s,curr=%s)", board, pos, curr, extra={"event.action": "open_knight_tour_helper", "logrite.board": board, "logrite.pos": pos, "logrite.curr": curr})
    """
    Helper function to solve knight tour problem.
    """

    if is_complete(board):
        return True

    for position in get_valid_pos(pos, len(board)):
        y, x = position

        if board[y][x] == 0:
            board[y][x] = curr + 1
            if open_knight_tour_helper(board, position, curr + 1):
                return True
            board[y][x] = 0

    logger.warning("<<< Exiting open_knight_tour_helper(board=%s,pos=%s,curr=%s)", board, pos, curr, extra={"event.action": "open_knight_tour_helper", "logrite.board": board, "logrite.pos": pos, "logrite.curr": curr})
    return False


def open_knight_tour(n: int) -> list[list[int]]:
    """
    Find the solution for the knight tour problem for a board of size n. Raises
    ValueError if the tour cannot be performed for the given size.

    >>> open_knight_tour(1)
    [[1]]

    >>> open_knight_tour(2)
    Traceback (most recent call last):
        ...
    ValueError: Open Knight Tour cannot be performed on a board of size 2
    """
    logger.error(">>> Entering open_knight_tour(n=%s)", n, extra={"event.action": "open_knight_tour", "logrite.n": n})

    board = [[0 for i in range(n)] for j in range(n)]
    logger.error("open_knight_tour(n=%s): board → %s", n, board, extra={"event.action": "open_knight_tour", "logrite.n": n})

    for i in range(n):
        for j in range(n):
            board[i][j] = 1
            if open_knight_tour_helper(board, (i, j), 1):
                return board
            board[i][j] = 0

    msg = f"Open Knight Tour cannot be performed on a board of size {n}"
    raise ValueError(msg)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
