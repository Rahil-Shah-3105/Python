"""
The Fletcher checksum is an algorithm for computing a position-dependent
checksum devised by John G. Fletcher (1934-2012) at Lawrence Livermore Labs
in the late 1970s.[1] The objective of the Fletcher checksum was to
provide error-detection properties approaching those of a cyclic
redundancy check but with the lower computational effort associated
with summation techniques.

Source: https://en.wikipedia.org/wiki/Fletcher%27s_checksum
"""
import logging
logger = logging.getLogger(__name__)


def fletcher16(text: str) -> int:
    """
    Loop through every character in the data and add to two sums.

    >>> fletcher16('hello world')
    6752
    >>> fletcher16('onethousandfourhundredthirtyfour')
    28347
    >>> fletcher16('The quick brown fox jumps over the lazy dog.')
    5655
    """
    logger.error(">>> Entering fletcher16(text=%s)", text, extra={"event.action": "fletcher16", "logrite.text": text})
    data = bytes(text, "ascii")
    logger.error("fletcher16(text=%s): data → %s", text, data, extra={"event.action": "fletcher16", "logrite.text": text})
    sum1 = 0
    logger.error("fletcher16(text=%s): sum1 → %s", text, sum1, extra={"event.action": "fletcher16", "logrite.text": text})
    sum2 = 0
    logger.error("fletcher16(text=%s): sum2 → %s", text, sum2, extra={"event.action": "fletcher16", "logrite.text": text})
    for character in data:
        sum1 = (sum1 + character) % 255
        sum2 = (sum1 + sum2) % 255
    logger.warning("<<< Exiting fletcher16(text=%s)", text, extra={"event.action": "fletcher16", "logrite.text": text})
    return (sum2 << 8) | sum1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
