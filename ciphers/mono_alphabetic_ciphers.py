from typing import Literal
import logging
logger = logging.getLogger(__name__)

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def translate_message(
    key: str, message: str, mode: Literal["encrypt", "decrypt"]
) -> str:
    """
    >>> translate_message("QWERTYUIOPASDFGHJKLZXCVBNM","Hello World","encrypt")
    'Pcssi Bidsm'
    """
    chars_a = LETTERS if mode == "decrypt" else key
    chars_b = key if mode == "decrypt" else LETTERS
    translated = ""
    # loop through each symbol in the message
    for symbol in message:
        if symbol.upper() in chars_a:
            # encrypt/decrypt the symbol
            sym_index = chars_a.find(symbol.upper())
            if symbol.isupper():
                translated += chars_b[sym_index].upper()
            else:
                translated += chars_b[sym_index].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol
    return translated


def encrypt_message(key: str, message: str) -> str:
    """
    >>> encrypt_message("QWERTYUIOPASDFGHJKLZXCVBNM", "Hello World")
    'Pcssi Bidsm'
    """
    logger.debug(">>> Entering encrypt_message(key=%s,message=%s)", key, message)
    logger.debug("<<< Exiting encrypt_message(key=%s,message=%s)", key, message)
    return translate_message(key, message, "encrypt")


def decrypt_message(key: str, message: str) -> str:
    """
    >>> decrypt_message("QWERTYUIOPASDFGHJKLZXCVBNM", "Hello World")
    'Itssg Vgksr'
    """
    logger.debug(">>> Entering decrypt_message(key=%s,message=%s)", key, message)
    logger.debug("<<< Exiting decrypt_message(key=%s,message=%s)", key, message)
    return translate_message(key, message, "decrypt")


def main() -> None:
    logger.debug(">>> Entering main()")
    message = "Hello World"
    logger.debug("main(): message → %s", message)
    key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    mode = "decrypt"  # set to 'encrypt' or 'decrypt'
    logger.warning("main(): key → %s", key)
    logger.debug("main(): key → %s", key)
    logger.debug("main(): mode → %s", mode)
    logger.debug("main(): translated → %s", translated)

    if mode == "encrypt":
        translated = encrypt_message(key, message)
    elif mode == "decrypt":
        translated = decrypt_message(key, message)
        logger.debug("<<< Exiting main()")
    print(f"Using the key {key}, the {mode}ed message is: {translated}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
