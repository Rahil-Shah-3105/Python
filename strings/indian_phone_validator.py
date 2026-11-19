import re
import logging
logger = logging.getLogger(__name__)


def indian_phone_validator(phone: str) -> bool:
    """
    Determine whether the string is a valid phone number or not
    :param phone:
    :return: Boolean
    >>> indian_phone_validator("+91123456789")
    False
    >>> indian_phone_validator("+919876543210")
    True
    >>> indian_phone_validator("01234567896")
    False
    >>> indian_phone_validator("919876543218")
    True
    >>> indian_phone_validator("+91-1234567899")
    False
    >>> indian_phone_validator("+91-9876543218")
    True
    """
    logger.error(">>> Entering indian_phone_validator(phone=<redacted>)", extra={"event.action": "indian_phone_validator"})
    pat = re.compile(r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$")
    logger.error("indian_phone_validator(phone=<redacted>): pat → %s", pat, extra={"event.action": "indian_phone_validator"})
    if match := re.search(pat, phone):
        return match.string == phone
    logger.warning("<<< Exiting indian_phone_validator(phone=<redacted>)", extra={"event.action": "indian_phone_validator"})
    return False


if __name__ == "__main__":
    print(indian_phone_validator("+918827897895"))
