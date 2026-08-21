import logging
logger = logging.getLogger(__name__)
# Minimum cut on Ford_Fulkerson algorithm.

test_graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]


def bfs(graph, s, t, parent):
    logger.debug(">>> Entering bfs(graph=%s,s=%s,t=%s,parent=%s)", graph, s, t, parent)
    # Return True if there is node that has not iterated.
    visited = [False] * len(graph)
    logger.debug("bfs(graph=%s,s=%s,t=%s,parent=%s): visited → %s", graph, s, t, parent, visited)
    queue = [s]
    logger.debug("bfs(graph=%s,s=%s,t=%s,parent=%s): queue → %s", graph, s, t, parent, queue)
    visited[s] = True

    while queue:
        u = queue.pop(0)
        logger.debug("bfs(graph=%s,s=%s,t=%s,parent=%s): u → %s", graph, s, t, parent, u)
        for ind in range(len(graph[u])):
            if visited[ind] is False and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    logger.debug("<<< Exiting bfs(graph=%s,s=%s,t=%s,parent=%s)", graph, s, t, parent)
    return visited[t]


def mincut(graph, source, sink):
    """This array is filled by BFS and to store path
    >>> mincut(test_graph, source=0, sink=5)
    [(1, 3), (4, 3), (4, 5)]
    """
    logger.debug(">>> Entering mincut(graph=%s,source=%s,sink=%s)", graph, source, sink)
    parent = [-1] * (len(graph))
    logger.debug("mincut(graph=%s,source=%s,sink=%s): parent → %s", graph, source, sink, parent)
    max_flow = 0
    logger.debug("mincut(graph=%s,source=%s,sink=%s): max_flow → %s", graph, source, sink, max_flow)
    res = []
    logger.debug("mincut(graph=%s,source=%s,sink=%s): res → %s", graph, source, sink, res)
    temp = [i[:] for i in graph]  # Record original cut, copy.
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        logger.debug("mincut(graph=%s,source=%s,sink=%s): path_flow → %s", graph, source, sink, path_flow)
        s = sink

        while s != source:
            # Find the minimum value in select path
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink

        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0 and temp[i][j] > 0:
                res.append((i, j))

    logger.debug("<<< Exiting mincut(graph=%s,source=%s,sink=%s)", graph, source, sink)
    return res


if __name__ == "__main__":
    print(mincut(test_graph, source=0, sink=5))
