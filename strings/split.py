import logging
logger = logging.getLogger(__name__)
def split(string: str, separator: str = " ") -> list:
    """
    Will split the string up into all the values separated by the separator
    (defaults to spaces)

    >>> split("apple#banana#cherry#orange",separator='#')
    ['apple', 'banana', 'cherry', 'orange']

    >>> split("Hello there")
    ['Hello', 'there']

    >>> split("11/22/63",separator = '/')
    ['11', '22', '63']

    >>> split("12:43:39",separator = ":")
    ['12', '43', '39']

    >>> split(";abbb;;c;", separator=';')
    ['', 'abbb', '', 'c', '']
    """
    logger.debug(">>> Entering split(string=%s,separator=%s)", string, separator)

    split_words = []
    logger.debug("split(string=%s,separator=%s): split_words → %s", string, separator, split_words)

    last_index = 0
    logger.debug("split(string=%s,separator=%s): last_index → %s", string, separator, last_index)
    for index, char in enumerate(string):
        if char == separator:
            split_words.append(string[last_index:index])
            last_index = index + 1
        if index + 1 == len(string):
            split_words.append(string[last_index : index + 1])
    logger.debug("<<< Exiting split(string=%s,separator=%s)", string, separator)
    return split_words


if __name__ == "__main__":
    from doctest import testmod

    testmod()
