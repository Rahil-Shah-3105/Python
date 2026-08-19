"""
Python program for the Fractionated Morse Cipher.

The Fractionated Morse cipher first converts the plaintext to Morse code,
then enciphers fixed-size blocks of Morse code back to letters.
This procedure means plaintext letters are mixed into the ciphertext letters,
making it more secure than substitution ciphers.

http://practicalcryptography.com/ciphers/fractionated-morse-cipher/
"""

import string
import logging
logger = logging.getLogger(__name__)

MORSE_CODE_DICT = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    " ": "",
}

# Define possible trigrams of Morse code
MORSE_COMBINATIONS = [
    "...",
    "..-",
    "..x",
    ".-.",
    ".--",
    ".-x",
    ".x.",
    ".x-",
    ".xx",
    "-..",
    "-.-",
    "-.x",
    "--.",
    "---",
    "--x",
    "-x.",
    "-x-",
    "-xx",
    "x..",
    "x.-",
    "x.x",
    "x-.",
    "x--",
    "x-x",
    "xx.",
    "xx-",
    "xxx",
]

# Create a reverse dictionary for Morse code
REVERSE_DICT = {value: key for key, value in MORSE_CODE_DICT.items()}


def encode_to_morse(plaintext: str) -> str:
    """Encode a plaintext message into Morse code.

    Args:
        plaintext: The plaintext message to encode.

    Returns:
        The Morse code representation of the plaintext message.

    Example:
        >>> encode_to_morse("defend the east")
        '-..x.x..-.x.x-.x-..xx-x....x.xx.x.-x...x-'
    """
    logger.debug(">>> Entering encode_to_morse(plaintext=%s)", plaintext)
    logger.debug("<<< Exiting encode_to_morse(plaintext=%s)", plaintext)
    return "x".join([MORSE_CODE_DICT.get(letter.upper(), "") for letter in plaintext])


def encrypt_fractionated_morse(plaintext: str, key: str) -> str:
    """Encrypt a plaintext message using Fractionated Morse Cipher.

    Args:
        plaintext: The plaintext message to encrypt.
        key: The encryption key.

    Returns:
        The encrypted ciphertext.

    Example:
        >>> encrypt_fractionated_morse("defend the east","Roundtable")
        'ESOAVVLJRSSTRX'

    """
    logger.debug(">>> Entering encrypt_fractionated_morse(plaintext=%s,key=%s)", plaintext, key)
    morse_code = encode_to_morse(plaintext)
    logger.debug("encrypt_fractionated_morse(plaintext=%s,key=%s): morse_code → %s", plaintext, key, morse_code)
    key = key.upper() + string.ascii_uppercase
    key = "".join(sorted(set(key), key=key.find))
    logger.debug("encrypt_fractionated_morse(plaintext=%s,key=%s): key → %s", plaintext, key, key)

    # Ensure morse_code length is a multiple of 3
    padding_length = 3 - (len(morse_code) % 3)
    logger.debug("encrypt_fractionated_morse(plaintext=%s,key=%s): padding_length → %s", plaintext, key, padding_length)
    morse_code += "x" * padding_length

    fractionated_morse_dict = {v: k for k, v in zip(key, MORSE_COMBINATIONS)}
    logger.debug("encrypt_fractionated_morse(plaintext=%s,key=%s): fractionated_morse_dict → %s", plaintext, key, fractionated_morse_dict)
    logger.debug("encrypt_fractionated_morse(plaintext=%s,key=%s): encrypted_text → %s", plaintext, key, encrypted_text)
    fractionated_morse_dict["xxx"] = ""
    encrypted_text = "".join(
        [
            fractionated_morse_dict[morse_code[i : i + 3]]
            for i in range(0, len(morse_code), 3)
        ]
    )
    logger.debug("<<< Exiting encrypt_fractionated_morse(plaintext=%s,key=%s)", plaintext, key)
    return encrypted_text


def decrypt_fractionated_morse(ciphertext: str, key: str) -> str:
    """Decrypt a ciphertext message encrypted with Fractionated Morse Cipher.

    Args:
        ciphertext: The ciphertext message to decrypt.
        key: The decryption key.

    Returns:
        The decrypted plaintext message.

    Example:
        >>> decrypt_fractionated_morse("ESOAVVLJRSSTRX","Roundtable")
        'DEFEND THE EAST'
    """
    logger.debug(">>> Entering decrypt_fractionated_morse(ciphertext=%s,key=%s)", ciphertext, key)
    key = key.upper() + string.ascii_uppercase
    key = "".join(sorted(set(key), key=key.find))
    logger.debug("decrypt_fractionated_morse(ciphertext=%s,key=%s): key → %s", ciphertext, key, key)

    inverse_fractionated_morse_dict = dict(zip(key, MORSE_COMBINATIONS))
    logger.debug("decrypt_fractionated_morse(ciphertext=%s,key=%s): inverse_fractionated_morse_dict → %s", ciphertext, key, inverse_fractionated_morse_dict)
    morse_code = "".join(
        [inverse_fractionated_morse_dict.get(letter, "") for letter in ciphertext]
    )
    decrypted_text = "".join(
        [REVERSE_DICT[code] for code in morse_code.split("x")]
    ).strip()
    logger.debug("<<< Exiting decrypt_fractionated_morse(ciphertext=%s,key=%s)", ciphertext, key)
    return decrypted_text


if __name__ == "__main__":
    """
    Example usage of Fractionated Morse Cipher.
    """
    plaintext = "defend the east"
    print("Plain Text:", plaintext)
    key = "ROUNDTABLE"

    ciphertext = encrypt_fractionated_morse(plaintext, key)
    print("Encrypted:", ciphertext)

    decrypted_text = decrypt_fractionated_morse(ciphertext, key)
    print("Decrypted:", decrypted_text)
