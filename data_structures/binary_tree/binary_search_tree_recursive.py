"""
This is a python3 implementation of binary search tree using recursion

To run tests:
python -m unittest binary_search_tree_recursive.py

To run an example:
python binary_search_tree_recursive.py
"""

from __future__ import annotations

import unittest
from collections.abc import Iterator

import pytest
import logging
logger = logging.getLogger(__name__)


class Node:
    def __init__(self, label: int, parent: Node | None) -> None:
        logger.debug(">>> Entering __init__(label=%s,parent=%s)", label, parent)
        self.label = label
        logger.debug("__init__(self=%s,label=%s,parent=%s): self.label → %s", self, label, parent, self.label)
        self.parent = parent
        logger.debug("__init__(self=%s,label=%s,parent=%s): self.parent → %s", self, label, parent, self.parent)
        self.left: Node | None = None
        self.right: Node | None = None
        logger.debug("<<< Exiting __init__(label=%s,parent=%s)", label, parent)

        logger.debug(">>> Entering __init__()")
        logger.debug("<<< Exiting __init__()")

class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def empty(self) -> None:
        """
        Empties the tree

        >>> t = BinarySearchTree()
        >>> assert t.root is None
        >>> t.put(8)
        >>> assert t.root is not None
        """
        logger.debug(">>> Entering empty()")
        self.root = None
        logger.debug("empty(self=%s): self.root → %s", self, self.root)
        logger.debug("<<< Exiting empty()")

    def is_empty(self) -> bool:
        """
        Checks if the tree is empty

        >>> t = BinarySearchTree()
        >>> t.is_empty()
        True
        >>> t.put(8)
        >>> t.is_empty()
        False
        """
        logger.debug(">>> Entering is_empty()")
        logger.debug("<<< Exiting is_empty()")
        return self.root is None

    def put(self, label: int) -> None:
        """
        Put a new node in the tree

        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> assert t.root.parent is None
        >>> assert t.root.label == 8

        >>> t.put(10)
        >>> assert t.root.right.parent == t.root
        >>> assert t.root.right.label == 10

        >>> t.put(3)
        >>> assert t.root.left.parent == t.root
        >>> assert t.root.left.label == 3
        """
        logger.debug(">>> Entering put(label=%s)", label)
        self.root = self._put(self.root, label)
        logger.debug("put(label=%s): self.root → %s", label, self.root)
        logger.debug("<<< Exiting put(label=%s)", label)

    def _put(self, node: Node | None, label: int, parent: Node | None = None) -> Node:
        logger.debug(">>> Entering _put(node=%s,label=%s,parent=%s)", node, label, parent)
        if node is None:
            node = Node(label, parent)
            logger.debug("_put(node=%s,label=%s,parent=%s): node → %s", node, label, parent, node)
        elif label < node.label:
            node.left = self._put(node.left, label, node)
        elif label > node.label:
            node.right = self._put(node.right, label, node)
        else:
            msg = f"Node with label {label} already exists"
            logger.debug("_put(self=%s,node=%s,label=%s,parent=%s): msg → %s", self, node, label, parent, msg)
            logger.debug("_put(node=%s,label=%s,parent=%s): msg → %s", node, label, parent, msg)
            raise ValueError(msg)

        logger.debug("<<< Exiting _put(node=%s,label=%s,parent=%s)", node, label, parent)
        return node

    def search(self, label: int) -> Node:
        """
        Searches a node in the tree

        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> t.put(10)
        >>> node = t.search(8)
        >>> assert node.label == 8

        >>> node = t.search(3)
        Traceback (most recent call last):
            ...
        ValueError: Node with label 3 does not exist
        """
        logger.debug(">>> Entering search(label=%s)", label)
        logger.debug("<<< Exiting search(label=%s)", label)
        return self._search(self.root, label)

    def _search(self, node: Node | None, label: int) -> Node:
        logger.debug(">>> Entering _search(node=%s,label=%s)", node, label)
        logger.debug("_search(node=%s,label=%s): msg → %s", node, label, msg)
        logger.debug("_search(self=%s,node=%s,label=%s): msg → %s", self, node, label, msg)
        if node is None:
            msg = f"Node with label {label} does not exist"
            raise ValueError(msg)
        elif label < node.label:
            node = self._search(node.left, label)
            logger.debug("_search(node=%s,label=%s): node → %s", node, label, node)
        elif label > node.label:
            node = self._search(node.right, label)

        logger.debug("<<< Exiting _search(node=%s,label=%s)", node, label)
        return node

    def remove(self, label: int) -> None:
        """
        Removes a node in the tree

        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> t.put(10)
        >>> t.remove(8)
        >>> assert t.root.label == 10

        >>> t.remove(3)
        Traceback (most recent call last):
            ...
        ValueError: Node with label 3 does not exist
        """
        logger.debug(">>> Entering remove(label=%s)", label)
        logger.debug("remove(label=%s): lowest_node → %s", label, lowest_node)
        logger.debug("remove(self=%s,label=%s): lowest_node → %s", self, label, lowest_node)
        logger.debug("remove(self=%s,label=%s): lowest_node.left → %s", self, label, lowest_node.left)
        logger.debug("remove(self=%s,label=%s): lowest_node.right → %s", self, label, lowest_node.right)
        node = self.search(label)
        logger.debug("remove(label=%s): node → %s", label, node)
        logger.debug("remove(self=%s,label=%s): node → %s", self, label, node)
        if node.right and node.left:
            lowest_node = self._get_lowest_node(node.right)
            lowest_node.left = node.left
            lowest_node.right = node.right
            node.left.parent = lowest_node
            if node.right:
                node.right.parent = lowest_node
            self._reassign_nodes(node, lowest_node)
        elif not node.right and node.left:
            self._reassign_nodes(node, node.left)
        elif node.right and not node.left:
            self._reassign_nodes(node, node.right)
        else:
            self._reassign_nodes(node, None)
            logger.debug("<<< Exiting remove(label=%s)", label)

    def _reassign_nodes(self, node: Node, new_children: Node | None) -> None:
        logger.debug(">>> Entering _reassign_nodes(node=%s,new_children=%s)", node, new_children)
        if new_children:
            new_children.parent = node.parent
            logger.debug("_reassign_nodes(self=%s,node=%s,new_children=%s): new_children.parent → %s", self, node, new_children, new_children.parent)

        if node.parent:
            if node.parent.right == node:
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            logger.debug("<<< Exiting _reassign_nodes(node=%s,new_children=%s)", node, new_children)
            self.root = new_children
            logger.debug("_reassign_nodes(self=%s,node=%s,new_children=%s): self.root → %s", self, node, new_children, self.root)

    def _get_lowest_node(self, node: Node) -> Node:
        logger.debug(">>> Entering _get_lowest_node(node=%s)", node)
        if node.left:
            lowest_node = self._get_lowest_node(node.left)
            logger.debug("_get_lowest_node(self=%s,node=%s): lowest_node → %s", self, node, lowest_node)
        else:
            lowest_node = node
            self._reassign_nodes(node, node.right)

        logger.debug("<<< Exiting _get_lowest_node(node=%s)", node)
        return lowest_node

    def exists(self, label: int) -> bool:
        """
        Checks if a node exists in the tree

        >>> t = BinarySearchTree()
        >>> t.put(8)
        >>> t.put(10)
        >>> t.exists(8)
        True

        >>> t.exists(3)
        False
        """
        logger.debug(">>> Entering exists(label=%s)", label)
        try:
            self.search(label)
            return True
        except ValueError:
            logger.error("Exception in exists(label=%s)", label, exc_info=True)
            logger.debug("<<< Exiting exists(label=%s)", label)
            return False

    def get_max_label(self) -> int:
        """
        Gets the max label inserted in the tree

        >>> t = BinarySearchTree()
        >>> t.get_max_label()
        Traceback (most recent call last):
            ...
        ValueError: Binary search tree is empty

        >>> t.put(8)
        >>> t.put(10)
        >>> t.get_max_label()
        10
        """
        logger.debug(">>> Entering get_max_label()")
        if self.root is None:
            raise ValueError("Binary search tree is empty")

        node = self.root
        logger.debug("get_max_label(self=%s): node → %s", self, node)
        while node.right is not None:
            node = node.right

        logger.debug("<<< Exiting get_max_label()")
        return node.label

    def get_min_label(self) -> int:
        """
        Gets the min label inserted in the tree

        >>> t = BinarySearchTree()
        >>> t.get_min_label()
        Traceback (most recent call last):
            ...
        ValueError: Binary search tree is empty

        >>> t.put(8)
        >>> t.put(10)
        >>> t.get_min_label()
        8
        """
        logger.debug(">>> Entering get_min_label()")
        if self.root is None:
            raise ValueError("Binary search tree is empty")

        node = self.root
        logger.debug("get_min_label(self=%s): node → %s", self, node)
        while node.left is not None:
            node = node.left

        logger.debug("<<< Exiting get_min_label()")
        return node.label

    def inorder_traversal(self) -> Iterator[Node]:
        """
        Return the inorder traversal of the tree

        >>> t = BinarySearchTree()
        >>> [i.label for i in t.inorder_traversal()]
        []

        >>> t.put(8)
        >>> t.put(10)
        >>> t.put(9)
        >>> [i.label for i in t.inorder_traversal()]
        [8, 9, 10]
        """
        logger.debug(">>> Entering inorder_traversal()")
        logger.debug("<<< Exiting inorder_traversal()")
        return self._inorder_traversal(self.root)

    def _inorder_traversal(self, node: Node | None) -> Iterator[Node]:
        logger.debug(">>> Entering _inorder_traversal(node=%s)", node)
        if node is not None:
            yield from self._inorder_traversal(node.left)
            yield node
            yield from self._inorder_traversal(node.right)
            logger.debug("<<< Exiting _inorder_traversal(node=%s)", node)

    def preorder_traversal(self) -> Iterator[Node]:
        """
        Return the preorder traversal of the tree

        >>> t = BinarySearchTree()
        >>> [i.label for i in t.preorder_traversal()]
        []

        >>> t.put(8)
        >>> t.put(10)
        >>> t.put(9)
        >>> [i.label for i in t.preorder_traversal()]
        [8, 10, 9]
        """
        logger.debug(">>> Entering preorder_traversal()")
        logger.debug("<<< Exiting preorder_traversal()")
        return self._preorder_traversal(self.root)

    def _preorder_traversal(self, node: Node | None) -> Iterator[Node]:
        logger.debug(">>> Entering _preorder_traversal(node=%s)", node)
        if node is not None:
            yield node
            yield from self._preorder_traversal(node.left)
            yield from self._preorder_traversal(node.right)
            logger.debug("<<< Exiting _preorder_traversal(node=%s)", node)


class BinarySearchTreeTest(unittest.TestCase):
    @staticmethod
    def _get_binary_search_tree() -> BinarySearchTree:
        r"""
              8
             / \
            3   10
           / \    \
          1   6    14
             / \   /
            4   7 13
             \
              5
        """
        logger.debug(">>> Entering _get_binary_search_tree()")
        t = BinarySearchTree()
        logger.debug("_get_binary_search_tree(): t → %s", t)
        t.put(8)
        t.put(3)
        t.put(6)
        t.put(1)
        t.put(10)
        t.put(14)
        t.put(13)
        t.put(4)
        t.put(7)
        t.put(5)

        logger.debug("<<< Exiting _get_binary_search_tree()")
        return t

    def test_put(self) -> None:
        logger.debug(">>> Entering test_put()")
        t = BinarySearchTree()
        logger.debug("test_put(): t → %s", t)
        assert t.is_empty()

        t.put(8)
        r"""
              8
        """
        assert t.root is not None
        assert t.root.parent is None
        assert t.root.label == 8

        t.put(10)
        r"""
              8
               \
                10
        """
        assert t.root.right is not None
        assert t.root.right.parent == t.root
        assert t.root.right.label == 10

        t.put(3)
        r"""
              8
             / \
            3   10
        """
        assert t.root.left is not None
        assert t.root.left.parent == t.root
        assert t.root.left.label == 3

        t.put(6)
        r"""
              8
             / \
            3   10
             \
              6
        """
        assert t.root.left.right is not None
        assert t.root.left.right.parent == t.root.left
        assert t.root.left.right.label == 6

        t.put(1)
        r"""
              8
             / \
            3   10
           / \
          1   6
        """
        assert t.root.left.left is not None
        assert t.root.left.left.parent == t.root.left
        assert t.root.left.left.label == 1

        with pytest.raises(ValueError):
            logger.error("Exception in test_put()", exc_info=True)
            t.put(1)
            logger.debug("<<< Exiting test_put()")

    def test_search(self) -> None:
        logger.debug(">>> Entering test_search()")
        t = self._get_binary_search_tree()
        logger.debug("test_search(): t → %s", t)

        node = t.search(6)
        logger.debug("test_search(self=%s): node → %s", self, node)
        assert node.label == 6

        node = t.search(13)
        assert node.label == 13

        with pytest.raises(ValueError):
            logger.error("Exception in test_search()", exc_info=True)
            t.search(2)
            logger.debug("<<< Exiting test_search()")

    def test_remove(self) -> None:
        logger.debug(">>> Entering test_remove()")
        t = self._get_binary_search_tree()
        logger.debug("test_remove(): t → %s", t)

        t.remove(13)
        r"""
              8
             / \
            3   10
           / \    \
          1   6    14
             / \
            4   7
             \
              5
        """
        assert t.root is not None
        assert t.root.right is not None
        assert t.root.right.right is not None
        assert t.root.right.right.right is None
        assert t.root.right.right.left is None

        t.remove(7)
        r"""
              8
             / \
            3   10
           / \    \
          1   6    14
             /
            4
             \
              5
        """
        assert t.root.left is not None
        assert t.root.left.right is not None
        assert t.root.left.right.left is not None
        assert t.root.left.right.right is None
        assert t.root.left.right.left.label == 4

        t.remove(6)
        r"""
              8
             / \
            3   10
           / \    \
          1   4    14
               \
                5
        """
        assert t.root.left.left is not None
        assert t.root.left.right.right is not None
        assert t.root.left.left.label == 1
        assert t.root.left.right.label == 4
        assert t.root.left.right.right.label == 5
        assert t.root.left.right.left is None
        assert t.root.left.left.parent == t.root.left
        assert t.root.left.right.parent == t.root.left

        t.remove(3)
        r"""
              8
             / \
            4   10
           / \    \
          1   5    14
        """
        assert t.root is not None
        assert t.root.left.label == 4
        assert t.root.left.right.label == 5
        assert t.root.left.left.label == 1
        assert t.root.left.parent == t.root
        assert t.root.left.left.parent == t.root.left
        assert t.root.left.right.parent == t.root.left

        t.remove(4)
        r"""
              8
             / \
            5   10
           /      \
          1        14
        """
        assert t.root.left is not None
        assert t.root.left.left is not None
        assert t.root.left.label == 5
        assert t.root.left.right is None
        assert t.root.left.left.label == 1
        assert t.root.left.parent == t.root
        assert t.root.left.left.parent == t.root.left
        logger.debug("<<< Exiting test_remove()")

    def test_remove_2(self) -> None:
        logger.debug(">>> Entering test_remove_2()")
        t = self._get_binary_search_tree()
        logger.debug("test_remove_2(): t → %s", t)

        t.remove(3)
        r"""
              8
             / \
            4   10
           / \    \
          1   6    14
             / \   /
            5   7 13
        """
        assert t.root is not None
        assert t.root.left is not None
        assert t.root.left.left is not None
        assert t.root.left.right is not None
        assert t.root.left.right.left is not None
        assert t.root.left.right.right is not None
        assert t.root.left.label == 4
        assert t.root.left.right.label == 6
        assert t.root.left.left.label == 1
        assert t.root.left.right.right.label == 7
        assert t.root.left.right.left.label == 5
        assert t.root.left.parent == t.root
        assert t.root.left.right.parent == t.root.left
        assert t.root.left.left.parent == t.root.left
        assert t.root.left.right.left.parent == t.root.left.right
        logger.debug("<<< Exiting test_remove_2()")

    def test_empty(self) -> None:
        logger.debug(">>> Entering test_empty()")
        t = self._get_binary_search_tree()
        logger.debug("test_empty(): t → %s", t)
        t.empty()
        assert t.root is None
        logger.debug("<<< Exiting test_empty()")

    def test_is_empty(self) -> None:
        logger.debug(">>> Entering test_is_empty()")
        t = self._get_binary_search_tree()
        logger.debug("test_is_empty(): t → %s", t)
        assert not t.is_empty()

        t.empty()
        assert t.is_empty()
        logger.debug("<<< Exiting test_is_empty()")

    def test_exists(self) -> None:
        logger.debug(">>> Entering test_exists()")
        t = self._get_binary_search_tree()
        logger.debug("test_exists(): t → %s", t)

        assert t.exists(6)
        assert not t.exists(-1)
        logger.debug("<<< Exiting test_exists()")

    def test_get_max_label(self) -> None:
        logger.debug(">>> Entering test_get_max_label()")
        t = self._get_binary_search_tree()
        logger.debug("test_get_max_label(): t → %s", t)

        assert t.get_max_label() == 14

        t.empty()
        with pytest.raises(ValueError):
            logger.error("Exception in test_get_max_label()", exc_info=True)
            t.get_max_label()
            logger.debug("<<< Exiting test_get_max_label()")

    def test_get_min_label(self) -> None:
        logger.debug(">>> Entering test_get_min_label()")
        t = self._get_binary_search_tree()
        logger.debug("test_get_min_label(): t → %s", t)

        assert t.get_min_label() == 1

        t.empty()
        with pytest.raises(ValueError):
            logger.error("Exception in test_get_min_label()", exc_info=True)
            t.get_min_label()
            logger.debug("<<< Exiting test_get_min_label()")

    def test_inorder_traversal(self) -> None:
        logger.debug(">>> Entering test_inorder_traversal()")
        t = self._get_binary_search_tree()
        logger.debug("test_inorder_traversal(): t → %s", t)

        inorder_traversal_nodes = [i.label for i in t.inorder_traversal()]
        logger.debug("test_inorder_traversal(): inorder_traversal_nodes → %s", inorder_traversal_nodes)
        assert inorder_traversal_nodes == [1, 3, 4, 5, 6, 7, 8, 10, 13, 14]
        logger.debug("<<< Exiting test_inorder_traversal()")

    def test_preorder_traversal(self) -> None:
        logger.debug(">>> Entering test_preorder_traversal()")
        t = self._get_binary_search_tree()
        logger.debug("test_preorder_traversal(): t → %s", t)

        preorder_traversal_nodes = [i.label for i in t.preorder_traversal()]
        logger.debug("test_preorder_traversal(): preorder_traversal_nodes → %s", preorder_traversal_nodes)
        assert preorder_traversal_nodes == [8, 3, 1, 6, 4, 5, 7, 10, 14, 13]
        logger.debug("<<< Exiting test_preorder_traversal()")


def binary_search_tree_example() -> None:
    r"""
    Example
                  8
                 / \
                3   10
               / \    \
              1   6    14
                 / \   /
                4   7 13
                \
                5

    Example After Deletion
                  4
                 / \
                1   7
                     \
                      5

    """
    logger.debug(">>> Entering binary_search_tree_example()")

    t = BinarySearchTree()
    logger.debug("binary_search_tree_example(): t → %s", t)
    t.put(8)
    t.put(3)
    t.put(6)
    t.put(1)
    t.put(10)
    t.put(14)
    t.put(13)
    t.put(4)
    t.put(7)
    t.put(5)

    print(
        """
            8
           / \\
          3   10
         / \\    \\
        1   6    14
           / \\   /
          4   7 13
           \\
            5
        """
    )

    print("Label 6 exists:", t.exists(6))
    print("Label 13 exists:", t.exists(13))
    print("Label -1 exists:", t.exists(-1))
    print("Label 12 exists:", t.exists(12))

    # Prints all the elements of the list in inorder traversal
    inorder_traversal_nodes = [i.label for i in t.inorder_traversal()]
    logger.debug("binary_search_tree_example(): inorder_traversal_nodes → %s", inorder_traversal_nodes)
    print("Inorder traversal:", inorder_traversal_nodes)

    # Prints all the elements of the list in preorder traversal
    preorder_traversal_nodes = [i.label for i in t.preorder_traversal()]
    logger.debug("binary_search_tree_example(): preorder_traversal_nodes → %s", preorder_traversal_nodes)
    print("Preorder traversal:", preorder_traversal_nodes)

    print("Max. label:", t.get_max_label())
    print("Min. label:", t.get_min_label())

    # Delete elements
    print("\nDeleting elements 13, 10, 8, 3, 6, 14")
    print(
        """
          4
         / \\
        1   7
             \\
              5
        """
    )
    t.remove(13)
    t.remove(10)
    t.remove(8)
    t.remove(3)
    t.remove(6)
    t.remove(14)

    # Prints all the elements of the list in inorder traversal after delete
    inorder_traversal_nodes = [i.label for i in t.inorder_traversal()]
    print("Inorder traversal after delete:", inorder_traversal_nodes)

    # Prints all the elements of the list in preorder traversal after delete
    preorder_traversal_nodes = [i.label for i in t.preorder_traversal()]
    print("Preorder traversal after delete:", preorder_traversal_nodes)

    print("Max. label:", t.get_max_label())
    print("Min. label:", t.get_min_label())
    logger.debug("<<< Exiting binary_search_tree_example()")


if __name__ == "__main__":
    binary_search_tree_example()
