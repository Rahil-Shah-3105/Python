import logging
logger = logging.getLogger(__name__)
# https://www.geeksforgeeks.org/solve-crossword-puzzle/


def is_valid(
    puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool
) -> bool:
    logger.error(">>> Entering is_valid(puzzle=%s,word=%s,row=%s,col=%s,vertical=%s)", puzzle, word, row, col, vertical, extra={"event.action": "is_valid", "logrite.puzzle": puzzle, "logrite.word": word, "logrite.row": row, "logrite.col": col, "logrite.vertical": vertical})
    """
    Check if a word can be placed at the given position.

    >>> puzzle = [
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', '']
    ... ]
    >>> is_valid(puzzle, 'word', 0, 0, True)
    True
    >>> puzzle = [
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', '']
    ... ]
    >>> is_valid(puzzle, 'word', 0, 0, False)
    True
    """
    for i in range(len(word)):
        if vertical:
            if row + i >= len(puzzle) or puzzle[row + i][col] != "":
                return False
        elif col + i >= len(puzzle[0]) or puzzle[row][col + i] != "":
            return False
    logger.warning("<<< Exiting is_valid(puzzle=%s,word=%s,row=%s,col=%s,vertical=%s)", puzzle, word, row, col, vertical, extra={"event.action": "is_valid", "logrite.puzzle": puzzle, "logrite.word": word, "logrite.row": row, "logrite.col": col, "logrite.vertical": vertical})
    return True


def place_word(
    puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool
) -> None:
    logger.error(">>> Entering place_word(puzzle=%s,word=%s,row=%s,col=%s,vertical=%s)", puzzle, word, row, col, vertical, extra={"event.action": "place_word", "logrite.puzzle": puzzle, "logrite.word": word, "logrite.row": row, "logrite.col": col, "logrite.vertical": vertical})
    """
    Place a word at the given position.

    >>> puzzle = [
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', '']
    ... ]
    >>> place_word(puzzle, 'word', 0, 0, True)
    >>> puzzle
    [['w', '', '', ''], ['o', '', '', ''], ['r', '', '', ''], ['d', '', '', '']]
    """
    for i, char in enumerate(word):
        if vertical:
            puzzle[row + i][col] = char
        else:
            puzzle[row][col + i] = char
            logger.warning("<<< Exiting place_word(puzzle=%s,word=%s,row=%s,col=%s,vertical=%s)", puzzle, word, row, col, vertical, extra={"event.action": "place_word", "logrite.puzzle": puzzle, "logrite.word": word, "logrite.row": row, "logrite.col": col, "logrite.vertical": vertical})


def remove_word(
    puzzle: list[list[str]], word: str, row: int, col: int, vertical: bool
) -> None:
    logger.error(">>> Entering remove_word(puzzle=%s,word=%s,row=%s,col=%s,vertical=%s)", puzzle, word, row, col, vertical, extra={"event.action": "remove_word", "logrite.puzzle": puzzle, "logrite.word": word, "logrite.row": row, "logrite.col": col, "logrite.vertical": vertical})
    """
    Remove a word from the given position.

    >>> puzzle = [
    ...     ['w', '', '', ''],
    ...     ['o', '', '', ''],
    ...     ['r', '', '', ''],
    ...     ['d', '', '', '']
    ... ]
    >>> remove_word(puzzle, 'word', 0, 0, True)
    >>> puzzle
    [['', '', '', ''], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']]
    """
    for i in range(len(word)):
        if vertical:
            puzzle[row + i][col] = ""
        else:
            puzzle[row][col + i] = ""
            logger.warning("<<< Exiting remove_word(puzzle=%s,word=%s,row=%s,col=%s,vertical=%s)", puzzle, word, row, col, vertical, extra={"event.action": "remove_word", "logrite.puzzle": puzzle, "logrite.word": word, "logrite.row": row, "logrite.col": col, "logrite.vertical": vertical})


def solve_crossword(puzzle: list[list[str]], words: list[str]) -> bool:
    """
    Solve the crossword puzzle using backtracking.

    >>> puzzle = [
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', '']
    ... ]

    >>> words = ['word', 'four', 'more', 'last']
    >>> solve_crossword(puzzle, words)
    True
    >>> puzzle = [
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', ''],
    ...     ['', '', '', '']
    ... ]
    >>> words = ['word', 'four', 'more', 'paragraphs']
    >>> solve_crossword(puzzle, words)
    False
    """
    logger.error(">>> Entering solve_crossword(puzzle=%s,words=%s)", puzzle, words, extra={"event.action": "solve_crossword", "logrite.puzzle": puzzle, "logrite.words": words})
    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            if puzzle[row][col] == "":
                for word in words:
                    for vertical in [True, False]:
                        if is_valid(puzzle, word, row, col, vertical):
                            place_word(puzzle, word, row, col, vertical)
                            words.remove(word)
                            if solve_crossword(puzzle, words):
                                return True
                            words.append(word)
                            remove_word(puzzle, word, row, col, vertical)
                return False
    logger.warning("<<< Exiting solve_crossword(puzzle=%s,words=%s)", puzzle, words, extra={"event.action": "solve_crossword", "logrite.puzzle": puzzle, "logrite.words": words})
    return True


if __name__ == "__main__":
    PUZZLE = [[""] * 3 for _ in range(3)]
    WORDS = ["cat", "dog", "car"]

    if solve_crossword(PUZZLE, WORDS):
        print("Solution found:")
        for row in PUZZLE:
            print(" ".join(row))
    else:
        print("No solution found:")
