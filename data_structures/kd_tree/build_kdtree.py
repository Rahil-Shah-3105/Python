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


def build_kdtree(points: list[list[float]], depth: int = 0) -> KDNode | None:
    """
    Builds a KD-Tree from a list of points.

    Args:
        points: The list of points to build the KD-Tree from.
        depth: The current depth in the tree
                     (used to determine axis for splitting).

    Returns:
        The root node of the KD-Tree,
                       or None if no points are provided.
    """
    logger.debug(">>> Entering build_kdtree(points=%s,depth=%s)", points, depth)
    if not points:
        return None

    k = len(points[0])  # Dimensionality of the points
    axis = depth % k
    logger.debug("build_kdtree(points=%s,depth=%s): axis → %s", points, depth, axis)

    # Sort point list and choose median as pivot element
    points.sort(key=lambda point: point[axis])
    logger.debug("build_kdtree(points=%s,depth=%s): right → %s", points, depth, right)
    logger.debug("build_kdtree(points=%s,depth=%s): left → %s", points, depth, left)
    logger.debug("build_kdtree(points=%s,depth=%s): point → %s", points, depth, point)
    logger.debug("build_kdtree(points=%s,depth=%s): left_points → %s", points, depth, left_points)
    logger.debug("build_kdtree(points=%s,depth=%s): right_points → %s", points, depth, right_points)
    median_idx = len(points) // 2
    logger.debug("build_kdtree(points=%s,depth=%s): median_idx → %s", points, depth, median_idx)

    # Create node and construct subtrees
    left_points = points[:median_idx]
    right_points = points[median_idx + 1 :]

    logger.debug("<<< Exiting build_kdtree(points=%s,depth=%s)", points, depth)
    return KDNode(
        point=points[median_idx],
        left=build_kdtree(left_points, depth + 1),
        right=build_kdtree(right_points, depth + 1),
    )
