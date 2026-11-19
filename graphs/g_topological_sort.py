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
    logger.error(">>> Entering print_stack(stack=%s,clothes=%s)", stack, clothes, extra={"event.action": "print_stack", "logrite.stack": stack, "logrite.clothes": clothes})
    order = 1
    while stack:
        current_clothing = stack.pop()
        logger.error("print_stack(stack=%s,clothes=%s): current_clothing → %s", stack, clothes, current_clothing, extra={"event.action": "print_stack", "logrite.stack": stack, "logrite.clothes": clothes})
        print(order, clothes[current_clothing])
        order += 1
        logger.warning("<<< Exiting print_stack(stack=%s,clothes=%s)", stack, clothes, extra={"event.action": "print_stack", "logrite.stack": stack, "logrite.clothes": clothes})


def depth_first_search(u, visited, graph):
    logger.error(">>> Entering depth_first_search(u=%s,visited=%s,graph=%s)", u, visited, graph, extra={"event.action": "depth_first_search", "logrite.u": u, "logrite.visited": visited, "logrite.graph": graph})
    visited[u] = 1
    for v in graph[u]:
        if not visited[v]:
            depth_first_search(v, visited, graph)

    stack.append(u)
    logger.warning("<<< Exiting depth_first_search(u=%s,visited=%s,graph=%s)", u, visited, graph, extra={"event.action": "depth_first_search", "logrite.u": u, "logrite.visited": visited, "logrite.graph": graph})


def topological_sort(graph, visited):
    logger.error(">>> Entering topological_sort(graph=%s,visited=%s)", graph, visited, extra={"event.action": "topological_sort", "logrite.graph": graph, "logrite.visited": visited})
    for v in range(len(graph)):
        if not visited[v]:
            depth_first_search(v, visited, graph)
            logger.warning("<<< Exiting topological_sort(graph=%s,visited=%s)", graph, visited, extra={"event.action": "topological_sort", "logrite.graph": graph, "logrite.visited": visited})


if __name__ == "__main__":
    topological_sort(graph, visited)
    print(stack)
    print_stack(stack, clothes)
