"""
Convert a string of characters to a sequence of numbers
corresponding to the character's position in the alphabet.

https://www.dcode.fr/letter-number-cipher
http://bestcodes.weebly.com/a1z26.html
"""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def encode(plain: str) -> list[int]:
    """
    >>> encode("myname")
    [13, 25, 14, 1, 13, 5]
    >>> encode("abCd")
    Traceback (most recent call last):
        ...
    ValueError: plain must contain only lowercase letters (a-z)
    >>> encode("n0w")
    Traceback (most recent call last):
        ...
    ValueError: plain must contain only lowercase letters (a-z)
    >>> encode("later!")
    Traceback (most recent call last):
        ...
    ValueError: plain must contain only lowercase letters (a-z)
    """
    logger.debug(">>> Entering encode(plain=%s)", plain)
    if not plain.islower() or not plain.isalpha():
        raise ValueError("plain must contain only lowercase letters (a-z)")
    logger.debug("<<< Exiting encode(plain=%s)", plain)
    return [ord(elem) - 96 for elem in plain]


def decode(encoded: list[int]) -> str:
    """
    >>> decode([13, 25, 14, 1, 13, 5])
    'myname'
    """
    logger.debug(">>> Entering decode(encoded=%s)", encoded)
    logger.debug("<<< Exiting decode(encoded=%s)", encoded)
    return "".join(chr(elem + 96) for elem in encoded)


def main() -> None:
    logger.debug(">>> Entering main()")
    encoded = encode(input("-> ").strip().lower())
    logger.debug("main(): encoded → %s", encoded)
    print("Encoded: ", encoded)
    print("Decoded:", decode(encoded))
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    main()
