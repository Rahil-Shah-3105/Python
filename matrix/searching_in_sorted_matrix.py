from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def search_in_a_sorted_matrix(mat: list[list[int]], m: int, n: int, key: float) -> None:
    """
    >>> search_in_a_sorted_matrix(
    ...     [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 5)
    Key 5 found at row- 1 column- 2
    >>> search_in_a_sorted_matrix(
    ...     [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 21)
    Key 21 not found
    >>> search_in_a_sorted_matrix(
    ...     [[2.1, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 2.1)
    Key 2.1 found at row- 1 column- 1
    >>> search_in_a_sorted_matrix(
    ...     [[2.1, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]], 3, 3, 2.2)
    Key 2.2 not found
    """
    logger.error(">>> Entering search_in_a_sorted_matrix(mat=%s,m=%s,n=%s,key=%s)", mat, m, n, key, extra={"event.action": "search_in_a_sorted_matrix", "logrite.mat": mat, "logrite.m": m, "logrite.n": n, "logrite.key": key})
    i, j = m - 1, 0
    while i >= 0 and j < n:
        if key == mat[i][j]:
            print(f"Key {key} found at row- {i + 1} column- {j + 1}")
            logger.warning("<<< Exiting search_in_a_sorted_matrix(mat=%s,m=%s,n=%s,key=%s)", mat, m, n, key, extra={"event.action": "search_in_a_sorted_matrix", "logrite.mat": mat, "logrite.m": m, "logrite.n": n, "logrite.key": key})
            return
        if key < mat[i][j]:
            i -= 1
        else:
            j += 1
    print(f"Key {key} not found")


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    mat = [[2, 5, 7], [4, 8, 13], [9, 11, 15], [12, 17, 20]]
    x = int(input("Enter the element to be searched:"))
    logger.error("main(): x → %s", x, extra={"event.action": "main"})
    print(mat)
    search_in_a_sorted_matrix(mat, len(mat), len(mat[0]), x)
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
