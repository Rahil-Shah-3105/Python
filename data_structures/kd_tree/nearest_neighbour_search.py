#  Created by: Ramy-Badr-Ahmed (https://github.com/Ramy-Badr-Ahmed)
#  in Pull Request: #11532
#  https://github.com/TheAlgorithms/Python/pull/11532
#
#  Please mention me (@Ramy-Badr-Ahmed) in any issue or pull request
#  addressing bugs/corrections to this file.
#  Thank you!

from data_structures.kd_tree.kd_node import KDNode
import logging
logger = logging.getLogger(__name__)


def nearest_neighbour_search(
    root: KDNode | None, query_point: list[float]
) -> tuple[list[float] | None, float, int]:
    """
    Performs a nearest neighbor search in a KD-Tree for a given query point.

    Args:
        root (KDNode | None): The root node of the KD-Tree.
        query_point (list[float]): The point for which the nearest neighbor
                                    is being searched.

    Returns:
        tuple[list[float] | None, float, int]:
            - The nearest point found in the KD-Tree to the query point,
              or None if no point is found.
            - The squared distance to the nearest point.
            - The number of nodes visited during the search.
    """
    nearest_point: list[float] | None = None
    nearest_dist: float = float("inf")
    nodes_visited: int = 0

    def search(node: KDNode | None, depth: int = 0) -> None:
        """
        Recursively searches for the nearest neighbor in the KD-Tree.

        Args:
            node: The current node in the KD-Tree.
            depth: The current depth in the KD-Tree.
        """
        logger.debug(">>> Entering search(node=%s,depth=%s)", node, depth)
        nonlocal nearest_point, nearest_dist, nodes_visited
        if node is None:
            logger.debug("<<< Exiting search(node=%s,depth=%s)", node, depth)
            return

        nodes_visited += 1

        # Calculate the current distance (squared distance)
        current_point = node.point
        logger.debug("search(node=%s,depth=%s): current_point → %s", node, depth, current_point)
        current_dist = sum(
        logger.debug("search(node=%s,depth=%s): current_dist → %s", node, depth, current_dist)
            (query_coord - point_coord) ** 2
            for query_coord, point_coord in zip(query_point, current_point)
        )

        # Update nearest point if the current node is closer
        if nearest_point is None or current_dist < nearest_dist:
            nearest_point = current_point
            logger.debug("search(node=%s,depth=%s): nearest_point → %s", node, depth, nearest_point)
            nearest_dist = current_dist
            logger.debug("search(node=%s,depth=%s): nearest_dist → %s", node, depth, nearest_dist)

        # Determine which subtree to search first (based on axis and query point)
        k = len(query_point)  # Dimensionality of points
        axis = depth % k
        logger.debug("search(node=%s,depth=%s): axis → %s", node, depth, axis)

        if query_point[axis] <= current_point[axis]:
            nearer_subtree = node.left
            logger.debug("search(node=%s,depth=%s): nearer_subtree → %s", node, depth, nearer_subtree)
            further_subtree = node.right
            logger.debug("search(node=%s,depth=%s): further_subtree → %s", node, depth, further_subtree)
        else:
            nearer_subtree = node.right
            further_subtree = node.left

        # Search the nearer subtree first
        search(nearer_subtree, depth + 1)

        # If the further subtree has a closer point
        if (query_point[axis] - current_point[axis]) ** 2 < nearest_dist:
            search(further_subtree, depth + 1)

    search(root, 0)
    return nearest_point, nearest_dist, nodes_visited
