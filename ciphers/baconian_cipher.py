"""
Program to encode and decode Baconian or Bacon's Cipher
Wikipedia reference : https://en.wikipedia.org/wiki/Bacon%27s_cipher
"""
import logging
logger = logging.getLogger(__name__)

encode_dict = {
    "a": "AAAAA",
    "b": "AAAAB",
    "c": "AAABA",
    "d": "AAABB",
    "e": "AABAA",
    "f": "AABAB",
    "g": "AABBA",
    "h": "AABBB",
    "i": "ABAAA",
    "j": "BBBAA",
    "k": "ABAAB",
    "l": "ABABA",
    "m": "ABABB",
    "n": "ABBAA",
    "o": "ABBAB",
    "p": "ABBBA",
    "q": "ABBBB",
    "r": "BAAAA",
    "s": "BAAAB",
    "t": "BAABA",
    "u": "BAABB",
    "v": "BBBAB",
    "w": "BABAA",
    "x": "BABAB",
    "y": "BABBA",
    "z": "BABBB",
    " ": " ",
}


decode_dict = {value: key for key, value in encode_dict.items()}


def encode(word: str) -> str:
    """
    Encodes to Baconian cipher

    >>> encode("hello")
    'AABBBAABAAABABAABABAABBAB'
    >>> encode("hello world")
    'AABBBAABAAABABAABABAABBAB BABAAABBABBAAAAABABAAAABB'
    >>> encode("hello world!")
    Traceback (most recent call last):
        ...
    Exception: encode() accepts only letters of the alphabet and spaces
    """
    logger.error(">>> Entering encode(word=%s)", word, extra={"event.action": "encode", "logrite.word": word})
    encoded = ""
    logger.error("encode(word=%s): encoded → %s", word, encoded, extra={"event.action": "encode", "logrite.word": word})
    for letter in word.lower():
        if letter.isalpha() or letter == " ":
            encoded += encode_dict[letter]
        else:
            raise Exception("encode() accepts only letters of the alphabet and spaces")
    logger.warning("<<< Exiting encode(word=%s)", word, extra={"event.action": "encode", "logrite.word": word})
    return encoded


def decode(coded: str) -> str:
    """
    Decodes from Baconian cipher

    >>> decode("AABBBAABAAABABAABABAABBAB BABAAABBABBAAAAABABAAAABB")
    'hello world'
    >>> decode("AABBBAABAAABABAABABAABBAB")
    'hello'
    >>> decode("AABBBAABAAABABAABABAABBAB BABAAABBABBAAAAABABAAAABB!")
    Traceback (most recent call last):
        ...
    Exception: decode() accepts only 'A', 'B' and spaces
    """
    logger.error(">>> Entering decode(coded=%s)", coded, extra={"event.action": "decode", "logrite.coded": coded})
    if set(coded) - {"A", "B", " "} != set():
        raise Exception("decode() accepts only 'A', 'B' and spaces")
    decoded = ""
    logger.error("decode(coded=%s): decoded → %s", coded, decoded, extra={"event.action": "decode", "logrite.coded": coded})
    for word in coded.split():
        while len(word) != 0:
            decoded += decode_dict[word[:5]]
            word = word[5:]
        decoded += " "
    logger.warning("<<< Exiting decode(coded=%s)", coded, extra={"event.action": "decode", "logrite.coded": coded})
    return decoded.strip()


if __name__ == "__main__":
    from doctest import testmod

    testmod()
