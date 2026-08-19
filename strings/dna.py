import re
import logging
logger = logging.getLogger(__name__)


def dna(dna: str) -> str:
    """
    https://en.wikipedia.org/wiki/DNA
    Returns the second side of a DNA strand

    >>> dna("GCTA")
    'CGAT'
    >>> dna("ATGC")
    'TACG'
    >>> dna("CTGA")
    'GACT'
    >>> dna("GFGG")
    Traceback (most recent call last):
        ...
    ValueError: Invalid Strand
    """
    logger.debug(">>> Entering dna(dna=%s)", dna)

    if len(re.findall("[ATCG]", dna)) != len(dna):
        raise ValueError("Invalid Strand")

    logger.debug("<<< Exiting dna(dna=%s)", dna)
    return dna.translate(dna.maketrans("ATCG", "TAGC"))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
