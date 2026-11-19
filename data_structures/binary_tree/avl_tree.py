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
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.data: list[Any] = []
        self.head: int = 0
        self.tail: int = 0
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})

    def is_empty(self) -> bool:
        logger.error(">>> Entering is_empty()", extra={"event.action": "is_empty"})
        logger.warning("<<< Exiting is_empty()", extra={"event.action": "is_empty"})
        return self.head == self.tail

    def push(self, data: Any) -> None:
        logger.error(">>> Entering push(data=%s)", data, extra={"event.action": "push"})
        self.data.append(data)
        logger.warning("<<< Exiting push(data=%s)", data, extra={"event.action": "push"})
        self.tail = self.tail + 1
        logger.debug("push(self=%s,data=%s): self.tail → %s", self, data, self.tail, extra={"event.action": "push"})

    def pop(self) -> Any:
        logger.error(">>> Entering pop()", extra={"event.action": "pop"})
        ret = self.data[self.head]
        self.head = self.head + 1
        logger.debug("pop(self=%s): self.head → %s", self, self.head, extra={"event.action": "pop"})
        logger.warning("<<< Exiting pop()", extra={"event.action": "pop"})
        return ret

    def count(self) -> int:
        logger.error(">>> Entering count()", extra={"event.action": "count"})
        logger.warning("<<< Exiting count()", extra={"event.action": "count"})
        return self.tail - self.head

    def print_queue(self) -> None:
        logger.error(">>> Entering print_queue()", extra={"event.action": "print_queue"})
        print(self.data)
        print("**************")
        print(self.data[self.head : self.tail])
        logger.warning("<<< Exiting print_queue()", extra={"event.action": "print_queue"})


class MyNode:
    def __init__(self, data: Any) -> None:
        logger.error(">>> Entering __init__(data=%s)", data, extra={"event.action": "__init__"})
        self.data = data
        logger.debug("__init__(self=%s,data=%s): self.data → %s", self, data, self.data, extra={"event.action": "__init__"})
        logger.error("__init__(data=%s): self.data → %s", data, self.data, extra={"event.action": "__init__"})
        self.left: MyNode | None = None
        self.right: MyNode | None = None
        self.height: int = 1
        logger.warning("<<< Exiting __init__(data=%s)", data, extra={"event.action": "__init__"})

    def get_data(self) -> Any:
        logger.error(">>> Entering get_data()", extra={"event.action": "get_data"})
        logger.warning("<<< Exiting get_data()", extra={"event.action": "get_data"})
        return self.data

    def get_left(self) -> MyNode | None:
        logger.error(">>> Entering get_left()", extra={"event.action": "get_left"})
        logger.warning("<<< Exiting get_left()", extra={"event.action": "get_left"})
        return self.left

    def get_right(self) -> MyNode | None:
        logger.error(">>> Entering get_right()", extra={"event.action": "get_right"})
        logger.warning("<<< Exiting get_right()", extra={"event.action": "get_right"})
        return self.right

    def get_height(self) -> int:
        logger.error(">>> Entering get_height()", extra={"event.action": "get_height"})
        logger.warning("<<< Exiting get_height()", extra={"event.action": "get_height"})
        return self.height

    def set_data(self, data: Any) -> None:
        logger.error(">>> Entering set_data(data=%s)", data, extra={"event.action": "set_data"})
        self.data = data
        logger.error("set_data(data=%s): self.data → %s", data, self.data, extra={"event.action": "set_data"})
        logger.debug("set_data(self=%s,data=%s): self.data → %s", self, data, self.data, extra={"event.action": "set_data"})

    def set_left(self, node: MyNode | None) -> None:
        logger.error(">>> Entering set_left(node=%s)", node, extra={"event.action": "set_left", "logrite.node": node})
        self.left = node
        logger.warning("<<< Exiting set_left(node=%s)", node, extra={"event.action": "set_left", "logrite.node": node})
        logger.debug("set_left(self=%s,node=%s): self.left → %s", self, node, self.left, extra={"event.action": "set_left", "logrite.node": node})

    def set_right(self, node: MyNode | None) -> None:
        logger.error(">>> Entering set_right(node=%s)", node, extra={"event.action": "set_right", "logrite.node": node})
        self.right = node
        logger.warning("<<< Exiting set_right(node=%s)", node, extra={"event.action": "set_right", "logrite.node": node})
        logger.debug("set_right(self=%s,node=%s): self.right → %s", self, node, self.right, extra={"event.action": "set_right", "logrite.node": node})

    def set_height(self, height: int) -> None:
        logger.error(">>> Entering set_height(height=%s)", height, extra={"event.action": "set_height", "logrite.height": height})
        self.height = height
        logger.warning("<<< Exiting set_height(height=%s)", height, extra={"event.action": "set_height", "logrite.height": height})
        logger.debug("set_height(self=%s,height=%s): self.height → %s", self, height, self.height, extra={"event.action": "set_height", "logrite.height": height})


def get_height(node: MyNode | None) -> int:
    logger.error(">>> Entering get_height(node=%s)", node, extra={"event.action": "get_height", "logrite.node": node})
    if node is None:
        return 0
    logger.warning("<<< Exiting get_height(node=%s)", node, extra={"event.action": "get_height", "logrite.node": node})
    return node.get_height()


def my_max(a: int, b: int) -> int:
    logger.error(">>> Entering my_max(a=%s,b=%s)", a, b, extra={"event.action": "my_max", "logrite.a": a, "logrite.b": b})
    if a > b:
        return a
    logger.warning("<<< Exiting my_max(a=%s,b=%s)", a, b, extra={"event.action": "my_max", "logrite.a": a, "logrite.b": b})
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
    logger.error(">>> Entering right_rotation(node=%s)", node, extra={"event.action": "right_rotation", "logrite.node": node})
    print("left rotation node:", node.get_data())
    ret = node.get_left()
    logger.error("right_rotation(node=%s): ret → %s", node, ret, extra={"event.action": "right_rotation", "logrite.node": node})
    assert ret is not None
    node.set_left(ret.get_right())
    logger.debug("right_rotation(node=%s): node → %s", node, node, extra={"event.action": "right_rotation", "logrite.node": node})
    logger.debug("right_rotation(node=%s): ret → %s", node, ret, extra={"event.action": "right_rotation", "logrite.node": node})
    ret.set_right(node)
    h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
    logger.error("right_rotation(node=%s): h1 → %s", node, h1, extra={"event.action": "right_rotation", "logrite.node": node})
    node.set_height(h1)
    h2 = my_max(get_height(ret.get_right()), get_height(ret.get_left())) + 1
    logger.error("right_rotation(node=%s): h2 → %s", node, h2, extra={"event.action": "right_rotation", "logrite.node": node})
    ret.set_height(h2)
    logger.warning("<<< Exiting right_rotation(node=%s)", node, extra={"event.action": "right_rotation", "logrite.node": node})
    return ret


def left_rotation(node: MyNode) -> MyNode:
    """
    a mirror symmetry rotation of the left_rotation
    """
    logger.error(">>> Entering left_rotation(node=%s)", node, extra={"event.action": "left_rotation", "logrite.node": node})
    print("right rotation node:", node.get_data())
    ret = node.get_right()
    logger.error("left_rotation(node=%s): ret → %s", node, ret, extra={"event.action": "left_rotation", "logrite.node": node})
    assert ret is not None
    node.set_right(ret.get_left())
    logger.debug("left_rotation(node=%s): node → %s", node, node, extra={"event.action": "left_rotation", "logrite.node": node})
    logger.debug("left_rotation(node=%s): ret → %s", node, ret, extra={"event.action": "left_rotation", "logrite.node": node})
    ret.set_left(node)
    h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
    logger.error("left_rotation(node=%s): h1 → %s", node, h1, extra={"event.action": "left_rotation", "logrite.node": node})
    node.set_height(h1)
    h2 = my_max(get_height(ret.get_right()), get_height(ret.get_left())) + 1
    logger.error("left_rotation(node=%s): h2 → %s", node, h2, extra={"event.action": "left_rotation", "logrite.node": node})
    ret.set_height(h2)
    logger.warning("<<< Exiting left_rotation(node=%s)", node, extra={"event.action": "left_rotation", "logrite.node": node})
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
    logger.error(">>> Entering lr_rotation(node=%s)", node, extra={"event.action": "lr_rotation", "logrite.node": node})
    left_child = node.get_left()
    logger.error("lr_rotation(node=%s): left_child → %s", node, left_child, extra={"event.action": "lr_rotation", "logrite.node": node})
    assert left_child is not None
    node.set_left(left_rotation(left_child))
    logger.debug("lr_rotation(node=%s): node → %s", node, node, extra={"event.action": "lr_rotation", "logrite.node": node})
    logger.warning("<<< Exiting lr_rotation(node=%s)", node, extra={"event.action": "lr_rotation", "logrite.node": node})
    return right_rotation(node)


def rl_rotation(node: MyNode) -> MyNode:
    logger.error(">>> Entering rl_rotation(node=%s)", node, extra={"event.action": "rl_rotation", "logrite.node": node})
    right_child = node.get_right()
    logger.error("rl_rotation(node=%s): right_child → %s", node, right_child, extra={"event.action": "rl_rotation", "logrite.node": node})
    assert right_child is not None
    node.set_right(right_rotation(right_child))
    logger.debug("rl_rotation(node=%s): node → %s", node, node, extra={"event.action": "rl_rotation", "logrite.node": node})
    logger.warning("<<< Exiting rl_rotation(node=%s)", node, extra={"event.action": "rl_rotation", "logrite.node": node})
    return left_rotation(node)


def insert_node(node: MyNode | None, data: Any) -> MyNode | None:
    logger.error(">>> Entering insert_node(node=%s,data=%s)", node, data, extra={"event.action": "insert_node", "logrite.node": node})
    if node is None:
        return MyNode(data)
    if data < node.get_data():
        node.set_left(insert_node(node.get_left(), data))
        if (
            get_height(node.get_left()) - get_height(node.get_right()) == 2
        ):  # an unbalance detected
            left_child = node.get_left()
            assert left_child is not None
            if (
                data < left_child.get_data()
            ):  # new node is the left child of the left child
                node = right_rotation(node)
            else:
                node = lr_rotation(node)
                logger.debug("insert_node(node=%s,data=%s): node → %s", node, data, node, extra={"event.action": "insert_node", "logrite.node": node})
    else:
        node.set_right(insert_node(node.get_right(), data))
        if get_height(node.get_right()) - get_height(node.get_left()) == 2:
            right_child = node.get_right()
            assert right_child is not None
            if data < right_child.get_data():
                node = rl_rotation(node)
            else:
                node = left_rotation(node)
    h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
    node.set_height(h1)
    logger.warning("<<< Exiting insert_node(node=%s,data=%s)", node, data, extra={"event.action": "insert_node", "logrite.node": node})
    return node


def get_right_most(root: MyNode) -> Any:
    logger.error(">>> Entering get_right_most(root=%s)", root, extra={"event.action": "get_right_most", "logrite.root": root})
    while True:
        right_child = root.get_right()
        logger.error("get_right_most(root=%s): right_child → %s", root, right_child, extra={"event.action": "get_right_most", "logrite.root": root})
        if right_child is None:
            break
        root = right_child
    logger.warning("<<< Exiting get_right_most(root=%s)", root, extra={"event.action": "get_right_most", "logrite.root": root})
    return root.get_data()


def get_left_most(root: MyNode) -> Any:
    logger.error(">>> Entering get_left_most(root=%s)", root, extra={"event.action": "get_left_most", "logrite.root": root})
    while True:
        left_child = root.get_left()
        logger.error("get_left_most(root=%s): left_child → %s", root, left_child, extra={"event.action": "get_left_most", "logrite.root": root})
        if left_child is None:
            break
        root = left_child
    logger.warning("<<< Exiting get_left_most(root=%s)", root, extra={"event.action": "get_left_most", "logrite.root": root})
    return root.get_data()


def del_node(root: MyNode, data: Any) -> MyNode | None:
    logger.error(">>> Entering del_node(root=%s,data=%s)", root, data, extra={"event.action": "del_node", "logrite.root": root})
    left_child = root.get_left()
    logger.error("del_node(root=%s,data=%s): left_child → %s", root, data, left_child, extra={"event.action": "del_node", "logrite.root": root})
    right_child = root.get_right()
    logger.error("del_node(root=%s,data=%s): right_child → %s", root, data, right_child, extra={"event.action": "del_node", "logrite.root": root})
    if root.get_data() == data:
        if left_child is not None and right_child is not None:
            temp_data = get_left_most(right_child)
            logger.error("del_node(root=%s,data=%s): temp_data → %s", root, data, temp_data, extra={"event.action": "del_node", "logrite.root": root})
            root.set_data(temp_data)
            root.set_right(del_node(right_child, temp_data))
        elif left_child is not None:
            root = left_child
        elif right_child is not None:
            root = right_child
            logger.error("del_node(root=%s,data=%s): root → %s", root, data, root, extra={"event.action": "del_node", "logrite.root": root})
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
            root = lr_rotation(root)
    height = my_max(get_height(root.get_right()), get_height(root.get_left())) + 1
    root.set_height(height)
    logger.warning("<<< Exiting del_node(root=%s,data=%s)", root, data, extra={"event.action": "del_node", "logrite.root": root})
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
        return get_height(self.root)

    def insert(self, data: Any) -> None:
        logger.error(">>> Entering insert(data=%s)", data, extra={"event.action": "insert"})
        print("insert:" + str(data))
        logger.warning("<<< Exiting insert(data=%s)", data, extra={"event.action": "insert"})
        self.root = insert_node(self.root, data)
        logger.error("insert(data=%s): self.root → %s", data, self.root, extra={"event.action": "insert"})

    def del_node(self, data: Any) -> None:
        logger.error(">>> Entering del_node(data=%s)", data, extra={"event.action": "del_node"})
        print("delete:" + str(data))
        if self.root is None:
            print("Tree is empty!")
            logger.warning("<<< Exiting del_node(data=%s)", data, extra={"event.action": "del_node"})
            return
        self.root = del_node(self.root, data)

    def __str__(
    logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
    logger.error("__str__(): output → %s", output, extra={"event.action": "__str__"})
    logger.error("__str__(): q → %s", q, extra={"event.action": "__str__"})
    logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
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
    logger.error(">>> Entering _test()", extra={"event.action": "_test"})
    import doctest

    doctest.testmod()
    logger.warning("<<< Exiting _test()", extra={"event.action": "_test"})


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
