import logging
logger = logging.getLogger(__name__)
"""
https://en.wikipedia.org/wiki/Component_(graph_theory)

Finding connected components in graph

"""

test_graph_1 = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1], 4: [5, 6], 5: [4, 6], 6: [4, 5]}

test_graph_2 = {0: [1, 2, 3], 1: [0, 3], 2: [0], 3: [0, 1], 4: [], 5: []}


def dfs(graph: dict, vert: int, visited: list) -> list:
    """
    Use depth first search to find all vertices
    being in the same component as initial vertex
    >>> dfs(test_graph_1, 0, 5 * [False])
    [0, 1, 3, 2]
    >>> dfs(test_graph_2, 0, 6 * [False])
    [0, 1, 3, 2]
    """
    logger.debug(">>> Entering dfs(graph=%s,vert=%s,visited=%s)", graph, vert, visited)

    visited[vert] = True
    connected_verts = []
    logger.debug("dfs(graph=%s,vert=%s,visited=%s): connected_verts → %s", graph, vert, visited, connected_verts)

    for neighbour in graph[vert]:
        if not visited[neighbour]:
            connected_verts += dfs(graph, neighbour, visited)

    logger.debug("<<< Exiting dfs(graph=%s,vert=%s,visited=%s)", graph, vert, visited)
    return [vert, *connected_verts]


def connected_components(graph: dict) -> list:
    """
    This function takes graph as a parameter
    and then returns the list of connected components
    >>> connected_components(test_graph_1)
    [[0, 1, 3, 2], [4, 5, 6]]
    >>> connected_components(test_graph_2)
    [[0, 1, 3, 2], [4], [5]]
    """
    logger.debug(">>> Entering connected_components(graph=%s)", graph)

    graph_size = len(graph)
    logger.debug("connected_components(graph=%s): graph_size → %s", graph, graph_size)
    visited = graph_size * [False]
    logger.debug("connected_components(graph=%s): visited → %s", graph, visited)
    components_list = []
    logger.debug("connected_components(graph=%s): components_list → %s", graph, components_list)

    for i in range(graph_size):
        if not visited[i]:
            i_connected = dfs(graph, i, visited)
            logger.debug("connected_components(graph=%s): i_connected → %s", graph, i_connected)
            components_list.append(i_connected)

    logger.debug("<<< Exiting connected_components(graph=%s)", graph)
    return components_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
