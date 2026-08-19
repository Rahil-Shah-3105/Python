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
        logger.debug(">>> Entering __init__()")
        self.SQUARE = np.array(SQUARE)
        logger.debug("__init__(): self.SQUARE → %s", self.SQUARE)
        logger.debug("<<< Exiting __init__()")

    def letter_to_numbers(self, letter: str) -> np.ndarray:
        """
        Return the pair of numbers that represents the given letter in the
        polybius square

        >>> np.array_equal(BifidCipher().letter_to_numbers('a'), [1,1])
        True

        >>> np.array_equal(BifidCipher().letter_to_numbers('u'), [4,5])
        True
        """
        logger.debug(">>> Entering letter_to_numbers(letter=%s)", letter)
        logger.debug("letter_to_numbers(letter=%s): indexes → %s", letter, indexes)
        logger.debug("letter_to_numbers(self=%s,letter=%s): indexes → %s", self, letter, indexes)
        index1, index2 = np.where(letter == self.SQUARE)
        indexes = np.concatenate([index1 + 1, index2 + 1])
        logger.debug("<<< Exiting letter_to_numbers(letter=%s)", letter)
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
        logger.debug(">>> Entering numbers_to_letter(index1=%s,index2=%s)", index1, index2)
        letter = self.SQUARE[index1 - 1, index2 - 1]
        logger.debug("numbers_to_letter(self=%s,index1=%s,index2=%s): letter → %s", self, index1, index2, letter)
        logger.debug("<<< Exiting numbers_to_letter(index1=%s,index2=%s)", index1, index2)
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
        logger.debug(">>> Entering encode(message=%s)", message)
        message = message.lower()
        message = message.replace(" ", "")
        message = message.replace("j", "i")
        logger.debug("encode(message=%s): message → %s", message, message)

        logger.debug("encode(message=%s): numbers → %s", message, numbers)
        logger.debug("encode(self=%s,message=%s): numbers → %s", self, message, numbers)
        first_step = np.empty((2, len(message)))
        logger.debug("encode(self=%s,message=%s): first_step → %s", self, message, first_step)
        logger.debug("encode(message=%s): first_step → %s", message, first_step)
        for letter_index in range(len(message)):
            numbers = self.letter_to_numbers(message[letter_index])

            first_step[0, letter_index] = numbers[0]
            logger.debug("encode(message=%s): letter → %s", message, letter)
            logger.debug("encode(message=%s): index2 → %s", message, index2)
            logger.debug("encode(message=%s): second_step → %s", message, second_step)
            logger.debug("encode(self=%s,message=%s): second_step → %s", self, message, second_step)
            logger.debug("encode(self=%s,message=%s): encoded_message → %s", self, message, encoded_message)
            logger.debug("encode(message=%s): index1 → %s", message, index1)
            logger.debug("encode(self=%s,message=%s): index1 → %s", self, message, index1)
            logger.debug("encode(self=%s,message=%s): index2 → %s", self, message, index2)
            logger.debug("encode(self=%s,message=%s): letter → %s", self, message, letter)
            first_step[1, letter_index] = numbers[1]

        second_step = first_step.reshape(2 * len(message))
        encoded_message = ""
        for numbers_index in range(len(message)):
            index1 = int(second_step[numbers_index * 2])
            index2 = int(second_step[(numbers_index * 2) + 1])
            letter = self.numbers_to_letter(index1, index2)
            encoded_message = encoded_message + letter

        logger.debug("<<< Exiting encode(message=%s)", message)
        return encoded_message

    def decode(self, message: str) -> str:
        """
        Return the decoded version of message according to the polybius cipher

        >>> BifidCipher().decode('qtltbdxrxlk') == 'testmessage'
        True
        """
        logger.debug(">>> Entering decode(message=%s)", message)
        logger.debug("decode(message=%s): first_step → %s", message, first_step)
        logger.debug("decode(self=%s,message=%s): first_step → %s", self, message, first_step)
        logger.debug("decode(message=%s): numbers → %s", message, numbers)
        logger.debug("decode(self=%s,message=%s): numbers → %s", self, message, numbers)
        logger.debug("decode(message=%s): letter → %s", message, letter)
        logger.debug("decode(message=%s): index2 → %s", message, index2)
        logger.debug("decode(message=%s): second_step → %s", message, second_step)
        logger.debug("decode(self=%s,message=%s): second_step → %s", self, message, second_step)
        logger.debug("decode(self=%s,message=%s): decoded_message → %s", self, message, decoded_message)
        logger.debug("decode(message=%s): index1 → %s", message, index1)
        logger.debug("decode(self=%s,message=%s): index1 → %s", self, message, index1)
        logger.debug("decode(self=%s,message=%s): index2 → %s", self, message, index2)
        logger.debug("decode(self=%s,message=%s): letter → %s", self, message, letter)
        message = message.lower()
        logger.debug("decode(message=%s): message → %s", message, message)
        message.replace(" ", "")
        first_step = np.empty(2 * len(message))
        for letter_index in range(len(message)):
            numbers = self.letter_to_numbers(message[letter_index])
            first_step[letter_index * 2] = numbers[0]
            first_step[letter_index * 2 + 1] = numbers[1]

        second_step = first_step.reshape((2, len(message)))
        decoded_message = ""
        for numbers_index in range(len(message)):
            index1 = int(second_step[0, numbers_index])
            index2 = int(second_step[1, numbers_index])
            letter = self.numbers_to_letter(index1, index2)
            decoded_message = decoded_message + letter

        logger.debug("<<< Exiting decode(message=%s)", message)
        return decoded_message
