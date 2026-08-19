import logging
logger = logging.getLogger(__name__)
def snake_to_camel_case(input_str: str, use_pascal: bool = False) -> str:
    """
    Transforms a snake_case given string to camelCase (or PascalCase if indicated)
    (defaults to not use Pascal)

    >>> snake_to_camel_case("some_random_string")
    'someRandomString'

    >>> snake_to_camel_case("some_random_string", use_pascal=True)
    'SomeRandomString'

    >>> snake_to_camel_case("some_random_string_with_numbers_123")
    'someRandomStringWithNumbers123'

    >>> snake_to_camel_case("some_random_string_with_numbers_123", use_pascal=True)
    'SomeRandomStringWithNumbers123'

    >>> snake_to_camel_case(123)
    Traceback (most recent call last):
        ...
    ValueError: Expected string as input, found <class 'int'>

    >>> snake_to_camel_case("some_string", use_pascal="True")
    Traceback (most recent call last):
        ...
    ValueError: Expected boolean as use_pascal parameter, found <class 'str'>
    """
    logger.debug(">>> Entering snake_to_camel_case(input_str=%s,use_pascal=%s)", input_str, use_pascal)

    if not isinstance(input_str, str):
        msg = f"Expected string as input, found {type(input_str)}"
        logger.debug("snake_to_camel_case(input_str=%s,use_pascal=%s): msg → %s", input_str, use_pascal, msg)
        raise ValueError(msg)
    if not isinstance(use_pascal, bool):
        msg = f"Expected boolean as use_pascal parameter, found {type(use_pascal)}"
        raise ValueError(msg)

    words = input_str.split("_")
    logger.debug("snake_to_camel_case(input_str=%s,use_pascal=%s): words → %s", input_str, use_pascal, words)

    start_index = 0 if use_pascal else 1
    logger.debug("snake_to_camel_case(input_str=%s,use_pascal=%s): start_index → %s", input_str, use_pascal, start_index)

    words_to_capitalize = words[start_index:]
    logger.debug("snake_to_camel_case(input_str=%s,use_pascal=%s): words_to_capitalize → %s", input_str, use_pascal, words_to_capitalize)

    capitalized_words = [word[0].upper() + word[1:] for word in words_to_capitalize]
    logger.debug("snake_to_camel_case(input_str=%s,use_pascal=%s): capitalized_words → %s", input_str, use_pascal, capitalized_words)

    initial_word = "" if use_pascal else words[0]
    logger.debug("snake_to_camel_case(input_str=%s,use_pascal=%s): initial_word → %s", input_str, use_pascal, initial_word)

    logger.debug("<<< Exiting snake_to_camel_case(input_str=%s,use_pascal=%s)", input_str, use_pascal)
    return "".join([initial_word, *capitalized_words])


if __name__ == "__main__":
    from doctest import testmod

    testmod()
