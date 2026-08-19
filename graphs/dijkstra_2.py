import logging
logger = logging.getLogger(__name__)
def print_dist(dist, v):
    logger.debug(">>> Entering print_dist(dist=%s,v=%s)", dist, v)
    print("\nVertex Distance")
    for i in range(v):
        if dist[i] != float("inf"):
            print(i, "\t", int(dist[i]), end="\t")
        else:
            print(i, "\t", "INF", end="\t")
        print()
        logger.debug("<<< Exiting print_dist(dist=%s,v=%s)", dist, v)


def min_dist(mdist, vset, v):
    logger.debug(">>> Entering min_dist(mdist=%s,vset=%s,v=%s)", mdist, vset, v)
    min_val = float("inf")
    logger.debug("min_dist(mdist=%s,vset=%s,v=%s): min_val → %s", mdist, vset, v, min_val)
    min_ind = -1
    logger.debug("min_dist(mdist=%s,vset=%s,v=%s): min_ind → %s", mdist, vset, v, min_ind)
    for i in range(v):
        if (not vset[i]) and mdist[i] < min_val:
            min_ind = i
            min_val = mdist[i]
    logger.debug("<<< Exiting min_dist(mdist=%s,vset=%s,v=%s)", mdist, vset, v)
    return min_ind


def dijkstra(graph, v, src):
    logger.debug(">>> Entering dijkstra(graph=%s,v=%s,src=%s)", graph, v, src)
    mdist = [float("inf") for _ in range(v)]
    logger.debug("dijkstra(graph=%s,v=%s,src=%s): mdist → %s", graph, v, src, mdist)
    vset = [False for _ in range(v)]
    mdist[src] = 0.0
    logger.debug("dijkstra(graph=%s,v=%s,src=%s): vset → %s", graph, v, src, vset)

    for _ in range(v - 1):
        u = min_dist(mdist, vset, v)
        logger.debug("dijkstra(graph=%s,v=%s,src=%s): u → %s", graph, v, src, u)
        vset[u] = True

        for i in range(v):
            if (
                (not vset[i])
                and graph[u][i] != float("inf")
                and mdist[u] + graph[u][i] < mdist[i]
            ):
                mdist[i] = mdist[u] + graph[u][i]

    print_dist(mdist, i)
    logger.debug("<<< Exiting dijkstra(graph=%s,v=%s,src=%s)", graph, v, src)


if __name__ == "__main__":
    V = int(input("Enter number of vertices: ").strip())
    E = int(input("Enter number of edges: ").strip())

    graph = [[float("inf") for i in range(V)] for j in range(V)]

    for i in range(V):
        graph[i][i] = 0.0

    for i in range(E):
        print("\nEdge ", i + 1)
        src = int(input("Enter source:").strip())
        dst = int(input("Enter destination:").strip())
        weight = float(input("Enter weight:").strip())
        graph[src][dst] = weight

    gsrc = int(input("\nEnter shortest path source:").strip())
    dijkstra(graph, V, gsrc)
