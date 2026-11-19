"""
https://en.wikipedia.org/wiki/Karnaugh_map
https://www.allaboutcircuits.com/technical-articles/karnaugh-map-boolean-algebraic-simplification-technique
"""
import logging
logger = logging.getLogger(__name__)


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
    logger.error(">>> Entering simplify_kmap(kmap=%s)", kmap, extra={"event.action": "simplify_kmap", "logrite.kmap": kmap})
    simplified_f = []
    for a, row in enumerate(kmap):
        for b, item in enumerate(row):
            if item:
                term = ("A" if a else "A'") + ("B" if b else "B'")
                logger.error("simplify_kmap(kmap=%s): term → %s", kmap, term, extra={"event.action": "simplify_kmap", "logrite.kmap": kmap})
                simplified_f.append(term)
    logger.warning("<<< Exiting simplify_kmap(kmap=%s)", kmap, extra={"event.action": "simplify_kmap", "logrite.kmap": kmap})
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
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    kmap = [[0, 1], [1, 1]]

    # Manually generate the product of [0, 1] and [0, 1]

    for row in kmap:
        print(row)

    print("Simplified Expression:")
    print(simplify_kmap(kmap))
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
    print(f"{simplify_kmap(kmap=[[0, 1], [1, 1]]) = }")
