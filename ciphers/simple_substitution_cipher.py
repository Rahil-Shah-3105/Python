import random
import sys
import logging
logger = logging.getLogger(__name__)

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    message = input("Enter message: ")
    logger.error("main(): message → %s", message, extra={"event.action": "main"})
    key = "LFWOAYUISVKMNXPBDCRJTQEGHZ"
    logger.error("main(): key → %s", key, extra={"event.action": "main"})
    resp = input("Encrypt/Decrypt [e/d]: ")
    logger.error("main(): resp → %s", resp, extra={"event.action": "main"})

    check_valid_key(key)

    if resp.lower().startswith("e"):
        mode = "encrypt"
        logger.error("main(): mode → %s", mode, extra={"event.action": "main"})
        translated = encrypt_message(key, message)
    elif resp.lower().startswith("d"):
        mode = "decrypt"
        translated = decrypt_message(key, message)
        logger.error("main(): translated → %s", translated, extra={"event.action": "main"})

    print(f"\n{mode.title()}ion: \n{translated}")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


def check_valid_key(key: str) -> None:
    logger.error(">>> Entering check_valid_key(key=%s)", key, extra={"event.action": "check_valid_key", "logrite.key": key})
    key_list = list(key)
    logger.error("check_valid_key(key=%s): key_list → %s", key, key_list, extra={"event.action": "check_valid_key", "logrite.key": key})
    letters_list = list(LETTERS)
    logger.error("check_valid_key(key=%s): letters_list → %s", key, letters_list, extra={"event.action": "check_valid_key", "logrite.key": key})
    key_list.sort()
    letters_list.sort()

    if key_list != letters_list:
        sys.exit("Error in the key or symbol set.")
        logger.warning("<<< Exiting check_valid_key(key=%s)", key, extra={"event.action": "check_valid_key", "logrite.key": key})


def encrypt_message(key: str, message: str) -> str:
    """
    >>> encrypt_message('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Harshil Darji')
    'Ilcrism Olcvs'
    """
    logger.error(">>> Entering encrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "encrypt_message", "logrite.key": key, "logrite.message": message})
    logger.warning("<<< Exiting encrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "encrypt_message", "logrite.key": key, "logrite.message": message})
    return translate_message(key, message, "encrypt")


def decrypt_message(key: str, message: str) -> str:
    """
    >>> decrypt_message('LFWOAYUISVKMNXPBDCRJTQEGHZ', 'Ilcrism Olcvs')
    'Harshil Darji'
    """
    logger.error(">>> Entering decrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
    logger.warning("<<< Exiting decrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
    return translate_message(key, message, "decrypt")


def translate_message(key: str, message: str, mode: str) -> str:
    logger.error(">>> Entering translate_message(key=%s,message=%s,mode=%s)", key, message, mode, extra={"event.action": "translate_message", "logrite.key": key, "logrite.message": message, "logrite.mode": mode})
    translated = ""
    logger.error("translate_message(key=%s,message=%s,mode=%s): translated → %s", key, message, mode, translated, extra={"event.action": "translate_message", "logrite.key": key, "logrite.message": message, "logrite.mode": mode})
    chars_a = LETTERS
    chars_b = key

    if mode == "decrypt":
        chars_a, chars_b = chars_b, chars_a

    for symbol in message:
        if symbol.upper() in chars_a:
            sym_index = chars_a.find(symbol.upper())
            logger.error("translate_message(key=%s,message=%s,mode=%s): sym_index → %s", key, message, mode, sym_index, extra={"event.action": "translate_message", "logrite.key": key, "logrite.message": message, "logrite.mode": mode})
            if symbol.isupper():
                translated += chars_b[sym_index].upper()
            else:
                translated += chars_b[sym_index].lower()
        else:
            translated += symbol

    logger.warning("<<< Exiting translate_message(key=%s,message=%s,mode=%s)", key, message, mode, extra={"event.action": "translate_message", "logrite.key": key, "logrite.message": message, "logrite.mode": mode})
    return translated


def get_random_key() -> str:
    logger.error(">>> Entering get_random_key()", extra={"event.action": "get_random_key"})
    key = list(LETTERS)
    logger.error("get_random_key(): key → %s", key, extra={"event.action": "get_random_key"})
    random.shuffle(key)
    logger.warning("<<< Exiting get_random_key()", extra={"event.action": "get_random_key"})
    return "".join(key)


if __name__ == "__main__":
    main()
