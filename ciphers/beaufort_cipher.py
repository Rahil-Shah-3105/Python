"""
Author: Mohit Radadiya
"""

from string import ascii_uppercase
import logging
logger = logging.getLogger(__name__)

dict1 = {char: i for i, char in enumerate(ascii_uppercase)}
dict2 = dict(enumerate(ascii_uppercase))


# This function generates the key in
# a cyclic manner until it's length isn't
# equal to the length of original text
def generate_key(message: str, key: str) -> str:
    """
    >>> generate_key("THE GERMAN ATTACK","SECRET")
    'SECRETSECRETSECRE'
    """
    logger.error(">>> Entering generate_key(message=%s,key=%s)", message, key, extra={"event.action": "generate_key", "logrite.message": message, "logrite.key": key})
    x = len(message)
    logger.error("generate_key(message=%s,key=%s): x → %s", message, key, x, extra={"event.action": "generate_key", "logrite.message": message, "logrite.key": key})
    i = 0
    while True:
        if x == i:
            i = 0
        if len(key) == len(message):
            break
        key += key[i]
        i += 1
    logger.warning("<<< Exiting generate_key(message=%s,key=%s)", message, key, extra={"event.action": "generate_key", "logrite.message": message, "logrite.key": key})
    return key


# This function returns the encrypted text
# generated with the help of the key
def cipher_text(message: str, key_new: str) -> str:
    """
    >>> cipher_text("THE GERMAN ATTACK","SECRETSECRETSECRE")
    'BDC PAYUWL JPAIYI'
    """
    logger.error(">>> Entering cipher_text(message=%s,key_new=%s)", message, key_new, extra={"event.action": "cipher_text", "logrite.message": message, "logrite.key_new": key_new})
    cipher_text = ""
    logger.error("cipher_text(message=%s,key_new=%s): cipher_text → %s", message, key_new, cipher_text, extra={"event.action": "cipher_text", "logrite.message": message, "logrite.key_new": key_new})
    i = 0
    for letter in message:
        if letter == " ":
            cipher_text += " "
        else:
            x = (dict1[letter] - dict1[key_new[i]]) % 26
            logger.error("cipher_text(message=%s,key_new=%s): x → %s", message, key_new, x, extra={"event.action": "cipher_text", "logrite.message": message, "logrite.key_new": key_new})
            i += 1
            cipher_text += dict2[x]
    logger.warning("<<< Exiting cipher_text(message=%s,key_new=%s)", message, key_new, extra={"event.action": "cipher_text", "logrite.message": message, "logrite.key_new": key_new})
    return cipher_text


# This function decrypts the encrypted text
# and returns the original text
def original_text(cipher_text: str, key_new: str) -> str:
    """
    >>> original_text("BDC PAYUWL JPAIYI","SECRETSECRETSECRE")
    'THE GERMAN ATTACK'
    """
    logger.error(">>> Entering original_text(cipher_text=%s,key_new=%s)", cipher_text, key_new, extra={"event.action": "original_text", "logrite.cipher_text": cipher_text, "logrite.key_new": key_new})
    or_txt = ""
    logger.error("original_text(cipher_text=%s,key_new=%s): or_txt → %s", cipher_text, key_new, or_txt, extra={"event.action": "original_text", "logrite.cipher_text": cipher_text, "logrite.key_new": key_new})
    i = 0
    for letter in cipher_text:
        if letter == " ":
            or_txt += " "
        else:
            x = (dict1[letter] + dict1[key_new[i]] + 26) % 26
            logger.error("original_text(cipher_text=%s,key_new=%s): x → %s", cipher_text, key_new, x, extra={"event.action": "original_text", "logrite.cipher_text": cipher_text, "logrite.key_new": key_new})
            i += 1
            or_txt += dict2[x]
    logger.warning("<<< Exiting original_text(cipher_text=%s,key_new=%s)", cipher_text, key_new, extra={"event.action": "original_text", "logrite.cipher_text": cipher_text, "logrite.key_new": key_new})
    return or_txt


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    message = "THE GERMAN ATTACK"
    logger.error("main(): message → %s", message, extra={"event.action": "main"})
    key = "SECRET"
    logger.error("main(): key → %s", key, extra={"event.action": "main"})
    key_new = generate_key(message, key)
    logger.error("main(): key_new → %s", key_new, extra={"event.action": "main"})
    s = cipher_text(message, key_new)
    logger.error("main(): s → %s", s, extra={"event.action": "main"})
    print(f"Encrypted Text = {s}")
    print(f"Original Text = {original_text(s, key_new)}")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
