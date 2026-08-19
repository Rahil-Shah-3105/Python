import logging
logger = logging.getLogger(__name__)
"""
wiki: https://en.wikipedia.org/wiki/Heterogram_(literature)#Isograms
"""


def is_isogram(string: str) -> bool:
    """
    An isogram is a word in which no letter is repeated.
    Examples of isograms are uncopyrightable and ambidextrously.
    >>> is_isogram('Uncopyrightable')
    True
    >>> is_isogram('allowance')
    False
    >>> is_isogram('copy1')
    Traceback (most recent call last):
     ...
    ValueError: String must only contain alphabetic characters.
    """
    logger.debug(">>> Entering is_isogram(string=%s)", string)
    if not all(x.isalpha() for x in string):
        raise ValueError("String must only contain alphabetic characters.")

    letters = sorted(string.lower())
    logger.debug("is_isogram(string=%s): letters → %s", string, letters)
    logger.debug("<<< Exiting is_isogram(string=%s)", string)
    return len(letters) == len(set(letters))


if __name__ == "__main__":
    input_str = input("Enter a string ").strip()

    isogram = is_isogram(input_str)
    print(f"{input_str} is {'an' if isogram else 'not an'} isogram.")
