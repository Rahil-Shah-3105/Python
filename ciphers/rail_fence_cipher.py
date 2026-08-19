import logging
logger = logging.getLogger(__name__)
"""https://en.wikipedia.org/wiki/Rail_fence_cipher"""


def encrypt(input_string: str, key: int) -> str:
    """
    Shuffles the character of a string by placing each of them
    in a grid (the height is dependent on the key) in a zigzag
    formation and reading it left to right.

    >>> encrypt("Hello World", 4)
    'HWe olordll'

    >>> encrypt("This is a message", 0)
    Traceback (most recent call last):
        ...
    ValueError: Height of grid can't be 0 or negative

    >>> encrypt(b"This is a byte string", 5)
    Traceback (most recent call last):
        ...
    TypeError: sequence item 0: expected str instance, int found
    """
    logger.debug(">>> Entering encrypt(input_string=%s,key=%s)", input_string, key)
    temp_grid: list[list[str]] = [[] for _ in range(key)]
    lowest = key - 1
    logger.debug("encrypt(input_string=%s,key=%s): lowest → %s", input_string, key, lowest)

    if key <= 0:
        raise ValueError("Height of grid can't be 0 or negative")
    if key == 1 or len(input_string) <= key:
        return input_string

    for position, character in enumerate(input_string):
        num = position % (lowest * 2)  # puts it in bounds
        num = min(num, lowest * 2 - num)  # creates zigzag pattern
        logger.debug("encrypt(input_string=%s,key=%s): num → %s", input_string, key, num)
        temp_grid[num].append(character)
    grid = ["".join(row) for row in temp_grid]
    logger.debug("encrypt(input_string=%s,key=%s): grid → %s", input_string, key, grid)
    output_string = "".join(grid)
    logger.debug("encrypt(input_string=%s,key=%s): output_string → %s", input_string, key, output_string)

    logger.debug("<<< Exiting encrypt(input_string=%s,key=%s)", input_string, key)
    return output_string


def decrypt(input_string: str, key: int) -> str:
    """
    Generates a template based on the key and fills it in with
    the characters of the input string and then reading it in
    a zigzag formation.

    >>> decrypt("HWe olordll", 4)
    'Hello World'

    >>> decrypt("This is a message", -10)
    Traceback (most recent call last):
        ...
    ValueError: Height of grid can't be 0 or negative

    >>> decrypt("My key is very big", 100)
    'My key is very big'
    """
    logger.debug(">>> Entering decrypt(input_string=%s,key=%s)", input_string, key)
    grid = []
    logger.debug("decrypt(input_string=%s,key=%s): grid → %s", input_string, key, grid)
    lowest = key - 1
    logger.debug("decrypt(input_string=%s,key=%s): lowest → %s", input_string, key, lowest)

    if key <= 0:
        raise ValueError("Height of grid can't be 0 or negative")
    if key == 1:
        return input_string

    temp_grid: list[list[str]] = [[] for _ in range(key)]  # generates template
    for position in range(len(input_string)):
        num = position % (lowest * 2)  # puts it in bounds
        num = min(num, lowest * 2 - num)  # creates zigzag pattern
        logger.debug("decrypt(input_string=%s,key=%s): num → %s", input_string, key, num)
        temp_grid[num].append("*")

    counter = 0
    logger.debug("decrypt(input_string=%s,key=%s): counter → %s", input_string, key, counter)
    for row in temp_grid:  # fills in the characters
        splice = input_string[counter : counter + len(row)]
        logger.debug("decrypt(input_string=%s,key=%s): splice → %s", input_string, key, splice)
        grid.append(list(splice))
        counter += len(row)

    output_string = ""  # reads as zigzag
    logger.debug("decrypt(input_string=%s,key=%s): output_string → %s", input_string, key, output_string)
    for position in range(len(input_string)):
        num = position % (lowest * 2)  # puts it in bounds
        num = min(num, lowest * 2 - num)  # creates zigzag pattern
        output_string += grid[num][0]
        grid[num].pop(0)
    logger.debug("<<< Exiting decrypt(input_string=%s,key=%s)", input_string, key)
    return output_string


def bruteforce(input_string: str) -> dict[int, str]:
    """Uses decrypt function by guessing every key

    >>> bruteforce("HWe olordll")[4]
    'Hello World'
    """
    logger.debug(">>> Entering bruteforce(input_string=%s)", input_string)
    results = {}
    logger.debug("bruteforce(input_string=%s): results → %s", input_string, results)
    for key_guess in range(1, len(input_string)):  # tries every key
        results[key_guess] = decrypt(input_string, key_guess)
    logger.debug("<<< Exiting bruteforce(input_string=%s)", input_string)
    return results


if __name__ == "__main__":
    import doctest

    doctest.testmod()
