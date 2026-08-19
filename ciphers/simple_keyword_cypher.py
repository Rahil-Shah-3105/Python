import logging
logger = logging.getLogger(__name__)
def remove_duplicates(key: str) -> str:
    """
    Removes duplicate alphabetic characters in a keyword (letter is ignored after its
    first appearance).

    :param key: Keyword to use
    :return: String with duplicates removed

    >>> remove_duplicates('Hello World!!')
    'Helo Wrd'
    """
    logger.debug(">>> Entering remove_duplicates(key=%s)", key)

    key_no_dups = ""
    logger.debug("remove_duplicates(key=%s): key_no_dups → %s", key, key_no_dups)
    for ch in key:
        if ch == " " or (ch not in key_no_dups and ch.isalpha()):
            key_no_dups += ch
    logger.debug("<<< Exiting remove_duplicates(key=%s)", key)
    return key_no_dups


def create_cipher_map(key: str) -> dict[str, str]:
    """
    Returns a cipher map given a keyword.

    :param key: keyword to use
    :return: dictionary cipher map
    """
    logger.debug(">>> Entering create_cipher_map(key=%s)", key)
    # Create a list of the letters in the alphabet
    alphabet = [chr(i + 65) for i in range(26)]
    logger.debug("create_cipher_map(key=%s): alphabet → %s", key, alphabet)
    # Remove duplicate characters from key
    key = remove_duplicates(key.upper())
    logger.debug("create_cipher_map(key=%s): key → %s", key, key)
    offset = len(key)
    logger.debug("create_cipher_map(key=%s): offset → %s", key, offset)
    # First fill cipher with key characters
    cipher_alphabet = {alphabet[i]: char for i, char in enumerate(key)}
    logger.debug("create_cipher_map(key=%s): cipher_alphabet → %s", key, cipher_alphabet)
    # Then map remaining characters in alphabet to
    # the alphabet from the beginning
    for i in range(len(cipher_alphabet), 26):
        char = alphabet[i - offset]
        logger.debug("create_cipher_map(key=%s): char → %s", key, char)
        # Ensure we are not mapping letters to letters previously mapped
        while char in key:
            offset -= 1
            char = alphabet[i - offset]
        cipher_alphabet[alphabet[i]] = char
    logger.debug("<<< Exiting create_cipher_map(key=%s)", key)
    return cipher_alphabet


def encipher(message: str, cipher_map: dict[str, str]) -> str:
    """
    Enciphers a message given a cipher map.

    :param message: Message to encipher
    :param cipher_map: Cipher map
    :return: enciphered string

    >>> encipher('Hello World!!', create_cipher_map('Goodbye!!'))
    'CYJJM VMQJB!!'
    """
    logger.debug(">>> Entering encipher(message=%s,cipher_map=%s)", message, cipher_map)
    logger.debug("<<< Exiting encipher(message=%s,cipher_map=%s)", message, cipher_map)
    return "".join(cipher_map.get(ch, ch) for ch in message.upper())


def decipher(message: str, cipher_map: dict[str, str]) -> str:
    """
    Deciphers a message given a cipher map

    :param message: Message to decipher
    :param cipher_map: Dictionary mapping to use
    :return: Deciphered string

    >>> cipher_map = create_cipher_map('Goodbye!!')
    >>> decipher(encipher('Hello World!!', cipher_map), cipher_map)
    'HELLO WORLD!!'
    """
    logger.debug(">>> Entering decipher(message=%s,cipher_map=%s)", message, cipher_map)
    # Reverse our cipher mappings
    rev_cipher_map = {v: k for k, v in cipher_map.items()}
    logger.debug("decipher(message=%s,cipher_map=%s): rev_cipher_map → %s", message, cipher_map, rev_cipher_map)
    logger.debug("<<< Exiting decipher(message=%s,cipher_map=%s)", message, cipher_map)
    return "".join(rev_cipher_map.get(ch, ch) for ch in message.upper())


def main() -> None:
    """
    Handles I/O

    :return: void
    """
    logger.debug(">>> Entering main()")
    logger.warning("main(): key → %s", key)
    logger.debug("main(): func → %s", func)
    message = input("Enter message to encode or decode: ").strip()
    logger.debug("main(): message → %s", message)
    key = input("Enter keyword: ").strip()
    logger.debug("main(): key → %s", key)
    option = input("Encipher or decipher? E/D:").strip()[0].lower()
    logger.debug("main(): option → %s", option)
    try:
        func = {"e": encipher, "d": decipher}[option]
    except KeyError:
        raise KeyError("invalid input option")
    cipher_map = create_cipher_map(key)
    logger.debug("main(): cipher_map → %s", cipher_map)
    print(func(message, cipher_map))
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
