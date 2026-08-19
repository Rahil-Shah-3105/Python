import logging
logger = logging.getLogger(__name__)
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> None:
    logger.debug(">>> Entering main()")
    message = input("Enter message: ")
    logger.debug("main(): message → %s", message)
    key = input("Enter key [alphanumeric]: ")
    mode = input("Encrypt/Decrypt [e/d]: ")
    logger.warning("main(): key → %s", key)
    logger.debug("main(): key → %s", key)
    logger.debug("main(): mode → %s", mode)

    if mode.lower().startswith("e"):
        mode = "encrypt"
        translated = encrypt_message(key, message)
    elif mode.lower().startswith("d"):
        mode = "decrypt"
        translated = decrypt_message(key, message)
        logger.debug("main(): translated → %s", translated)

    print(f"\n{mode.title()}ed message:")
    logger.debug("<<< Exiting main()")
    print(translated)


def encrypt_message(key: str, message: str) -> str:
    """
    >>> encrypt_message('HDarji', 'This is Harshil Darji from Dharmaj.')
    'Akij ra Odrjqqs Gaisq muod Mphumrs.'
    """
    logger.debug(">>> Entering encrypt_message(key=%s,message=%s)", key, message)
    logger.debug("<<< Exiting encrypt_message(key=%s,message=%s)", key, message)
    return translate_message(key, message, "encrypt")


def decrypt_message(key: str, message: str) -> str:
    """
    >>> decrypt_message('HDarji', 'Akij ra Odrjqqs Gaisq muod Mphumrs.')
    'This is Harshil Darji from Dharmaj.'
    """
    logger.debug(">>> Entering decrypt_message(key=%s,message=%s)", key, message)
    logger.debug("<<< Exiting decrypt_message(key=%s,message=%s)", key, message)
    return translate_message(key, message, "decrypt")


def translate_message(key: str, message: str, mode: str) -> str:
    logger.debug(">>> Entering translate_message(key=%s,message=%s,mode=%s)", key, message, mode)
    translated = []
    logger.debug("translate_message(key=%s,message=%s,mode=%s): translated → %s", key, message, mode, translated)
    key_index = 0
    key = key.upper()
    logger.debug("translate_message(key=%s,message=%s,mode=%s): key → %s", key, message, mode, key)

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        logger.debug("translate_message(key=%s,message=%s,mode=%s): num → %s", key, message, mode, num)
        if num != -1:
            if mode == "encrypt":
                num += LETTERS.find(key[key_index])
            elif mode == "decrypt":
                num -= LETTERS.find(key[key_index])

            num %= len(LETTERS)

            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())

            key_index += 1
            if key_index == len(key):
                key_index = 0
        else:
            translated.append(symbol)
    logger.debug("<<< Exiting translate_message(key=%s,message=%s,mode=%s)", key, message, mode)
    return "".join(translated)


if __name__ == "__main__":
    main()
