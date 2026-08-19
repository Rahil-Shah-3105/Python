"""
Implementation of an auto-balanced binary tree!
For doctests run following command:
python3 -m doctest -v avl_tree.py
For testing run:
python avl_tree.py
"""

from __future__ import annotations

import math
import random
from typing import Any
import logging
logger = logging.getLogger(__name__)


class MyQueue:
    def __init__(self) -> None:
        logger.debug(">>> Entering __init__()")
        self.data: list[Any] = []
        self.head: int = 0
        self.tail: int = 0
        logger.debug("<<< Exiting __init__()")
        logger.debug(">>> Entering __init__(data=%s)", data)
        logger.debug("__init__(self=%s,data=%s): self.data → %s", self, data, self.data)
        logger.debug("__init__(data=%s): self.data → %s", data, self.data)
        logger.debug("<<< Exiting __init__(data=%s)", data)

    def is_empty(self) -> bool:
        logger.debug(">>> Entering is_empty()")
        logger.debug("<<< Exiting is_empty()")
        return self.head == self.tail

    def push(self, data: Any) -> None:
        logger.debug(">>> Entering push(data=%s)", data)
        logger.debug("push(self=%s,data=%s): self.tail → %s", self, data, self.tail)
        self.data.append(data)
        logger.debug("<<< Exiting push(data=%s)", data)
        self.tail = self.tail + 1

    def pop(self) -> Any:
        logger.debug(">>> Entering pop()")
        ret = self.data[self.head]
        logger.debug("pop(self=%s): ret → %s", self, ret)
        self.head = self.head + 1
        logger.debug("pop(self=%s): self.head → %s", self, self.head)
        logger.debug("<<< Exiting pop()")
        return ret

    def count(self) -> int:
        logger.debug(">>> Entering count()")
        logger.debug("<<< Exiting count()")
        return self.tail - self.head

    def print_queue(self) -> None:
        logger.debug(">>> Entering print_queue()")
        print(self.data)
        print("**************")
        print(self.data[self.head : self.tail])
        logger.debug("<<< Exiting print_queue()")


class MyNode:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left: MyNode | None = None
        self.right: MyNode | None = None
        self.height: int = 1

    def get_data(self) -> Any:
        logger.debug(">>> Entering get_data()")
        logger.debug("<<< Exiting get_data()")
        return self.data

    def get_left(self) -> MyNode | None:
        logger.debug(">>> Entering get_left()")
        logger.debug("<<< Exiting get_left()")
        return self.left

    def get_right(self) -> MyNode | None:
        logger.debug(">>> Entering get_right()")
        logger.debug("<<< Exiting get_right()")
        return self.right

    def get_height(self) -> int:
        logger.debug(">>> Entering get_height(node=%s)", node)
        logger.debug("<<< Exiting get_height(node=%s)", node)
        return self.height

    def set_data(self, data: Any) -> None:
        logger.debug(">>> Entering set_data(data=%s)", data)
        self.data = data
        logger.debug("set_data(self=%s,data=%s): self.data → %s", self, data, self.data)
        logger.debug("set_data(data=%s): self.data → %s", data, self.data)
        logger.debug("<<< Exiting set_data(data=%s)", data)

    def set_left(self, node: MyNode | None) -> None:
        self.left = node
        logger.debug(">>> Entering set_left(node=%s)", node)
        logger.debug("set_left(self=%s,node=%s): self.left → %s", self, node, self.left)
        logger.debug("<<< Exiting set_left(node=%s)", node)

    def set_right(self, node: MyNode | None) -> None:
        self.right = node
        logger.debug(">>> Entering set_right(node=%s)", node)
        logger.debug("set_right(self=%s,node=%s): self.right → %s", self, node, self.right)
        logger.debug("<<< Exiting set_right(node=%s)", node)

    def set_height(self, height: int) -> None:
        self.height = height
        logger.debug(">>> Entering set_height(height=%s)", height)
        logger.debug("set_height(self=%s,height=%s): self.height → %s", self, height, self.height)

        logger.debug("<<< Exiting set_height(height=%s)", height)

def get_height(node: MyNode | None) -> int:
    logger.debug(">>> Entering get_height(node=%s)", node)
    if node is None:
        return 0
    return node.get_height()


def my_max(a: int, b: int) -> int:
    logger.debug(">>> Entering my_max(a=%s,b=%s)", a, b)
    if a > b:
        return a
    logger.debug("<<< Exiting my_max(a=%s,b=%s)", a, b)
    return b


def right_rotation(node: MyNode) -> MyNode:
    r"""
            A                      B
           / \                    / \
          B   C                  Bl  A
         / \       -->          /   / \
        Bl  Br                 UB Br  C
       /
     UB
    UB = unbalanced node
    """
    logger.debug(">>> Entering right_rotation(node=%s)", node)
    print("left rotation node:", node.get_data())
    ret = node.get_left()
    logger.debug("right_rotation(node=%s): ret → %s", node, ret)
    assert ret is not None
    node.set_left(ret.get_right())
    logger.debug("right_rotation(node=%s): node → %s", node, node)
    ret.set_right(node)
    h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
    logger.debug("right_rotation(node=%s): h1 → %s", node, h1)
    node.set_height(h1)
    h2 = my_max(get_height(ret.get_right()), get_height(ret.get_left())) + 1
    logger.debug("right_rotation(node=%s): h2 → %s", node, h2)
    ret.set_height(h2)
    logger.debug("<<< Exiting right_rotation(node=%s)", node)
    return ret


def left_rotation(node: MyNode) -> MyNode:
    """
    a mirror symmetry rotation of the left_rotation
    """
    logger.debug(">>> Entering left_rotation(node=%s)", node)
    print("right rotation node:", node.get_data())
    ret = node.get_right()
    logger.debug("left_rotation(node=%s): ret → %s", node, ret)
    assert ret is not None
    node.set_right(ret.get_left())
    logger.debug("left_rotation(node=%s): node → %s", node, node)
    ret.set_left(node)
    h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
    logger.debug("left_rotation(node=%s): h1 → %s", node, h1)
    node.set_height(h1)
    h2 = my_max(get_height(ret.get_right()), get_height(ret.get_left())) + 1
    logger.debug("left_rotation(node=%s): h2 → %s", node, h2)
    ret.set_height(h2)
    logger.debug("<<< Exiting left_rotation(node=%s)", node)
    return ret


def lr_rotation(node: MyNode) -> MyNode:
    r"""
            A              A                    Br
           / \            / \                  /  \
          B   C    LR    Br  C       RR       B    A
         / \       -->  /  \         -->    /     / \
        Bl  Br         B   UB              Bl    UB  C
             \        /
             UB     Bl
    RR = right_rotation   LR = left_rotation
    """
    logger.debug(">>> Entering lr_rotation(node=%s)", node)
    left_child = node.get_left()
    logger.debug("lr_rotation(node=%s): left_child → %s", node, left_child)
    assert left_child is not None
    node.set_left(left_rotation(left_child))
    logger.debug("lr_rotation(node=%s): node → %s", node, node)
    logger.debug("<<< Exiting lr_rotation(node=%s)", node)
    return right_rotation(node)


def rl_rotation(node: MyNode) -> MyNode:
    logger.debug(">>> Entering rl_rotation(node=%s)", node)
    right_child = node.get_right()
    logger.debug("rl_rotation(node=%s): right_child → %s", node, right_child)
    assert right_child is not None
    node.set_right(right_rotation(right_child))
    logger.debug("rl_rotation(node=%s): node → %s", node, node)
    logger.debug("<<< Exiting rl_rotation(node=%s)", node)
    return left_rotation(node)


def insert_node(node: MyNode | None, data: Any) -> MyNode | None:
    logger.debug(">>> Entering insert_node(node=%s,data=%s)", node, data)
    if node is None:
        return MyNode(data)
    if data < node.get_data():
        node.set_left(insert_node(node.get_left(), data))
        logger.debug("insert_node(node=%s,data=%s): node → %s", node, data, node)
        if (
            get_height(node.get_left()) - get_height(node.get_right()) == 2
        ):  # an unbalance detected
            left_child = node.get_left()
            logger.debug("insert_node(node=%s,data=%s): left_child → %s", node, data, left_child)
            assert left_child is not None
            if (
                data < left_child.get_data()
            ):  # new node is the left child of the left child
                node = right_rotation(node)
            else:
                node = lr_rotation(node)
    else:
        node.set_right(insert_node(node.get_right(), data))
        if get_height(node.get_right()) - get_height(node.get_left()) == 2:
            right_child = node.get_right()
            logger.debug("insert_node(node=%s,data=%s): right_child → %s", node, data, right_child)
            assert right_child is not None
            if data < right_child.get_data():
                node = rl_rotation(node)
            else:
                node = left_rotation(node)
    h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
    node.set_height(h1)
    logger.debug("<<< Exiting insert_node(node=%s,data=%s)", node, data)
    return node


def get_right_most(root: MyNode) -> Any:
    logger.debug(">>> Entering get_right_most(root=%s)", root)
    while True:
        right_child = root.get_right()
        logger.debug("get_right_most(root=%s): right_child → %s", root, right_child)
        if right_child is None:
            break
        root = right_child
    logger.debug("<<< Exiting get_right_most(root=%s)", root)
    return root.get_data()


def get_left_most(root: MyNode) -> Any:
    logger.debug(">>> Entering get_left_most(root=%s)", root)
    while True:
        left_child = root.get_left()
        logger.debug("get_left_most(root=%s): left_child → %s", root, left_child)
        if left_child is None:
            break
        root = left_child
    logger.debug("<<< Exiting get_left_most(root=%s)", root)
    return root.get_data()


def del_node(root: MyNode, data: Any) -> MyNode | None:
    logger.debug(">>> Entering del_node(root=%s,data=%s)", root, data)
    left_child = root.get_left()
    logger.debug("del_node(root=%s,data=%s): left_child → %s", root, data, left_child)
    right_child = root.get_right()
    if root.get_data() == data:
        logger.debug("del_node(root=%s,data=%s): right_child → %s", root, data, right_child)
        if left_child is not None and right_child is not None:
            temp_data = get_left_most(right_child)
            logger.debug("del_node(root=%s,data=%s): temp_data → %s", root, data, temp_data)
            root.set_data(temp_data)
            root.set_right(del_node(right_child, temp_data))
            logger.warning("del_node(root=%s,data=%s): root → %s", root, data, root)
        elif left_child is not None:
            root = left_child
            logger.debug("del_node(root=%s,data=%s): root → %s", root, data, root)
        elif right_child is not None:
            root = right_child
        else:
            return None
    elif root.get_data() > data:
        if left_child is None:
            print("No such data")
            return root
        else:
            root.set_left(del_node(left_child, data))
    # root.get_data() < data
    elif right_child is None:
        return root
    else:
        root.set_right(del_node(right_child, data))

    # Re-fetch left_child and right_child references
    left_child = root.get_left()
    right_child = root.get_right()

    if get_height(right_child) - get_height(left_child) == 2:
        assert right_child is not None
        if get_height(right_child.get_right()) > get_height(right_child.get_left()):
            root = left_rotation(root)
        else:
            root = rl_rotation(root)
    elif get_height(right_child) - get_height(left_child) == -2:
        assert left_child is not None
        if get_height(left_child.get_left()) > get_height(left_child.get_right()):
            root = right_rotation(root)
        else:
            logger.debug(">>> Entering get_height()")
            logger.debug("<<< Exiting get_height()")
            root = lr_rotation(root)
    height = my_max(get_height(root.get_right()), get_height(root.get_left())) + 1
    logger.debug("del_node(root=%s,data=%s): height → %s", root, data, height)
    root.set_height(height)
    logger.debug("<<< Exiting del_node(root=%s,data=%s)", root, data)
    logger.debug(">>> Entering del_node(data=%s)", data)
    logger.debug("<<< Exiting del_node(data=%s)", data)
    return root


class AVLtree:
    """
    An AVL tree doctest
    Examples:
    >>> t = AVLtree()
    >>> t.insert(4)
    insert:4
    >>> print(str(t).replace(" \\n","\\n"))
     4
    *************************************
    >>> t.insert(2)
    insert:2
    >>> print(str(t).replace(" \\n","\\n").replace(" \\n","\\n"))
      4
     2  *
    *************************************
    >>> t.insert(3)
    insert:3
    right rotation node: 2
    left rotation node: 4
    >>> print(str(t).replace(" \\n","\\n").replace(" \\n","\\n"))
      3
     2  4
    *************************************
    >>> t.get_height()
    2
    >>> t.del_node(3)
    delete:3
    >>> print(str(t).replace(" \\n","\\n").replace(" \\n","\\n"))
      4
     2  *
    *************************************
    """

    def __init__(self) -> None:
        self.root: MyNode | None = None

    def get_height(self) -> int:
        logger.debug(">>> Entering get_height()")
        return get_height(self.root)

    def insert(self, data: Any) -> None:
        logger.debug(">>> Entering insert(data=%s)", data)
        logger.debug("insert(data=%s): self.root → %s", data, self.root)
        print("insert:" + str(data))
        logger.debug("<<< Exiting insert(data=%s)", data)
        self.root = insert_node(self.root, data)

    def del_node(self, data: Any) -> None:
        print("delete:" + str(data))
        if self.root is None:
            print("Tree is empty!")
            return
        self.root = del_node(self.root, data)

    def __str__(
        self,
    ) -> str:  # a level traversale, gives a more intuitive look on the tree
        output = ""
        q = MyQueue()
        q.push(self.root)
        layer = self.get_height()
        if layer == 0:
            return output
        cnt = 0
        while not q.is_empty():
            node = q.pop()
            space = " " * int(math.pow(2, layer - 1))
            output += space
            if node is None:
                output += "*"
                q.push(None)
                q.push(None)
            else:
                output += str(node.get_data())
                q.push(node.get_left())
                q.push(node.get_right())
            output += space
            cnt = cnt + 1
            for i in range(100):
                if cnt == math.pow(2, i) - 1:
                    layer = layer - 1
                    if layer == 0:
                        output += "\n*************************************"
                        return output
                    output += "\n"
                    break
        output += "\n*************************************"
        return output


def _test() -> None:
    logger.debug(">>> Entering _test()")
    import doctest

    doctest.testmod()
    logger.debug("<<< Exiting _test()")


if __name__ == "__main__":
    _test()
    t = AVLtree()
    lst = list(range(10))
    random.shuffle(lst)
    for i in lst:
        t.insert(i)
        print(str(t))
    random.shuffle(lst)
    for i in lst:
        t.del_node(i)
        print(str(t))
