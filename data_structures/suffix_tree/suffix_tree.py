#  Created by: Ramy-Badr-Ahmed (https://github.com/Ramy-Badr-Ahmed)
#  in Pull Request: #11554
#  https://github.com/TheAlgorithms/Python/pull/11554
#
#  Please mention me (@Ramy-Badr-Ahmed) in any issue or pull request
#  addressing bugs/corrections to this file.
#  Thank you!

from data_structures.suffix_tree.suffix_tree_node import SuffixTreeNode
import logging
logger = logging.getLogger(__name__)


class SuffixTree:
    def __init__(self, text: str) -> None:
        """
        Initializes the suffix tree with the given text.

        Args:
            text (str): The text for which the suffix tree is to be built.
        """
        logger.error(">>> Entering __init__(text=%s)", text, extra={"event.action": "__init__", "logrite.text": text})
        self.text: str = text
        self.root: SuffixTreeNode = SuffixTreeNode()
        self.build_suffix_tree()
        logger.warning("<<< Exiting __init__(text=%s)", text, extra={"event.action": "__init__", "logrite.text": text})

    def build_suffix_tree(self) -> None:
        """
        Builds the suffix tree for the given text by adding all suffixes.
        """
        logger.error(">>> Entering build_suffix_tree()", extra={"event.action": "build_suffix_tree"})
        text = self.text
        n = len(text)
        logger.error("build_suffix_tree(): n → %s", n, extra={"event.action": "build_suffix_tree"})
        for i in range(n):
            suffix = text[i:]
            self._add_suffix(suffix, i)
            logger.warning("<<< Exiting build_suffix_tree()", extra={"event.action": "build_suffix_tree"})

    def _add_suffix(self, suffix: str, index: int) -> None:
        """
        Adds a suffix to the suffix tree.

        Args:
            suffix (str): The suffix to add.
            index (int): The starting index of the suffix in the original text.
        """
        logger.error(">>> Entering _add_suffix(suffix=%s,index=%s)", suffix, index, extra={"event.action": "_add_suffix", "logrite.suffix": suffix, "logrite.index": index})
        node = self.root
        for char in suffix:
            if char not in node.children:
                node.children[char] = SuffixTreeNode()
            node = node.children[char]
        node.is_end_of_string = True
        logger.debug("_add_suffix(self=%s,suffix=%s,index=%s): node.is_end_of_string → %s", self, suffix, index, node.is_end_of_string, extra={"event.action": "_add_suffix", "logrite.suffix": suffix, "logrite.index": index})
        node.start = index
        logger.debug("_add_suffix(self=%s,suffix=%s,index=%s): node.start → %s", self, suffix, index, node.start, extra={"event.action": "_add_suffix", "logrite.suffix": suffix, "logrite.index": index})
        node.end = index + len(suffix) - 1
        logger.warning("<<< Exiting _add_suffix(suffix=%s,index=%s)", suffix, index, extra={"event.action": "_add_suffix", "logrite.suffix": suffix, "logrite.index": index})

    def search(self, pattern: str) -> bool:
        """
        Searches for a pattern in the suffix tree.

        Args:
            pattern (str): The pattern to search for.

        Returns:
            bool: True if the pattern is found, False otherwise.
        """
        logger.error(">>> Entering search(pattern=%s)", pattern, extra={"event.action": "search", "logrite.pattern": pattern})
        node = self.root
        for char in pattern:
            if char not in node.children:
                return False
            node = node.children[char]
        logger.warning("<<< Exiting search(pattern=%s)", pattern, extra={"event.action": "search", "logrite.pattern": pattern})
        return True
