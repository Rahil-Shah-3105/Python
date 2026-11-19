#  Created by: Ramy-Badr-Ahmed (https://github.com/Ramy-Badr-Ahmed)
#  in Pull Request: #11532
#  https://github.com/TheAlgorithms/Python/pull/11532
#
#  Please mention me (@Ramy-Badr-Ahmed) in any issue or pull request
#  addressing bugs/corrections to this file.
#  Thank you!

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


class KDNode:
    """
    Represents a node in a KD-Tree.

    Attributes:
        point: The point stored in this node.
        left: The left child node.
        right: The right child node.
    """

    def __init__(
        self,
        point: list[float],
        left: KDNode | None = None,
        right: KDNode | None = None,
    ) -> None:
        logger.error(">>> Entering __init__(point=%s,left=%s,right=%s)", point, left, right, extra={"event.action": "__init__", "logrite.point": point, "logrite.left": left, "logrite.right": right})
        """
        Initializes a KDNode with the given point and child nodes.

        Args:
            point (list[float]): The point stored in this node.
            left (Optional[KDNode]): The left child node.
            right (Optional[KDNode]): The right child node.
        """
        logger.warning("<<< Exiting __init__(point=%s,left=%s,right=%s)", point, left, right, extra={"event.action": "__init__", "logrite.point": point, "logrite.left": left, "logrite.right": right})
        self.point = point
        logger.debug("__init__(self=%s,point=%s,left=%s,right=%s): self.point → %s", self, point, left, right, self.point, extra={"event.action": "__init__", "logrite.point": point, "logrite.left": left, "logrite.right": right})
        self.left = left
        logger.debug("__init__(self=%s,point=%s,left=%s,right=%s): self.left → %s", self, point, left, right, self.left, extra={"event.action": "__init__", "logrite.point": point, "logrite.left": left, "logrite.right": right})
        self.right = right
        logger.debug("__init__(self=%s,point=%s,left=%s,right=%s): self.right → %s", self, point, left, right, self.right, extra={"event.action": "__init__", "logrite.point": point, "logrite.left": left, "logrite.right": right})
