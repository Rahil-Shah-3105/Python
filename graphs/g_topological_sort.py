import logging
logger = logging.getLogger(__name__)
# Author: Phyllipe Bezerra (https://github.com/pmba)

clothes = {
    0: "underwear",
    1: "pants",
    2: "belt",
    3: "suit",
    4: "shoe",
    5: "socks",
    6: "shirt",
    7: "tie",
    8: "watch",
}

graph = [[1, 4], [2, 4], [3], [], [], [4], [2, 7], [3], []]

visited = [0 for x in range(len(graph))]
stack = []


def print_stack(stack, clothes):
    logger.debug(">>> Entering print_stack(stack=%s,clothes=%s)", stack, clothes)
    order = 1
    logger.debug("print_stack(stack=%s,clothes=%s): order → %s", stack, clothes, order)
    while stack:
        current_clothing = stack.pop()
        logger.debug("print_stack(stack=%s,clothes=%s): current_clothing → %s", stack, clothes, current_clothing)
        print(order, clothes[current_clothing])
        order += 1
        logger.debug("<<< Exiting print_stack(stack=%s,clothes=%s)", stack, clothes)


def depth_first_search(u, visited, graph):
    logger.debug(">>> Entering depth_first_search(u=%s,visited=%s,graph=%s)", u, visited, graph)
    visited[u] = 1
    for v in graph[u]:
        if not visited[v]:
            depth_first_search(v, visited, graph)

    stack.append(u)
    logger.debug("<<< Exiting depth_first_search(u=%s,visited=%s,graph=%s)", u, visited, graph)


def topological_sort(graph, visited):
    logger.debug(">>> Entering topological_sort(graph=%s,visited=%s)", graph, visited)
    for v in range(len(graph)):
        if not visited[v]:
            depth_first_search(v, visited, graph)
            logger.debug("<<< Exiting topological_sort(graph=%s,visited=%s)", graph, visited)


if __name__ == "__main__":
    topological_sort(graph, visited)
    print(stack)
    print_stack(stack, clothes)
