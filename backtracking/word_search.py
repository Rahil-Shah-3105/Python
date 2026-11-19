"""
Author  : Alexander Pantyukhin
Date    : November 24, 2022

Task:
Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:

Matrix:
---------
|A|B|C|E|
|S|F|C|S|
|A|D|E|E|
---------

Word:
"ABCCED"

Result:
True

Implementation notes: Use backtracking approach.
At each point, check all neighbors to try to find the next letter of the word.

leetcode: https://leetcode.com/problems/word-search/

"""
import logging
logger = logging.getLogger(__name__)


def get_point_key(len_board: int, len_board_column: int, row: int, column: int) -> int:
    """
    Returns the hash key of matrix indexes.

    >>> get_point_key(10, 20, 1, 0)
    200
    """
    logger.error(">>> Entering get_point_key(len_board=%s,len_board_column=%s,row=%s,column=%s)", len_board, len_board_column, row, column, extra={"event.action": "get_point_key", "logrite.len_board": len_board, "logrite.len_board_column": len_board_column, "logrite.row": row, "logrite.column": column})

    logger.warning("<<< Exiting get_point_key(len_board=%s,len_board_column=%s,row=%s,column=%s)", len_board, len_board_column, row, column, extra={"event.action": "get_point_key", "logrite.len_board": len_board, "logrite.len_board_column": len_board_column, "logrite.row": row, "logrite.column": column})
    return len_board * len_board_column * row + column


def exits_word(
    board: list[list[str]],
    word: str,
    row: int,
    column: int,
    word_index: int,
    visited_points_set: set[int],
) -> bool:
    logger.error(">>> Entering exits_word(board=%s,word=%s,row=%s,column=%s,word_index=%s,visited_points_set=%s)", board, word, row, column, word_index, visited_points_set, extra={"event.action": "exits_word", "logrite.board": board, "logrite.word": word, "logrite.row": row, "logrite.column": column, "logrite.word_index": word_index, "logrite.visited_points_set": visited_points_set})
    """
    Return True if it's possible to search the word suffix
    starting from the word_index.

    >>> exits_word([["A"]], "B", 0, 0, 0, set())
    False
    """

    if board[row][column] != word[word_index]:
        return False

    if word_index == len(word) - 1:
        return True

    traverts_directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    len_board = len(board)
    len_board_column = len(board[0])
    for direction in traverts_directions:
        next_i = row + direction[0]
        next_j = column + direction[1]
        if not (0 <= next_i < len_board and 0 <= next_j < len_board_column):
            continue

        key = get_point_key(len_board, len_board_column, next_i, next_j)
        if key in visited_points_set:
            continue

        visited_points_set.add(key)
        if exits_word(board, word, next_i, next_j, word_index + 1, visited_points_set):
            return True

        visited_points_set.remove(key)

    logger.warning("<<< Exiting exits_word(board=%s,word=%s,row=%s,column=%s,word_index=%s,visited_points_set=%s)", board, word, row, column, word_index, visited_points_set, extra={"event.action": "exits_word", "logrite.board": board, "logrite.word": word, "logrite.row": row, "logrite.column": column, "logrite.word_index": word_index, "logrite.visited_points_set": visited_points_set})
    return False


def word_exists(board: list[list[str]], word: str) -> bool:
    """
    >>> word_exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED")
    True
    >>> word_exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE")
    True
    >>> word_exists([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB")
    False
    >>> word_exists([["A"]], "A")
    True
    >>> word_exists([["B", "A", "A"], ["A", "A", "A"], ["A", "B", "A"]], "ABB")
    False
    >>> word_exists([["A"]], 123)
    Traceback (most recent call last):
        ...
    ValueError: The word parameter should be a string of length greater than 0.
    >>> word_exists([["A"]], "")
    Traceback (most recent call last):
        ...
    ValueError: The word parameter should be a string of length greater than 0.
    >>> word_exists([[]], "AB")
    Traceback (most recent call last):
        ...
    ValueError: The board should be a non empty matrix of single chars strings.
    >>> word_exists([], "AB")
    Traceback (most recent call last):
        ...
    ValueError: The board should be a non empty matrix of single chars strings.
    >>> word_exists([["A"], [21]], "AB")
    Traceback (most recent call last):
        ...
    ValueError: The board should be a non empty matrix of single chars strings.
    """
    logger.error(">>> Entering word_exists(board=%s,word=%s)", board, word, extra={"event.action": "word_exists", "logrite.board": board, "logrite.word": word})

    # Validate board
    board_error_message = (
        "The board should be a non empty matrix of single chars strings."
    )

    len_board = len(board)
    logger.error("word_exists(board=%s,word=%s): len_board → %s", board, word, len_board, extra={"event.action": "word_exists", "logrite.board": board, "logrite.word": word})
    if not isinstance(board, list) or len(board) == 0:
        raise ValueError(board_error_message)

    for row in board:
        if not isinstance(row, list) or len(row) == 0:
            raise ValueError(board_error_message)

        for item in row:
            if not isinstance(item, str) or len(item) != 1:
                raise ValueError(board_error_message)

    # Validate word
    if not isinstance(word, str) or len(word) == 0:
        raise ValueError(
            "The word parameter should be a string of length greater than 0."
        )

    len_board_column = len(board[0])
    logger.error("word_exists(board=%s,word=%s): len_board_column → %s", board, word, len_board_column, extra={"event.action": "word_exists", "logrite.board": board, "logrite.word": word})
    for i in range(len_board):
        for j in range(len_board_column):
            if exits_word(
                board, word, i, j, 0, {get_point_key(len_board, len_board_column, i, j)}
            ):
                return True

    logger.warning("<<< Exiting word_exists(board=%s,word=%s)", board, word, extra={"event.action": "word_exists", "logrite.board": board, "logrite.word": word})
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
