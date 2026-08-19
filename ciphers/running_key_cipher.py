import logging
logger = logging.getLogger(__name__)
"""
https://en.wikipedia.org/wiki/Running_key_cipher
"""


def running_key_encrypt(key: str, plaintext: str) -> str:
    """
    Encrypts the plaintext using the Running Key Cipher.

    :param key: The running key (long piece of text).
    :param plaintext: The plaintext to be encrypted.
    :return: The ciphertext.
    """
    logger.debug(">>> Entering running_key_encrypt(key=%s,plaintext=%s)", key, plaintext)
    plaintext = plaintext.replace(" ", "").upper()
    logger.debug("running_key_encrypt(key=%s,plaintext=%s): plaintext → %s", key, plaintext, plaintext)
    key = key.replace(" ", "").upper()
    logger.debug("running_key_encrypt(key=%s,plaintext=%s): key → %s", key, plaintext, key)
    key_length = len(key)
    logger.debug("running_key_encrypt(key=%s,plaintext=%s): key_length → %s", key, plaintext, key_length)
    ciphertext = []
    logger.debug("running_key_encrypt(key=%s,plaintext=%s): ciphertext → %s", key, plaintext, ciphertext)
    ord_a = ord("A")
    logger.debug("running_key_encrypt(key=%s,plaintext=%s): ord_a → %s", key, plaintext, ord_a)

    for i, char in enumerate(plaintext):
        p = ord(char) - ord_a
        logger.debug("running_key_encrypt(key=%s,plaintext=%s): p → %s", key, plaintext, p)
        k = ord(key[i % key_length]) - ord_a
        c = (p + k) % 26
        logger.debug("running_key_encrypt(key=%s,plaintext=%s): c → %s", key, plaintext, c)
        ciphertext.append(chr(c + ord_a))

    logger.debug("<<< Exiting running_key_encrypt(key=%s,plaintext=%s)", key, plaintext)
    return "".join(ciphertext)


def running_key_decrypt(key: str, ciphertext: str) -> str:
    """
    Decrypts the ciphertext using the Running Key Cipher.

    :param key: The running key (long piece of text).
    :param ciphertext: The ciphertext to be decrypted.
    :return: The plaintext.
    """
    logger.debug(">>> Entering running_key_decrypt(key=%s,ciphertext=%s)", key, ciphertext)
    ciphertext = ciphertext.replace(" ", "").upper()
    logger.debug("running_key_decrypt(key=%s,ciphertext=%s): ciphertext → %s", key, ciphertext, ciphertext)
    key = key.replace(" ", "").upper()
    logger.debug("running_key_decrypt(key=%s,ciphertext=%s): key → %s", key, ciphertext, key)
    key_length = len(key)
    logger.debug("running_key_decrypt(key=%s,ciphertext=%s): key_length → %s", key, ciphertext, key_length)
    plaintext = []
    logger.debug("running_key_decrypt(key=%s,ciphertext=%s): plaintext → %s", key, ciphertext, plaintext)
    ord_a = ord("A")
    logger.debug("running_key_decrypt(key=%s,ciphertext=%s): ord_a → %s", key, ciphertext, ord_a)

    for i, char in enumerate(ciphertext):
        c = ord(char) - ord_a
        logger.debug("running_key_decrypt(key=%s,ciphertext=%s): c → %s", key, ciphertext, c)
        k = ord(key[i % key_length]) - ord_a
        p = (c - k) % 26
        logger.debug("running_key_decrypt(key=%s,ciphertext=%s): p → %s", key, ciphertext, p)
        plaintext.append(chr(p + ord_a))

    logger.debug("<<< Exiting running_key_decrypt(key=%s,ciphertext=%s)", key, ciphertext)
    return "".join(plaintext)


def test_running_key_encrypt() -> None:
    """
    >>> key = "How does the duck know that? said Victor"
    >>> ciphertext = running_key_encrypt(key, "DEFEND THIS")
    >>> running_key_decrypt(key, ciphertext) == "DEFENDTHIS"
    True
    """
    logger.debug(">>> Entering test_running_key_encrypt()")

    logger.debug("<<< Exiting test_running_key_encrypt()")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    test_running_key_encrypt()

    plaintext = input("Enter the plaintext: ").upper()
    print(f"\n{plaintext = }")

    key = "How does the duck know that? said Victor"
    encrypted_text = running_key_encrypt(key, plaintext)
    print(f"{encrypted_text = }")

    decrypted_text = running_key_decrypt(key, encrypted_text)
    print(f"{decrypted_text = }")
