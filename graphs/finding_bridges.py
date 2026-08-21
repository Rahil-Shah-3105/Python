import logging
logger = logging.getLogger(__name__)
"""
An edge is a bridge if, after removing it count of connected components in graph will
be increased by one. Bridges represent vulnerabilities in a connected network and are
useful for designing reliable networks. For example, in a wired computer network, an
articulation point indicates the critical computers and a bridge indicates the critical
wires or connections.

For more details, refer this article:
https://www.geeksforgeeks.org/bridge-in-a-graph/
"""


def __get_demo_graph(index):
    logger.debug(">>> Entering __get_demo_graph(index=%s)", index)
    return [
        {
            0: [1, 2],
            1: [0, 2],
            2: [0, 1, 3, 5],
            3: [2, 4],
            4: [3],
            5: [2, 6, 8],
            6: [5, 7],
            7: [6, 8],
            8: [5, 7],
        },
        {
            0: [6],
            1: [9],
            2: [4, 5],
            3: [4],
            4: [2, 3],
            5: [2],
            6: [0, 7],
            7: [6],
            8: [],
            9: [1],
        },
        {
            0: [4],
            1: [6],
            2: [],
            3: [5, 6, 7],
            4: [0, 6],
            5: [3, 8, 9],
            6: [1, 3, 4, 7],
            7: [3, 6, 8, 9],
            8: [5, 7],
            9: [5, 7],
        },
        {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 3, 4],
            3: [0, 2, 4],
            4: [1, 2, 3],
        },
    ][index]
    logger.debug("<<< Exiting __get_demo_graph(index=%s)", index)


def compute_bridges(graph: dict[int, list[int]]) -> list[tuple[int, int]]:
    """
    Return the list of undirected graph bridges [(a1, b1), ..., (ak, bk)]; ai <= bi
    >>> compute_bridges(__get_demo_graph(0))
    [(3, 4), (2, 3), (2, 5)]
    >>> compute_bridges(__get_demo_graph(1))
    [(6, 7), (0, 6), (1, 9), (3, 4), (2, 4), (2, 5)]
    >>> compute_bridges(__get_demo_graph(2))
    [(1, 6), (4, 6), (0, 4)]
    >>> compute_bridges(__get_demo_graph(3))
    []
    >>> compute_bridges({})
    []
    """
    logger.debug(">>> Entering compute_bridges(graph=%s)", graph)

    logger.debug("<<< Exiting compute_bridges(graph=%s)", graph)
    id_ = 0
    logger.debug("compute_bridges(graph=%s): id_ → %s", graph, id_)
    n = len(graph)  # No of vertices in graph
    logger.debug("compute_bridges(graph=%s): n → %s", graph, n)
    low = [0] * n
    logger.debug("compute_bridges(graph=%s): low → %s", graph, low)
    visited = [False] * n
    logger.debug("compute_bridges(graph=%s): visited → %s", graph, visited)

    def dfs(at, parent, bridges, id_):
        logger.debug(">>> Entering dfs(at=%s,parent=%s,bridges=%s,id_=%s)", at, parent, bridges, id_)
        visited[at] = True
        low[at] = id_
        id_ += 1
        for to in graph[at]:
            if to == parent:
                pass
            elif not visited[to]:
                dfs(to, at, bridges, id_)
                low[at] = min(low[at], low[to])
                if id_ <= low[to]:
                    bridges.append((at, to) if at < to else (to, at))
            else:
                # This edge is a back edge and cannot be a bridge
                low[at] = min(low[at], low[to])
                logger.debug("<<< Exiting dfs(at=%s,parent=%s,bridges=%s,id_=%s)", at, parent, bridges, id_)

    bridges: list[tuple[int, int]] = []
    for i in range(n):
        if not visited[i]:
            dfs(i, -1, bridges, id_)
    return bridges


if __name__ == "__main__":
    import doctest

    doctest.testmod()
