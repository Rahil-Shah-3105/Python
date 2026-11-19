import logging
logger = logging.getLogger(__name__)
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    message = input("Enter message: ")
    logger.error("main(): message → %s", message, extra={"event.action": "main"})
    key = input("Enter key [alphanumeric]: ")
    logger.error("main(): key → %s", key, extra={"event.action": "main"})
    mode = input("Encrypt/Decrypt [e/d]: ")
    logger.error("main(): mode → %s", mode, extra={"event.action": "main"})

    if mode.lower().startswith("e"):
        mode = "encrypt"
        translated = encrypt_message(key, message)
    elif mode.lower().startswith("d"):
        mode = "decrypt"
        translated = decrypt_message(key, message)
        logger.error("main(): translated → %s", translated, extra={"event.action": "main"})

    print(f"\n{mode.title()}ed message:")
    print(translated)
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


def encrypt_message(key: str, message: str) -> str:
    """
    >>> encrypt_message('HDarji', 'This is Harshil Darji from Dharmaj.')
    'Akij ra Odrjqqs Gaisq muod Mphumrs.'
    """
    logger.error(">>> Entering encrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "encrypt_message", "logrite.key": key, "logrite.message": message})
    logger.warning("<<< Exiting encrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "encrypt_message", "logrite.key": key, "logrite.message": message})
    return translate_message(key, message, "encrypt")


def decrypt_message(key: str, message: str) -> str:
    """
    >>> decrypt_message('HDarji', 'Akij ra Odrjqqs Gaisq muod Mphumrs.')
    'This is Harshil Darji from Dharmaj.'
    """
    logger.error(">>> Entering decrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
    logger.warning("<<< Exiting decrypt_message(key=%s,message=%s)", key, message, extra={"event.action": "decrypt_message", "logrite.key": key, "logrite.message": message})
    return translate_message(key, message, "decrypt")


def translate_message(key: str, message: str, mode: str) -> str:
    logger.error(">>> Entering translate_message(key=%s,message=%s,mode=%s)", key, message, mode, extra={"event.action": "translate_message", "logrite.key": key, "logrite.message": message, "logrite.mode": mode})
    translated = []
    key_index = 0
    key = key.upper()
    logger.error("translate_message(key=%s,message=%s,mode=%s): key → %s", key, message, mode, key, extra={"event.action": "translate_message", "logrite.key": key, "logrite.message": message, "logrite.mode": mode})

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        logger.error("translate_message(key=%s,message=%s,mode=%s): num → %s", key, message, mode, num, extra={"event.action": "translate_message", "logrite.key": key, "logrite.message": message, "logrite.mode": mode})
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
    logger.warning("<<< Exiting translate_message(key=%s,message=%s,mode=%s)", key, message, mode, extra={"event.action": "translate_message", "logrite.key": key, "logrite.message": message, "logrite.mode": mode})
    return "".join(translated)


if __name__ == "__main__":
    main()
