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
    logger.debug(">>> Entering make_tree()")
    tree = Node(1)
    logger.debug("make_tree(): tree → %s", tree)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(4)
    tree.left.right = Node(5)
    logger.debug("<<< Exiting make_tree()")
    return tree


def preorder(root: Node | None) -> Generator[int]:
    """
    Pre-order traversal visits root node, left subtree, right subtree.
    >>> list(preorder(make_tree()))
    [1, 2, 4, 5, 3]
    """
    logger.debug(">>> Entering preorder(root=%s)", root)
    if not root:
        logger.debug("<<< Exiting preorder(root=%s)", root)
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
    logger.debug(">>> Entering postorder(root=%s)", root)
    if not root:
        logger.debug("<<< Exiting postorder(root=%s)", root)
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
    logger.debug(">>> Entering inorder(root=%s)", root)
    if not root:
        logger.debug("<<< Exiting inorder(root=%s)", root)
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
    logger.debug(">>> Entering reverse_inorder(root=%s)", root)
    if not root:
        logger.debug("<<< Exiting reverse_inorder(root=%s)", root)
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
    logger.debug(">>> Entering height(root=%s)", root)
    logger.debug("<<< Exiting height(root=%s)", root)
    return (max(height(root.left), height(root.right)) + 1) if root else 0


def level_order(root: Node | None) -> Generator[int]:
    """
    Returns a list of nodes value from a whole binary tree in Level Order Traverse.
    Level Order traverse: Visit nodes of the tree level-by-level.
    >>> list(level_order(make_tree()))
    [1, 2, 3, 4, 5]
    """
    logger.debug(">>> Entering level_order(root=%s)", root)

    if root is None:
        logger.debug("<<< Exiting level_order(root=%s)", root)
        return

    process_queue = deque([root])
    logger.debug("level_order(root=%s): process_queue → %s", root, process_queue)

    while process_queue:
        node = process_queue.popleft()
        logger.debug("level_order(root=%s): node → %s", root, node)
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
    logger.debug(">>> Entering get_nodes_from_left_to_right(root=%s,level=%s)", root, level)

    logger.debug("<<< Exiting get_nodes_from_left_to_right(root=%s,level=%s)", root, level)
    def populate_output(root: Node | None, level: int) -> Generator[int]:
        logger.debug(">>> Entering populate_output(root=%s,level=%s)", root, level)
        if not root:
            logger.debug("<<< Exiting populate_output(root=%s,level=%s)", root, level)
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
    logger.debug(">>> Entering get_nodes_from_right_to_left(root=%s,level=%s)", root, level)

    logger.debug("<<< Exiting get_nodes_from_right_to_left(root=%s,level=%s)", root, level)
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
    logger.debug(">>> Entering zigzag(root=%s)", root)
    if root is None:
        logger.debug("<<< Exiting zigzag(root=%s)", root)
        return

    flag = 0
    logger.debug("zigzag(root=%s): flag → %s", root, flag)
    height_tree = height(root)
    logger.debug("zigzag(root=%s): height_tree → %s", root, height_tree)

    for h in range(1, height_tree + 1):
        if not flag:
            yield from get_nodes_from_left_to_right(root, h)
            flag = 1
        else:
            yield from get_nodes_from_right_to_left(root, h)
            flag = 0


def main() -> None:  # Main function for testing.
    logger.debug(">>> Entering main()")
    logger.debug("main(): root → %s", root)
    logger.warning("main(): root → %s", root)
    # Create binary tree.
    root = make_tree()

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
    logger.debug("<<< Exiting main()")
    print(f"{list(zigzag(root))}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
