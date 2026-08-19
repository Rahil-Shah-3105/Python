from __future__ import annotations
import logging
logger = logging.getLogger(__name__)

END = "#"


class Trie:
    def __init__(self) -> None:
        logger.debug(">>> Entering __init__()")
        self._trie: dict = {}
        logger.debug("<<< Exiting __init__()")

    def insert_word(self, text: str) -> None:
        logger.debug(">>> Entering insert_word(text=%s)", text)
        trie = self._trie
        logger.debug("insert_word(self=%s,text=%s): trie → %s", self, text, trie)
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[END] = True
        logger.debug("<<< Exiting insert_word(text=%s)", text)

    def find_word(self, prefix: str) -> tuple | list:
        logger.debug(">>> Entering find_word(prefix=%s)", prefix)
        trie = self._trie
        logger.debug("find_word(self=%s,prefix=%s): trie → %s", self, prefix, trie)
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return []
        logger.debug("<<< Exiting find_word(prefix=%s)", prefix)
        return self._elements(trie)

    def _elements(self, d: dict) -> tuple:
        logger.debug(">>> Entering _elements(d=%s)", d)
        result = []
        logger.debug("_elements(d=%s): result → %s", d, result)
        for c, v in d.items():
            sub_result = [" "] if c == END else [(c + s) for s in self._elements(v)]
            logger.debug("_elements(d=%s): sub_result → %s", d, sub_result)
            result.extend(sub_result)
        logger.debug("<<< Exiting _elements(d=%s)", d)
        return tuple(result)


trie = Trie()
words = ("depart", "detergent", "daring", "dog", "deer", "deal")
for word in words:
    trie.insert_word(word)


def autocomplete_using_trie(string: str) -> tuple:
    """
    >>> trie = Trie()
    >>> for word in words:
    ...     trie.insert_word(word)
    ...
    >>> matches = autocomplete_using_trie("de")
    >>> "detergent " in matches
    True
    >>> "dog " in matches
    False
    """
    logger.debug(">>> Entering autocomplete_using_trie(string=%s)", string)
    suffixes = trie.find_word(string)
    logger.debug("autocomplete_using_trie(string=%s): suffixes → %s", string, suffixes)
    logger.debug("<<< Exiting autocomplete_using_trie(string=%s)", string)
    return tuple(string + word for word in suffixes)


def main() -> None:
    logger.debug(">>> Entering main()")
    print(autocomplete_using_trie("de"))
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
