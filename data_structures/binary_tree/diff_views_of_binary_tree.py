r"""
Problem: Given root of a binary tree, return the:
1. binary-tree-right-side-view
2. binary-tree-left-side-view
3. binary-tree-top-side-view
4. binary-tree-bottom-side-view
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import logging
logger = logging.getLogger(__name__)


@dataclass
class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None


def make_tree() -> TreeNode:
    """
    >>> make_tree().val
    3
    """
    logger.error(">>> Entering make_tree()", extra={"event.action": "make_tree"})
    logger.warning("<<< Exiting make_tree()", extra={"event.action": "make_tree"})
    return TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))


def binary_tree_right_side_view(root: TreeNode) -> list[int]:
    r"""
    Function returns the right side view of binary tree.

       3       <-  3
     / \
    9   20    <-  20
       /  \
      15   7  <-  7

    >>> binary_tree_right_side_view(make_tree())
    [3, 20, 7]
    >>> binary_tree_right_side_view(None)
    []
    """
    logger.error(">>> Entering binary_tree_right_side_view(root=%s)", root, extra={"event.action": "binary_tree_right_side_view", "logrite.root": root})

    logger.warning("<<< Exiting binary_tree_right_side_view(root=%s)", root, extra={"event.action": "binary_tree_right_side_view", "logrite.root": root})
    def depth_first_search(
        root: TreeNode | None, depth: int, right_view: list[int]
    ) -> None:
        logger.error(">>> Entering depth_first_search(root=%s,depth=%s,right_view=%s)", root, depth, right_view, extra={"event.action": "depth_first_search", "logrite.root": root, "logrite.depth": depth, "logrite.right_view": right_view})
        """
        A depth first search preorder traversal to append the values at
        right side of tree.
        """
        if not root:
            logger.warning("<<< Exiting depth_first_search(root=%s,depth=%s,right_view=%s)", root, depth, right_view, extra={"event.action": "depth_first_search", "logrite.root": root, "logrite.depth": depth, "logrite.right_view": right_view})
            return

        if depth == len(right_view):
            right_view.append(root.val)

        depth_first_search(root.right, depth + 1, right_view)
        depth_first_search(root.left, depth + 1, right_view)

    right_view: list = []
    if not root:
        return right_view

    depth_first_search(root, 0, right_view)
    return right_view


def binary_tree_left_side_view(root: TreeNode) -> list[int]:
    r"""
    Function returns the left side view of binary tree.

    3  ->    3
            / \
    9  ->  9   20
              /  \
    15 ->    15   7

    >>> binary_tree_left_side_view(make_tree())
    [3, 9, 15]
    >>> binary_tree_left_side_view(None)
    []
    """
    logger.error(">>> Entering binary_tree_left_side_view(root=%s)", root, extra={"event.action": "binary_tree_left_side_view", "logrite.root": root})

    logger.warning("<<< Exiting binary_tree_left_side_view(root=%s)", root, extra={"event.action": "binary_tree_left_side_view", "logrite.root": root})
    def depth_first_search(
        root: TreeNode | None, depth: int, left_view: list[int]
    ) -> None:
        logger.error(">>> Entering depth_first_search(root=%s,depth=%s,left_view=%s)", root, depth, left_view, extra={"event.action": "depth_first_search", "logrite.root": root, "logrite.depth": depth, "logrite.left_view": left_view})
        """
        A depth first search preorder traversal to append the values
        at left side of tree.
        """
        if not root:
            logger.warning("<<< Exiting depth_first_search(root=%s,depth=%s,left_view=%s)", root, depth, left_view, extra={"event.action": "depth_first_search", "logrite.root": root, "logrite.depth": depth, "logrite.left_view": left_view})
            return

        if depth == len(left_view):
            left_view.append(root.val)

        depth_first_search(root.left, depth + 1, left_view)
        depth_first_search(root.right, depth + 1, left_view)

    left_view: list = []
    if not root:
        return left_view

    depth_first_search(root, 0, left_view)
    return left_view


def binary_tree_top_side_view(root: TreeNode) -> list[int]:
    r"""
    Function returns the top side view of binary tree.

    9 3 20 7
    ⬇ ⬇ ⬇  ⬇

      3
     / \
    9   20
       /  \
      15   7

    >>> binary_tree_top_side_view(make_tree())
    [9, 3, 20, 7]
    >>> binary_tree_top_side_view(None)
    []
    """
    logger.error(">>> Entering binary_tree_top_side_view(root=%s)", root, extra={"event.action": "binary_tree_top_side_view", "logrite.root": root})

    logger.warning("<<< Exiting binary_tree_top_side_view(root=%s)", root, extra={"event.action": "binary_tree_top_side_view", "logrite.root": root})
    def breadth_first_search(root: TreeNode, top_view: list[int]) -> None:
        """
        A breadth first search traversal with defaultdict ds to append
        the values of tree from top view
        """
        logger.error(">>> Entering breadth_first_search(root=%s,top_view=%s)", root, top_view, extra={"event.action": "breadth_first_search", "logrite.root": root, "logrite.top_view": top_view})
        queue = [(root, 0)]
        logger.error("breadth_first_search(root=%s,top_view=%s): queue → %s", root, top_view, queue, extra={"event.action": "breadth_first_search", "logrite.root": root, "logrite.top_view": top_view})
        lookup = defaultdict(list)
        logger.error("breadth_first_search(root=%s,top_view=%s): lookup → %s", root, top_view, lookup, extra={"event.action": "breadth_first_search", "logrite.root": root, "logrite.top_view": top_view})

        while queue:
            first = queue.pop(0)
            logger.error("breadth_first_search(root=%s,top_view=%s): first → %s", root, top_view, first, extra={"event.action": "breadth_first_search", "logrite.root": root, "logrite.top_view": top_view})
            node, hd = first

            lookup[hd].append(node.val)

            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        for pair in sorted(lookup.items(), key=lambda each: each[0]):
            top_view.append(pair[1][0])
            logger.warning("<<< Exiting breadth_first_search(root=%s,top_view=%s)", root, top_view, extra={"event.action": "breadth_first_search", "logrite.root": root, "logrite.top_view": top_view})

    top_view: list = []
    if not root:
        return top_view

    breadth_first_search(root, top_view)
    return top_view


def binary_tree_bottom_side_view(root: TreeNode) -> list[int]:
    r"""
    Function returns the bottom side view of binary tree

      3
     / \
    9   20
       /  \
      15   7
    ↑  ↑ ↑  ↑
    9 15 20 7

    >>> binary_tree_bottom_side_view(make_tree())
    [9, 15, 20, 7]
    >>> binary_tree_bottom_side_view(None)
    []
    """
    logger.error(">>> Entering binary_tree_bottom_side_view(root=%s)", root, extra={"event.action": "binary_tree_bottom_side_view", "logrite.root": root})
    from collections import defaultdict
    logger.warning("<<< Exiting binary_tree_bottom_side_view(root=%s)", root, extra={"event.action": "binary_tree_bottom_side_view", "logrite.root": root})

    def breadth_first_search(root: TreeNode, bottom_view: list[int]) -> None:
        """
        A breadth first search traversal with defaultdict ds to append
        the values of tree from bottom view
        """
        logger.error(">>> Entering breadth_first_search(root=%s,bottom_view=%s)", root, bottom_view, extra={"event.action": "breadth_first_search", "logrite.root": root, "logrite.bottom_view": bottom_view})
        queue = [(root, 0)]
        logger.error("breadth_first_search(root=%s,bottom_view=%s): queue → %s", root, bottom_view, queue, extra={"event.action": "breadth_first_search", "logrite.root": root, "logrite.bottom_view": bottom_view})
        lookup = defaultdict(list)
        logger.error("breadth_first_search(root=%s,bottom_view=%s): lookup → %s", root, bottom_view, lookup, extra={"event.action": "breadth_first_search", "logrite.root": root, "logrite.bottom_view": bottom_view})

        while queue:
            first = queue.pop(0)
            logger.error("breadth_first_search(root=%s,bottom_view=%s): first → %s", root, bottom_view, first, extra={"event.action": "breadth_first_search", "logrite.root": root, "logrite.bottom_view": bottom_view})
            node, hd = first
            lookup[hd].append(node.val)

            if node.left:
                queue.append((node.left, hd - 1))
            if node.right:
                queue.append((node.right, hd + 1))

        for pair in sorted(lookup.items(), key=lambda each: each[0]):
            bottom_view.append(pair[1][-1])
            logger.warning("<<< Exiting breadth_first_search(root=%s,bottom_view=%s)", root, bottom_view, extra={"event.action": "breadth_first_search", "logrite.root": root, "logrite.bottom_view": bottom_view})

    bottom_view: list = []
    if not root:
        return bottom_view

    breadth_first_search(root, bottom_view)
    return bottom_view


if __name__ == "__main__":
    import doctest

    doctest.testmod()
