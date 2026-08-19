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
    logger.debug(">>> Entering main()")
    message = input("Enter message: ")
    logger.debug("main(): message → %s", message)
    key = int(input(f"Enter key [2-{len(message) - 1}]: "))
    mode = input("Encryption/Decryption [e/d]: ")
    logger.warning("main(): key → %s", key)
    logger.debug("main(): key → %s", key)
    logger.debug("main(): mode → %s", mode)

    if mode.lower().startswith("e"):
        text = encrypt_message(key, message)
    elif mode.lower().startswith("d"):
        text = decrypt_message(key, message)
        logger.debug("main(): text → %s", text)

    # Append pipe symbol (vertical bar) to identify spaces at the end.
    print(f"Output:\n{text + '|'}")
    logger.debug("<<< Exiting main()")


def encrypt_message(key: int, message: str) -> str:
    """
    >>> encrypt_message(6, 'Harshil Darji')
    'Hlia rDsahrij'
    """
    logger.debug(">>> Entering encrypt_message(key=%s,message=%s)", key, message)
    cipher_text = [""] * key
    logger.debug("encrypt_message(key=%s,message=%s): cipher_text → %s", key, message, cipher_text)
    for col in range(key):
        pointer = col
        logger.debug("encrypt_message(key=%s,message=%s): pointer → %s", key, message, pointer)
        while pointer < len(message):
            cipher_text[col] += message[pointer]
            pointer += key
    logger.debug("<<< Exiting encrypt_message(key=%s,message=%s)", key, message)
    return "".join(cipher_text)


def decrypt_message(key: int, message: str) -> str:
    """
    >>> decrypt_message(6, 'Hlia rDsahrij')
    'Harshil Darji'
    """
    logger.debug(">>> Entering decrypt_message(key=%s,message=%s)", key, message)
    num_cols = math.ceil(len(message) / key)
    logger.debug("decrypt_message(key=%s,message=%s): num_cols → %s", key, message, num_cols)
    num_rows = key
    logger.debug("decrypt_message(key=%s,message=%s): num_rows → %s", key, message, num_rows)
    num_shaded_boxes = (num_cols * num_rows) - len(message)
    logger.debug("decrypt_message(key=%s,message=%s): num_shaded_boxes → %s", key, message, num_shaded_boxes)
    plain_text = [""] * num_cols
    logger.debug("decrypt_message(key=%s,message=%s): plain_text → %s", key, message, plain_text)
    col = 0
    logger.debug("decrypt_message(key=%s,message=%s): col → %s", key, message, col)
    row = 0
    logger.debug("decrypt_message(key=%s,message=%s): row → %s", key, message, row)

    for symbol in message:
        plain_text[col] += symbol
        col += 1

        if (col == num_cols) or (
            (col == num_cols - 1) and (row >= num_rows - num_shaded_boxes)
        ):
            col = 0
            row += 1

    logger.debug("<<< Exiting decrypt_message(key=%s,message=%s)", key, message)
    return "".join(plain_text)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
