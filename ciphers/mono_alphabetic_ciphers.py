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
    logger.warning("<<< Exiting translate_message(key=%s,message=%s,mode=%s)", key, message, mode, extra={"event.action": "translate_message", "logrite.key": key, "logrite.message": message, "logrite.mode": mode})
    return translated


def encrypt_message(key: str, message: str) -> str:
    """
    >>> encrypt_message("QWERTYUIOPASDFGHJKLZXCVBNM", "Hello World")
    'Pcssi Bidsm'
    """
    logger.error(">>> Entering encrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "encrypt_message", "logrite.key": key, "logrite.message": message})
    logger.warning("<<< Exiting encrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "encrypt_message", "logrite.key": key, "logrite.message": message})
    return translate_message(key, message, "encrypt")


def decrypt_message(key: str, message: str) -> str:
    """
    >>> decrypt_message("QWERTYUIOPASDFGHJKLZXCVBNM", "Hello World")
    'Itssg Vgksr'
    """
    logger.error(">>> Entering decrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
    logger.warning("<<< Exiting decrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
    return translate_message(key, message, "decrypt")


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    message = "Hello World"
    logger.error("main(): message → %s", message, extra={"event.action": "main"})
    key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    logger.error("main(): key → %s", key, extra={"event.action": "main"})
    mode = "decrypt"  # set to 'encrypt' or 'decrypt'
    logger.error("main(): mode → %s", mode, extra={"event.action": "main"})

    if mode == "encrypt":
        translated = encrypt_message(key, message)
    elif mode == "decrypt":
        translated = decrypt_message(key, message)
        logger.error("main(): translated → %s", translated, extra={"event.action": "main"})
    print(f"Using the key {key}, the {mode}ed message is: {translated}")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
