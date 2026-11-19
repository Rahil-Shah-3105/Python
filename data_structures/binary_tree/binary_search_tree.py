r"""
A binary search Tree

Example
              8
             / \
            3   10
           / \    \
          1   6    14
             / \   /
            4   7 13

>>> t = BinarySearchTree().insert(8, 3, 6, 1, 10, 14, 13, 4, 7)
>>> print(" ".join(repr(i.value) for i in t.traversal_tree()))
8 3 1 6 4 7 10 14 13

>>> tuple(i.value for i in t.traversal_tree(inorder))
(1, 3, 4, 6, 7, 8, 10, 13, 14)
>>> tuple(t)
(1, 3, 4, 6, 7, 8, 10, 13, 14)
>>> t.find_kth_smallest(3, t.root)
4
>>> tuple(t)[3-1]
4

>>> print(" ".join(repr(i.value) for i in t.traversal_tree(postorder)))
1 4 7 6 3 13 14 10 8
>>> t.remove(20)
Traceback (most recent call last):
    ...
ValueError: Value 20 not found
>>> BinarySearchTree().search(6)
Traceback (most recent call last):
    ...
IndexError: Warning: Tree is empty! please use another.

Other example:

>>> testlist = (8, 3, 6, 1, 10, 14, 13, 4, 7)
>>> t = BinarySearchTree()
>>> for i in testlist:
...     t.insert(i)  # doctest: +ELLIPSIS
BinarySearchTree(root=8)
BinarySearchTree(root={'8': (3, None)})
BinarySearchTree(root={'8': ({'3': (None, 6)}, None)})
BinarySearchTree(root={'8': ({'3': (1, 6)}, None)})
BinarySearchTree(root={'8': ({'3': (1, 6)}, 10)})
BinarySearchTree(root={'8': ({'3': (1, 6)}, {'10': (None, 14)})})
BinarySearchTree(root={'8': ({'3': (1, 6)}, {'10': (None, {'14': (13, None)})})})
BinarySearchTree(root={'8': ({'3': (1, {'6': (4, None)})}, {'10': (None, {'14': ...
BinarySearchTree(root={'8': ({'3': (1, {'6': (4, 7)})}, {'10': (None, {'14': (13, ...

Prints all the elements of the list in order traversal
>>> print(t)
{'8': ({'3': (1, {'6': (4, 7)})}, {'10': (None, {'14': (13, None)})})}

Test existence
>>> t.search(6) is not None
True
>>> 6 in t
True
>>> t.search(-1) is not None
False
>>> -1 in t
False

>>> t.search(6).is_right
True
>>> t.search(1).is_right
False

>>> t.get_max().value
14
>>> max(t)
14
>>> t.get_min().value
1
>>> min(t)
1
>>> t.empty()
False
>>> not t
False
>>> for i in testlist:
...     t.remove(i)
>>> t.empty()
True
>>> not t
True
"""

from __future__ import annotations

from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Any, Self
import logging
logger = logging.getLogger(__name__)


@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None
    parent: Node | None = None  # Added in order to delete a node easier

    def __iter__(self) -> Iterator[int]:
        """
        >>> list(Node(0))
        [0]
        >>> list(Node(0, Node(-1), Node(1), None))
        [-1, 0, 1]
        """
        logger.error(">>> Entering __iter__()", extra={"event.action": "__iter__"})
        yield from self.left or []
        yield self.value
        yield from self.right or []
        logger.warning("<<< Exiting __iter__()", extra={"event.action": "__iter__"})

    def __repr__(self) -> str:
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        from pprint import pformat

        if self.left is None and self.right is None:
            return str(self.value)
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return pformat({f"{self.value}": (self.left, self.right)}, indent=1)

    @property
    def is_right(self) -> bool:
        logger.error(">>> Entering is_right()", extra={"event.action": "is_right"})
        logger.warning("<<< Exiting is_right()", extra={"event.action": "is_right"})
        return bool(self.parent and self is self.parent.right)


@dataclass
class BinarySearchTree:
    root: Node | None = None

    def __bool__(self) -> bool:
        logger.error(">>> Entering __bool__()", extra={"event.action": "__bool__"})
        logger.warning("<<< Exiting __bool__()", extra={"event.action": "__bool__"})
        return bool(self.root)

    def __iter__(self) -> Iterator[int]:
        yield from self.root or []

    def __str__(self) -> str:
        """
        Return a string of all the Nodes using in order traversal
        """
        logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
        logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
        return str(self.root)

    def __reassign_nodes(self, node: Node, new_children: Node | None) -> None:
        logger.error(">>> Entering __reassign_nodes(node=%s,new_children=%s)", node, new_children, extra={"event.action": "__reassign_nodes", "logrite.node": node, "logrite.new_children": new_children})
        if new_children is not None:  # reset its kids
            new_children.parent = node.parent
            logger.debug("__reassign_nodes(self=%s,node=%s,new_children=%s): new_children.parent → %s", self, node, new_children, new_children.parent, extra={"event.action": "__reassign_nodes", "logrite.node": node, "logrite.new_children": new_children})
        if node.parent is not None:  # reset its parent
            if node.is_right:  # If it is the right child
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            logger.warning("<<< Exiting __reassign_nodes(node=%s,new_children=%s)", node, new_children, extra={"event.action": "__reassign_nodes", "logrite.node": node, "logrite.new_children": new_children})
            self.root = new_children
            logger.debug("__reassign_nodes(self=%s,node=%s,new_children=%s): self.root → %s", self, node, new_children, self.root, extra={"event.action": "__reassign_nodes", "logrite.node": node, "logrite.new_children": new_children})

    def empty(self) -> bool:
        """
        Returns True if the tree does not have any element(s).
        False if the tree has element(s).

        >>> BinarySearchTree().empty()
        True
        >>> BinarySearchTree().insert(1).empty()
        False
        >>> BinarySearchTree().insert(8, 3, 6, 1, 10, 14, 13, 4, 7).empty()
        False
        """
        logger.error(">>> Entering empty()", extra={"event.action": "empty"})
        logger.warning("<<< Exiting empty()", extra={"event.action": "empty"})
        return not self.root

    def __insert(self, value) -> None:
        """
        Insert a new node in Binary Search Tree with value label
        """
        logger.error(">>> Entering __insert(value=%s)", value, extra={"event.action": "__insert", "logrite.value": value})
        new_node = Node(value)  # create a new Node
        logger.error("__insert(value=%s): new_node → %s", value, new_node, extra={"event.action": "__insert", "logrite.value": value})
        if self.empty():  # if Tree is empty
            self.root = new_node  # set its root
        else:  # Tree is not empty
            logger.debug("__insert(self=%s,value=%s): self.root → %s", self, value, self.root, extra={"event.action": "__insert", "logrite.value": value})
            parent_node = self.root  # from root
            if parent_node is None:
                logger.warning("<<< Exiting __insert(value=%s)", value, extra={"event.action": "__insert", "logrite.value": value})
                return
            while True:  # While we don't get to a leaf
                if value < parent_node.value:  # We go left
                    if parent_node.left is None:
                        parent_node.left = new_node  # We insert the new node in a leaf
                        logger.debug("__insert(self=%s,value=%s): parent_node.left → %s", self, value, parent_node.left, extra={"event.action": "__insert", "logrite.value": value})
                        break
                    else:
                        parent_node = parent_node.left
                elif parent_node.right is None:
                    parent_node.right = new_node
                    logger.debug("__insert(self=%s,value=%s): parent_node.right → %s", self, value, parent_node.right, extra={"event.action": "__insert", "logrite.value": value})
                    break
                else:
                    parent_node = parent_node.right
            new_node.parent = parent_node
            logger.debug("__insert(self=%s,value=%s): new_node.parent → %s", self, value, new_node.parent, extra={"event.action": "__insert", "logrite.value": value})

    def insert(self, *values) -> Self:
        logger.error(">>> Entering insert()", extra={"event.action": "insert"})
        for value in values:
            self.__insert(value)
        logger.warning("<<< Exiting insert()", extra={"event.action": "insert"})
        return self

    def search(self, value) -> Node | None:
        """
        >>> tree = BinarySearchTree().insert(10, 20, 30, 40, 50)
        >>> tree.search(10)
        {'10': (None, {'20': (None, {'30': (None, {'40': (None, 50)})})})}
        >>> tree.search(20)
        {'20': (None, {'30': (None, {'40': (None, 50)})})}
        >>> tree.search(30)
        {'30': (None, {'40': (None, 50)})}
        >>> tree.search(40)
        {'40': (None, 50)}
        >>> tree.search(50)
        50
        >>> tree.search(5) is None  # element not present
        True
        >>> tree.search(0) is None  # element not present
        True
        >>> tree.search(-5) is None  # element not present
        True
        >>> BinarySearchTree().search(10)
        Traceback (most recent call last):
            ...
        IndexError: Warning: Tree is empty! please use another.
        """
        logger.error(">>> Entering search(value=%s)", value, extra={"event.action": "search", "logrite.value": value})

        if self.empty():
            raise IndexError("Warning: Tree is empty! please use another.")
        else:
            node = self.root
            # use lazy evaluation here to avoid NoneType Attribute error
            while node is not None and node.value is not value:
                node = node.left if value < node.value else node.right
            logger.warning("<<< Exiting search(value=%s)", value, extra={"event.action": "search", "logrite.value": value})
            return node

    def get_max(self, node: Node | None = None) -> Node | None:
        """
        We go deep on the right branch

        >>> BinarySearchTree().insert(10, 20, 30, 40, 50).get_max()
        50
        >>> BinarySearchTree().insert(-5, -1, 0.1, -0.3, -4.5).get_max()
        {'0.1': (-0.3, None)}
        >>> BinarySearchTree().insert(1, 78.3, 30, 74.0, 1).get_max()
        {'78.3': ({'30': (1, 74.0)}, None)}
        >>> BinarySearchTree().insert(1, 783, 30, 740, 1).get_max()
        {'783': ({'30': (1, 740)}, None)}
        """
        logger.error(">>> Entering get_max(node=%s)", node, extra={"event.action": "get_max", "logrite.node": node})
        if node is None:
            if self.root is None:
                return None
            node = self.root

        if not self.empty():
            while node.right is not None:
                node = node.right
        logger.warning("<<< Exiting get_max(node=%s)", node, extra={"event.action": "get_max", "logrite.node": node})
        return node

    def get_min(self, node: Node | None = None) -> Node | None:
        """
        We go deep on the left branch

        >>> BinarySearchTree().insert(10, 20, 30, 40, 50).get_min()
        {'10': (None, {'20': (None, {'30': (None, {'40': (None, 50)})})})}
        >>> BinarySearchTree().insert(-5, -1, 0, -0.3, -4.5).get_min()
        {'-5': (None, {'-1': (-4.5, {'0': (-0.3, None)})})}
        >>> BinarySearchTree().insert(1, 78.3, 30, 74.0, 1).get_min()
        {'1': (None, {'78.3': ({'30': (1, 74.0)}, None)})}
        >>> BinarySearchTree().insert(1, 783, 30, 740, 1).get_min()
        {'1': (None, {'783': ({'30': (1, 740)}, None)})}
        """
        logger.error(">>> Entering get_min(node=%s)", node, extra={"event.action": "get_min", "logrite.node": node})
        if node is None:
            node = self.root
        if self.root is None:
            return None
        if not self.empty():
            node = self.root
            while node.left is not None:
                node = node.left
        logger.warning("<<< Exiting get_min(node=%s)", node, extra={"event.action": "get_min", "logrite.node": node})
        return node

    def remove(self, value: int) -> None:
        logger.error(">>> Entering remove(value=%s)", value, extra={"event.action": "remove", "logrite.value": value})
        # Look for the node with that label
        node = self.search(value)
        logger.error("remove(value=%s): node → %s", value, node, extra={"event.action": "remove", "logrite.value": value})
        if node is None:
            msg = f"Value {value} not found"
            logger.error("remove(value=%s): msg → %s", value, msg, extra={"event.action": "remove", "logrite.value": value})
            raise ValueError(msg)

        if node.left is None and node.right is None:  # If it has no children
            self.__reassign_nodes(node, None)
        elif node.left is None:  # Has only right children
            self.__reassign_nodes(node, node.right)
        elif node.right is None:  # Has only left children
            self.__reassign_nodes(node, node.left)
        else:
            predecessor = self.get_max(
                node.left
            )  # Gets the max value of the left branch
            self.remove(predecessor.value)  # type: ignore[union-attr]
            node.value = (
                predecessor.value  # type: ignore[union-attr]
            )  # Assigns the value to the node to delete and keep tree structure
            logger.warning("<<< Exiting remove(value=%s)", value, extra={"event.action": "remove", "logrite.value": value})

    def preorder_traverse(self, node: Node | None) -> Iterable:
        logger.error(">>> Entering preorder_traverse(node=%s)", node, extra={"event.action": "preorder_traverse", "logrite.node": node})
        if node is not None:
            yield node  # Preorder Traversal
            yield from self.preorder_traverse(node.left)
            yield from self.preorder_traverse(node.right)
            logger.warning("<<< Exiting preorder_traverse(node=%s)", node, extra={"event.action": "preorder_traverse", "logrite.node": node})

    def traversal_tree(self, traversal_function=None) -> Any:
        """
        This function traversal the tree.
        You can pass a function to traversal the tree as needed by client code
        """
        logger.error(">>> Entering traversal_tree(traversal_function=%s)", traversal_function, extra={"event.action": "traversal_tree", "logrite.traversal_function": traversal_function})
        if traversal_function is None:
            return self.preorder_traverse(self.root)
        else:
            logger.warning("<<< Exiting traversal_tree(traversal_function=%s)", traversal_function, extra={"event.action": "traversal_tree", "logrite.traversal_function": traversal_function})
            return traversal_function(self.root)

    def inorder(self, arr: list, node: Node | None) -> None:
        """Perform an inorder traversal and append values of the nodes to
        a list named arr"""
        logger.error(">>> Entering inorder(arr=%s,node=%s)", arr, node, extra={"event.action": "inorder", "logrite.arr": arr, "logrite.node": node})
        if node:
            self.inorder(arr, node.left)
            arr.append(node.value)
            self.inorder(arr, node.right)
            logger.warning("<<< Exiting inorder(arr=%s,node=%s)", arr, node, extra={"event.action": "inorder", "logrite.arr": arr, "logrite.node": node})

    def find_kth_smallest(self, k: int, node: Node) -> int:
        """Return the kth smallest element in a binary search tree"""
        logger.error(">>> Entering find_kth_smallest(k=%s,node=%s)", k, node, extra={"event.action": "find_kth_smallest", "logrite.k": k, "logrite.node": node})
        arr: list[int] = []
        self.inorder(arr, node)  # append all values to list using inorder traversal
        logger.warning("<<< Exiting find_kth_smallest(k=%s,node=%s)", k, node, extra={"event.action": "find_kth_smallest", "logrite.k": k, "logrite.node": node})
        return arr[k - 1]


def inorder(curr_node: Node | None) -> list[Node]:
    """
    inorder (left, self, right)
    """
    logger.error(">>> Entering inorder(curr_node=%s)", curr_node, extra={"event.action": "inorder", "logrite.curr_node": curr_node})
    node_list = []
    logger.error("inorder(curr_node=%s): node_list → %s", curr_node, node_list, extra={"event.action": "inorder", "logrite.curr_node": curr_node})
    if curr_node is not None:
        node_list = [*inorder(curr_node.left), curr_node, *inorder(curr_node.right)]
    logger.warning("<<< Exiting inorder(curr_node=%s)", curr_node, extra={"event.action": "inorder", "logrite.curr_node": curr_node})
    return node_list


def postorder(curr_node: Node | None) -> list[Node]:
    """
    postOrder (left, right, self)
    """
    logger.error(">>> Entering postorder(curr_node=%s)", curr_node, extra={"event.action": "postorder", "logrite.curr_node": curr_node})
    node_list = []
    logger.error("postorder(curr_node=%s): node_list → %s", curr_node, node_list, extra={"event.action": "postorder", "logrite.curr_node": curr_node})
    if curr_node is not None:
        node_list = postorder(curr_node.left) + postorder(curr_node.right) + [curr_node]
    logger.warning("<<< Exiting postorder(curr_node=%s)", curr_node, extra={"event.action": "postorder", "logrite.curr_node": curr_node})
    return node_list


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
