"""
https://en.wikipedia.org/wiki/Playfair_cipher#Description

The Playfair cipher was developed by Charles Wheatstone in 1854
It's use was heavily promotedby Lord Playfair, hence its name

Some features of the Playfair cipher are:

1) It was the first literal diagram substitution cipher
2) It is a manual symmetric encryption technique
3) It is a multiple letter encryption cipher

The implementation in the code below encodes alphabets only.
It removes spaces, special characters and numbers from the
code.

Playfair is no longer used by military forces because of known
insecurities and of the advent of automated encryption devices.
This cipher is regarded as insecure since before World War I.
"""

import itertools
import string
from collections.abc import Generator, Iterable
import logging
logger = logging.getLogger(__name__)


def chunker(seq: Iterable[str], size: int) -> Generator[tuple[str, ...]]:
    logger.debug(">>> Entering chunker(seq=%s,size=%s)", seq, size)
    it = iter(seq)
    logger.debug("chunker(seq=%s,size=%s): it → %s", seq, size, it)
    while True:
        chunk = tuple(itertools.islice(it, size))
        logger.debug("chunker(seq=%s,size=%s): chunk → %s", seq, size, chunk)
        if not chunk:
            logger.debug("<<< Exiting chunker(seq=%s,size=%s)", seq, size)
            return
        yield chunk


def prepare_input(dirty: str) -> str:
    """
    Prepare the plaintext by up-casing it
    and separating repeated letters with X's
    """
    logger.debug(">>> Entering prepare_input(dirty=%s)", dirty)

    dirty = "".join([c.upper() for c in dirty if c in string.ascii_letters])
    logger.debug("prepare_input(dirty=%s): dirty → %s", dirty, dirty)
    clean = ""
    logger.debug("prepare_input(dirty=%s): clean → %s", dirty, clean)

    if len(dirty) < 2:
        return dirty

    for i in range(len(dirty) - 1):
        clean += dirty[i]

        if dirty[i] == dirty[i + 1]:
            clean += "X"

    clean += dirty[-1]

    if len(clean) & 1:
        clean += "X"

    logger.debug("<<< Exiting prepare_input(dirty=%s)", dirty)
    return clean


def generate_table(key: str) -> list[str]:
    logger.debug(">>> Entering generate_table(key=%s)", key)
    # I and J are used interchangeably to allow
    # us to use a 5x5 table (25 letters)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    logger.debug("generate_table(key=%s): alphabet → %s", key, alphabet)
    # we're using a list instead of a '2d' array because it makes the math
    # for setting up the table and doing the actual encoding/decoding simpler
    table = []
    logger.debug("generate_table(key=%s): table → %s", key, table)

    # copy key chars into the table if they are in `alphabet` ignoring duplicates
    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)

    # fill the rest of the table in with the remaining alphabet chars
    for char in alphabet:
        if char not in table:
            table.append(char)

    logger.debug("<<< Exiting generate_table(key=%s)", key)
    return table


def encode(plaintext: str, key: str) -> str:
    """
    Encode the given plaintext using the Playfair cipher.
    Takes the plaintext and the key as input and returns the encoded string.

    >>> encode("Hello", "MONARCHY")
    'CFSUPM'
    >>> encode("attack on the left flank", "EMERGENCY")
    'DQZSBYFSDZFMFNLOHFDRSG'
    >>> encode("Sorry!", "SPECIAL")
    'AVXETX'
    >>> encode("Number 1", "NUMBER")
    'UMBENF'
    >>> encode("Photosynthesis!", "THE SUN")
    'OEMHQHVCHESUKE'
    """
    logger.debug(">>> Entering encode(plaintext=%s,key=%s)", plaintext, key)

    table = generate_table(key)
    logger.debug("encode(plaintext=%s,key=%s): table → %s", plaintext, key, table)
    plaintext = prepare_input(plaintext)
    logger.debug("encode(plaintext=%s,key=%s): plaintext → %s", plaintext, key, plaintext)
    ciphertext = ""
    logger.debug("encode(plaintext=%s,key=%s): ciphertext → %s", plaintext, key, ciphertext)

    for char1, char2 in chunker(plaintext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            ciphertext += table[row1 * 5 + (col1 + 1) % 5]
            ciphertext += table[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += table[((row1 + 1) % 5) * 5 + col1]
            ciphertext += table[((row2 + 1) % 5) * 5 + col2]
        else:  # rectangle
            ciphertext += table[row1 * 5 + col2]
            ciphertext += table[row2 * 5 + col1]

    logger.debug("<<< Exiting encode(plaintext=%s,key=%s)", plaintext, key)
    return ciphertext


def decode(ciphertext: str, key: str) -> str:
    """
    Decode the input string using the provided key.

    >>> decode("BMZFAZRZDH", "HAZARD")
    'FIREHAZARD'
    >>> decode("HNBWBPQT", "AUTOMOBILE")
    'DRIVINGX'
    >>> decode("SLYSSAQS", "CASTLE")
    'ATXTACKX'
    """
    logger.debug(">>> Entering decode(ciphertext=%s,key=%s)", ciphertext, key)

    table = generate_table(key)
    logger.debug("decode(ciphertext=%s,key=%s): table → %s", ciphertext, key, table)
    plaintext = ""
    logger.debug("decode(ciphertext=%s,key=%s): plaintext → %s", ciphertext, key, plaintext)

    for char1, char2 in chunker(ciphertext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            plaintext += table[row1 * 5 + (col1 - 1) % 5]
            plaintext += table[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += table[((row1 - 1) % 5) * 5 + col1]
            plaintext += table[((row2 - 1) % 5) * 5 + col2]
        else:  # rectangle
            plaintext += table[row1 * 5 + col2]
            plaintext += table[row2 * 5 + col1]

    logger.debug("<<< Exiting decode(ciphertext=%s,key=%s)", ciphertext, key)
    return plaintext


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Encoded:", encode("BYE AND THANKS", "GREETING"))
    print("Decoded:", decode("CXRBANRLBALQ", "GREETING"))
