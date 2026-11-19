"""
This is pure Python implementation of tree traversal algorithms
"""

from __future__ import annotations

import queue
import logging
logger = logging.getLogger(__name__)


class TreeNode:
    def __init__(self, data):
        logger.error(">>> Entering __init__(data=%s)", data, extra={"event.action": "__init__"})
        self.data = data
        logger.debug("__init__(self=%s,data=%s): self.data → %s", self, data, self.data, extra={"event.action": "__init__"})
        logger.error("__init__(data=%s): self.data → %s", data, self.data, extra={"event.action": "__init__"})
        self.right = None
        self.left = None
        logger.debug("__init__(self=%s,data=%s): self.left → %s", self, data, self.left, extra={"event.action": "__init__"})
        logger.debug("__init__(self=%s,data=%s): self.right → %s", self, data, self.right, extra={"event.action": "__init__"})

        logger.warning("<<< Exiting __init__(data=%s)", data, extra={"event.action": "__init__"})

def build_tree() -> TreeNode:
    logger.error(">>> Entering build_tree()", extra={"event.action": "build_tree"})
    print("\n********Press N to stop entering at any point of time********\n")
    check = input("Enter the value of the root node: ").strip().lower()
    logger.error("build_tree(): check → %s", check, extra={"event.action": "build_tree"})
    q: queue.Queue = queue.Queue()
    tree_node = TreeNode(int(check))
    logger.error("build_tree(): tree_node → %s", tree_node, extra={"event.action": "build_tree"})
    q.put(tree_node)
    while not q.empty():
        node_found = q.get()
        logger.error("build_tree(): node_found → %s", node_found, extra={"event.action": "build_tree"})
        msg = f"Enter the left node of {node_found.data}: "
        logger.error("build_tree(): msg → %s", msg, extra={"event.action": "build_tree"})
        check = input(msg).strip().lower() or "n"
        if check == "n":
            return tree_node
        left_node = TreeNode(int(check))
        node_found.left = left_node
        logger.debug("build_tree(): node_found.left → %s", node_found.left, extra={"event.action": "build_tree"})
        q.put(left_node)
        msg = f"Enter the right node of {node_found.data}: "
        check = input(msg).strip().lower() or "n"
        if check == "n":
            logger.warning("<<< Exiting build_tree()", extra={"event.action": "build_tree"})
            return tree_node
        right_node = TreeNode(int(check))
        node_found.right = right_node
        logger.debug("build_tree(): node_found.right → %s", node_found.right, extra={"event.action": "build_tree"})
        q.put(right_node)
    raise ValueError("Something went wrong")


def pre_order(node: TreeNode) -> None:
    """
    >>> root = TreeNode(1)
    >>> tree_node2 = TreeNode(2)
    >>> tree_node3 = TreeNode(3)
    >>> tree_node4 = TreeNode(4)
    >>> tree_node5 = TreeNode(5)
    >>> tree_node6 = TreeNode(6)
    >>> tree_node7 = TreeNode(7)
    >>> root.left, root.right = tree_node2, tree_node3
    >>> tree_node2.left, tree_node2.right = tree_node4 , tree_node5
    >>> tree_node3.left, tree_node3.right = tree_node6 , tree_node7
    >>> pre_order(root)
    1,2,4,5,3,6,7,
    """
    logger.error(">>> Entering pre_order(node=%s)", node, extra={"event.action": "pre_order", "logrite.node": node})
    if not isinstance(node, TreeNode) or not node:
        logger.warning("<<< Exiting pre_order(node=%s)", node, extra={"event.action": "pre_order", "logrite.node": node})
        return
    print(node.data, end=",")
    pre_order(node.left)
    pre_order(node.right)


def in_order(node: TreeNode) -> None:
    """
    >>> root = TreeNode(1)
    >>> tree_node2 = TreeNode(2)
    >>> tree_node3 = TreeNode(3)
    >>> tree_node4 = TreeNode(4)
    >>> tree_node5 = TreeNode(5)
    >>> tree_node6 = TreeNode(6)
    >>> tree_node7 = TreeNode(7)
    >>> root.left, root.right = tree_node2, tree_node3
    >>> tree_node2.left, tree_node2.right = tree_node4 , tree_node5
    >>> tree_node3.left, tree_node3.right = tree_node6 , tree_node7
    >>> in_order(root)
    4,2,5,1,6,3,7,
    """
    logger.error(">>> Entering in_order(node=%s)", node, extra={"event.action": "in_order", "logrite.node": node})
    if not isinstance(node, TreeNode) or not node:
        logger.warning("<<< Exiting in_order(node=%s)", node, extra={"event.action": "in_order", "logrite.node": node})
        return
    in_order(node.left)
    print(node.data, end=",")
    in_order(node.right)


def post_order(node: TreeNode) -> None:
    """
    >>> root = TreeNode(1)
    >>> tree_node2 = TreeNode(2)
    >>> tree_node3 = TreeNode(3)
    >>> tree_node4 = TreeNode(4)
    >>> tree_node5 = TreeNode(5)
    >>> tree_node6 = TreeNode(6)
    >>> tree_node7 = TreeNode(7)
    >>> root.left, root.right = tree_node2, tree_node3
    >>> tree_node2.left, tree_node2.right = tree_node4 , tree_node5
    >>> tree_node3.left, tree_node3.right = tree_node6 , tree_node7
    >>> post_order(root)
    4,5,2,6,7,3,1,
    """
    logger.error(">>> Entering post_order(node=%s)", node, extra={"event.action": "post_order", "logrite.node": node})
    if not isinstance(node, TreeNode) or not node:
        logger.warning("<<< Exiting post_order(node=%s)", node, extra={"event.action": "post_order", "logrite.node": node})
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end=",")


def level_order(node: TreeNode) -> None:
    """
    >>> root = TreeNode(1)
    >>> tree_node2 = TreeNode(2)
    >>> tree_node3 = TreeNode(3)
    >>> tree_node4 = TreeNode(4)
    >>> tree_node5 = TreeNode(5)
    >>> tree_node6 = TreeNode(6)
    >>> tree_node7 = TreeNode(7)
    >>> root.left, root.right = tree_node2, tree_node3
    >>> tree_node2.left, tree_node2.right = tree_node4 , tree_node5
    >>> tree_node3.left, tree_node3.right = tree_node6 , tree_node7
    >>> level_order(root)
    1,2,3,4,5,6,7,
    """
    logger.error(">>> Entering level_order(node=%s)", node, extra={"event.action": "level_order", "logrite.node": node})
    if not isinstance(node, TreeNode) or not node:
        logger.warning("<<< Exiting level_order(node=%s)", node, extra={"event.action": "level_order", "logrite.node": node})
        return
    q: queue.Queue = queue.Queue()
    q.put(node)
    while not q.empty():
        node_dequeued = q.get()
        print(node_dequeued.data, end=",")
        if node_dequeued.left:
            q.put(node_dequeued.left)
        if node_dequeued.right:
            q.put(node_dequeued.right)


def level_order_actual(node: TreeNode) -> None:
    """
    >>> root = TreeNode(1)
    >>> tree_node2 = TreeNode(2)
    >>> tree_node3 = TreeNode(3)
    >>> tree_node4 = TreeNode(4)
    >>> tree_node5 = TreeNode(5)
    >>> tree_node6 = TreeNode(6)
    >>> tree_node7 = TreeNode(7)
    >>> root.left, root.right = tree_node2, tree_node3
    >>> tree_node2.left, tree_node2.right = tree_node4 , tree_node5
    >>> tree_node3.left, tree_node3.right = tree_node6 , tree_node7
    >>> level_order_actual(root)
    1,
    2,3,
    4,5,6,7,
    """
    logger.error(">>> Entering level_order_actual(node=%s)", node, extra={"event.action": "level_order_actual", "logrite.node": node})
    if not isinstance(node, TreeNode) or not node:
        logger.warning("<<< Exiting level_order_actual(node=%s)", node, extra={"event.action": "level_order_actual", "logrite.node": node})
        return
    q: queue.Queue = queue.Queue()
    q.put(node)
    while not q.empty():
        list_ = []
        while not q.empty():
            node_dequeued = q.get()
            print(node_dequeued.data, end=",")
            if node_dequeued.left:
                list_.append(node_dequeued.left)
            if node_dequeued.right:
                list_.append(node_dequeued.right)
        print()
        for inner_node in list_:
            q.put(inner_node)


# iteration version
def pre_order_iter(node: TreeNode) -> None:
    """
    >>> root = TreeNode(1)
    >>> tree_node2 = TreeNode(2)
    >>> tree_node3 = TreeNode(3)
    >>> tree_node4 = TreeNode(4)
    >>> tree_node5 = TreeNode(5)
    >>> tree_node6 = TreeNode(6)
    >>> tree_node7 = TreeNode(7)
    >>> root.left, root.right = tree_node2, tree_node3
    >>> tree_node2.left, tree_node2.right = tree_node4 , tree_node5
    >>> tree_node3.left, tree_node3.right = tree_node6 , tree_node7
    >>> pre_order_iter(root)
    1,2,4,5,3,6,7,
    """
    logger.error(">>> Entering pre_order_iter(node=%s)", node, extra={"event.action": "pre_order_iter", "logrite.node": node})
    if not isinstance(node, TreeNode) or not node:
        logger.warning("<<< Exiting pre_order_iter(node=%s)", node, extra={"event.action": "pre_order_iter", "logrite.node": node})
        return
    stack: list[TreeNode] = []
    n = node
    while n or stack:
        while n:  # start from root node, find its left child
            print(n.data, end=",")
            stack.append(n)
            n = n.left
        # end of while means current node doesn't have left child
        n = stack.pop()
        # start to traverse its right child
        n = n.right


def in_order_iter(node: TreeNode) -> None:
    """
    >>> root = TreeNode(1)
    >>> tree_node2 = TreeNode(2)
    >>> tree_node3 = TreeNode(3)
    >>> tree_node4 = TreeNode(4)
    >>> tree_node5 = TreeNode(5)
    >>> tree_node6 = TreeNode(6)
    >>> tree_node7 = TreeNode(7)
    >>> root.left, root.right = tree_node2, tree_node3
    >>> tree_node2.left, tree_node2.right = tree_node4 , tree_node5
    >>> tree_node3.left, tree_node3.right = tree_node6 , tree_node7
    >>> in_order_iter(root)
    4,2,5,1,6,3,7,
    """
    logger.error(">>> Entering in_order_iter(node=%s)", node, extra={"event.action": "in_order_iter", "logrite.node": node})
    if not isinstance(node, TreeNode) or not node:
        logger.warning("<<< Exiting in_order_iter(node=%s)", node, extra={"event.action": "in_order_iter", "logrite.node": node})
        return
    stack: list[TreeNode] = []
    n = node
    while n or stack:
        while n:
            stack.append(n)
            n = n.left
        n = stack.pop()
        print(n.data, end=",")
        n = n.right


def post_order_iter(node: TreeNode) -> None:
    """
    >>> root = TreeNode(1)
    >>> tree_node2 = TreeNode(2)
    >>> tree_node3 = TreeNode(3)
    >>> tree_node4 = TreeNode(4)
    >>> tree_node5 = TreeNode(5)
    >>> tree_node6 = TreeNode(6)
    >>> tree_node7 = TreeNode(7)
    >>> root.left, root.right = tree_node2, tree_node3
    >>> tree_node2.left, tree_node2.right = tree_node4 , tree_node5
    >>> tree_node3.left, tree_node3.right = tree_node6 , tree_node7
    >>> post_order_iter(root)
    4,5,2,6,7,3,1,
    """
    logger.error(">>> Entering post_order_iter(node=%s)", node, extra={"event.action": "post_order_iter", "logrite.node": node})
    if not isinstance(node, TreeNode) or not node:
        logger.warning("<<< Exiting post_order_iter(node=%s)", node, extra={"event.action": "post_order_iter", "logrite.node": node})
        return
    stack1, stack2 = [], []
    n = node
    stack1.append(n)
    while stack1:  # to find the reversed order of post order, store it in stack2
        n = stack1.pop()
        if n.left:
            stack1.append(n.left)
        if n.right:
            stack1.append(n.right)
        stack2.append(n)
    while stack2:  # pop up from stack2 will be the post order
        print(stack2.pop().data, end=",")


def prompt(s: str = "", width=50, char="*") -> str:
    logger.error(">>> Entering prompt(s=%s,width=%s,char=%s)", s, width, char, extra={"event.action": "prompt", "logrite.s": s, "logrite.width": width, "logrite.char": char})
    if not s:
        return "\n" + width * char
    left, extra = divmod(width - len(s) - 2, 2)
    logger.warning("<<< Exiting prompt(s=%s,width=%s,char=%s)", s, width, char, extra={"event.action": "prompt", "logrite.s": s, "logrite.width": width, "logrite.char": char})
    return f"{left * char} {s} {(left + extra) * char}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(prompt("Binary Tree Traversals"))

    node: TreeNode = build_tree()
    print(prompt("Pre Order Traversal"))
    pre_order(node)
    print(prompt() + "\n")

    print(prompt("In Order Traversal"))
    in_order(node)
    print(prompt() + "\n")

    print(prompt("Post Order Traversal"))
    post_order(node)
    print(prompt() + "\n")

    print(prompt("Level Order Traversal"))
    level_order(node)
    print(prompt() + "\n")

    print(prompt("Actual Level Order Traversal"))
    level_order_actual(node)
    print("*" * 50 + "\n")

    print(prompt("Pre Order Traversal - Iteration Version"))
    pre_order_iter(node)
    print(prompt() + "\n")

    print(prompt("In Order Traversal - Iteration Version"))
    in_order_iter(node)
    print(prompt() + "\n")

    print(prompt("Post Order Traversal - Iteration Version"))
    post_order_iter(node)
    print(prompt())
