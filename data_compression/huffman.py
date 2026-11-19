from __future__ import annotations

import sys
import logging
logger = logging.getLogger(__name__)


class Letter:
    def __init__(self, letter: str, freq: int):
        logger.error(">>> Entering __init__(letter=%s,freq=%s)", letter, freq, extra={"event.action": "__init__", "logrite.letter": letter, "logrite.freq": freq})
        self.letter: str = letter
        self.freq: int = freq
        self.bitstring: dict[str, str] = {}
        logger.warning("<<< Exiting __init__(letter=%s,freq=%s)", letter, freq, extra={"event.action": "__init__", "logrite.letter": letter, "logrite.freq": freq})

    def __repr__(self) -> str:
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return f"{self.letter}:{self.freq}"


class TreeNode:
    def __init__(self, freq: int, left: Letter | TreeNode, right: Letter | TreeNode):
        logger.error(">>> Entering __init__(freq=%s,left=%s,right=%s)", freq, left, right, extra={"event.action": "__init__", "logrite.freq": freq, "logrite.left": left, "logrite.right": right})
        self.freq: int = freq
        self.left: Letter | TreeNode = left
        self.right: Letter | TreeNode = right
        logger.warning("<<< Exiting __init__(freq=%s,left=%s,right=%s)", freq, left, right, extra={"event.action": "__init__", "logrite.freq": freq, "logrite.left": left, "logrite.right": right})


def parse_file(file_path: str) -> list[Letter]:
    """
    Read the file and build a dict of all letters and their
    frequencies, then convert the dict into a list of Letters.
    """
    logger.error(">>> Entering parse_file(file_path=%s)", file_path, extra={"event.action": "parse_file", "logrite.file_path": file_path})
    chars: dict[str, int] = {}
    with open(file_path) as f:
        while True:
            c = f.read(1)
            logger.error("parse_file(file_path=%s): c → %s", file_path, c, extra={"event.action": "parse_file", "logrite.file_path": file_path})
            if not c:
                break
            chars[c] = chars[c] + 1 if c in chars else 1
    logger.warning("<<< Exiting parse_file(file_path=%s)", file_path, extra={"event.action": "parse_file", "logrite.file_path": file_path})
    return sorted((Letter(c, f) for c, f in chars.items()), key=lambda x: x.freq)


def build_tree(letters: list[Letter]) -> Letter | TreeNode:
    """
    Run through the list of Letters and build the min heap
    for the Huffman Tree.
    """
    logger.error(">>> Entering build_tree(letters=%s)", letters, extra={"event.action": "build_tree", "logrite.letters": letters})
    response: list[Letter | TreeNode] = list(letters)
    while len(response) > 1:
        left = response.pop(0)
        logger.error("build_tree(letters=%s): left → %s", letters, left, extra={"event.action": "build_tree", "logrite.letters": letters})
        right = response.pop(0)
        logger.error("build_tree(letters=%s): right → %s", letters, right, extra={"event.action": "build_tree", "logrite.letters": letters})
        total_freq = left.freq + right.freq
        node = TreeNode(total_freq, left, right)
        logger.error("build_tree(letters=%s): node → %s", letters, node, extra={"event.action": "build_tree", "logrite.letters": letters})
        response.append(node)
        response.sort(key=lambda x: x.freq)
    logger.warning("<<< Exiting build_tree(letters=%s)", letters, extra={"event.action": "build_tree", "logrite.letters": letters})
    return response[0]


def traverse_tree(root: Letter | TreeNode, bitstring: str) -> list[Letter]:
    """
    Recursively traverse the Huffman Tree to set each
    Letter's bitstring dictionary, and return the list of Letters
    """
    logger.error(">>> Entering traverse_tree(root=%s,bitstring=%s)", root, bitstring, extra={"event.action": "traverse_tree", "logrite.root": root, "logrite.bitstring": bitstring})
    if isinstance(root, Letter):
        root.bitstring[root.letter] = bitstring
        return [root]
    treenode: TreeNode = root
    letters = []
    letters += traverse_tree(treenode.left, bitstring + "0")
    letters += traverse_tree(treenode.right, bitstring + "1")
    logger.warning("<<< Exiting traverse_tree(root=%s,bitstring=%s)", root, bitstring, extra={"event.action": "traverse_tree", "logrite.root": root, "logrite.bitstring": bitstring})
    return letters


def huffman(file_path: str) -> None:
    """
    Parse the file, build the tree, then run through the file
    again, using the letters dictionary to find and print out the
    bitstring for each letter.
    """
    logger.error(">>> Entering huffman(file_path=%s)", file_path, extra={"event.action": "huffman", "logrite.file_path": file_path})
    letters_list = parse_file(file_path)
    logger.error("huffman(file_path=%s): letters_list → %s", file_path, letters_list, extra={"event.action": "huffman", "logrite.file_path": file_path})
    root = build_tree(letters_list)
    logger.error("huffman(file_path=%s): root → %s", file_path, root, extra={"event.action": "huffman", "logrite.file_path": file_path})
    letters = {
        k: v for letter in traverse_tree(root, "") for k, v in letter.bitstring.items()
    }
    print(f"Huffman Coding  of {file_path}: ")
    with open(file_path) as f:
        while True:
            c = f.read(1)
            logger.error("huffman(file_path=%s): c → %s", file_path, c, extra={"event.action": "huffman", "logrite.file_path": file_path})
            if not c:
                break
            print(letters[c], end=" ")
    print()
    logger.warning("<<< Exiting huffman(file_path=%s)", file_path, extra={"event.action": "huffman", "logrite.file_path": file_path})


if __name__ == "__main__":
    # pass the file path to the huffman function
    huffman(sys.argv[1])
