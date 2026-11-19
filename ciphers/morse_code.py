#!/usr/bin/env python3

"""
Python program to translate to and from Morse code.

https://en.wikipedia.org/wiki/Morse_code
"""
import logging
logger = logging.getLogger(__name__)

# fmt: off
MORSE_CODE_DICT = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "0": "-----", "&": ".-...", "@": ".--.-.",
    ":": "---...", ",": "--..--", ".": ".-.-.-", "'": ".----.", '"': ".-..-.",
    "?": "..--..", "/": "-..-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "(": "-.--.", ")": "-.--.-", "!": "-.-.--", " ": "/"
}  # Exclamation mark is not in ITU-R recommendation
# fmt: on
REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def encrypt(message: str) -> str:
    """
    >>> encrypt("Sos!")
    '... --- ... -.-.--'
    >>> encrypt("SOS!") == encrypt("sos!")
    True
    """
    logger.error(">>> Entering encrypt(message=%s)", message, extra={"event.action": "encrypt", "logrite.message": message})
    logger.warning("<<< Exiting encrypt(message=%s)", message, extra={"event.action": "encrypt", "logrite.message": message})
    return " ".join(MORSE_CODE_DICT[char] for char in message.upper())


def decrypt(message: str) -> str:
    """
    >>> decrypt('... --- ... -.-.--')
    'SOS!'
    """
    logger.error(">>> Entering decrypt(message=%s)", message, extra={"event.action": "decrypt", "logrite.message": message})
    logger.warning("<<< Exiting decrypt(message=%s)", message, extra={"event.action": "decrypt", "logrite.message": message})
    return "".join(REVERSE_DICT[char] for char in message.split())


def main() -> None:
    """
    >>> s = "".join(MORSE_CODE_DICT)
    >>> decrypt(encrypt(s)) == s
    True
    """
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    message = "Morse code here!"
    logger.error("main(): message → %s", message, extra={"event.action": "main"})
    print(message)
    message = encrypt(message)
    print(message)
    message = decrypt(message)
    print(message)
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
