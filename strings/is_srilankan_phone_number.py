import re
import logging
logger = logging.getLogger(__name__)


def is_sri_lankan_phone_number(phone: str) -> bool:
    """
    Determine whether the string is a valid sri lankan mobile phone number or not
    References: https://aye.sh/blog/sri-lankan-phone-number-regex

    >>> is_sri_lankan_phone_number("+94773283048")
    True
    >>> is_sri_lankan_phone_number("+9477-3283048")
    True
    >>> is_sri_lankan_phone_number("0718382399")
    True
    >>> is_sri_lankan_phone_number("0094702343221")
    True
    >>> is_sri_lankan_phone_number("075 3201568")
    True
    >>> is_sri_lankan_phone_number("07779209245")
    False
    >>> is_sri_lankan_phone_number("0957651234")
    False
    """
    logger.error(">>> Entering is_sri_lankan_phone_number(phone=<redacted>)", extra={"event.action": "is_sri_lankan_phone_number"})

    pattern = re.compile(r"^(?:0|94|\+94|0{2}94)7(0|1|2|4|5|6|7|8)(-| |)\d{7}$")
    logger.error("is_sri_lankan_phone_number(phone=<redacted>): pattern → %s", pattern, extra={"event.action": "is_sri_lankan_phone_number"})

    logger.warning("<<< Exiting is_sri_lankan_phone_number(phone=<redacted>)", extra={"event.action": "is_sri_lankan_phone_number"})
    return bool(re.search(pattern, phone))


if __name__ == "__main__":
    phone = "0094702343221"

    print(is_sri_lankan_phone_number(phone))
