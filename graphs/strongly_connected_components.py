"""
https://en.wikipedia.org/wiki/Strongly_connected_component

Finding strongly connected components in directed graph

"""
import logging
logger = logging.getLogger(__name__)

test_graph_1 = {0: [2, 3], 1: [0], 2: [1], 3: [4], 4: []}

test_graph_2 = {0: [1, 2, 3], 1: [2], 2: [0], 3: [4], 4: [5], 5: [3]}


def topology_sort(
    graph: dict[int, list[int]], vert: int, visited: list[bool]
) -> list[int]:
    logger.error(">>> Entering topology_sort(graph=%s,vert=%s,visited=%s)", graph, vert, visited, extra={"event.action": "topology_sort", "logrite.graph": graph, "logrite.vert": vert, "logrite.visited": visited})
    """
    Use depth first search to sort graph
    At this time graph is the same as input
    >>> topology_sort(test_graph_1, 0, 5 * [False])
    [1, 2, 4, 3, 0]
    >>> topology_sort(test_graph_2, 0, 6 * [False])
    [2, 1, 5, 4, 3, 0]
    """

    visited[vert] = True
    order = []

    for neighbour in graph[vert]:
        if not visited[neighbour]:
            order += topology_sort(graph, neighbour, visited)

    order.append(vert)

    logger.warning("<<< Exiting topology_sort(graph=%s,vert=%s,visited=%s)", graph, vert, visited, extra={"event.action": "topology_sort", "logrite.graph": graph, "logrite.vert": vert, "logrite.visited": visited})
    return order


def find_components(
    reversed_graph: dict[int, list[int]], vert: int, visited: list[bool]
) -> list[int]:
    logger.error(">>> Entering find_components(reversed_graph=%s,vert=%s,visited=%s)", reversed_graph, vert, visited, extra={"event.action": "find_components", "logrite.reversed_graph": reversed_graph, "logrite.vert": vert, "logrite.visited": visited})
    """
    Use depth first search to find strongly connected
    vertices. Now graph is reversed
    >>> find_components({0: [1], 1: [2], 2: [0]}, 0, 5 * [False])
    [0, 1, 2]
    >>> find_components({0: [2], 1: [0], 2: [0, 1]}, 0, 6 * [False])
    [0, 2, 1]
    """

    visited[vert] = True
    component = [vert]

    for neighbour in reversed_graph[vert]:
        if not visited[neighbour]:
            component += find_components(reversed_graph, neighbour, visited)

    logger.warning("<<< Exiting find_components(reversed_graph=%s,vert=%s,visited=%s)", reversed_graph, vert, visited, extra={"event.action": "find_components", "logrite.reversed_graph": reversed_graph, "logrite.vert": vert, "logrite.visited": visited})
    return component


def strongly_connected_components(graph: dict[int, list[int]]) -> list[list[int]]:
    """
    This function takes graph as a parameter
    and then returns the list of strongly connected components
    >>> strongly_connected_components(test_graph_1)
    [[0, 1, 2], [3], [4]]
    >>> strongly_connected_components(test_graph_2)
    [[0, 2, 1], [3, 5, 4]]
    """
    logger.error(">>> Entering strongly_connected_components(graph=%s)", graph, extra={"event.action": "strongly_connected_components", "logrite.graph": graph})

    visited = len(graph) * [False]
    logger.error("strongly_connected_components(graph=%s): visited → %s", graph, visited, extra={"event.action": "strongly_connected_components", "logrite.graph": graph})
    reversed_graph: dict[int, list[int]] = {vert: [] for vert in range(len(graph))}

    for vert, neighbours in graph.items():
        for neighbour in neighbours:
            reversed_graph[neighbour].append(vert)

    order = []
    for i, was_visited in enumerate(visited):
        if not was_visited:
            order += topology_sort(graph, i, visited)

    components_list = []
    visited = len(graph) * [False]

    for i in range(len(graph)):
        vert = order[len(graph) - i - 1]
        logger.error("strongly_connected_components(graph=%s): vert → %s", graph, vert, extra={"event.action": "strongly_connected_components", "logrite.graph": graph})
        if not visited[vert]:
            component = find_components(reversed_graph, vert, visited)
            logger.error("strongly_connected_components(graph=%s): component → %s", graph, component, extra={"event.action": "strongly_connected_components", "logrite.graph": graph})
            components_list.append(component)

    logger.warning("<<< Exiting strongly_connected_components(graph=%s)", graph, extra={"event.action": "strongly_connected_components", "logrite.graph": graph})
    return components_list
