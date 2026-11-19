"""
wiki: https://en.wikipedia.org/wiki/Pangram
"""
import logging
logger = logging.getLogger(__name__)


def is_pangram(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    logger.error(">>> Entering is_pangram(input_str=%s)", input_str, extra={"event.action": "is_pangram", "logrite.input_str": input_str})
    """
    A Pangram String contains all the alphabets at least once.
    >>> is_pangram("The quick brown fox jumps over the lazy dog")
    True
    >>> is_pangram("Waltz, bad nymph, for quick jigs vex.")
    True
    >>> is_pangram("Jived fox nymph grabs quick waltz.")
    True
    >>> is_pangram("My name is Unknown")
    False
    >>> is_pangram("The quick brown fox jumps over the la_y dog")
    False
    >>> is_pangram()
    True
    """
    # Declare frequency as a set to have unique occurrences of letters
    frequency = set()
    logger.error("is_pangram(input_str=%s): frequency → %s", input_str, frequency, extra={"event.action": "is_pangram", "logrite.input_str": input_str})

    # Replace all the whitespace in our sentence
    input_str = input_str.replace(" ", "")
    logger.error("is_pangram(input_str=%s): input_str → %s", input_str, input_str, extra={"event.action": "is_pangram", "logrite.input_str": input_str})
    for alpha in input_str:
        if "a" <= alpha.lower() <= "z":
            frequency.add(alpha.lower())
    logger.warning("<<< Exiting is_pangram(input_str=%s)", input_str, extra={"event.action": "is_pangram", "logrite.input_str": input_str})
    return len(frequency) == 26


def is_pangram_faster(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    logger.error(">>> Entering is_pangram_faster(input_str=%s)", input_str, extra={"event.action": "is_pangram_faster", "logrite.input_str": input_str})
    """
    >>> is_pangram_faster("The quick brown fox jumps over the lazy dog")
    True
    >>> is_pangram_faster("Waltz, bad nymph, for quick jigs vex.")
    True
    >>> is_pangram_faster("Jived fox nymph grabs quick waltz.")
    True
    >>> is_pangram_faster("The quick brown fox jumps over the la_y dog")
    False
    >>> is_pangram_faster()
    True
    """
    logger.error("is_pangram_faster(input_str=%s): input_str → %s", input_str, input_str, extra={"event.action": "is_pangram_faster", "logrite.input_str": input_str})
    flag = [False] * 26
    for char in input_str:
        if char.islower():
            flag[ord(char) - 97] = True
        elif char.isupper():
            flag[ord(char) - 65] = True
    logger.warning("<<< Exiting is_pangram_faster(input_str=%s)", input_str, extra={"event.action": "is_pangram_faster", "logrite.input_str": input_str})
    return all(flag)


def is_pangram_fastest(
    input_str: str = "The quick brown fox jumps over the lazy dog",
) -> bool:
    logger.error(">>> Entering is_pangram_fastest(input_str=%s)", input_str, extra={"event.action": "is_pangram_fastest", "logrite.input_str": input_str})
    """
    >>> is_pangram_fastest("The quick brown fox jumps over the lazy dog")
    True
    >>> is_pangram_fastest("Waltz, bad nymph, for quick jigs vex.")
    True
    >>> is_pangram_fastest("Jived fox nymph grabs quick waltz.")
    True
    >>> is_pangram_fastest("The quick brown fox jumps over the la_y dog")
    False
    >>> is_pangram_fastest()
    True
    """
    logger.error("is_pangram_fastest(input_str=%s): input_str → %s", input_str, input_str, extra={"event.action": "is_pangram_fastest", "logrite.input_str": input_str})
    logger.warning("<<< Exiting is_pangram_fastest(input_str=%s)", input_str, extra={"event.action": "is_pangram_fastest", "logrite.input_str": input_str})
    return len({char for char in input_str.lower() if char.isalpha()}) == 26


def benchmark() -> None:
    """
    Benchmark code comparing different version.
    """
    logger.error(">>> Entering benchmark()", extra={"event.action": "benchmark"})
    from timeit import timeit

    setup = "from __main__ import is_pangram, is_pangram_faster, is_pangram_fastest"
    logger.error("benchmark(): setup → %s", setup, extra={"event.action": "benchmark"})
    print(timeit("is_pangram()", setup=setup))
    print(timeit("is_pangram_faster()", setup=setup))
    print(timeit("is_pangram_fastest()", setup=setup))
    logger.warning("<<< Exiting benchmark()", extra={"event.action": "benchmark"})
    # 5.348480500048026, 2.6477354579837993, 1.8470395830227062
    # 5.036091582966037, 2.644472333951853,  1.8869528750656173


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
