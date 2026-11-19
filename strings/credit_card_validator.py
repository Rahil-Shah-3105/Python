"""
Functions for testing the validity of credit card numbers.

https://en.wikipedia.org/wiki/Luhn_algorithm
"""
import logging
logger = logging.getLogger(__name__)


def validate_initial_digits(credit_card_number: str) -> bool:
    """
    Function to validate initial digits of a given credit card number.
    >>> valid = "4111111111111111 41111111111111 34 35 37 412345 523456 634567"
    >>> all(validate_initial_digits(cc) for cc in valid.split())
    True
    >>> invalid = "14 25 76 32323 36111111111111"
    >>> all(validate_initial_digits(cc) is False for cc in invalid.split())
    True
    """
    logger.error(">>> Entering validate_initial_digits(credit_card_number=<redacted>)", extra={"event.action": "validate_initial_digits"})
    logger.warning("<<< Exiting validate_initial_digits(credit_card_number=<redacted>)", extra={"event.action": "validate_initial_digits"})
    return credit_card_number.startswith(("34", "35", "37", "4", "5", "6"))


def luhn_validation(credit_card_number: str) -> bool:
    """
    Function to luhn algorithm validation for a given credit card number.
    >>> luhn_validation('4111111111111111')
    True
    >>> luhn_validation('36111111111111')
    True
    >>> luhn_validation('41111111111111')
    False
    """
    logger.error(">>> Entering luhn_validation(credit_card_number=<redacted>)", extra={"event.action": "luhn_validation"})
    cc_number = credit_card_number
    logger.error("luhn_validation(credit_card_number=<redacted>): cc_number → %s", cc_number, extra={"event.action": "luhn_validation"})
    total = 0
    logger.error("luhn_validation(credit_card_number=<redacted>): total → %s", total, extra={"event.action": "luhn_validation"})
    half_len = len(cc_number) - 2
    logger.error("luhn_validation(credit_card_number=<redacted>): half_len → %s", half_len, extra={"event.action": "luhn_validation"})
    for i in range(half_len, -1, -2):
        #  double the value of every second digit
        digit = int(cc_number[i])
        logger.error("luhn_validation(credit_card_number=<redacted>): digit → %s", digit, extra={"event.action": "luhn_validation"})
        digit *= 2
        # If doubling of a number results in a two digit number
        # i.e greater than 9(e.g., 6 x 2 = 12),
        # then add the digits of the product (e.g., 12: 1 + 2 = 3, 15: 1 + 5 = 6),
        # to get a single digit number.
        if digit > 9:
            digit %= 10
            digit += 1
        cc_number = cc_number[:i] + str(digit) + cc_number[i + 1 :]
        total += digit

    # Sum up the remaining digits
    for i in range(len(cc_number) - 1, -1, -2):
        total += int(cc_number[i])

    logger.warning("<<< Exiting luhn_validation(credit_card_number=<redacted>)", extra={"event.action": "luhn_validation"})
    return total % 10 == 0


def validate_credit_card_number(credit_card_number: str) -> bool:
    """
    Function to validate the given credit card number.
    >>> validate_credit_card_number('4111111111111111')
    4111111111111111 is a valid credit card number.
    True
    >>> validate_credit_card_number('helloworld$')
    helloworld$ is an invalid credit card number because it has nonnumerical characters.
    False
    >>> validate_credit_card_number('32323')
    32323 is an invalid credit card number because of its length.
    False
    >>> validate_credit_card_number('32323323233232332323')
    32323323233232332323 is an invalid credit card number because of its length.
    False
    >>> validate_credit_card_number('36111111111111')
    36111111111111 is an invalid credit card number because of its first two digits.
    False
    >>> validate_credit_card_number('41111111111111')
    41111111111111 is an invalid credit card number because it fails the Luhn check.
    False
    """
    logger.error(">>> Entering validate_credit_card_number(credit_card_number=<redacted>)", extra={"event.action": "validate_credit_card_number"})
    error_message = f"{credit_card_number} is an invalid credit card number because"
    logger.error("validate_credit_card_number(credit_card_number=<redacted>): error_message → %s", error_message, extra={"event.action": "validate_credit_card_number"})
    if not credit_card_number.isdigit():
        print(f"{error_message} it has nonnumerical characters.")
        return False

    if not 13 <= len(credit_card_number) <= 16:
        print(f"{error_message} of its length.")
        return False

    if not validate_initial_digits(credit_card_number):
        print(f"{error_message} of its first two digits.")
        return False

    if not luhn_validation(credit_card_number):
        print(f"{error_message} it fails the Luhn check.")
        return False

    print(f"{credit_card_number} is a valid credit card number.")
    logger.warning("<<< Exiting validate_credit_card_number(credit_card_number=<redacted>)", extra={"event.action": "validate_credit_card_number"})
    return True


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    validate_credit_card_number("4111111111111111")
    validate_credit_card_number("32323")
