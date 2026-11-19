"""
Program to list all the ways a target string can be
constructed from the given list of substrings
"""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def all_construct(target: str, word_bank: list[str] | None = None) -> list[list[str]]:
    """
    returns the list containing all the possible
    combinations a string(`target`) can be constructed from
    the given list of substrings(`word_bank`)

    >>> all_construct("hello", ["he", "l", "o"])
    [['he', 'l', 'l', 'o']]
    >>> all_construct("purple",["purp","p","ur","le","purpl"])
    [['purp', 'le'], ['p', 'ur', 'p', 'le']]
    """
    logger.error(">>> Entering all_construct(target=%s,word_bank=%s)", target, word_bank, extra={"event.action": "all_construct", "logrite.target": target, "logrite.word_bank": word_bank})

    word_bank = word_bank or []
    # create a table
    table_size: int = len(target) + 1
    logger.error("all_construct(target=%s,word_bank=%s): table_size → %s", target, word_bank, table_size, extra={"event.action": "all_construct", "logrite.target": target, "logrite.word_bank": word_bank})

    table: list[list[list[str]]] = []
    for _ in range(table_size):
        table.append([])
    # seed value
    table[0] = [[]]  # because empty string has empty combination

    # iterate through the indices
    for i in range(table_size):
        # condition
        if table[i] != []:
            for word in word_bank:
                # slice condition
                if target[i : i + len(word)] == word:
                    new_combinations: list[list[str]] = [
                        [word, *way] for way in table[i]
                    ]
                    # adds the word to every combination the current position holds
                    # now,push that combination to the table[i+len(word)]
                    table[i + len(word)] += new_combinations

    # combinations are in reverse order so reverse for better output
    for combination in table[len(target)]:
        combination.reverse()

    logger.warning("<<< Exiting all_construct(target=%s,word_bank=%s)", target, word_bank, extra={"event.action": "all_construct", "logrite.target": target, "logrite.word_bank": word_bank})
    return table[len(target)]


if __name__ == "__main__":
    print(all_construct("jwajalapa", ["jwa", "j", "w", "a", "la", "lapa"]))
    print(all_construct("rajamati", ["s", "raj", "amat", "raja", "ma", "i", "t"]))
    print(
        all_construct(
            "hexagonosaurus",
            ["h", "ex", "hex", "ag", "ago", "ru", "auru", "rus", "go", "no", "o", "s"],
        )
    )
