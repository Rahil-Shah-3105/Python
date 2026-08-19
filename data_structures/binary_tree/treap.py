from __future__ import annotations

from random import random
import logging
logger = logging.getLogger(__name__)


class Node:
    """
    Treap's node
    Treap is a binary tree by value and heap by priority
    """

    def __init__(self, value: int | None = None):
        logger.debug(">>> Entering __init__(value=%s)", value)
        self.value = value
        logger.debug("__init__(self=%s,value=%s): self.value → %s", self, value, self.value)
        self.prior = random()
        logger.debug("__init__(value=%s): self.prior → %s", value, self.prior)
        self.left: Node | None = None
        self.right: Node | None = None
        logger.debug("<<< Exiting __init__(value=%s)", value)

    def __repr__(self) -> str:
        logger.debug(">>> Entering __repr__()")
        from pprint import pformat

        if self.left is None and self.right is None:
            return f"'{self.value}: {self.prior:.5}'"
        else:
            logger.debug("<<< Exiting __repr__()")
            return pformat(
                {f"{self.value}: {self.prior:.5}": (self.left, self.right)}, indent=1
            )

    def __str__(self) -> str:
        logger.debug(">>> Entering __str__()")
        value = str(self.value) + " "
        left = str(self.left or "")
        logger.debug("__str__(): value → %s", value)
        logger.debug("__str__(self=%s): value → %s", self, value)
        logger.debug("__str__(self=%s): left → %s", self, left)
        logger.debug("__str__(): left → %s", left)
        right = str(self.right or "")
        logger.debug("__str__(self=%s): right → %s", self, right)
        logger.debug("__str__(): right → %s", right)
        logger.debug("<<< Exiting __str__()")
        return value + left + right


def split(root: Node | None, value: int) -> tuple[Node | None, Node | None]:
    """
    We split current tree into 2 trees with value:

    Left tree contains all values less than split value.
    Right tree contains all values greater or equal, than split value
    """
    logger.debug(">>> Entering split(root=%s,value=%s)", root, value)
    if root is None or root.value is None:  # None tree is split into 2 Nones
        return None, None
    elif value < root.value:
        """
        Right tree's root will be current node.
        Now we split(with the same value) current node's left son
        Left tree: left part of that split
        Right tree's left son: right part of that split
        """
        left, root.left = split(root.left, value)
        return left, root
    else:
        """
        Just symmetric to previous case
        """
        root.right, right = split(root.right, value)
        logger.debug("<<< Exiting split(root=%s,value=%s)", root, value)
        return root, right


def merge(left: Node | None, right: Node | None) -> Node | None:
    """
    We merge 2 trees into one.
    Note: all left tree's values must be less than all right tree's
    """
    logger.debug(">>> Entering merge(left=%s,right=%s)", left, right)
    if (not left) or (not right):  # If one node is None, return the other
        return left or right
    elif left.prior < right.prior:
        """
        Left will be root because it has more priority
        Now we need to merge left's right son and right tree
        """
        left.right = merge(left.right, right)
        return left
    else:
        """
        Symmetric as well
        """
        right.left = merge(left, right.left)
        logger.debug("<<< Exiting merge(left=%s,right=%s)", left, right)
        return right


def insert(root: Node | None, value: int) -> Node | None:
    """
    Insert element

    Split current tree with a value into left, right,
    Insert new node into the middle
    Merge left, node, right into root
    """
    logger.debug(">>> Entering insert(root=%s,value=%s)", root, value)
    node = Node(value)
    logger.debug("insert(root=%s,value=%s): node → %s", root, value, node)
    left, right = split(root, value)
    logger.debug("<<< Exiting insert(root=%s,value=%s)", root, value)
    return merge(merge(left, node), right)


def erase(root: Node | None, value: int) -> Node | None:
    """
    Erase element

    Split all nodes with values less into left,
    Split all nodes with values greater into right.
    Merge left, right
    """
    logger.debug(">>> Entering erase(root=%s,value=%s)", root, value)
    left, right = split(root, value - 1)
    _, right = split(right, value)
    logger.debug("<<< Exiting erase(root=%s,value=%s)", root, value)
    return merge(left, right)


def inorder(root: Node | None) -> None:
    """
    Just recursive print of a tree
    """
    logger.debug(">>> Entering inorder(root=%s)", root)
    if not root:  # None
        logger.debug("<<< Exiting inorder(root=%s)", root)
        return
    else:
        inorder(root.left)
        print(root.value, end=",")
        inorder(root.right)


def interact_treap(root: Node | None, args: str) -> Node | None:
    """
    Commands:
    + value to add value into treap
    - value to erase all nodes with value

        >>> root = interact_treap(None, "+1")
        >>> inorder(root)
        1,
        >>> root = interact_treap(root, "+3 +5 +17 +19 +2 +16 +4 +0")
        >>> inorder(root)
        0,1,2,3,4,5,16,17,19,
        >>> root = interact_treap(root, "+4 +4 +4")
        >>> inorder(root)
        0,1,2,3,4,4,4,4,5,16,17,19,
        >>> root = interact_treap(root, "-0")
        >>> inorder(root)
        1,2,3,4,4,4,4,5,16,17,19,
        >>> root = interact_treap(root, "-4")
        >>> inorder(root)
        1,2,3,5,16,17,19,
        >>> root = interact_treap(root, "=0")
        Unknown command
    """
    logger.debug(">>> Entering interact_treap(root=%s,args=%s)", root, args)
    for arg in args.split():
        if arg[0] == "+":
            root = insert(root, int(arg[1:]))
            logger.debug("interact_treap(root=%s,args=%s): root → %s", root, args, root)

        elif arg[0] == "-":
            root = erase(root, int(arg[1:]))

        else:
            print("Unknown command")

    logger.debug("<<< Exiting interact_treap(root=%s,args=%s)", root, args)
    logger.debug("main(): root → %s", root)
    return root


def main() -> None:
    """After each command, program prints treap"""
    logger.debug(">>> Entering main()")
    import time; __log_start = time.time()
    root = None
    logger.warning("main(): root → %s", root)
    print(
        "enter numbers to create a tree, + value to add value into treap, "
        "- value to erase all nodes with value. 'q' to quit. "
    )
    logger.info("main()=: database operation took %s ms", int((time.time() - __log_start) * 1000))

    args = input()
    logger.debug("main(): args → %s", args)
    while args != "q":
        root = interact_treap(root, args)
        print(root)
        args = input()

    print("good by!")
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
