import logging
logger = logging.getLogger(__name__)
# Finding longest distance in Directed Acyclic Graph using KahnsAlgorithm
def longest_distance(graph):
    logger.debug(">>> Entering longest_distance(graph=%s)", graph)
    indegree = [0] * len(graph)
    logger.debug("longest_distance(graph=%s): indegree → %s", graph, indegree)
    queue = []
    long_dist = [1] * len(graph)
    logger.debug("longest_distance(graph=%s): queue → %s", graph, queue)
    logger.debug("longest_distance(graph=%s): long_dist → %s", graph, long_dist)

    for values in graph.values():
        for i in values:
            indegree[i] += 1

    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        vertex = queue.pop(0)
        logger.debug("longest_distance(graph=%s): vertex → %s", graph, vertex)
        for x in graph[vertex]:
            indegree[x] -= 1

            long_dist[x] = max(long_dist[x], long_dist[vertex] + 1)

            if indegree[x] == 0:
                queue.append(x)

    print(max(long_dist))
    logger.debug("<<< Exiting longest_distance(graph=%s)", graph)


# Adjacency list of Graph
graph = {0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
longest_distance(graph)
