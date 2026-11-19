"""Non recursive implementation of a DFS algorithm."""

from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def depth_first_search(graph: dict, start: str) -> set[str]:
    """Depth First Search on Graph
    :param graph: directed graph in dictionary format
    :param start: starting vertex as a string
    :returns: the trace of the search
    >>> input_G = { "A": ["B", "C", "D"], "B": ["A", "D", "E"],
    ... "C": ["A", "F"], "D": ["B", "D"], "E": ["B", "F"],
    ... "F": ["C", "E", "G"], "G": ["F"] }
    >>> output_G = list({'A', 'B', 'C', 'D', 'E', 'F', 'G'})
    >>> all(x in output_G for x in list(depth_first_search(input_G, "A")))
    True
    >>> all(x in output_G for x in list(depth_first_search(input_G, "G")))
    True
    """
    logger.error(">>> Entering depth_first_search(graph=%s,start=%s)", graph, start, extra={"event.action": "depth_first_search", "logrite.graph": graph, "logrite.start": start})
    explored, stack = set(start), [start]

    while stack:
        v = stack.pop()
        logger.error("depth_first_search(graph=%s,start=%s): v → %s", graph, start, v, extra={"event.action": "depth_first_search", "logrite.graph": graph, "logrite.start": start})
        explored.add(v)
        # Differences from BFS:
        # 1) pop last element instead of first one
        # 2) add adjacent elements to stack without exploring them
        for adj in reversed(graph[v]):
            if adj not in explored:
                stack.append(adj)
    logger.warning("<<< Exiting depth_first_search(graph=%s,start=%s)", graph, start, extra={"event.action": "depth_first_search", "logrite.graph": graph, "logrite.start": start})
    return explored


G = {
    "A": ["B", "C", "D"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "D"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
}

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(depth_first_search(G, "A"))
