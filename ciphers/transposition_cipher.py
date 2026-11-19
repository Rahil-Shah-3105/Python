import math
import logging
logger = logging.getLogger(__name__)

"""
In cryptography, the TRANSPOSITION cipher is a method of encryption where the
positions of plaintext are shifted a certain number(determined by the key) that
follows a regular system that results in the permuted text, known as the encrypted
text. The type of transposition cipher demonstrated under is the ROUTE cipher.
"""


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    message = input("Enter message: ")
    logger.error("main(): message → %s", message, extra={"event.action": "main"})
    key = int(input(f"Enter key [2-{len(message) - 1}]: "))
    logger.error("main(): key → %s", key, extra={"event.action": "main"})
    mode = input("Encryption/Decryption [e/d]: ")
    logger.error("main(): mode → %s", mode, extra={"event.action": "main"})

    if mode.lower().startswith("e"):
        text = encrypt_message(key, message)
    elif mode.lower().startswith("d"):
        text = decrypt_message(key, message)
        logger.error("main(): text → %s", text, extra={"event.action": "main"})

    # Append pipe symbol (vertical bar) to identify spaces at the end.
    print(f"Output:\n{text + '|'}")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


def encrypt_message(key: int, message: str) -> str:
    """
    >>> encrypt_message(6, 'Harshil Darji')
    'Hlia rDsahrij'
    """
    logger.error(">>> Entering encrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "encrypt_message", "logrite.key": key, "logrite.message": message})
    cipher_text = [""] * key
    logger.error("encrypt_message(key=%s,message=%s): cipher_text → %s", key, message, cipher_text, extra={"event.action": "encrypt_message", "logrite.key": key, "logrite.message": message})
    for col in range(key):
        pointer = col
        while pointer < len(message):
            cipher_text[col] += message[pointer]
            pointer += key
    logger.warning("<<< Exiting encrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "encrypt_message", "logrite.key": key, "logrite.message": message})
    return "".join(cipher_text)


def decrypt_message(key: int, message: str) -> str:
    """
    >>> decrypt_message(6, 'Hlia rDsahrij')
    'Harshil Darji'
    """
    logger.error(">>> Entering decrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
    num_cols = math.ceil(len(message) / key)
    logger.error("decrypt_message(key=%s,message=%s): num_cols → %s", key, message, num_cols, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
    num_rows = key
    num_shaded_boxes = (num_cols * num_rows) - len(message)
    logger.error("decrypt_message(key=%s,message=%s): num_shaded_boxes → %s", key, message, num_shaded_boxes, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
    plain_text = [""] * num_cols
    logger.error("decrypt_message(key=%s,message=%s): plain_text → %s", key, message, plain_text, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
    col = 0
    row = 0

    for symbol in message:
        plain_text[col] += symbol
        col += 1

        if (col == num_cols) or (
            (col == num_cols - 1) and (row >= num_rows - num_shaded_boxes)
        ):
            col = 0
            row += 1

    logger.warning("<<< Exiting decrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
    return "".join(plain_text)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
