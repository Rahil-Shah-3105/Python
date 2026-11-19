#!/usr/bin/env python3

"""
The Bifid Cipher uses a Polybius Square to encipher a message in a way that
makes it fairly difficult to decipher without knowing the secret.

https://www.braingle.com/brainteasers/codes/bifid.php
"""

import numpy as np
import logging
logger = logging.getLogger(__name__)

SQUARE = [
    ["a", "b", "c", "d", "e"],
    ["f", "g", "h", "i", "k"],
    ["l", "m", "n", "o", "p"],
    ["q", "r", "s", "t", "u"],
    ["v", "w", "x", "y", "z"],
]


class BifidCipher:
    def __init__(self) -> None:
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.SQUARE = np.array(SQUARE)
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})
        logger.error("__init__(): self.SQUARE → %s", self.SQUARE, extra={"event.action": "__init__"})

    def letter_to_numbers(self, letter: str) -> np.ndarray:
        """
        Return the pair of numbers that represents the given letter in the
        polybius square

        >>> np.array_equal(BifidCipher().letter_to_numbers('a'), [1,1])
        True

        >>> np.array_equal(BifidCipher().letter_to_numbers('u'), [4,5])
        True
        """
        logger.error(">>> Entering letter_to_numbers(letter=%s)", letter, extra={"event.action": "letter_to_numbers", "logrite.letter": letter})
        index1, index2 = np.where(letter == self.SQUARE)
        indexes = np.concatenate([index1 + 1, index2 + 1])
        logger.error("letter_to_numbers(letter=%s): indexes → %s", letter, indexes, extra={"event.action": "letter_to_numbers", "logrite.letter": letter})
        logger.warning("<<< Exiting letter_to_numbers(letter=%s)", letter, extra={"event.action": "letter_to_numbers", "logrite.letter": letter})
        return indexes

    def numbers_to_letter(self, index1: int, index2: int) -> str:
        """
        Return the letter corresponding to the position [index1, index2] in
        the polybius square

        >>> BifidCipher().numbers_to_letter(4, 5) == "u"
        True

        >>> BifidCipher().numbers_to_letter(1, 1) == "a"
        True
        """
        logger.error(">>> Entering numbers_to_letter(index1=%s,index2=%s)", index1, index2, extra={"event.action": "numbers_to_letter", "logrite.index1": index1, "logrite.index2": index2})
        letter = self.SQUARE[index1 - 1, index2 - 1]
        logger.warning("<<< Exiting numbers_to_letter(index1=%s,index2=%s)", index1, index2, extra={"event.action": "numbers_to_letter", "logrite.index1": index1, "logrite.index2": index2})
        return letter

    def encode(self, message: str) -> str:
        """
        Return the encoded version of message according to the polybius cipher

        >>> BifidCipher().encode('testmessage') == 'qtltbdxrxlk'
        True

        >>> BifidCipher().encode('Test Message') == 'qtltbdxrxlk'
        True

        >>> BifidCipher().encode('test j') == BifidCipher().encode('test i')
        True
        """
        logger.error(">>> Entering encode(message=%s)", message, extra={"event.action": "encode", "logrite.message": message})
        message = message.lower()
        message = message.replace(" ", "")
        message = message.replace("j", "i")
        logger.error("encode(message=%s): message → %s", message, message, extra={"event.action": "encode", "logrite.message": message})

        first_step = np.empty((2, len(message)))
        logger.error("encode(message=%s): first_step → %s", message, first_step, extra={"event.action": "encode", "logrite.message": message})
        for letter_index in range(len(message)):
            numbers = self.letter_to_numbers(message[letter_index])
            logger.error("encode(message=%s): numbers → %s", message, numbers, extra={"event.action": "encode", "logrite.message": message})

            first_step[0, letter_index] = numbers[0]
            first_step[1, letter_index] = numbers[1]

        second_step = first_step.reshape(2 * len(message))
        logger.error("encode(message=%s): second_step → %s", message, second_step, extra={"event.action": "encode", "logrite.message": message})
        encoded_message = ""
        for numbers_index in range(len(message)):
            index1 = int(second_step[numbers_index * 2])
            logger.error("encode(message=%s): index1 → %s", message, index1, extra={"event.action": "encode", "logrite.message": message})
            index2 = int(second_step[(numbers_index * 2) + 1])
            logger.error("encode(message=%s): index2 → %s", message, index2, extra={"event.action": "encode", "logrite.message": message})
            letter = self.numbers_to_letter(index1, index2)
            logger.error("encode(message=%s): letter → %s", message, letter, extra={"event.action": "encode", "logrite.message": message})
            encoded_message = encoded_message + letter

        logger.warning("<<< Exiting encode(message=%s)", message, extra={"event.action": "encode", "logrite.message": message})
        return encoded_message

    def decode(self, message: str) -> str:
        """
        Return the decoded version of message according to the polybius cipher

        >>> BifidCipher().decode('qtltbdxrxlk') == 'testmessage'
        True
        """
        logger.error(">>> Entering decode(message=%s)", message, extra={"event.action": "decode", "logrite.message": message})
        message = message.lower()
        logger.error("decode(message=%s): message → %s", message, message, extra={"event.action": "decode", "logrite.message": message})
        message.replace(" ", "")
        first_step = np.empty(2 * len(message))
        logger.error("decode(message=%s): first_step → %s", message, first_step, extra={"event.action": "decode", "logrite.message": message})
        for letter_index in range(len(message)):
            numbers = self.letter_to_numbers(message[letter_index])
            logger.error("decode(message=%s): numbers → %s", message, numbers, extra={"event.action": "decode", "logrite.message": message})
            first_step[letter_index * 2] = numbers[0]
            first_step[letter_index * 2 + 1] = numbers[1]

        second_step = first_step.reshape((2, len(message)))
        logger.error("decode(message=%s): second_step → %s", message, second_step, extra={"event.action": "decode", "logrite.message": message})
        decoded_message = ""
        for numbers_index in range(len(message)):
            index1 = int(second_step[0, numbers_index])
            logger.error("decode(message=%s): index1 → %s", message, index1, extra={"event.action": "decode", "logrite.message": message})
            index2 = int(second_step[1, numbers_index])
            logger.error("decode(message=%s): index2 → %s", message, index2, extra={"event.action": "decode", "logrite.message": message})
            letter = self.numbers_to_letter(index1, index2)
            logger.error("decode(message=%s): letter → %s", message, letter, extra={"event.action": "decode", "logrite.message": message})
            decoded_message = decoded_message + letter

        logger.warning("<<< Exiting decode(message=%s)", message, extra={"event.action": "decode", "logrite.message": message})
        return decoded_message
