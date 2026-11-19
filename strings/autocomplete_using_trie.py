from __future__ import annotations
import logging
logger = logging.getLogger(__name__)

END = "#"


class Trie:
    def __init__(self) -> None:
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self._trie: dict = {}
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})

    def insert_word(self, text: str) -> None:
        logger.error(">>> Entering insert_word(text=%s)", text, extra={"event.action": "insert_word", "logrite.text": text})
        trie = self._trie
        for char in text:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]
        trie[END] = True
        logger.warning("<<< Exiting insert_word(text=%s)", text, extra={"event.action": "insert_word", "logrite.text": text})

    def find_word(self, prefix: str) -> tuple | list:
        logger.error(">>> Entering find_word(prefix=%s)", prefix, extra={"event.action": "find_word", "logrite.prefix": prefix})
        trie = self._trie
        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return []
        logger.warning("<<< Exiting find_word(prefix=%s)", prefix, extra={"event.action": "find_word", "logrite.prefix": prefix})
        return self._elements(trie)

    def _elements(self, d: dict) -> tuple:
        logger.error(">>> Entering _elements(d=%s)", d, extra={"event.action": "_elements", "logrite.d": d})
        result = []
        logger.error("_elements(d=%s): result → %s", d, result, extra={"event.action": "_elements", "logrite.d": d})
        for c, v in d.items():
            sub_result = [" "] if c == END else [(c + s) for s in self._elements(v)]
            logger.error("_elements(d=%s): sub_result → %s", d, sub_result, extra={"event.action": "_elements", "logrite.d": d})
            result.extend(sub_result)
        logger.warning("<<< Exiting _elements(d=%s)", d, extra={"event.action": "_elements", "logrite.d": d})
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
    logger.error(">>> Entering autocomplete_using_trie(string=%s)", string, extra={"event.action": "autocomplete_using_trie", "logrite.string": string})
    suffixes = trie.find_word(string)
    logger.error("autocomplete_using_trie(string=%s): suffixes → %s", string, suffixes, extra={"event.action": "autocomplete_using_trie", "logrite.string": string})
    logger.warning("<<< Exiting autocomplete_using_trie(string=%s)", string, extra={"event.action": "autocomplete_using_trie", "logrite.string": string})
    return tuple(string + word for word in suffixes)


def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    print(autocomplete_using_trie("de"))
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
