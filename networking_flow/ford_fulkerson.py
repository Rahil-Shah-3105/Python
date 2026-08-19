import logging
logger = logging.getLogger(__name__)
"""
Ford-Fulkerson Algorithm for Maximum Flow Problem
* https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm

Description:
    (1) Start with initial flow as 0
    (2) Choose the augmenting path from source to sink and add the path to flow
"""

graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]


def breadth_first_search(graph: list, source: int, sink: int, parents: list) -> bool:
    """
    This function returns True if there is a node that has not iterated.

    Args:
        graph: Adjacency matrix of graph
        source: Source
        sink: Sink
        parents: Parent list

    Returns:
        True if there is a node that has not iterated.

    >>> breadth_first_search(graph, 0, 5, [-1, -1, -1, -1, -1, -1])
    True
    >>> breadth_first_search(graph, 0, 6, [-1, -1, -1, -1, -1, -1])
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    """
    logger.debug(">>> Entering breadth_first_search(graph=%s,source=%s,sink=%s,parents=%s)", graph, source, sink, parents)
    visited = [False] * len(graph)  # Mark all nodes as not visited
    logger.debug("breadth_first_search(graph=%s,source=%s,sink=%s,parents=%s): visited → %s", graph, source, sink, parents, visited)
    queue = []  # breadth-first search queue
    logger.debug("breadth_first_search(graph=%s,source=%s,sink=%s,parents=%s): queue → %s", graph, source, sink, parents, queue)

    # Source node
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.pop(0)  # Pop the front node
        logger.debug("breadth_first_search(graph=%s,source=%s,sink=%s,parents=%s): u → %s", graph, source, sink, parents, u)
        # Traverse all adjacent nodes of u
        for ind, node in enumerate(graph[u]):
            if visited[ind] is False and node > 0:
                queue.append(ind)
                visited[ind] = True
                parents[ind] = u
    logger.debug("<<< Exiting breadth_first_search(graph=%s,source=%s,sink=%s,parents=%s)", graph, source, sink, parents)
    return visited[sink]


def ford_fulkerson(graph: list, source: int, sink: int) -> int:
    """
    This function returns the maximum flow from source to sink in the given graph.

    CAUTION: This function changes the given graph.

    Args:
        graph: Adjacency matrix of graph
        source: Source
        sink: Sink

    Returns:
        Maximum flow

    >>> test_graph = [
    ...     [0, 16, 13, 0, 0, 0],
    ...     [0, 0, 10, 12, 0, 0],
    ...     [0, 4, 0, 0, 14, 0],
    ...     [0, 0, 9, 0, 0, 20],
    ...     [0, 0, 0, 7, 0, 4],
    ...     [0, 0, 0, 0, 0, 0],
    ... ]
    >>> ford_fulkerson(test_graph, 0, 5)
    23
    """
    logger.debug(">>> Entering ford_fulkerson(graph=%s,source=%s,sink=%s)", graph, source, sink)
    # This array is filled by breadth-first search and to store path
    parent = [-1] * (len(graph))
    logger.debug("ford_fulkerson(graph=%s,source=%s,sink=%s): parent → %s", graph, source, sink, parent)
    max_flow = 0
    logger.debug("ford_fulkerson(graph=%s,source=%s,sink=%s): max_flow → %s", graph, source, sink, max_flow)

    # While there is a path from source to sink
    while breadth_first_search(graph, source, sink, parent):
        path_flow = int(1e9)  # Infinite value
        logger.debug("ford_fulkerson(graph=%s,source=%s,sink=%s): path_flow → %s", graph, source, sink, path_flow)
        s = sink

        while s != source:
            # Find the minimum value in the selected path
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink

        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    logger.debug("<<< Exiting ford_fulkerson(graph=%s,source=%s,sink=%s)", graph, source, sink)
    return max_flow


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{ford_fulkerson(graph, source=0, sink=5) = }")
