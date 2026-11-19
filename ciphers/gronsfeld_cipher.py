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
    logger.error(">>> Entering gronsfeld(text=%s,key=%s)", text, key, extra={"event.action": "gronsfeld", "logrite.text": text, "logrite.key": key})
    ascii_len = len(ascii_uppercase)
    logger.error("gronsfeld(text=%s,key=%s): ascii_len → %s", text, key, ascii_len, extra={"event.action": "gronsfeld", "logrite.text": text, "logrite.key": key})
    key_len = len(key)
    logger.error("gronsfeld(text=%s,key=%s): key_len → %s", text, key, key_len, extra={"event.action": "gronsfeld", "logrite.text": text, "logrite.key": key})
    encrypted_text = ""
    logger.error("gronsfeld(text=%s,key=%s): encrypted_text → %s", text, key, encrypted_text, extra={"event.action": "gronsfeld", "logrite.text": text, "logrite.key": key})
    keys = [int(char) for char in key]
    logger.error("gronsfeld(text=%s,key=%s): keys → %s", text, key, keys, extra={"event.action": "gronsfeld", "logrite.text": text, "logrite.key": key})
    upper_case_text = text.upper()
    logger.error("gronsfeld(text=%s,key=%s): upper_case_text → %s", text, key, upper_case_text, extra={"event.action": "gronsfeld", "logrite.text": text, "logrite.key": key})

    for i, char in enumerate(upper_case_text):
        if char in ascii_uppercase:
            new_position = (ascii_uppercase.index(char) + keys[i % key_len]) % ascii_len
            logger.error("gronsfeld(text=%s,key=%s): new_position → %s", text, key, new_position, extra={"event.action": "gronsfeld", "logrite.text": text, "logrite.key": key})
            shifted_letter = ascii_uppercase[new_position]
            encrypted_text += shifted_letter
        else:
            encrypted_text += char

    logger.warning("<<< Exiting gronsfeld(text=%s,key=%s)", text, key, extra={"event.action": "gronsfeld", "logrite.text": text, "logrite.key": key})
    return encrypted_text


if __name__ == "__main__":
    from doctest import testmod

    testmod()
