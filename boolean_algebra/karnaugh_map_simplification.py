import logging
logger = logging.getLogger(__name__)
"""
https://en.wikipedia.org/wiki/Karnaugh_map
https://www.allaboutcircuits.com/technical-articles/karnaugh-map-boolean-algebraic-simplification-technique
"""


def simplify_kmap(kmap: list[list[int]]) -> str:
    """
    Simplify the Karnaugh map.
    >>> simplify_kmap(kmap=[[0, 1], [1, 1]])
    "A'B + AB' + AB"
    >>> simplify_kmap(kmap=[[0, 0], [0, 0]])
    ''
    >>> simplify_kmap(kmap=[[0, 1], [1, -1]])
    "A'B + AB' + AB"
    >>> simplify_kmap(kmap=[[0, 1], [1, 2]])
    "A'B + AB' + AB"
    >>> simplify_kmap(kmap=[[0, 1], [1, 1.1]])
    "A'B + AB' + AB"
    >>> simplify_kmap(kmap=[[0, 1], [1, 'a']])
    "A'B + AB' + AB"
    """
    logger.debug(">>> Entering simplify_kmap(kmap=%s)", kmap)
    simplified_f = []
    logger.debug("simplify_kmap(kmap=%s): simplified_f → %s", kmap, simplified_f)
    for a, row in enumerate(kmap):
        for b, item in enumerate(row):
            if item:
                term = ("A" if a else "A'") + ("B" if b else "B'")
                logger.debug("simplify_kmap(kmap=%s): term → %s", kmap, term)
                simplified_f.append(term)
    logger.debug("<<< Exiting simplify_kmap(kmap=%s)", kmap)
    return " + ".join(simplified_f)


def main() -> None:
    """
    Main function to create and simplify a K-Map.

    >>> main()
    [0, 1]
    [1, 1]
    Simplified Expression:
    A'B + AB' + AB
    """
    logger.debug(">>> Entering main()")
    kmap = [[0, 1], [1, 1]]
    logger.debug("main(): kmap → %s", kmap)

    # Manually generate the product of [0, 1] and [0, 1]

    for row in kmap:
        print(row)

    print("Simplified Expression:")
    print(simplify_kmap(kmap))
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    main()
    print(f"{simplify_kmap(kmap=[[0, 1], [1, 1]]) = }")
