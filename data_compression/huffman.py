from __future__ import annotations

import sys
import logging
logger = logging.getLogger(__name__)


class Letter:
    def __init__(self, letter: str, freq: int):
        logger.debug(">>> Entering __init__(letter=%s,freq=%s)", letter, freq)
        self.letter: str = letter
        self.freq: int = freq
        self.bitstring: dict[str, str] = {}
        logger.debug("<<< Exiting __init__(letter=%s,freq=%s)", letter, freq)
        logger.debug(">>> Entering __init__(freq=%s,left=%s,right=%s)", freq, left, right)
        logger.debug("<<< Exiting __init__(freq=%s,left=%s,right=%s)", freq, left, right)

    def __repr__(self) -> str:
        logger.debug(">>> Entering __repr__()")
        logger.debug("<<< Exiting __repr__()")
        return f"{self.letter}:{self.freq}"


class TreeNode:
    def __init__(self, freq: int, left: Letter | TreeNode, right: Letter | TreeNode):
        self.freq: int = freq
        self.left: Letter | TreeNode = left
        self.right: Letter | TreeNode = right


def parse_file(file_path: str) -> list[Letter]:
    """
    Read the file and build a dict of all letters and their
    frequencies, then convert the dict into a list of Letters.
    """
    logger.debug(">>> Entering parse_file(file_path=%s)", file_path)
    chars: dict[str, int] = {}
    with open(file_path) as f:
        logger.error("Exception in parse_file(file_path=%s)", file_path, exc_info=True)
        while True:
            c = f.read(1)
            logger.debug("parse_file(file_path=%s): c → %s", file_path, c)
            if not c:
                break
            chars[c] = chars[c] + 1 if c in chars else 1
    logger.debug("<<< Exiting parse_file(file_path=%s)", file_path)
    return sorted((Letter(c, f) for c, f in chars.items()), key=lambda x: x.freq)


def build_tree(letters: list[Letter]) -> Letter | TreeNode:
    """
    Run through the list of Letters and build the min heap
    for the Huffman Tree.
    """
    logger.debug(">>> Entering build_tree(letters=%s)", letters)
    response: list[Letter | TreeNode] = list(letters)
    while len(response) > 1:
        left = response.pop(0)
        logger.debug("build_tree(letters=%s): left → %s", letters, left)
        right = response.pop(0)
        logger.debug("build_tree(letters=%s): right → %s", letters, right)
        total_freq = left.freq + right.freq
        logger.debug("build_tree(letters=%s): total_freq → %s", letters, total_freq)
        node = TreeNode(total_freq, left, right)
        logger.debug("build_tree(letters=%s): node → %s", letters, node)
        response.append(node)
        response.sort(key=lambda x: x.freq)
    logger.debug("<<< Exiting build_tree(letters=%s)", letters)
    return response[0]


def traverse_tree(root: Letter | TreeNode, bitstring: str) -> list[Letter]:
    """
    Recursively traverse the Huffman Tree to set each
    Letter's bitstring dictionary, and return the list of Letters
    """
    logger.debug(">>> Entering traverse_tree(root=%s,bitstring=%s)", root, bitstring)
    if isinstance(root, Letter):
        root.bitstring[root.letter] = bitstring
        return [root]
    treenode: TreeNode = root
    letters = []
    logger.debug("traverse_tree(root=%s,bitstring=%s): letters → %s", root, bitstring, letters)
    letters += traverse_tree(treenode.left, bitstring + "0")
    letters += traverse_tree(treenode.right, bitstring + "1")
    logger.debug("<<< Exiting traverse_tree(root=%s,bitstring=%s)", root, bitstring)
    return letters


def huffman(file_path: str) -> None:
    """
    Parse the file, build the tree, then run through the file
    again, using the letters dictionary to find and print out the
    bitstring for each letter.
    """
    logger.debug(">>> Entering huffman(file_path=%s)", file_path)
    logger.warning("huffman(file_path=%s): root → %s", file_path, root)
    letters_list = parse_file(file_path)
    logger.debug("huffman(file_path=%s): letters_list → %s", file_path, letters_list)
    root = build_tree(letters_list)
    logger.debug("huffman(file_path=%s): root → %s", file_path, root)
    letters = {
        k: v for letter in traverse_tree(root, "") for k, v in letter.bitstring.items()
    }
    print(f"Huffman Coding  of {file_path}: ")
    with open(file_path) as f:
        while True:
            c = f.read(1)
            logger.debug("huffman(file_path=%s): c → %s", file_path, c)
            if not c:
                break
            print(letters[c], end=" ")
    print()
    logger.debug("<<< Exiting huffman(file_path=%s)", file_path)


if __name__ == "__main__":
    # pass the file path to the huffman function
    huffman(sys.argv[1])
