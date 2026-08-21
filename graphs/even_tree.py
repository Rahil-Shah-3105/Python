"""
You are given a tree(a simple connected graph with no cycles). The tree has N
nodes numbered from 1 to N and is rooted at node 1.

Find the maximum number of edges you can remove from the tree to get a forest
such that each connected component of the forest contains an even number of
nodes.

Constraints
2 <= 2 <= 100

Note: The tree input will be such that it can always be decomposed into
components containing an even number of nodes.
"""

# pylint: disable=invalid-name
from collections import defaultdict
import logging
logger = logging.getLogger(__name__)


def dfs(start: int) -> int:
    """DFS traversal"""
    logger.debug(">>> Entering dfs(start=%s)", start)
    # pylint: disable=redefined-outer-name
    ret = 1
    logger.debug("dfs(start=%s): ret → %s", start, ret)
    visited[start] = True
    for v in tree[start]:
        if v not in visited:
            ret += dfs(v)
    if ret % 2 == 0:
        cuts.append(start)
    logger.debug("<<< Exiting dfs(start=%s)", start)
    return ret


def even_tree():
    """
    2 1
    3 1
    4 3
    5 2
    6 1
    7 2
    8 6
    9 8
    10 8
    On removing edges (1,3) and (1,6), we can get the desired result 2.
    """
    logger.debug(">>> Entering even_tree()")
    dfs(1)
    logger.debug("<<< Exiting even_tree()")


if __name__ == "__main__":
    n, m = 10, 9
    tree = defaultdict(list)
    visited: dict[int, bool] = {}
    cuts: list[int] = []
    count = 0
    edges = [(2, 1), (3, 1), (4, 3), (5, 2), (6, 1), (7, 2), (8, 6), (9, 8), (10, 8)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    even_tree()
    print(len(cuts) - 1)
