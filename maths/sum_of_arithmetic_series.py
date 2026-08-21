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
    logger.debug(">>> Entering sum_of_series(first_term=%s,common_diff=%s,num_of_terms=%s)", first_term, common_diff, num_of_terms)
    total = (num_of_terms / 2) * (2 * first_term + (num_of_terms - 1) * common_diff)
    logger.debug("sum_of_series(first_term=%s,common_diff=%s,num_of_terms=%s): total → %s", first_term, common_diff, num_of_terms, total)
    # formula for sum of series
    logger.debug("<<< Exiting sum_of_series(first_term=%s,common_diff=%s,num_of_terms=%s)", first_term, common_diff, num_of_terms)
    return total


def main():
    logger.debug(">>> Entering main()")
    print(sum_of_series(1, 1, 10))
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
