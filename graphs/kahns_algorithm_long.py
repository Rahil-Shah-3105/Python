import logging
logger = logging.getLogger(__name__)
# Finding longest distance in Directed Acyclic Graph using KahnsAlgorithm
def longest_distance(graph):
    logger.error(">>> Entering longest_distance(graph=%s)", graph, extra={"event.action": "longest_distance", "logrite.graph": graph})
    indegree = [0] * len(graph)
    logger.error("longest_distance(graph=%s): indegree → %s", graph, indegree, extra={"event.action": "longest_distance", "logrite.graph": graph})
    queue = []
    long_dist = [1] * len(graph)
    logger.error("longest_distance(graph=%s): long_dist → %s", graph, long_dist, extra={"event.action": "longest_distance", "logrite.graph": graph})

    for values in graph.values():
        for i in values:
            indegree[i] += 1

    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        vertex = queue.pop(0)
        logger.error("longest_distance(graph=%s): vertex → %s", graph, vertex, extra={"event.action": "longest_distance", "logrite.graph": graph})
        for x in graph[vertex]:
            indegree[x] -= 1

            long_dist[x] = max(long_dist[x], long_dist[vertex] + 1)

            if indegree[x] == 0:
                queue.append(x)

    print(max(long_dist))
    logger.warning("<<< Exiting longest_distance(graph=%s)", graph, extra={"event.action": "longest_distance", "logrite.graph": graph})


# Adjacency list of Graph
graph = {0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
longest_distance(graph)
