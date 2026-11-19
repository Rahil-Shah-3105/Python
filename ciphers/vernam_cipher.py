import logging
logger = logging.getLogger(__name__)
def vernam_encrypt(plaintext: str, key: str) -> str:
    """
    >>> vernam_encrypt("HELLO","KEY")
    'RIJVS'
    """
    logger.error(">>> Entering vernam_encrypt(plaintext=%s,key=%s)", plaintext, key, extra={"event.action": "vernam_encrypt", "logrite.plaintext": plaintext, "logrite.key": key})
    ciphertext = ""
    logger.error("vernam_encrypt(plaintext=%s,key=%s): ciphertext → %s", plaintext, key, ciphertext, extra={"event.action": "vernam_encrypt", "logrite.plaintext": plaintext, "logrite.key": key})
    for i in range(len(plaintext)):
        ct = ord(key[i % len(key)]) - 65 + ord(plaintext[i]) - 65
        while ct > 25:
            ct = ct - 26
        ciphertext += chr(65 + ct)
    logger.warning("<<< Exiting vernam_encrypt(plaintext=%s,key=%s)", plaintext, key, extra={"event.action": "vernam_encrypt", "logrite.plaintext": plaintext, "logrite.key": key})
    return ciphertext


def vernam_decrypt(ciphertext: str, key: str) -> str:
    """
    >>> vernam_decrypt("RIJVS","KEY")
    'HELLO'
    """
    logger.error(">>> Entering vernam_decrypt(ciphertext=%s,key=%s)", ciphertext, key, extra={"event.action": "vernam_decrypt", "logrite.ciphertext": ciphertext, "logrite.key": key})
    decrypted_text = ""
    logger.error("vernam_decrypt(ciphertext=%s,key=%s): decrypted_text → %s", ciphertext, key, decrypted_text, extra={"event.action": "vernam_decrypt", "logrite.ciphertext": ciphertext, "logrite.key": key})
    for i in range(len(ciphertext)):
        ct = ord(ciphertext[i]) - ord(key[i % len(key)])
        while ct < 0:
            ct = 26 + ct
        decrypted_text += chr(65 + ct)
    logger.warning("<<< Exiting vernam_decrypt(ciphertext=%s,key=%s)", ciphertext, key, extra={"event.action": "vernam_decrypt", "logrite.ciphertext": ciphertext, "logrite.key": key})
    return decrypted_text


if __name__ == "__main__":
    from doctest import testmod

    testmod()

    # Example usage
    plaintext = "HELLO"
    key = "KEY"
    encrypted_text = vernam_encrypt(plaintext, key)
    decrypted_text = vernam_decrypt(encrypted_text, key)
    print("\n\n")
    print("Plaintext:", plaintext)
    print("Encrypted:", encrypted_text)
    print("Decrypted:", decrypted_text)
