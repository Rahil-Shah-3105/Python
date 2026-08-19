import logging
logger = logging.getLogger(__name__)
"""
Illustrate how to implement inorder traversal in binary search tree.
Author: Gurneet Singh
https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
"""


class BinaryTreeNode:
    """Defining the structure of BinaryTreeNode"""

    def __init__(self, data: int) -> None:
        logger.debug(">>> Entering __init__(data=%s)", data)
        self.data = data
        logger.debug("__init__(data=%s): self.data → %s", data, self.data)
        logger.debug("__init__(self=%s,data=%s): self.data → %s", self, data, self.data)
        self.left_child: BinaryTreeNode | None = None
        self.right_child: BinaryTreeNode | None = None
        logger.debug("<<< Exiting __init__(data=%s)", data)


def insert(node: BinaryTreeNode | None, new_value: int) -> BinaryTreeNode | None:
    """
    If the binary search tree is empty, make a new node and declare it as root.
    >>> node_a = BinaryTreeNode(12345)
    >>> node_b = insert(node_a, 67890)
    >>> node_a.left_child == node_b.left_child
    True
    >>> node_a.right_child == node_b.right_child
    True
    >>> node_a.data == node_b.data
    True
    """
    logger.debug(">>> Entering insert(node=%s,new_value=%s)", node, new_value)
    if node is None:
        node = BinaryTreeNode(new_value)
        logger.debug("insert(node=%s,new_value=%s): node → %s", node, new_value, node)
        return node

    # binary search tree is not empty,
    # so we will insert it into the tree
    # if new_value is less than value of data in node,
    #  add it to left subtree and proceed recursively
    if new_value < node.data:
        node.left_child = insert(node.left_child, new_value)
    else:
        # if new_value is greater than value of data in node,
        #  add it to right subtree and proceed recursively
        node.right_child = insert(node.right_child, new_value)
    logger.debug("<<< Exiting insert(node=%s,new_value=%s)", node, new_value)
    return node


def inorder(node: BinaryTreeNode | None) -> list[int]:  # if node is None,return
    logger.debug(">>> Entering inorder(node=%s)", node)
    """
    >>> inorder(make_tree())
    [6, 10, 14, 15, 20, 25, 60]
    """
    if node:
        inorder_array = inorder(node.left_child)
        inorder_array = [*inorder_array, node.data]
        inorder_array = inorder_array + inorder(node.right_child)
        logger.debug("inorder(node=%s): inorder_array → %s", node, inorder_array)
    else:
        inorder_array = []
    logger.debug("<<< Exiting inorder(node=%s)", node)
    return inorder_array


def make_tree() -> BinaryTreeNode | None:
    logger.debug(">>> Entering make_tree()")
    logger.warning("make_tree(): root → %s", root)
    root = insert(None, 15)
    logger.debug("make_tree(): root → %s", root)
    insert(root, 10)
    insert(root, 25)
    insert(root, 6)
    insert(root, 14)
    insert(root, 20)
    insert(root, 60)
    logger.debug("<<< Exiting make_tree()")
    return root


def main() -> None:
    logger.debug(">>> Entering main()")
    logger.debug("main(): root → %s", root)
    logger.warning("main(): root → %s", root)
    # main function
    root = make_tree()
    print("Printing values of binary search tree in Inorder Traversal.")
    inorder(root)
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
