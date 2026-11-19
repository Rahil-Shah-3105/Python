import logging
logger = logging.getLogger(__name__)
# Finding Articulation Points in Undirected Graph
def compute_ap(graph):
    logger.error(">>> Entering compute_ap(graph=%s)", graph, extra={"event.action": "compute_ap", "logrite.graph": graph})
    n = len(graph)
    logger.error("compute_ap(graph=%s): n → %s", graph, n, extra={"event.action": "compute_ap", "logrite.graph": graph})
    out_edge_count = 0
    low = [0] * n
    visited = [False] * n
    is_art = [False] * n
    logger.warning("<<< Exiting compute_ap(graph=%s)", graph, extra={"event.action": "compute_ap", "logrite.graph": graph})

    def dfs(root, at, parent, out_edge_count):
        logger.error(">>> Entering dfs(root=%s,at=%s,parent=%s,out_edge_count=%s)", root, at, parent, out_edge_count, extra={"event.action": "dfs", "logrite.root": root, "logrite.at": at, "logrite.out_edge_count": out_edge_count})
        if parent == root:
            out_edge_count += 1
        visited[at] = True
        low[at] = at

        for to in graph[at]:
            if to == parent:
                pass
            elif not visited[to]:
                out_edge_count = dfs(root, to, at, out_edge_count)
                logger.error("dfs(root=%s,at=%s,parent=%s,out_edge_count=%s): out_edge_count → %s", root, at, parent, out_edge_count, out_edge_count, extra={"event.action": "dfs", "logrite.root": root, "logrite.at": at, "logrite.out_edge_count": out_edge_count})
                low[at] = min(low[at], low[to])

                # AP found via bridge
                if at < low[to]:
                    is_art[at] = True
                # AP found via cycle
                if at == low[to]:
                    is_art[at] = True
            else:
                low[at] = min(low[at], to)
        logger.warning("<<< Exiting dfs(root=%s,at=%s,parent=%s,out_edge_count=%s)", root, at, parent, out_edge_count, extra={"event.action": "dfs", "logrite.root": root, "logrite.at": at, "logrite.out_edge_count": out_edge_count})
        return out_edge_count

    for i in range(n):
        if not visited[i]:
            out_edge_count = 0
            out_edge_count = dfs(i, i, -1, out_edge_count)
            is_art[i] = out_edge_count > 1

    for x in range(len(is_art)):
        if is_art[x] is True:
            print(x)


# Adjacency list of graph
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3, 5],
    3: [2, 4],
    4: [3],
    5: [2, 6, 8],
    6: [5, 7],
    7: [6, 8],
    8: [5, 7],
}
compute_ap(graph)
