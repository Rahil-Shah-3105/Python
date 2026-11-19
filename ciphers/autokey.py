"""
https://en.wikipedia.org/wiki/Autokey_cipher

An autokey cipher (also known as the autoclave cipher) is a cipher that
incorporates the message (the plaintext) into the key.
The key is generated from the message in some automated fashion,
sometimes by selecting certain letters from the text or, more commonly,
by adding a short primer key to the front of the message.
"""
import logging
logger = logging.getLogger(__name__)


def encrypt(plaintext: str, key: str) -> str:
    """
    Encrypt a given `plaintext` (string) and `key` (string), returning the
    encrypted ciphertext.

    >>> encrypt("hello world", "coffee")
    'jsqqs avvwo'
    >>> encrypt("coffee is good as python", "TheAlgorithms")
    'vvjfpk wj ohvp su ddylsv'
    >>> encrypt("coffee is good as python", 2)
    Traceback (most recent call last):
        ...
    TypeError: key must be a string
    >>> encrypt("", "TheAlgorithms")
    Traceback (most recent call last):
        ...
    ValueError: plaintext is empty
    >>> encrypt("coffee is good as python", "")
    Traceback (most recent call last):
        ...
    ValueError: key is empty
    >>> encrypt(527.26, "TheAlgorithms")
    Traceback (most recent call last):
        ...
    TypeError: plaintext must be a string
    """
    logger.error(">>> Entering encrypt(plaintext=%s,key=%s)", plaintext, key, extra={"event.action": "encrypt", "logrite.plaintext": plaintext, "logrite.key": key})
    if not isinstance(plaintext, str):
        raise TypeError("plaintext must be a string")
    if not isinstance(key, str):
        raise TypeError("key must be a string")

    if not plaintext:
        raise ValueError("plaintext is empty")
    if not key:
        raise ValueError("key is empty")

    key += plaintext
    plaintext = plaintext.lower()
    logger.error("encrypt(plaintext=%s,key=%s): plaintext → %s", plaintext, key, plaintext, extra={"event.action": "encrypt", "logrite.plaintext": plaintext, "logrite.key": key})
    key = key.lower()
    logger.error("encrypt(plaintext=%s,key=%s): key → %s", plaintext, key, key, extra={"event.action": "encrypt", "logrite.plaintext": plaintext, "logrite.key": key})
    plaintext_iterator = 0
    key_iterator = 0
    ciphertext = ""
    logger.error("encrypt(plaintext=%s,key=%s): ciphertext → %s", plaintext, key, ciphertext, extra={"event.action": "encrypt", "logrite.plaintext": plaintext, "logrite.key": key})
    while plaintext_iterator < len(plaintext):
        if (
            ord(plaintext[plaintext_iterator]) < 97
            or ord(plaintext[plaintext_iterator]) > 122
        ):
            ciphertext += plaintext[plaintext_iterator]
            plaintext_iterator += 1
        elif ord(key[key_iterator]) < 97 or ord(key[key_iterator]) > 122:
            key_iterator += 1
        else:
            ciphertext += chr(
                (
                    (ord(plaintext[plaintext_iterator]) - 97 + ord(key[key_iterator]))
                    - 97
                )
                % 26
                + 97
            )
            key_iterator += 1
            plaintext_iterator += 1
    logger.warning("<<< Exiting encrypt(plaintext=%s,key=%s)", plaintext, key, extra={"event.action": "encrypt", "logrite.plaintext": plaintext, "logrite.key": key})
    return ciphertext


def decrypt(ciphertext: str, key: str) -> str:
    """
    Decrypt a given `ciphertext` (string) and `key` (string), returning the decrypted
    ciphertext.

    >>> decrypt("jsqqs avvwo", "coffee")
    'hello world'
    >>> decrypt("vvjfpk wj ohvp su ddylsv", "TheAlgorithms")
    'coffee is good as python'
    >>> decrypt("vvjfpk wj ohvp su ddylsv", "")
    Traceback (most recent call last):
        ...
    ValueError: key is empty
    >>> decrypt(527.26, "TheAlgorithms")
    Traceback (most recent call last):
        ...
    TypeError: ciphertext must be a string
    >>> decrypt("", "TheAlgorithms")
    Traceback (most recent call last):
        ...
    ValueError: ciphertext is empty
    >>> decrypt("vvjfpk wj ohvp su ddylsv", 2)
    Traceback (most recent call last):
        ...
    TypeError: key must be a string
    """
    logger.error(">>> Entering decrypt(ciphertext=%s,key=%s)", ciphertext, key, extra={"event.action": "decrypt", "logrite.ciphertext": ciphertext, "logrite.key": key})
    if not isinstance(ciphertext, str):
        raise TypeError("ciphertext must be a string")
    if not isinstance(key, str):
        raise TypeError("key must be a string")

    if not ciphertext:
        raise ValueError("ciphertext is empty")
    if not key:
        raise ValueError("key is empty")

    key = key.lower()
    logger.error("decrypt(ciphertext=%s,key=%s): key → %s", ciphertext, key, key, extra={"event.action": "decrypt", "logrite.ciphertext": ciphertext, "logrite.key": key})
    ciphertext_iterator = 0
    key_iterator = 0
    plaintext = ""
    logger.error("decrypt(ciphertext=%s,key=%s): plaintext → %s", ciphertext, key, plaintext, extra={"event.action": "decrypt", "logrite.ciphertext": ciphertext, "logrite.key": key})
    while ciphertext_iterator < len(ciphertext):
        if (
            ord(ciphertext[ciphertext_iterator]) < 97
            or ord(ciphertext[ciphertext_iterator]) > 122
        ):
            plaintext += ciphertext[ciphertext_iterator]
        else:
            plaintext += chr(
                (ord(ciphertext[ciphertext_iterator]) - ord(key[key_iterator])) % 26
                + 97
            )
            key += chr(
                (ord(ciphertext[ciphertext_iterator]) - ord(key[key_iterator])) % 26
                + 97
            )
            key_iterator += 1
        ciphertext_iterator += 1
    logger.warning("<<< Exiting decrypt(ciphertext=%s,key=%s)", ciphertext, key, extra={"event.action": "decrypt", "logrite.ciphertext": ciphertext, "logrite.key": key})
    return plaintext


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    operation = int(input("Type 1 to encrypt or 2 to decrypt:"))
    if operation == 1:
        plaintext = input("Typeplaintext to be encrypted:\n")
        key = input("Type the key:\n")
        print(encrypt(plaintext, key))
    elif operation == 2:
        ciphertext = input("Type the ciphertext to be decrypted:\n")
        key = input("Type the key:\n")
        print(decrypt(ciphertext, key))
    decrypt("jsqqs avvwo", "coffee")
