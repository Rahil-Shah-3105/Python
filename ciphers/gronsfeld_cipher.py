from string import ascii_uppercase
import logging
logger = logging.getLogger(__name__)


def gronsfeld(text: str, key: str) -> str:
    """
    Encrypt plaintext with the Gronsfeld cipher

    >>> gronsfeld('hello', '412')
    'LFNPP'
    >>> gronsfeld('hello', '123')
    'IGOMQ'
    >>> gronsfeld('', '123')
    ''
    >>> gronsfeld('yes, ¥€$ - _!@#%?', '0')
    'YES, ¥€$ - _!@#%?'
    >>> gronsfeld('yes, ¥€$ - _!@#%?', '01')
    'YFS, ¥€$ - _!@#%?'
    >>> gronsfeld('yes, ¥€$ - _!@#%?', '012')
    'YFU, ¥€$ - _!@#%?'
    >>> gronsfeld('yes, ¥€$ - _!@#%?', '')
    Traceback (most recent call last):
      ...
    ZeroDivisionError: division by zero
    """
    logger.debug(">>> Entering gronsfeld(text=%s,key=%s)", text, key)
    ascii_len = len(ascii_uppercase)
    logger.debug("gronsfeld(text=%s,key=%s): ascii_len → %s", text, key, ascii_len)
    key_len = len(key)
    logger.debug("gronsfeld(text=%s,key=%s): key_len → %s", text, key, key_len)
    encrypted_text = ""
    logger.debug("gronsfeld(text=%s,key=%s): encrypted_text → %s", text, key, encrypted_text)
    keys = [int(char) for char in key]
    logger.debug("gronsfeld(text=%s,key=%s): keys → %s", text, key, keys)
    upper_case_text = text.upper()
    logger.debug("gronsfeld(text=%s,key=%s): upper_case_text → %s", text, key, upper_case_text)

    for i, char in enumerate(upper_case_text):
        if char in ascii_uppercase:
            new_position = (ascii_uppercase.index(char) + keys[i % key_len]) % ascii_len
            logger.debug("gronsfeld(text=%s,key=%s): new_position → %s", text, key, new_position)
            shifted_letter = ascii_uppercase[new_position]
            logger.debug("gronsfeld(text=%s,key=%s): shifted_letter → %s", text, key, shifted_letter)
            encrypted_text += shifted_letter
        else:
            encrypted_text += char

    logger.debug("<<< Exiting gronsfeld(text=%s,key=%s)", text, key)
    return encrypted_text


if __name__ == "__main__":
    from doctest import testmod

    testmod()
