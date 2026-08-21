import random
import sys
import logging
logger = logging.getLogger(__name__)

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> None:
    logger.debug(">>> Entering main()")
    message = input("Enter message: ")
    logger.debug("main(): message → %s", message)
    key = "LFWOAYUISVKMNXPBDCRJTQEGHZ"
    resp = input("Encrypt/Decrypt [e/d]: ")
    logger.warning("main(): key → %s", key)
    logger.debug("main(): key → %s", key)
    logger.debug("main(): resp → %s", resp)

    check_valid_key(key)

    if resp.lower().startswith("e"):
        mode = "encrypt"
        logger.debug("main(): mode → %s", mode)
        translated = encrypt_message(key, message)
        logger.debug("main(): translated → %s", translated)
    elif resp.lower().startswith("d"):
        mode = "decrypt"
        translated = decrypt_message(key, message)

        logger.debug("<<< Exiting main()")
    print(f"\n{mode.title()}ion: \n{translated}")


def check_valid_key(key: str) -> None:
    logger.debug(">>> Entering check_valid_key(key=%s)", key)
    key_list = list(key)
    logger.debug("check_valid_key(key=%s): key_list → %s", key, key_list)
    letters_list = list(LETTERS)
    key_list.sort()
    logger.debug("check_valid_key(key=%s): letters_list → %s", key, letters_list)
    letters_list.sort()

    if key_list != letters_list:
        sys.exit("Error in the key or symbol set.")
        logger.debug("<<< Exiting check_valid_key(key=%s)", key)


def encrypt_message(key: str, message: str) -> str:
    """
    >>> encrypt_message('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Harshil Darji')
    'Ilcrism Olcvs'
    """
    logger.debug(">>> Entering encrypt_message(key=%s,message=%s)", key, message)
    logger.debug("<<< Exiting encrypt_message(key=%s,message=%s)", key, message)
    return translate_message(key, message, "encrypt")


def decrypt_message(key: str, message: str) -> str:
    """
    >>> decrypt_message('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Ilcrism Olcvs')
    'Harshil Darji'
    """
    logger.debug(">>> Entering decrypt_message(key=%s,message=%s)", key, message)
    logger.debug("<<< Exiting decrypt_message(key=%s,message=%s)", key, message)
    return translate_message(key, message, "decrypt")


def translate_message(key: str, message: str, mode: str) -> str:
    logger.debug(">>> Entering translate_message(key=%s,message=%s,mode=%s)", key, message, mode)
    translated = ""
    logger.debug("translate_message(key=%s,message=%s,mode=%s): translated → %s", key, message, mode, translated)
    chars_a = LETTERS
    chars_b = key
    logger.debug("translate_message(key=%s,message=%s,mode=%s): chars_a → %s", key, message, mode, chars_a)
    logger.debug("translate_message(key=%s,message=%s,mode=%s): chars_b → %s", key, message, mode, chars_b)

    if mode == "decrypt":
        chars_a, chars_b = chars_b, chars_a

    for symbol in message:
        if symbol.upper() in chars_a:
            sym_index = chars_a.find(symbol.upper())
            logger.debug("translate_message(key=%s,message=%s,mode=%s): sym_index → %s", key, message, mode, sym_index)
            if symbol.isupper():
                translated += chars_b[sym_index].upper()
            else:
                translated += chars_b[sym_index].lower()
        else:
            translated += symbol

    logger.debug("<<< Exiting translate_message(key=%s,message=%s,mode=%s)", key, message, mode)
    return translated


def get_random_key() -> str:
    logger.debug(">>> Entering get_random_key()")
    logger.warning("get_random_key(): key → %s", key)
    key = list(LETTERS)
    logger.debug("get_random_key(): key → %s", key)
    random.shuffle(key)
    logger.debug("<<< Exiting get_random_key()")
    return "".join(key)


if __name__ == "__main__":
    main()
