from __future__ import annotations

from collections import deque
from collections.abc import Generator
from dataclasses import dataclass
import logging
logger = logging.getLogger(__name__)


# https://en.wikipedia.org/wiki/Tree_traversal
@dataclass
class Node:
    data: int
    left: Node | None = None
    right: Node | None = None


def make_tree() -> Node | None:
    r"""
    The below tree
        1
       / \
      2   3
     / \
    4   5
    """
    logger.error(">>> Entering make_tree()", extra={"event.action": "make_tree"})
    tree = Node(1)
    logger.error("make_tree(): tree → %s", tree, extra={"event.action": "make_tree"})
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    logger.warning("<<< Exiting make_tree()", extra={"event.action": "make_tree"})
    return tree


def preorder(root: Node | None) -> Generator[int]:
    """
    Pre-order traversal visits root node, left subtree, right subtree.
    >>> list(preorder(make_tree()))
    [1, 2, 4, 5, 3]
    """
    logger.error(">>> Entering preorder(root=%s)", root, extra={"event.action": "preorder", "logrite.root": root})
    if not root:
        logger.warning("<<< Exiting preorder(root=%s)", root, extra={"event.action": "preorder", "logrite.root": root})
        return
    yield root.data
    yield from preorder(root.left)
    yield from preorder(root.right)


def postorder(root: Node | None) -> Generator[int]:
    """
    Post-order traversal visits left subtree, right subtree, root node.
    >>> list(postorder(make_tree()))
    [4, 5, 2, 3, 1]
    """
    logger.error(">>> Entering postorder(root=%s)", root, extra={"event.action": "postorder", "logrite.root": root})
    if not root:
        logger.warning("<<< Exiting postorder(root=%s)", root, extra={"event.action": "postorder", "logrite.root": root})
        return
    yield from postorder(root.left)
    yield from postorder(root.right)
    yield root.data


def inorder(root: Node | None) -> Generator[int]:
    """
    In-order traversal visits left subtree, root node, right subtree.
    >>> list(inorder(make_tree()))
    [4, 2, 5, 1, 3]
    """
    logger.error(">>> Entering inorder(root=%s)", root, extra={"event.action": "inorder", "logrite.root": root})
    if not root:
        logger.warning("<<< Exiting inorder(root=%s)", root, extra={"event.action": "inorder", "logrite.root": root})
        return
    yield from inorder(root.left)
    yield root.data
    yield from inorder(root.right)


def reverse_inorder(root: Node | None) -> Generator[int]:
    """
    Reverse in-order traversal visits right subtree, root node, left subtree.
    >>> list(reverse_inorder(make_tree()))
    [3, 1, 5, 2, 4]
    """
    logger.error(">>> Entering reverse_inorder(root=%s)", root, extra={"event.action": "reverse_inorder", "logrite.root": root})
    if not root:
        logger.warning("<<< Exiting reverse_inorder(root=%s)", root, extra={"event.action": "reverse_inorder", "logrite.root": root})
        return
    yield from reverse_inorder(root.right)
    yield root.data
    yield from reverse_inorder(root.left)


def height(root: Node | None) -> int:
    """
    Recursive function for calculating the height of the binary tree.
    >>> height(None)
    0
    >>> height(make_tree())
    3
    """
    logger.error(">>> Entering height(root=%s)", root, extra={"event.action": "height", "logrite.root": root})
    logger.warning("<<< Exiting height(root=%s)", root, extra={"event.action": "height", "logrite.root": root})
    return (max(height(root.left), height(root.right)) + 1) if root else 0


def level_order(root: Node | None) -> Generator[int]:
    """
    Returns a list of nodes value from a whole binary tree in Level Order Traverse.
    Level Order traverse: Visit nodes of the tree level-by-level.
    >>> list(level_order(make_tree()))
    [1, 2, 3, 4, 5]
    """
    logger.error(">>> Entering level_order(root=%s)", root, extra={"event.action": "level_order", "logrite.root": root})

    if root is None:
        logger.warning("<<< Exiting level_order(root=%s)", root, extra={"event.action": "level_order", "logrite.root": root})
        return

    process_queue = deque([root])

    while process_queue:
        node = process_queue.popleft()
        yield node.data

        if node.left:
            process_queue.append(node.left)
        if node.right:
            process_queue.append(node.right)


def get_nodes_from_left_to_right(root: Node | None, level: int) -> Generator[int]:
    """
    Returns a list of nodes value from a particular level:
    Left to right direction of the binary tree.
    >>> list(get_nodes_from_left_to_right(make_tree(), 1))
    [1]
    >>> list(get_nodes_from_left_to_right(make_tree(), 2))
    [2, 3]
    """
    logger.error(">>> Entering get_nodes_from_left_to_right(root=%s,level=%s)", root, level, extra={"event.action": "get_nodes_from_left_to_right", "logrite.root": root, "logrite.level": level})

    logger.warning("<<< Exiting get_nodes_from_left_to_right(root=%s,level=%s)", root, level, extra={"event.action": "get_nodes_from_left_to_right", "logrite.root": root, "logrite.level": level})
    def populate_output(root: Node | None, level: int) -> Generator[int]:
        logger.error(">>> Entering populate_output(root=%s,level=%s)", root, level, extra={"event.action": "populate_output", "logrite.root": root, "logrite.level": level})
        if not root:
            logger.warning("<<< Exiting populate_output(root=%s,level=%s)", root, level, extra={"event.action": "populate_output", "logrite.root": root, "logrite.level": level})
            return
        if level == 1:
            yield root.data
        elif level > 1:
            yield from populate_output(root.left, level - 1)
            yield from populate_output(root.right, level - 1)

    yield from populate_output(root, level)


def get_nodes_from_right_to_left(root: Node | None, level: int) -> Generator[int]:
    """
    Returns a list of nodes value from a particular level:
    Right to left direction of the binary tree.
    >>> list(get_nodes_from_right_to_left(make_tree(), 1))
    [1]
    >>> list(get_nodes_from_right_to_left(make_tree(), 2))
    [3, 2]
    """
    logger.error(">>> Entering get_nodes_from_right_to_left(root=%s,level=%s)", root, level, extra={"event.action": "get_nodes_from_right_to_left", "logrite.root": root, "logrite.level": level})

    logger.warning("<<< Exiting get_nodes_from_right_to_left(root=%s,level=%s)", root, level, extra={"event.action": "get_nodes_from_right_to_left", "logrite.root": root, "logrite.level": level})
    def populate_output(root: Node | None, level: int) -> Generator[int]:
        if not root:
            return
        if level == 1:
            yield root.data
        elif level > 1:
            yield from populate_output(root.right, level - 1)
            yield from populate_output(root.left, level - 1)

    yield from populate_output(root, level)


def zigzag(root: Node | None) -> Generator[int]:
    """
    ZigZag traverse:
    Returns a list of nodes value from left to right and right to left, alternatively.
    >>> list(zigzag(make_tree()))
    [1, 3, 2, 4, 5]
    """
    logger.error(">>> Entering zigzag(root=%s)", root, extra={"event.action": "zigzag", "logrite.root": root})
    if root is None:
        logger.warning("<<< Exiting zigzag(root=%s)", root, extra={"event.action": "zigzag", "logrite.root": root})
        return

    flag = 0
    height_tree = height(root)

    for h in range(1, height_tree + 1):
        if not flag:
            yield from get_nodes_from_left_to_right(root, h)
            flag = 1
        else:
            yield from get_nodes_from_right_to_left(root, h)
            flag = 0


def main() -> None:  # Main function for testing.
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    # Create binary tree.
    root = make_tree()
    logger.error("main(): root → %s", root, extra={"event.action": "main"})

    # All Traversals of the binary are as follows:
    print(f"In-order Traversal: {list(inorder(root))}")
    print(f"Reverse In-order Traversal: {list(reverse_inorder(root))}")
    print(f"Pre-order Traversal: {list(preorder(root))}")
    print(f"Post-order Traversal: {list(postorder(root))}", "\n")

    print(f"Height of Tree: {height(root)}", "\n")

    print("Complete Level Order Traversal: ")
    print(f"{list(level_order(root))} \n")

    print("Level-wise order Traversal: ")

    for level in range(1, height(root) + 1):
        print(f"Level {level}:", list(get_nodes_from_left_to_right(root, level=level)))

    print("\nZigZag order Traversal: ")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})
    print(f"{list(zigzag(root))}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
