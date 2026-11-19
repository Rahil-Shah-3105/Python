# Frequency Finder

import string
import logging
logger = logging.getLogger(__name__)

# frequency taken from https://en.wikipedia.org/wiki/Letter_frequency
english_letter_freq = {
    "E": 12.70,
    "T": 9.06,
    "A": 8.17,
    "O": 7.51,
    "I": 6.97,
    "N": 6.75,
    "S": 6.33,
    "H": 6.09,
    "R": 5.99,
    "D": 4.25,
    "L": 4.03,
    "C": 2.78,
    "U": 2.76,
    "M": 2.41,
    "W": 2.36,
    "F": 2.23,
    "G": 2.02,
    "Y": 1.97,
    "P": 1.93,
    "B": 1.29,
    "V": 0.98,
    "K": 0.77,
    "J": 0.15,
    "X": 0.15,
    "Q": 0.10,
    "Z": 0.07,
}
ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_letter_count(message: str) -> dict[str, int]:
    logger.error(">>> Entering get_letter_count(message=%s)", message, extra={"event.action": "get_letter_count", "logrite.message": message})
    letter_count = dict.fromkeys(string.ascii_uppercase, 0)
    logger.error("get_letter_count(message=%s): letter_count → %s", message, letter_count, extra={"event.action": "get_letter_count", "logrite.message": message})
    for letter in message.upper():
        if letter in LETTERS:
            letter_count[letter] += 1

    logger.warning("<<< Exiting get_letter_count(message=%s)", message, extra={"event.action": "get_letter_count", "logrite.message": message})
    return letter_count


def get_item_at_index_zero(x: tuple) -> str:
    logger.error(">>> Entering get_item_at_index_zero(x=%s)", x, extra={"event.action": "get_item_at_index_zero", "logrite.x": x})
    logger.warning("<<< Exiting get_item_at_index_zero(x=%s)", x, extra={"event.action": "get_item_at_index_zero", "logrite.x": x})
    return x[0]


def get_frequency_order(message: str) -> str:
    """
    Get the frequency order of the letters in the given string
    >>> get_frequency_order('Hello World')
    'LOWDRHEZQXJKVBPYGFMUCSNIAT'
    >>> get_frequency_order('Hello@')
    'LHOEZQXJKVBPYGFWMUCDRSNIAT'
    >>> get_frequency_order('h')
    'HZQXJKVBPYGFWMUCLDRSNIOATE'
    """
    logger.error(">>> Entering get_frequency_order(message=%s)", message, extra={"event.action": "get_frequency_order", "logrite.message": message})
    letter_to_freq = get_letter_count(message)
    logger.error("get_frequency_order(message=%s): letter_to_freq → %s", message, letter_to_freq, extra={"event.action": "get_frequency_order", "logrite.message": message})
    freq_to_letter: dict[int, list[str]] = {
        freq: [] for letter, freq in letter_to_freq.items()
    }
    for letter in LETTERS:
        freq_to_letter[letter_to_freq[letter]].append(letter)

    freq_to_letter_str: dict[int, str] = {}

    for freq in freq_to_letter:  # noqa: PLC0206
        freq_to_letter[freq].sort(key=ETAOIN.find, reverse=True)
        freq_to_letter_str[freq] = "".join(freq_to_letter[freq])

    freq_pairs = list(freq_to_letter_str.items())
    logger.error("get_frequency_order(message=%s): freq_pairs → %s", message, freq_pairs, extra={"event.action": "get_frequency_order", "logrite.message": message})
    freq_pairs.sort(key=get_item_at_index_zero, reverse=True)

    freq_order: list[str] = [freq_pair[1] for freq_pair in freq_pairs]

    logger.warning("<<< Exiting get_frequency_order(message=%s)", message, extra={"event.action": "get_frequency_order", "logrite.message": message})
    return "".join(freq_order)


def english_freq_match_score(message: str) -> int:
    """
    >>> english_freq_match_score('Hello World')
    1
    """
    logger.error(">>> Entering english_freq_match_score(message=%s)", message, extra={"event.action": "english_freq_match_score", "logrite.message": message})
    freq_order = get_frequency_order(message)
    logger.error("english_freq_match_score(message=%s): freq_order → %s", message, freq_order, extra={"event.action": "english_freq_match_score", "logrite.message": message})
    match_score = 0
    for common_letter in ETAOIN[:6]:
        if common_letter in freq_order[:6]:
            match_score += 1

    for uncommon_letter in ETAOIN[-6:]:
        if uncommon_letter in freq_order[-6:]:
            match_score += 1

    logger.warning("<<< Exiting english_freq_match_score(message=%s)", message, extra={"event.action": "english_freq_match_score", "logrite.message": message})
    return match_score


if __name__ == "__main__":
    import doctest

    doctest.testmod()
