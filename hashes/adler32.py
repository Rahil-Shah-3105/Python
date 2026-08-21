import logging
logger = logging.getLogger(__name__)
"""
Adler-32 is a checksum algorithm which was invented by Mark Adler in 1995.
Compared to a cyclic redundancy check of the same length, it trades reliability for
speed (preferring the latter).
Adler-32 is more reliable than Fletcher-16, and slightly less reliable than
Fletcher-32.[2]

source: https://en.wikipedia.org/wiki/Adler-32
"""

MOD_ADLER = 65521


def adler32(plain_text: str) -> int:
    """
    Function implements adler-32 hash.
    Iterates and evaluates a new value for each character

    >>> adler32('Algorithms')
    363791387

    >>> adler32('go adler em all')
    708642122
    """
    logger.debug(">>> Entering adler32(plain_text=%s)", plain_text)
    a = 1
    logger.debug("adler32(plain_text=%s): a → %s", plain_text, a)
    b = 0
    logger.debug("adler32(plain_text=%s): b → %s", plain_text, b)
    for plain_chr in plain_text:
        a = (a + ord(plain_chr)) % MOD_ADLER
        b = (b + a) % MOD_ADLER
    logger.debug("<<< Exiting adler32(plain_text=%s)", plain_text)
    return (b << 16) | a
