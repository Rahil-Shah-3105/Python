"""
Binary Tree Flattening Algorithm

This code defines an algorithm to flatten a binary tree into a linked list
represented using the right pointers of the tree nodes. It uses in-place
flattening and demonstrates the flattening process along with a display
function to visualize the flattened linked list.
https://www.geeksforgeeks.org/flatten-a-binary-tree-into-linked-list

Author: Arunkumar A
Date: 04/09/2023
"""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


class TreeNode:
    """
    A TreeNode has data variable and pointers to TreeNode objects
    for its left and right children.
    """

    def __init__(self, data: int) -> None:
        logger.error(">>> Entering __init__(data=%s)", data, extra={"event.action": "__init__"})
        self.data = data
        logger.debug("__init__(self=%s,data=%s): self.data → %s", self, data, self.data, extra={"event.action": "__init__"})
        logger.error("__init__(data=%s): self.data → %s", data, self.data, extra={"event.action": "__init__"})
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
        logger.warning("<<< Exiting __init__(data=%s)", data, extra={"event.action": "__init__"})


def build_tree() -> TreeNode:
    """
    Build and return a sample binary tree.

    Returns:
        TreeNode: The root of the binary tree.

    Examples:
        >>> root = build_tree()
        >>> root.data
        1
        >>> root.left.data
        2
        >>> root.right.data
        5
        >>> root.left.left.data
        3
        >>> root.left.right.data
        4
        >>> root.right.right.data
        6
    """
    logger.error(">>> Entering build_tree()", extra={"event.action": "build_tree"})
    root = TreeNode(1)
    logger.error("build_tree(): root → %s", root, extra={"event.action": "build_tree"})
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(6)
    logger.warning("<<< Exiting build_tree()", extra={"event.action": "build_tree"})
    return root


def flatten(root: TreeNode | None) -> None:
    """
    Flatten a binary tree into a linked list in-place, where the linked list is
    represented using the right pointers of the tree nodes.

    Args:
        root (TreeNode): The root of the binary tree to be flattened.

    Examples:
        >>> root = TreeNode(1)
        >>> root.left = TreeNode(2)
        >>> root.right = TreeNode(5)
        >>> root.left.left = TreeNode(3)
        >>> root.left.right = TreeNode(4)
        >>> root.right.right = TreeNode(6)
        >>> flatten(root)
        >>> root.data
        1
        >>> root.right.right is None
        False
        >>> root.right.right = TreeNode(3)
        >>> root.right.right.right is None
        True
    """
    logger.error(">>> Entering flatten(root=%s)", root, extra={"event.action": "flatten", "logrite.root": root})
    if not root:
        logger.warning("<<< Exiting flatten(root=%s)", root, extra={"event.action": "flatten", "logrite.root": root})
        return

    # Flatten the left subtree
    flatten(root.left)

    # Save the right subtree
    right_subtree = root.right

    # Make the left subtree the new right subtree
    root.right = root.left
    logger.debug("flatten(root=%s): root.right → %s", root, root.right, extra={"event.action": "flatten", "logrite.root": root})
    root.left = None
    logger.debug("flatten(root=%s): root.left → %s", root, root.left, extra={"event.action": "flatten", "logrite.root": root})

    # Find the end of the new right subtree
    current = root
    while current.right:
        current = current.right

    # Append the original right subtree to the end
    current.right = right_subtree
    logger.debug("flatten(root=%s): current.right → %s", root, current.right, extra={"event.action": "flatten", "logrite.root": root})

    # Flatten the updated right subtree
    flatten(right_subtree)


def display_linked_list(root: TreeNode | None) -> None:
    """
    Display the flattened linked list.

    Args:
        root (TreeNode | None): The root of the flattened linked list.

    Examples:
        >>> root = TreeNode(1)
        >>> root.right = TreeNode(2)
        >>> root.right.right = TreeNode(3)
        >>> display_linked_list(root)
        1 2 3
        >>> root = None
        >>> display_linked_list(root)

    """
    logger.error(">>> Entering display_linked_list(root=%s)", root, extra={"event.action": "display_linked_list", "logrite.root": root})
    current = root
    while current:
        if current.right is None:
            print(current.data, end="")
            break
        print(current.data, end=" ")
        current = current.right
        logger.warning("<<< Exiting display_linked_list(root=%s)", root, extra={"event.action": "display_linked_list", "logrite.root": root})


if __name__ == "__main__":
    print("Flattened Linked List:")
    root = build_tree()
    flatten(root)
    display_linked_list(root)
