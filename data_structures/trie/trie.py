"""
A Trie/Prefix Tree is a kind of search tree used to provide quick lookup
of words/patterns in a set of words. A basic Trie however has O(n^2) space complexity
making it impractical in practice. It however provides O(max(search_string, length of
longest word)) lookup time making it an optimal approach when space is not an issue.
"""
import time
import logging
logger = logging.getLogger(__name__)


class TrieNode:
    def __init__(self) -> None:
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.nodes: dict[str, TrieNode] = {}  # Mapping from char to TrieNode
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})
        self.is_leaf = False
        logger.debug("__init__(self=%s): self.is_leaf → %s", self, self.is_leaf, extra={"event.action": "__init__"})

    def insert_many(self, words: list[str]) -> None:
        """
        Inserts a list of words into the Trie
        :param words: list of string words
        :return: None
        """
        logger.error(">>> Entering insert_many(words=%s)", words, extra={"event.action": "insert_many", "logrite.words": words})
        for word in words:
            self.insert(word)
            logger.warning("<<< Exiting insert_many(words=%s)", words, extra={"event.action": "insert_many", "logrite.words": words})

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie
        :param word: word to be inserted
        :return: None
        """
        logger.error(">>> Entering insert(word=%s)", word, extra={"event.action": "insert", "logrite.word": word})
        curr = self
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
            curr = curr.nodes[char]
            logger.warning("<<< Exiting insert(word=%s)", word, extra={"event.action": "insert", "logrite.word": word})
        curr.is_leaf = True
        logger.debug("insert(self=%s,word=%s): curr.is_leaf → %s", self, word, curr.is_leaf, extra={"event.action": "insert", "logrite.word": word})

    def find(self, word: str) -> bool:
        """
        Tries to find word in a Trie
        :param word: word to look for
        :return: Returns True if word is found, False otherwise
        """
        logger.error(">>> Entering find(word=%s)", word, extra={"event.action": "find", "logrite.word": word})
        curr = self
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        logger.warning("<<< Exiting find(word=%s)", word, extra={"event.action": "find", "logrite.word": word})
        return curr.is_leaf

    def delete(self, word: str) -> None:
        """
        Deletes a word in a Trie
        :param word: word to delete
        :return: None
        """
        logger.error(">>> Entering delete(word=%s)", word, extra={"event.action": "delete", "logrite.word": word})

        logger.warning("<<< Exiting delete(word=%s)", word, extra={"event.action": "delete", "logrite.word": word})
        def _delete(curr: TrieNode, word: str, index: int) -> bool:
            logger.error(">>> Entering _delete(curr=%s,word=%s,index=%s)", curr, word, index, extra={"event.action": "_delete", "logrite.curr": curr, "logrite.word": word, "logrite.index": index})
            if index == len(word):
                # If word does not exist
                if not curr.is_leaf:
                    return False
                curr.is_leaf = False
                logger.debug("_delete(curr=%s,word=%s,index=%s): curr.is_leaf → %s", curr, word, index, curr.is_leaf, extra={"event.action": "_delete", "logrite.curr": curr, "logrite.word": word, "logrite.index": index})
                return len(curr.nodes) == 0
            char = word[index]
            char_node = curr.nodes.get(char)
            # If char not in current trie node
            if not char_node:
                return False
            # Flag to check if node can be deleted
            delete_curr = _delete(char_node, word, index + 1)
            if delete_curr:
                del curr.nodes[char]
                return len(curr.nodes) == 0
            logger.warning("<<< Exiting _delete(curr=%s,word=%s,index=%s)", curr, word, index, extra={"event.action": "_delete", "logrite.curr": curr, "logrite.word": word, "logrite.index": index})
            return delete_curr

        _delete(self, word, 0)


def print_words(node: TrieNode, word: str) -> None:
    """
    Prints all the words in a Trie
    :param node: root node of Trie
    :param word: Word variable should be empty at start
    :return: None
    """
    logger.error(">>> Entering print_words(node=%s,word=%s)", node, word, extra={"event.action": "print_words", "logrite.node": node, "logrite.word": word})
    if node.is_leaf:
        print(word, end=" ")

    for key, value in node.nodes.items():
        print_words(value, word + key)
        logger.warning("<<< Exiting print_words(node=%s,word=%s)", node, word, extra={"event.action": "print_words", "logrite.node": node, "logrite.word": word})


def test_trie() -> bool:
    logger.error(">>> Entering test_trie()", extra={"event.action": "test_trie"})
    __log_start = time.time()
    words = "banana bananas bandana band apple all beast".split()
    root = TrieNode()
    logger.error("test_trie(): words → %s", words, extra={"event.action": "test_trie"})
    logger.error("test_trie(): root → %s", root, extra={"event.action": "test_trie"})
    root.insert_many(words)
    # print_words(root, "")
    logger.error("test_trie()=: save operation took %s ms", int((time.time() - __log_start) * 1000), extra={"event.action": "test_trie", "event.category": "database"})
    assert all(root.find(word) for word in words)
    assert root.find("banana")
    assert not root.find("bandanas")
    assert not root.find("apps")
    assert root.find("apple")
    assert root.find("all")
    root.delete("all")
    assert not root.find("all")
    root.delete("banana")
    assert not root.find("banana")
    assert root.find("bananas")
    logger.warning("<<< Exiting test_trie()", extra={"event.action": "test_trie"})
    return True


def print_results(msg: str, passes: bool) -> None:
    logger.error(">>> Entering print_results(msg=%s,passes=%s)", msg, passes, extra={"event.action": "print_results", "logrite.msg": msg, "logrite.passes": passes})
    print(str(msg), "works!" if passes else "doesn't work :(")
    logger.warning("<<< Exiting print_results(msg=%s,passes=%s)", msg, passes, extra={"event.action": "print_results", "logrite.msg": msg, "logrite.passes": passes})


def pytests() -> None:
    logger.error(">>> Entering pytests()", extra={"event.action": "pytests"})
    assert test_trie()
    logger.warning("<<< Exiting pytests()", extra={"event.action": "pytests"})


def main() -> None:
    """
    >>> pytests()
    """
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    print_results("Testing trie functionality", test_trie())
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
