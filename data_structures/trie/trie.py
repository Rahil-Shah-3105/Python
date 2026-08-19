import logging
logger = logging.getLogger(__name__)
"""
A Trie/Prefix Tree is a kind of search tree used to provide quick lookup
of words/patterns in a set of words. A basic Trie however has O(n^2) space complexity
making it impractical in practice. It however provides O(max(search_string, length of
longest word)) lookup time making it an optimal approach when space is not an issue.
"""


class TrieNode:
    def __init__(self) -> None:
        logger.debug(">>> Entering __init__()")
        logger.debug("__init__(self=%s): self.is_leaf → %s", self, self.is_leaf)
        self.nodes: dict[str, TrieNode] = {}  # Mapping from char to TrieNode
        logger.debug("<<< Exiting __init__()")
        self.is_leaf = False

    def insert_many(self, words: list[str]) -> None:
        """
        Inserts a list of words into the Trie
        :param words: list of string words
        :return: None
        """
        logger.debug(">>> Entering insert_many(words=%s)", words)
        for word in words:
            self.insert(word)
            logger.debug("<<< Exiting insert_many(words=%s)", words)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the Trie
        :param word: word to be inserted
        :return: None
        """
        logger.debug(">>> Entering insert(word=%s)", word)
        curr = self
        logger.debug("insert(self=%s,word=%s): curr → %s", self, word, curr)
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = TrieNode()
                logger.debug("<<< Exiting insert(word=%s)", word)
            curr = curr.nodes[char]
        curr.is_leaf = True
        logger.debug("insert(self=%s,word=%s): curr.is_leaf → %s", self, word, curr.is_leaf)

    def find(self, word: str) -> bool:
        """
        Tries to find word in a Trie
        :param word: word to look for
        :return: Returns True if word is found, False otherwise
        """
        logger.debug(">>> Entering find(word=%s)", word)
        curr = self
        logger.debug("find(self=%s,word=%s): curr → %s", self, word, curr)
        for char in word:
            if char not in curr.nodes:
                return False
            curr = curr.nodes[char]
        logger.debug("<<< Exiting find(word=%s)", word)
        return curr.is_leaf

    def delete(self, word: str) -> None:
        """
        Deletes a word in a Trie
        :param word: word to delete
        :return: None
        """
        logger.debug(">>> Entering delete(word=%s)", word)

        logger.debug("<<< Exiting delete(word=%s)", word)
        def _delete(curr: TrieNode, word: str, index: int) -> bool:
            logger.debug(">>> Entering _delete(curr=%s,word=%s,index=%s)", curr, word, index)
            if index == len(word):
                # If word does not exist
                if not curr.is_leaf:
                    return False
                curr.is_leaf = False
                logger.debug("_delete(curr=%s,word=%s,index=%s): curr.is_leaf → %s", curr, word, index, curr.is_leaf)
                return len(curr.nodes) == 0
            char = word[index]
            logger.debug("_delete(curr=%s,word=%s,index=%s): char → %s", curr, word, index, char)
            char_node = curr.nodes.get(char)
            logger.debug("_delete(curr=%s,word=%s,index=%s): char_node → %s", curr, word, index, char_node)
            # If char not in current trie node
            if not char_node:
                return False
            # Flag to check if node can be deleted
            delete_curr = _delete(char_node, word, index + 1)
            logger.debug("_delete(curr=%s,word=%s,index=%s): delete_curr → %s", curr, word, index, delete_curr)
            if delete_curr:
                del curr.nodes[char]
                return len(curr.nodes) == 0
            logger.debug("<<< Exiting _delete(curr=%s,word=%s,index=%s)", curr, word, index)
            return delete_curr

        _delete(self, word, 0)


def print_words(node: TrieNode, word: str) -> None:
    """
    Prints all the words in a Trie
    :param node: root node of Trie
    :param word: Word variable should be empty at start
    :return: None
    """
    logger.debug(">>> Entering print_words(node=%s,word=%s)", node, word)
    if node.is_leaf:
        print(word, end=" ")

    for key, value in node.nodes.items():
        print_words(value, word + key)
        logger.debug("<<< Exiting print_words(node=%s,word=%s)", node, word)


def test_trie() -> bool:
    logger.debug(">>> Entering test_trie()")
    import time; __log_start = time.time()
    words = "banana bananas bandana band apple all beast".split()
    root = TrieNode()
    logger.debug("test_trie(): words → %s", words)
    root.insert_many(words)
    # print_words(root, "")
    logger.warning("test_trie(): root → %s", root)
    logger.debug("test_trie(): root → %s", root)
    logger.info("test_trie()=: save operation took %s ms", int((time.time() - __log_start) * 1000))
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
    logger.debug("<<< Exiting test_trie()")
    return True


def print_results(msg: str, passes: bool) -> None:
    logger.debug(">>> Entering print_results(msg=%s,passes=%s)", msg, passes)
    print(str(msg), "works!" if passes else "doesn't work :(")
    logger.debug("<<< Exiting print_results(msg=%s,passes=%s)", msg, passes)


def pytests() -> None:
    logger.debug(">>> Entering pytests()")
    assert test_trie()
    logger.debug("<<< Exiting pytests()")


def main() -> None:
    """
    >>> pytests()
    """
    logger.debug(">>> Entering main()")
    print_results("Testing trie functionality", test_trie())
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    main()
