from __future__ import annotations

from collections.abc import Iterator
import logging
logger = logging.getLogger(__name__)


class RedBlackTree:
    """
    A Red-Black tree, which is a self-balancing BST (binary search
    tree).
    This tree has similar performance to AVL trees, but the balancing is
    less strict, so it will perform faster for writing/deleting nodes
    and slower for reading in the average case, though, because they're
    both balanced binary search trees, both will get the same asymptotic
    performance.
    To read more about them, https://en.wikipedia.org/wiki/Red-black_tree
    Unless otherwise specified, all asymptotic runtimes are specified in
    terms of the size of the tree.
    """

    def __init__(
        self,
        label: int | None = None,
        color: int = 0,
        parent: RedBlackTree | None = None,
        left: RedBlackTree | None = None,
        right: RedBlackTree | None = None,
    ) -> None:
        """Initialize a new Red-Black Tree node with the given values:
        label: The value associated with this node
        color: 0 if black, 1 if red
        parent: The parent to this node
        left: This node's left child
        right: This node's right child
        """
        self.label = label
        self.parent = parent
        self.left = left
        self.right = right
        self.color = color

    # Here are functions which are specific to red-black trees

    def rotate_left(self) -> RedBlackTree:
        """Rotate the subtree rooted at this node to the left and
        returns the new root to this subtree.
        Performing one rotation can be done in O(1).
        """
        logger.error(">>> Entering rotate_left()", extra={"event.action": "rotate_left"})
        parent = self.parent
        right = self.right
        if right is None:
            return self
        self.right = right.left
        logger.debug("rotate_left(self=%s): self.right → %s", self, self.right, extra={"event.action": "rotate_left"})
        if self.right:
            self.right.parent = self
        self.parent = right
        logger.debug("rotate_left(self=%s): self.parent → %s", self, self.parent, extra={"event.action": "rotate_left"})
        right.left = self
        logger.debug("rotate_left(self=%s): right.left → %s", self, right.left, extra={"event.action": "rotate_left"})
        if parent is not None:
            if parent.left == self:
                parent.left = right
            else:
                logger.debug("rotate_left(self=%s): parent.left → %s", self, parent.left, extra={"event.action": "rotate_left"})
                parent.right = right
                logger.debug("rotate_left(self=%s): parent.right → %s", self, parent.right, extra={"event.action": "rotate_left"})
        right.parent = parent
        logger.debug("rotate_left(self=%s): right.parent → %s", self, right.parent, extra={"event.action": "rotate_left"})
        logger.warning("<<< Exiting rotate_left()", extra={"event.action": "rotate_left"})
        return right

    def rotate_right(self) -> RedBlackTree:
        """Rotate the subtree rooted at this node to the right and
        returns the new root to this subtree.
        Performing one rotation can be done in O(1).
        """
        logger.error(">>> Entering rotate_right()", extra={"event.action": "rotate_right"})
        if self.left is None:
            return self
        parent = self.parent
        left = self.left
        self.left = left.right
        logger.debug("rotate_right(self=%s): self.left → %s", self, self.left, extra={"event.action": "rotate_right"})
        if self.left:
            self.left.parent = self
        self.parent = left
        logger.debug("rotate_right(self=%s): self.parent → %s", self, self.parent, extra={"event.action": "rotate_right"})
        left.right = self
        logger.debug("rotate_right(self=%s): left.right → %s", self, left.right, extra={"event.action": "rotate_right"})
        if parent is not None:
            if parent.right is self:
                parent.right = left
            else:
                logger.debug("rotate_right(self=%s): parent.right → %s", self, parent.right, extra={"event.action": "rotate_right"})
                parent.left = left
                logger.debug("rotate_right(self=%s): parent.left → %s", self, parent.left, extra={"event.action": "rotate_right"})
        left.parent = parent
        logger.debug("rotate_right(self=%s): left.parent → %s", self, left.parent, extra={"event.action": "rotate_right"})
        logger.warning("<<< Exiting rotate_right()", extra={"event.action": "rotate_right"})
        return left

    def insert(self, label: int) -> RedBlackTree:
        """Inserts label into the subtree rooted at self, performs any
        rotations necessary to maintain balance, and then returns the
        new root to this subtree (likely self).
        This is guaranteed to run in O(log(n)) time.
        """
        logger.error(">>> Entering insert(label=%s)", label, extra={"event.action": "insert", "logrite.label": label})
        if self.label is None:
            # Only possible with an empty tree
            self.label = label
            logger.debug("insert(self=%s,label=%s): self.label → %s", self, label, self.label, extra={"event.action": "insert", "logrite.label": label})
            return self
        if self.label == label:
            return self
        elif self.label > label:
            if self.left:
                self.left.insert(label)
            else:
                self.left = RedBlackTree(label, 1, self)
                self.left._insert_repair()
        elif self.right:
            self.right.insert(label)
        else:
            self.right = RedBlackTree(label, 1, self)
            self.right._insert_repair()
        logger.warning("<<< Exiting insert(label=%s)", label, extra={"event.action": "insert", "logrite.label": label})
        return self.parent or self

    def _insert_repair(self) -> None:
        """Repair the coloring from inserting into a tree."""
        logger.error(">>> Entering _insert_repair()", extra={"event.action": "_insert_repair"})
        if self.parent is None:
            # This node is the root, so it just needs to be black
            self.color = 0
        elif color(self.parent) == 0:
            logger.debug("_insert_repair(self=%s): self.color → %s", self, self.color, extra={"event.action": "_insert_repair"})
            # If the parent is black, then it just needs to be red
            self.color = 1
        else:
            uncle = self.parent.sibling
            if color(uncle) == 0:
                if self.is_left() and self.parent.is_right():
                    self.parent.rotate_right()
                    if self.right:
                        self.right._insert_repair()
                elif self.is_right() and self.parent.is_left():
                    self.parent.rotate_left()
                    if self.left:
                        self.left._insert_repair()
                elif self.is_left():
                    if self.grandparent:
                        self.grandparent.rotate_right()
                        self.parent.color = 0
                    if self.parent.right:
                        self.parent.right.color = 1
                else:
                    if self.grandparent:
                        self.grandparent.rotate_left()
                        self.parent.color = 0
                    if self.parent.left:
                        self.parent.left.color = 1
            else:
                self.parent.color = 0
                if uncle and self.grandparent:
                    uncle.color = 0
                    logger.debug("_insert_repair(self=%s): uncle.color → %s", self, uncle.color, extra={"event.action": "_insert_repair"})
                    self.grandparent.color = 1
                    self.grandparent._insert_repair()
                    logger.warning("<<< Exiting _insert_repair()", extra={"event.action": "_insert_repair"})

    def remove(self, label: int) -> RedBlackTree:
        """Remove label from this tree."""
        logger.error(">>> Entering remove(label=%s)", label, extra={"event.action": "remove", "logrite.label": label})
        if self.label == label:
            if self.left and self.right:
                # It's easier to balance a node with at most one child,
                # so we replace this node with the greatest one less than
                # it and remove that.
                value = self.left.get_max()
                logger.error("remove(label=%s): value → %s", label, value, extra={"event.action": "remove", "logrite.label": label})
                if value is not None:
                    self.label = value
                    logger.debug("remove(self=%s,label=%s): self.label → %s", self, label, self.label, extra={"event.action": "remove", "logrite.label": label})
                    self.left.remove(value)
            else:
                # This node has at most one non-None child, so we don't
                # need to replace
                child = self.left or self.right
                if self.color == 1:
                    # This node is red, and its child is black
                    # The only way this happens to a node with one child
                    # is if both children are None leaves.
                    # We can just remove this node and call it a day.
                    if self.parent:
                        if self.is_left():
                            self.parent.left = None
                        else:
                            self.parent.right = None
                # The node is black
                elif child is None:
                    # This node and its child are black
                    if self.parent is None:
                        # The tree is now empty
                        return RedBlackTree(None)
                    else:
                        self._remove_repair()
                        if self.is_left():
                            self.parent.left = None
                        else:
                            self.parent.right = None
                        self.parent = None
                else:
                    logger.debug("remove(self=%s,label=%s): self.parent → %s", self, label, self.parent, extra={"event.action": "remove", "logrite.label": label})
                    # This node is black and its child is red
                    # Move the child node here and make it black
                    self.label = child.label
                    self.left = child.left
                    logger.debug("remove(self=%s,label=%s): self.left → %s", self, label, self.left, extra={"event.action": "remove", "logrite.label": label})
                    self.right = child.right
                    logger.debug("remove(self=%s,label=%s): self.right → %s", self, label, self.right, extra={"event.action": "remove", "logrite.label": label})
                    if self.left:
                        self.left.parent = self
                    if self.right:
                        self.right.parent = self
        elif self.label is not None and self.label > label:
            if self.left:
                self.left.remove(label)
        elif self.right:
            self.right.remove(label)
        logger.warning("<<< Exiting remove(label=%s)", label, extra={"event.action": "remove", "logrite.label": label})
        return self.parent or self

    def _remove_repair(self) -> None:
        """Repair the coloring of the tree that may have been messed up."""
        logger.error(">>> Entering _remove_repair()", extra={"event.action": "_remove_repair"})
        if (
            self.parent is None
            or self.sibling is None
            or self.parent.sibling is None
            or self.grandparent is None
        ):
            return
        if color(self.sibling) == 1:
            self.sibling.color = 0
            self.parent.color = 1
            if self.is_left():
                self.parent.rotate_left()
            else:
                self.parent.rotate_right()
        if (
            color(self.parent) == 0
            and color(self.sibling) == 0
            and color(self.sibling.left) == 0
            and color(self.sibling.right) == 0
        ):
            self.sibling.color = 1
            self.parent._remove_repair()
            return
        if (
            color(self.parent) == 1
            and color(self.sibling) == 0
            and color(self.sibling.left) == 0
            and color(self.sibling.right) == 0
        ):
            self.sibling.color = 1
            self.parent.color = 0
            logger.warning("<<< Exiting _remove_repair()", extra={"event.action": "_remove_repair"})
            return
        if (
            self.is_left()
            and color(self.sibling) == 0
            and color(self.sibling.right) == 0
            and color(self.sibling.left) == 1
        ):
            self.sibling.rotate_right()
            self.sibling.color = 0
            if self.sibling.right:
                self.sibling.right.color = 1
        if (
            self.is_right()
            and color(self.sibling) == 0
            and color(self.sibling.right) == 1
            and color(self.sibling.left) == 0
        ):
            self.sibling.rotate_left()
            self.sibling.color = 0
            if self.sibling.left:
                self.sibling.left.color = 1
        if (
            self.is_left()
            and color(self.sibling) == 0
            and color(self.sibling.right) == 1
        ):
            self.parent.rotate_left()
            self.grandparent.color = self.parent.color
            self.parent.color = 0
            self.parent.sibling.color = 0
        if (
            self.is_right()
            and color(self.sibling) == 0
            and color(self.sibling.left) == 1
        ):
            self.parent.rotate_right()
            self.grandparent.color = self.parent.color
            self.parent.color = 0
            self.parent.sibling.color = 0

    def check_color_properties(self) -> bool:
        """Check the coloring of the tree, and return True iff the tree
        is colored in a way which matches these five properties:
        (wording stolen from wikipedia article)
         1. Each node is either red or black.
         2. The root node is black.
         3. All leaves are black.
         4. If a node is red, then both its children are black.
         5. Every path from any node to all of its descendent NIL nodes
            has the same number of black nodes.
        This function runs in O(n) time, because properties 4 and 5 take
        that long to check.
        """
        logger.error(">>> Entering check_color_properties()", extra={"event.action": "check_color_properties"})
        # I assume property 1 to hold because there is nothing that can
        # make the color be anything other than 0 or 1.
        # Property 2
        if self.color:
            # The root was red
            print("Property 2")
            return False
        # Property 3 does not need to be checked, because None is assumed
        # to be black and is all the leaves.
        # Property 4
        if not self.check_coloring():
            print("Property 4")
            return False
        # Property 5
        if self.black_height() is None:
            print("Property 5")
            return False
        # All properties were met
        logger.warning("<<< Exiting check_color_properties()", extra={"event.action": "check_color_properties"})
        return True

    def check_coloring(self) -> bool:
        """A helper function to recursively check Property 4 of a
        Red-Black Tree. See check_color_properties for more info.
        """
        logger.error(">>> Entering check_coloring()", extra={"event.action": "check_coloring"})
        if self.color == 1 and 1 in (color(self.left), color(self.right)):
            return False
        if self.left and not self.left.check_coloring():
            return False
        logger.warning("<<< Exiting check_coloring()", extra={"event.action": "check_coloring"})
        return not (self.right and not self.right.check_coloring())

    def black_height(self) -> int | None:
        """Returns the number of black nodes from this node to the
        leaves of the tree, or None if there isn't one such value (the
        tree is color incorrectly).
        """
        logger.error(">>> Entering black_height()", extra={"event.action": "black_height"})
        if self is None or self.left is None or self.right is None:
            # If we're already at a leaf, there is no path
            return 1
        left = RedBlackTree.black_height(self.left)
        right = RedBlackTree.black_height(self.right)
        if left is None or right is None:
            # There are issues with coloring below children nodes
            return None
        if left != right:
            # The two children have unequal depths
            return None
        # Return the black depth of children, plus one if this node is
        # black
        logger.warning("<<< Exiting black_height()", extra={"event.action": "black_height"})
        return left + (1 - self.color)

    # Here are functions which are general to all binary search trees

    def __contains__(self, label: int) -> bool:
        """Search through the tree for label, returning True iff it is
        found somewhere in the tree.
        Guaranteed to run in O(log(n)) time.
        """
        logger.error(">>> Entering __contains__(label=%s)", label, extra={"event.action": "__contains__", "logrite.label": label})
        logger.warning("<<< Exiting __contains__(label=%s)", label, extra={"event.action": "__contains__", "logrite.label": label})
        return self.search(label) is not None

    def search(self, label: int) -> RedBlackTree | None:
        """Search through the tree for label, returning its node if
        it's found, and None otherwise.
        This method is guaranteed to run in O(log(n)) time.
        """
        logger.error(">>> Entering search(label=%s)", label, extra={"event.action": "search", "logrite.label": label})
        if self.label == label:
            return self
        elif self.label is not None and label > self.label:
            if self.right is None:
                return None
            else:
                return self.right.search(label)
        elif self.left is None:
            return None
        else:
            logger.warning("<<< Exiting search(label=%s)", label, extra={"event.action": "search", "logrite.label": label})
            return self.left.search(label)

    def floor(self, label: int) -> int | None:
        """Returns the largest element in this tree which is at most label.
        This method is guaranteed to run in O(log(n)) time."""
        logger.error(">>> Entering floor(label=%s)", label, extra={"event.action": "floor", "logrite.label": label})
        if self.label == label:
            return self.label
        elif self.label is not None and self.label > label:
            if self.left:
                return self.left.floor(label)
            else:
                return None
        else:
            if self.right:
                attempt = self.right.floor(label)
                if attempt is not None:
                    return attempt
            logger.warning("<<< Exiting floor(label=%s)", label, extra={"event.action": "floor", "logrite.label": label})
            return self.label

    def ceil(self, label: int) -> int | None:
        """Returns the smallest element in this tree which is at least label.
        This method is guaranteed to run in O(log(n)) time.
        """
        logger.error(">>> Entering ceil(label=%s)", label, extra={"event.action": "ceil", "logrite.label": label})
        if self.label == label:
            return self.label
        elif self.label is not None and self.label < label:
            if self.right:
                return self.right.ceil(label)
            else:
                return None
        else:
            if self.left:
                attempt = self.left.ceil(label)
                if attempt is not None:
                    return attempt
            logger.warning("<<< Exiting ceil(label=%s)", label, extra={"event.action": "ceil", "logrite.label": label})
            return self.label

    def get_max(self) -> int | None:
        """Returns the largest element in this tree.
        This method is guaranteed to run in O(log(n)) time.
        """
        logger.error(">>> Entering get_max()", extra={"event.action": "get_max"})
        if self.right:
            # Go as far right as possible
            return self.right.get_max()
        else:
            logger.warning("<<< Exiting get_max()", extra={"event.action": "get_max"})
            return self.label

    def get_min(self) -> int | None:
        """Returns the smallest element in this tree.
        This method is guaranteed to run in O(log(n)) time.
        """
        logger.error(">>> Entering get_min()", extra={"event.action": "get_min"})
        if self.left:
            # Go as far left as possible
            return self.left.get_min()
        else:
            logger.warning("<<< Exiting get_min()", extra={"event.action": "get_min"})
            return self.label

    @property
    def grandparent(self) -> RedBlackTree | None:
        """Get the current node's grandparent, or None if it doesn't exist."""
        logger.error(">>> Entering grandparent()", extra={"event.action": "grandparent"})
        if self.parent is None:
            return None
        else:
            logger.warning("<<< Exiting grandparent()", extra={"event.action": "grandparent"})
            return self.parent.parent

    @property
    def sibling(self) -> RedBlackTree | None:
        """Get the current node's sibling, or None if it doesn't exist."""
        logger.error(">>> Entering sibling()", extra={"event.action": "sibling"})
        if self.parent is None:
            return None
        elif self.parent.left is self:
            return self.parent.right
        else:
            logger.warning("<<< Exiting sibling()", extra={"event.action": "sibling"})
            return self.parent.left

    def is_left(self) -> bool:
        """Returns true iff this node is the left child of its parent."""
        logger.error(">>> Entering is_left()", extra={"event.action": "is_left"})
        if self.parent is None:
            return False
        logger.warning("<<< Exiting is_left()", extra={"event.action": "is_left"})
        return self.parent.left is self

    def is_right(self) -> bool:
        """Returns true iff this node is the right child of its parent."""
        logger.error(">>> Entering is_right()", extra={"event.action": "is_right"})
        if self.parent is None:
            return False
        logger.warning("<<< Exiting is_right()", extra={"event.action": "is_right"})
        return self.parent.right is self

    def __bool__(self) -> bool:
        logger.error(">>> Entering __bool__()", extra={"event.action": "__bool__"})
        logger.warning("<<< Exiting __bool__()", extra={"event.action": "__bool__"})
        return True

    def __len__(self) -> int:
        """
        Return the number of nodes in this tree.
        """
        logger.error(">>> Entering __len__()", extra={"event.action": "__len__"})
        ln = 1
        if self.left:
            ln += len(self.left)
        if self.right:
            ln += len(self.right)
        logger.warning("<<< Exiting __len__()", extra={"event.action": "__len__"})
        return ln

    def preorder_traverse(self) -> Iterator[int | None]:
        logger.error(">>> Entering preorder_traverse()", extra={"event.action": "preorder_traverse"})
        yield self.label
        if self.left:
            yield from self.left.preorder_traverse()
        if self.right:
            yield from self.right.preorder_traverse()
            logger.warning("<<< Exiting preorder_traverse()", extra={"event.action": "preorder_traverse"})

    def inorder_traverse(self) -> Iterator[int | None]:
        logger.error(">>> Entering inorder_traverse()", extra={"event.action": "inorder_traverse"})
        if self.left:
            yield from self.left.inorder_traverse()
        yield self.label
        if self.right:
            yield from self.right.inorder_traverse()
            logger.warning("<<< Exiting inorder_traverse()", extra={"event.action": "inorder_traverse"})

    def postorder_traverse(self) -> Iterator[int | None]:
        logger.error(">>> Entering postorder_traverse()", extra={"event.action": "postorder_traverse"})
        if self.left:
            yield from self.left.postorder_traverse()
        if self.right:
            yield from self.right.postorder_traverse()
        yield self.label
        logger.warning("<<< Exiting postorder_traverse()", extra={"event.action": "postorder_traverse"})

    def __repr__(self) -> str:
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        from pprint import pformat

        if self.left is None and self.right is None:
            logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
            return f"'{self.label} {(self.color and 'red') or 'blk'}'"
        return pformat(
            {
                f"{self.label} {(self.color and 'red') or 'blk'}": (
                    self.left,
                    self.right,
                )
            },
            indent=1,
        )

    def __eq__(self, other: object) -> bool:
        """Test if two trees are equal."""
        logger.error(">>> Entering __eq__(other=%s)", other, extra={"event.action": "__eq__", "logrite.other": other})
        if not isinstance(other, RedBlackTree):
            return NotImplemented
        if self.label == other.label:
            return self.left == other.left and self.right == other.right
        else:
            logger.warning("<<< Exiting __eq__(other=%s)", other, extra={"event.action": "__eq__", "logrite.other": other})
            return False


def color(node: RedBlackTree | None) -> int:
    """Returns the color of a node, allowing for None leaves."""
    logger.error(">>> Entering color(node=%s)", node, extra={"event.action": "color", "logrite.node": node})
    if node is None:
        return 0
    else:
        logger.warning("<<< Exiting color(node=%s)", node, extra={"event.action": "color", "logrite.node": node})
        return node.color


"""
Code for testing the various
functions of the red-black tree.
"""


def test_rotations() -> bool:
    """Test that the rotate_left and rotate_right functions work."""
    logger.error(">>> Entering test_rotations()", extra={"event.action": "test_rotations"})
    # Make a tree to test on
    tree = RedBlackTree(0)
    logger.error("test_rotations(): tree → %s", tree, extra={"event.action": "test_rotations"})
    tree.left = RedBlackTree(-10, parent=tree)
    tree.right = RedBlackTree(10, parent=tree)
    tree.left.left = RedBlackTree(-20, parent=tree.left)
    tree.left.right = RedBlackTree(-5, parent=tree.left)
    tree.right.left = RedBlackTree(5, parent=tree.right)
    tree.right.right = RedBlackTree(20, parent=tree.right)
    # Make the right rotation
    left_rot = RedBlackTree(10)
    logger.error("test_rotations(): left_rot → %s", left_rot, extra={"event.action": "test_rotations"})
    left_rot.left = RedBlackTree(0, parent=left_rot)
    left_rot.left.left = RedBlackTree(-10, parent=left_rot.left)
    left_rot.left.right = RedBlackTree(5, parent=left_rot.left)
    left_rot.left.left.left = RedBlackTree(-20, parent=left_rot.left.left)
    left_rot.left.left.right = RedBlackTree(-5, parent=left_rot.left.left)
    left_rot.right = RedBlackTree(20, parent=left_rot)
    tree = tree.rotate_left()
    if tree != left_rot:
        return False
    tree = tree.rotate_right()
    tree = tree.rotate_right()
    # Make the left rotation
    right_rot = RedBlackTree(-10)
    right_rot.left = RedBlackTree(-20, parent=right_rot)
    right_rot.right = RedBlackTree(0, parent=right_rot)
    right_rot.right.left = RedBlackTree(-5, parent=right_rot.right)
    right_rot.right.right = RedBlackTree(10, parent=right_rot.right)
    right_rot.right.right.left = RedBlackTree(5, parent=right_rot.right.right)
    right_rot.right.right.right = RedBlackTree(20, parent=right_rot.right.right)
    logger.warning("<<< Exiting test_rotations()", extra={"event.action": "test_rotations"})
    return tree == right_rot


def test_insertion_speed() -> bool:
    """Test that the tree balances inserts to O(log(n)) by doing a lot
    of them.
    """
    logger.error(">>> Entering test_insertion_speed()", extra={"event.action": "test_insertion_speed"})
    tree = RedBlackTree(-1)
    logger.error("test_insertion_speed(): tree → %s", tree, extra={"event.action": "test_insertion_speed"})
    for i in range(300000):
        tree = tree.insert(i)
    logger.warning("<<< Exiting test_insertion_speed()", extra={"event.action": "test_insertion_speed"})
    return True


def test_insert() -> bool:
    """Test the insert() method of the tree correctly balances, colors,
    and inserts.
    """
    logger.error(">>> Entering test_insert()", extra={"event.action": "test_insert"})
    tree = RedBlackTree(0)
    logger.error("test_insert(): tree → %s", tree, extra={"event.action": "test_insert"})
    tree.insert(8)
    tree.insert(-8)
    tree.insert(4)
    tree.insert(12)
    tree.insert(10)
    tree.insert(11)
    ans = RedBlackTree(0, 0)
    logger.error("test_insert(): ans → %s", ans, extra={"event.action": "test_insert"})
    ans.left = RedBlackTree(-8, 0, ans)
    ans.right = RedBlackTree(8, 1, ans)
    ans.right.left = RedBlackTree(4, 0, ans.right)
    ans.right.right = RedBlackTree(11, 0, ans.right)
    ans.right.right.left = RedBlackTree(10, 1, ans.right.right)
    ans.right.right.right = RedBlackTree(12, 1, ans.right.right)
    logger.warning("<<< Exiting test_insert()", extra={"event.action": "test_insert"})
    return tree == ans


def test_insert_and_search() -> bool:
    """Tests searching through the tree for values."""
    logger.error(">>> Entering test_insert_and_search()", extra={"event.action": "test_insert_and_search"})
    tree = RedBlackTree(0)
    logger.error("test_insert_and_search(): tree → %s", tree, extra={"event.action": "test_insert_and_search"})
    tree.insert(8)
    tree.insert(-8)
    tree.insert(4)
    tree.insert(12)
    tree.insert(10)
    tree.insert(11)
    if any(i in tree for i in (5, -6, -10, 13)):
        # Found something not in there
        return False
    # Find all these things in there
    logger.warning("<<< Exiting test_insert_and_search()", extra={"event.action": "test_insert_and_search"})
    return all(i in tree for i in (11, 12, -8, 0))


def test_insert_delete() -> bool:
    """Test the insert() and delete() method of the tree, verifying the
    insertion and removal of elements, and the balancing of the tree.
    """
    logger.error(">>> Entering test_insert_delete()", extra={"event.action": "test_insert_delete"})
    tree = RedBlackTree(0)
    tree = tree.insert(-12)
    tree = tree.insert(8)
    tree = tree.insert(-8)
    tree = tree.insert(15)
    tree = tree.insert(4)
    tree = tree.insert(12)
    tree = tree.insert(10)
    tree = tree.insert(9)
    tree = tree.insert(11)
    tree = tree.remove(15)
    tree = tree.remove(-12)
    tree = tree.remove(9)
    logger.error("test_insert_delete(): tree → %s", tree, extra={"event.action": "test_insert_delete"})
    if not tree.check_color_properties():
        return False
    logger.warning("<<< Exiting test_insert_delete()", extra={"event.action": "test_insert_delete"})
    return list(tree.inorder_traverse()) == [-8, 0, 4, 8, 10, 11, 12]


def test_floor_ceil() -> bool:
    """Tests the floor and ceiling functions in the tree."""
    logger.error(">>> Entering test_floor_ceil()", extra={"event.action": "test_floor_ceil"})
    tree = RedBlackTree(0)
    logger.error("test_floor_ceil(): tree → %s", tree, extra={"event.action": "test_floor_ceil"})
    tree.insert(-16)
    tree.insert(16)
    tree.insert(8)
    tree.insert(24)
    tree.insert(20)
    tree.insert(22)
    tuples = [(-20, None, -16), (-10, -16, 0), (8, 8, 8), (50, 24, None)]
    logger.error("test_floor_ceil(): tuples → %s", tuples, extra={"event.action": "test_floor_ceil"})
    for val, floor, ceil in tuples:
        if tree.floor(val) != floor or tree.ceil(val) != ceil:
            return False
    logger.warning("<<< Exiting test_floor_ceil()", extra={"event.action": "test_floor_ceil"})
    return True


def test_min_max() -> bool:
    """Tests the min and max functions in the tree."""
    logger.error(">>> Entering test_min_max()", extra={"event.action": "test_min_max"})
    tree = RedBlackTree(0)
    logger.error("test_min_max(): tree → %s", tree, extra={"event.action": "test_min_max"})
    tree.insert(-16)
    tree.insert(16)
    tree.insert(8)
    tree.insert(24)
    tree.insert(20)
    tree.insert(22)
    logger.warning("<<< Exiting test_min_max()", extra={"event.action": "test_min_max"})
    return not (tree.get_max() != 22 or tree.get_min() != -16)


def test_tree_traversal() -> bool:
    """Tests the three different tree traversal functions."""
    logger.error(">>> Entering test_tree_traversal()", extra={"event.action": "test_tree_traversal"})
    tree = RedBlackTree(0)
    tree = tree.insert(-16)
    logger.error("test_tree_traversal(): tree → %s", tree, extra={"event.action": "test_tree_traversal"})
    tree.insert(16)
    tree.insert(8)
    tree.insert(24)
    tree.insert(20)
    tree.insert(22)
    if list(tree.inorder_traverse()) != [-16, 0, 8, 16, 20, 22, 24]:
        return False
    if list(tree.preorder_traverse()) != [0, -16, 16, 8, 22, 20, 24]:
        return False
    logger.warning("<<< Exiting test_tree_traversal()", extra={"event.action": "test_tree_traversal"})
    return list(tree.postorder_traverse()) == [-16, 8, 20, 24, 22, 16, 0]


def test_tree_chaining() -> bool:
    """Tests the three different tree chaining functions."""
    logger.error(">>> Entering test_tree_chaining()", extra={"event.action": "test_tree_chaining"})
    tree = RedBlackTree(0)
    tree = tree.insert(-16).insert(16).insert(8).insert(24).insert(20).insert(22)
    logger.error("test_tree_chaining(): tree → %s", tree, extra={"event.action": "test_tree_chaining"})
    if list(tree.inorder_traverse()) != [-16, 0, 8, 16, 20, 22, 24]:
        return False
    if list(tree.preorder_traverse()) != [0, -16, 16, 8, 22, 20, 24]:
        return False
    logger.warning("<<< Exiting test_tree_chaining()", extra={"event.action": "test_tree_chaining"})
    return list(tree.postorder_traverse()) == [-16, 8, 20, 24, 22, 16, 0]


def print_results(msg: str, passes: bool) -> None:
    logger.error(">>> Entering print_results(msg=%s,passes=%s)", msg, passes, extra={"event.action": "print_results", "logrite.msg": msg, "logrite.passes": passes})
    print(str(msg), "works!" if passes else "doesn't work :(")
    logger.warning("<<< Exiting print_results(msg=%s,passes=%s)", msg, passes, extra={"event.action": "print_results", "logrite.msg": msg, "logrite.passes": passes})


def pytests() -> None:
    logger.error(">>> Entering pytests()", extra={"event.action": "pytests"})
    assert test_rotations()
    assert test_insert()
    assert test_insert_and_search()
    assert test_insert_delete()
    assert test_floor_ceil()
    assert test_tree_traversal()
    assert test_tree_chaining()
    logger.warning("<<< Exiting pytests()", extra={"event.action": "pytests"})


def main() -> None:
    """
    >>> pytests()
    """
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    print_results("Rotating right and left", test_rotations())
    print_results("Inserting", test_insert())
    print_results("Searching", test_insert_and_search())
    print_results("Deleting", test_insert_delete())
    print_results("Floor and ceil", test_floor_ceil())
    print_results("Tree traversal", test_tree_traversal())
    print_results("Tree traversal", test_tree_chaining())
    print("Testing tree balancing...")
    print("This should only be a few seconds.")
    test_insertion_speed()
    print("Done!")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
