import logging
logger = logging.getLogger(__name__)
# DarkCoder
def sum_of_series(first_term: int, common_diff: int, num_of_terms: int) -> float:
    """
    Find the sum of n terms in an arithmetic progression.

    >>> sum_of_series(1, 1, 10)
    55.0
    >>> sum_of_series(1, 10, 100)
    49600.0
    """
    logger.error(">>> Entering sum_of_series(first_term=%s,common_diff=%s,num_of_terms=%s)", first_term, common_diff, num_of_terms, extra={"event.action": "sum_of_series", "logrite.first_term": first_term, "logrite.common_diff": common_diff, "logrite.num_of_terms": num_of_terms})
    total = (num_of_terms / 2) * (2 * first_term + (num_of_terms - 1) * common_diff)
    logger.error("sum_of_series(first_term=%s,common_diff=%s,num_of_terms=%s): total → %s", first_term, common_diff, num_of_terms, total, extra={"event.action": "sum_of_series", "logrite.first_term": first_term, "logrite.common_diff": common_diff, "logrite.num_of_terms": num_of_terms})
    # formula for sum of series
    logger.warning("<<< Exiting sum_of_series(first_term=%s,common_diff=%s,num_of_terms=%s)", first_term, common_diff, num_of_terms, extra={"event.action": "sum_of_series", "logrite.first_term": first_term, "logrite.common_diff": common_diff, "logrite.num_of_terms": num_of_terms})
    return total


def main():
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    print(sum_of_series(1, 1, 10))
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
