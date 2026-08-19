import secrets
from random import shuffle
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, punctuation
import logging
logger = logging.getLogger(__name__)


def password_generator(length: int = 8) -> str:
    """
    Password Generator allows you to generate a random password of length N.

    >>> len(password_generator())
    8
    >>> len(password_generator(length=16))
    16
    >>> len(password_generator(257))
    257
    >>> len(password_generator(length=0))
    0
    >>> len(password_generator(-1))
    0
    """
    logger.debug(">>> Entering password_generator(length=%s)", length)
    chars = ascii_letters + digits + punctuation
    logger.debug("password_generator(length=%s): chars → %s", length, chars)
    logger.debug("<<< Exiting password_generator(length=%s)", length)
    return "".join(secrets.choice(chars) for _ in range(length))


# ALTERNATIVE METHODS
# chars_incl= characters that must be in password
# i= how many letters or characters the password length will be
def alternative_password_generator(chars_incl: str, i: int) -> str:
    logger.debug(">>> Entering alternative_password_generator(chars_incl=%s,i=%s)", chars_incl, i)
    # Password Generator = full boot with random_number, random_letters, and
    # random_character FUNCTIONS
    # Put your code here...
    i -= len(chars_incl)
    quotient = i // 3
    logger.debug("alternative_password_generator(chars_incl=%s,i=%s): quotient → %s", chars_incl, i, quotient)
    remainder = i % 3
    logger.debug("alternative_password_generator(chars_incl=%s,i=%s): remainder → %s", chars_incl, i, remainder)
    # chars = chars_incl + random_letters(ascii_letters, i / 3 + remainder) +
    #     random_number(digits, i / 3) + random_characters(punctuation, i / 3)
    chars = (
        chars_incl
        + random(ascii_letters, quotient + remainder)
        + random(digits, quotient)
        + random(punctuation, quotient)
    )
    list_of_chars = list(chars)
    logger.debug("alternative_password_generator(chars_incl=%s,i=%s): list_of_chars → %s", chars_incl, i, list_of_chars)
    shuffle(list_of_chars)
    logger.debug("<<< Exiting alternative_password_generator(chars_incl=%s,i=%s)", chars_incl, i)
    return "".join(list_of_chars)

    # random is a generalised function for letters, characters and numbers


def random(chars_incl: str, i: int) -> str:
    logger.debug(">>> Entering random(chars_incl=%s,i=%s)", chars_incl, i)
    logger.debug("<<< Exiting random(chars_incl=%s,i=%s)", chars_incl, i)
    return "".join(secrets.choice(chars_incl) for _ in range(i))


def is_strong_password(password: str, min_length: int = 8) -> bool:
    """
    This will check whether a given password is strong or not. The password must be at
    least as long as the provided minimum length, and it must contain at least 1
    lowercase letter, 1 uppercase letter, 1 number and 1 special character.

    >>> is_strong_password('Hwea7$2!')
    True
    >>> is_strong_password('Sh0r1')
    False
    >>> is_strong_password('Hello123')
    False
    >>> is_strong_password('Hello1238udfhiaf038fajdvjjf!jaiuFhkqi1')
    True
    >>> is_strong_password('0')
    False
    """
    logger.debug(">>> Entering is_strong_password(password=<redacted>,min_length=%s)", min_length)

    if len(password) < min_length:
        return False

    upper = any(char in ascii_uppercase for char in password)
    logger.debug("is_strong_password(password=<redacted>,min_length=%s): upper → %s", min_length, upper)
    lower = any(char in ascii_lowercase for char in password)
    logger.debug("is_strong_password(password=<redacted>,min_length=%s): lower → %s", min_length, lower)
    num = any(char in digits for char in password)
    logger.debug("is_strong_password(password=<redacted>,min_length=%s): num → %s", min_length, num)
    spec_char = any(char in punctuation for char in password)
    logger.debug("is_strong_password(password=<redacted>,min_length=%s): spec_char → %s", min_length, spec_char)

    logger.debug("<<< Exiting is_strong_password(password=<redacted>,min_length=%s)", min_length)
    return upper and lower and num and spec_char


def main():
    logger.debug(">>> Entering main()")
    length = int(input("Please indicate the max length of your password: ").strip())
    logger.debug("main(): length → %s", length)
    chars_incl = input(
        "Please indicate the characters that must be in your password: "
    ).strip()
    print("Password generated:", password_generator(length))
    logger.debug("main(): chars_incl → %s", chars_incl)
    print(
        "Alternative Password generated:",
        alternative_password_generator(chars_incl, length),
    )
    print("[If you are thinking of using this password, You better save it.]")
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    main()
