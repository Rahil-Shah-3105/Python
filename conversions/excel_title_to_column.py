import logging
logger = logging.getLogger(__name__)
def excel_title_to_column(column_title: str) -> int:
    """
    Given a string column_title that represents
    the column title in an Excel sheet, return
    its corresponding column number.

    >>> excel_title_to_column("A")
    1
    >>> excel_title_to_column("B")
    2
    >>> excel_title_to_column("AB")
    28
    >>> excel_title_to_column("Z")
    26
    """
    logger.debug(">>> Entering excel_title_to_column(column_title=%s)", column_title)
    assert column_title.isupper()
    answer = 0
    logger.debug("excel_title_to_column(column_title=%s): answer → %s", column_title, answer)
    index = len(column_title) - 1
    logger.debug("excel_title_to_column(column_title=%s): index → %s", column_title, index)
    power = 0
    logger.debug("excel_title_to_column(column_title=%s): power → %s", column_title, power)

    while index >= 0:
        value = (ord(column_title[index]) - 64) * pow(26, power)
        logger.debug("excel_title_to_column(column_title=%s): value → %s", column_title, value)
        answer += value
        power += 1
        index -= 1

    logger.debug("<<< Exiting excel_title_to_column(column_title=%s)", column_title)
    return answer


if __name__ == "__main__":
    from doctest import testmod

    testmod()
