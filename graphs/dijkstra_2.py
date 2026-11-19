import logging
logger = logging.getLogger(__name__)
def print_dist(dist, v):
    logger.error(">>> Entering print_dist(dist=%s,v=%s)", dist, v, extra={"event.action": "print_dist", "logrite.dist": dist, "logrite.v": v})
    print("\nVertex Distance")
    for i in range(v):
        if dist[i] != float("inf"):
            print(i, "\t", int(dist[i]), end="\t")
        else:
            print(i, "\t", "INF", end="\t")
        print()
        logger.warning("<<< Exiting print_dist(dist=%s,v=%s)", dist, v, extra={"event.action": "print_dist", "logrite.dist": dist, "logrite.v": v})


def min_dist(mdist, vset, v):
    logger.error(">>> Entering min_dist(mdist=%s,vset=%s,v=%s)", mdist, vset, v, extra={"event.action": "min_dist", "logrite.mdist": mdist, "logrite.vset": vset, "logrite.v": v})
    min_val = float("inf")
    min_ind = -1
    for i in range(v):
        if (not vset[i]) and mdist[i] < min_val:
            min_ind = i
            min_val = mdist[i]
    logger.warning("<<< Exiting min_dist(mdist=%s,vset=%s,v=%s)", mdist, vset, v, extra={"event.action": "min_dist", "logrite.mdist": mdist, "logrite.vset": vset, "logrite.v": v})
    return min_ind


def dijkstra(graph, v, src):
    logger.error(">>> Entering dijkstra(graph=%s,v=%s,src=%s)", graph, v, src, extra={"event.action": "dijkstra", "logrite.graph": graph, "logrite.v": v, "logrite.src": src})
    mdist = [float("inf") for _ in range(v)]
    logger.error("dijkstra(graph=%s,v=%s,src=%s): mdist → %s", graph, v, src, mdist, extra={"event.action": "dijkstra", "logrite.graph": graph, "logrite.v": v, "logrite.src": src})
    vset = [False for _ in range(v)]
    logger.error("dijkstra(graph=%s,v=%s,src=%s): vset → %s", graph, v, src, vset, extra={"event.action": "dijkstra", "logrite.graph": graph, "logrite.v": v, "logrite.src": src})
    mdist[src] = 0.0

    for _ in range(v - 1):
        u = min_dist(mdist, vset, v)
        logger.error("dijkstra(graph=%s,v=%s,src=%s): u → %s", graph, v, src, u, extra={"event.action": "dijkstra", "logrite.graph": graph, "logrite.v": v, "logrite.src": src})
        vset[u] = True

        for i in range(v):
            if (
                (not vset[i])
                and graph[u][i] != float("inf")
                and mdist[u] + graph[u][i] < mdist[i]
            ):
                mdist[i] = mdist[u] + graph[u][i]

    print_dist(mdist, i)
    logger.warning("<<< Exiting dijkstra(graph=%s,v=%s,src=%s)", graph, v, src, extra={"event.action": "dijkstra", "logrite.graph": graph, "logrite.v": v, "logrite.src": src})


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
