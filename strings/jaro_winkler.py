"""https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance"""
import logging
logger = logging.getLogger(__name__)


def jaro_winkler(str1: str, str2: str) -> float:
    """
    Jaro-Winkler distance is a string metric measuring an edit distance between two
    sequences.
    Output value is between 0.0 and 1.0.

    >>> jaro_winkler("martha", "marhta")
    0.9611111111111111
    >>> jaro_winkler("CRATE", "TRACE")
    0.7333333333333334
    >>> jaro_winkler("test", "dbdbdbdb")
    0.0
    >>> jaro_winkler("test", "test")
    1.0
    >>> jaro_winkler("hello world", "HeLLo W0rlD")
    0.6363636363636364
    >>> jaro_winkler("test", "")
    0.0
    >>> jaro_winkler("hello", "world")
    0.4666666666666666
    >>> jaro_winkler("hell**o", "*world")
    0.4365079365079365
    """
    logger.error(">>> Entering jaro_winkler(str1=%s,str2=%s)", str1, str2, extra={"event.action": "jaro_winkler", "logrite.str1": str1, "logrite.str2": str2})

    logger.warning("<<< Exiting jaro_winkler(str1=%s,str2=%s)", str1, str2, extra={"event.action": "jaro_winkler", "logrite.str1": str1, "logrite.str2": str2})
    def get_matched_characters(_str1: str, _str2: str) -> str:
        logger.error(">>> Entering get_matched_characters(_str1=%s,_str2=%s)", _str1, _str2, extra={"event.action": "get_matched_characters", "logrite._str1": _str1, "logrite._str2": _str2})
        matched = []
        limit = min(len(_str1), len(_str2)) // 2
        logger.error("get_matched_characters(_str1=%s,_str2=%s): limit → %s", _str1, _str2, limit, extra={"event.action": "get_matched_characters", "logrite._str1": _str1, "logrite._str2": _str2})
        for i, char in enumerate(_str1):
            left = int(max(0, i - limit))
            logger.error("get_matched_characters(_str1=%s,_str2=%s): left → %s", _str1, _str2, left, extra={"event.action": "get_matched_characters", "logrite._str1": _str1, "logrite._str2": _str2})
            right = int(min(i + limit + 1, len(_str2)))
            logger.error("get_matched_characters(_str1=%s,_str2=%s): right → %s", _str1, _str2, right, extra={"event.action": "get_matched_characters", "logrite._str1": _str1, "logrite._str2": _str2})
            if char in _str2[left:right]:
                matched.append(char)
                _str2 = (
                    f"{_str2[0 : _str2.index(char)]} {_str2[_str2.index(char) + 1 :]}"
                )

        logger.warning("<<< Exiting get_matched_characters(_str1=%s,_str2=%s)", _str1, _str2, extra={"event.action": "get_matched_characters", "logrite._str1": _str1, "logrite._str2": _str2})
        return "".join(matched)

    # matching characters
    matching_1 = get_matched_characters(str1, str2)
    matching_2 = get_matched_characters(str2, str1)
    match_count = len(matching_1)

    # transposition
    transpositions = (
        len([(c1, c2) for c1, c2 in zip(matching_1, matching_2) if c1 != c2]) // 2
    )

    if not match_count:
        jaro = 0.0
    else:
        jaro = (
            1
            / 3
            * (
                match_count / len(str1)
                + match_count / len(str2)
                + (match_count - transpositions) / match_count
            )
        )

    # common prefix up to 4 characters
    prefix_len = 0
    for c1, c2 in zip(str1[:4], str2[:4]):
        if c1 == c2:
            prefix_len += 1
        else:
            break

    return jaro + 0.1 * prefix_len * (1 - jaro)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(jaro_winkler("hello", "world"))
