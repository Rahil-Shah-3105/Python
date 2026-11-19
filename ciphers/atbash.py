"""https://en.wikipedia.org/wiki/Atbash"""

import string
import logging
logger = logging.getLogger(__name__)


def atbash_slow(sequence: str) -> str:
    """
    >>> atbash_slow("ABCDEFG")
    'ZYXWVUT'

    >>> atbash_slow("aW;;123BX")
    'zD;;123YC'
    """
    logger.error(">>> Entering atbash_slow(sequence=%s)", sequence, extra={"event.action": "atbash_slow", "logrite.sequence": sequence})
    output = ""
    logger.error("atbash_slow(sequence=%s): output → %s", sequence, output, extra={"event.action": "atbash_slow", "logrite.sequence": sequence})
    for i in sequence:
        extract = ord(i)
        logger.error("atbash_slow(sequence=%s): extract → %s", sequence, extract, extra={"event.action": "atbash_slow", "logrite.sequence": sequence})
        if 65 <= extract <= 90:
            output += chr(155 - extract)
        elif 97 <= extract <= 122:
            output += chr(219 - extract)
        else:
            output += i
    logger.warning("<<< Exiting atbash_slow(sequence=%s)", sequence, extra={"event.action": "atbash_slow", "logrite.sequence": sequence})
    return output


def atbash(sequence: str) -> str:
    """
    >>> atbash("ABCDEFG")
    'ZYXWVUT'

    >>> atbash("aW;;123BX")
    'zD;;123YC'
    """
    logger.error(">>> Entering atbash(sequence=%s)", sequence, extra={"event.action": "atbash", "logrite.sequence": sequence})
    letters = string.ascii_letters
    letters_reversed = string.ascii_lowercase[::-1] + string.ascii_uppercase[::-1]
    logger.warning("<<< Exiting atbash(sequence=%s)", sequence, extra={"event.action": "atbash", "logrite.sequence": sequence})
    return "".join(
        letters_reversed[letters.index(c)] if c in letters else c for c in sequence
    )


def benchmark() -> None:
    """Let's benchmark our functions side-by-side..."""
    logger.error(">>> Entering benchmark()", extra={"event.action": "benchmark"})
    from timeit import timeit

    print("Running performance benchmarks...")
    setup = "from string import printable ; from __main__ import atbash, atbash_slow"
    logger.error("benchmark(): setup → %s", setup, extra={"event.action": "benchmark"})
    print(f"> atbash_slow(): {timeit('atbash_slow(printable)', setup=setup)} seconds")
    print(f">      atbash(): {timeit('atbash(printable)', setup=setup)} seconds")
    logger.warning("<<< Exiting benchmark()", extra={"event.action": "benchmark"})


if __name__ == "__main__":
    for example in ("ABCDEFGH", "123GGjj", "testStringtest", "with space"):
        print(f"{example} encrypted in atbash: {atbash(example)}")
    benchmark()
