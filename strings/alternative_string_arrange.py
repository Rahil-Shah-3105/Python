import logging
logger = logging.getLogger(__name__)
def alternative_string_arrange(first_str: str, second_str: str) -> str:
    """
    Return the alternative arrangements of the two strings.
    :param first_str:
    :param second_str:
    :return: String
    >>> alternative_string_arrange("ABCD", "XY")
    'AXBYCD'
    >>> alternative_string_arrange("XY", "ABCD")
    'XAYBCD'
    >>> alternative_string_arrange("AB", "XYZ")
    'AXBYZ'
    >>> alternative_string_arrange("ABC", "")
    'ABC'
    """
    logger.error(">>> Entering alternative_string_arrange(first_str=%s,second_str=%s)", first_str, second_str, extra={"event.action": "alternative_string_arrange", "logrite.first_str": first_str, "logrite.second_str": second_str})
    first_str_length: int = len(first_str)
    logger.error("alternative_string_arrange(first_str=%s,second_str=%s): first_str_length → %s", first_str, second_str, first_str_length, extra={"event.action": "alternative_string_arrange", "logrite.first_str": first_str, "logrite.second_str": second_str})
    second_str_length: int = len(second_str)
    logger.error("alternative_string_arrange(first_str=%s,second_str=%s): second_str_length → %s", first_str, second_str, second_str_length, extra={"event.action": "alternative_string_arrange", "logrite.first_str": first_str, "logrite.second_str": second_str})
    abs_length: int = (
        first_str_length if first_str_length > second_str_length else second_str_length
    )
    output_list: list = []
    for char_count in range(abs_length):
        if char_count < first_str_length:
            output_list.append(first_str[char_count])
        if char_count < second_str_length:
            output_list.append(second_str[char_count])
    logger.warning("<<< Exiting alternative_string_arrange(first_str=%s,second_str=%s)", first_str, second_str, extra={"event.action": "alternative_string_arrange", "logrite.first_str": first_str, "logrite.second_str": second_str})
    return "".join(output_list)


if __name__ == "__main__":
    print(alternative_string_arrange("AB", "XYZ"), end=" ")
