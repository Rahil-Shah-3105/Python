import random
import sys

from maths.greatest_common_divisor import gcd_by_iterative

from . import cryptomath_module as cryptomath
import logging
logger = logging.getLogger(__name__)

SYMBOLS = (
    r""" !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`"""
    r"""abcdefghijklmnopqrstuvwxyz{|}~"""
)


def check_keys(key_a: int, key_b: int, mode: str) -> None:
    logger.error(">>> Entering check_keys(key_a=%s,key_b=%s,mode=%s)", key_a, key_b, mode, extra={"event.action": "check_keys", "logrite.key_a": key_a, "logrite.key_b": key_b, "logrite.mode": mode})
    if mode == "encrypt":
        if key_a == 1:
            sys.exit(
                "The affine cipher becomes weak when key "
                "A is set to 1. Choose different key"
            )
        if key_b == 0:
            sys.exit(
                "The affine cipher becomes weak when key "
                "B is set to 0. Choose different key"
            )
    if key_a < 0 or key_b < 0 or key_b > len(SYMBOLS) - 1:
        sys.exit(
            "Key A must be greater than 0 and key B must "
            f"be between 0 and {len(SYMBOLS) - 1}."
        )
    if gcd_by_iterative(key_a, len(SYMBOLS)) != 1:
        sys.exit(
            f"Key A {key_a} and the symbol set size {len(SYMBOLS)} "
            "are not relatively prime. Choose a different key."
        )
        logger.warning("<<< Exiting check_keys(key_a=%s,key_b=%s,mode=%s)", key_a, key_b, mode, extra={"event.action": "check_keys", "logrite.key_a": key_a, "logrite.key_b": key_b, "logrite.mode": mode})


def encrypt_message(key: int, message: str) -> str:
    """
    >>> encrypt_message(4545, 'The affine cipher is a type of monoalphabetic '
    ...                       'substitution cipher.')
    'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF{xIp~{HL}Gi'
    """
    logger.error(">>> Entering encrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "encrypt_message", "logrite.key": key, "logrite.message": message})
    key_a, key_b = divmod(key, len(SYMBOLS))
    check_keys(key_a, key_b, "encrypt")
    cipher_text = ""
    logger.error("encrypt_message(key=%s,message=%s): cipher_text → %s", key, message, cipher_text, extra={"event.action": "encrypt_message", "logrite.key": key, "logrite.message": message})
    for symbol in message:
        if symbol in SYMBOLS:
            sym_index = SYMBOLS.find(symbol)
            logger.error("encrypt_message(key=%s,message=%s): sym_index → %s", key, message, sym_index, extra={"event.action": "encrypt_message", "logrite.key": key, "logrite.message": message})
            cipher_text += SYMBOLS[(sym_index * key_a + key_b) % len(SYMBOLS)]
        else:
            cipher_text += symbol
    logger.warning("<<< Exiting encrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "encrypt_message", "logrite.key": key, "logrite.message": message})
    return cipher_text


def decrypt_message(key: int, message: str) -> str:
    """
    >>> decrypt_message(4545, 'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF'
    ...                       '{xIp~{HL}Gi')
    'The affine cipher is a type of monoalphabetic substitution cipher.'
    """
    logger.error(">>> Entering decrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
    key_a, key_b = divmod(key, len(SYMBOLS))
    check_keys(key_a, key_b, "decrypt")
    plain_text = ""
    logger.error("decrypt_message(key=%s,message=%s): plain_text → %s", key, message, plain_text, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
    mod_inverse_of_key_a = cryptomath.find_mod_inverse(key_a, len(SYMBOLS))
    logger.error("decrypt_message(key=%s,message=%s): mod_inverse_of_key_a → %s", key, message, mod_inverse_of_key_a, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
    for symbol in message:
        if symbol in SYMBOLS:
            sym_index = SYMBOLS.find(symbol)
            logger.error("decrypt_message(key=%s,message=%s): sym_index → %s", key, message, sym_index, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
            plain_text += SYMBOLS[
                (sym_index - key_b) * mod_inverse_of_key_a % len(SYMBOLS)
            ]
        else:
            plain_text += symbol
    logger.warning("<<< Exiting decrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
    return plain_text


def get_random_key() -> int:
    logger.error(">>> Entering get_random_key()", extra={"event.action": "get_random_key"})
    while True:
        key_b = random.randint(2, len(SYMBOLS))
        key_b = random.randint(2, len(SYMBOLS))
        logger.error("get_random_key(): key_b → %s", key_b, extra={"event.action": "get_random_key"})
        if gcd_by_iterative(key_b, len(SYMBOLS)) == 1 and key_b % len(SYMBOLS) != 0:
            logger.warning("<<< Exiting get_random_key()", extra={"event.action": "get_random_key"})
            return key_b * len(SYMBOLS) + key_b


def main() -> None:
    """
    >>> key = get_random_key()
    >>> msg = "This is a test!"
    >>> decrypt_message(key, encrypt_message(key, msg)) == msg
    True
    """
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    message = input("Enter message: ").strip()
    logger.error("main(): message → %s", message, extra={"event.action": "main"})
    key = int(input("Enter key [2000 - 9000]: ").strip())
    logger.error("main(): key → %s", key, extra={"event.action": "main"})
    mode = input("Encrypt/Decrypt [E/D]: ").strip().lower()
    logger.error("main(): mode → %s", mode, extra={"event.action": "main"})

    if mode.startswith("e"):
        mode = "encrypt"
        translated = encrypt_message(key, message)
    elif mode.startswith("d"):
        mode = "decrypt"
        translated = decrypt_message(key, message)
        logger.error("main(): translated → %s", translated, extra={"event.action": "main"})
    print(f"\n{mode.title()}ed text: \n{translated}")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # main()
