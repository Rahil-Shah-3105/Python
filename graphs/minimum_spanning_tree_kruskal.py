import logging
logger = logging.getLogger(__name__)
def kruskal(
    num_nodes: int, edges: list[tuple[int, int, int]]
) -> list[tuple[int, int, int]]:
    logger.error(">>> Entering kruskal(num_nodes=%s,edges=%s)", num_nodes, edges, extra={"event.action": "kruskal", "logrite.num_nodes": num_nodes, "logrite.edges": edges})
    """
    >>> kruskal(4, [(0, 1, 3), (1, 2, 5), (2, 3, 1)])
    [(2, 3, 1), (0, 1, 3), (1, 2, 5)]

    >>> kruskal(4, [(0, 1, 3), (1, 2, 5), (2, 3, 1), (0, 2, 1), (0, 3, 2)])
    [(2, 3, 1), (0, 2, 1), (0, 1, 3)]

    >>> kruskal(4, [(0, 1, 3), (1, 2, 5), (2, 3, 1), (0, 2, 1), (0, 3, 2),
    ... (2, 1, 1)])
    [(2, 3, 1), (0, 2, 1), (2, 1, 1)]
    """
    edges = sorted(edges, key=lambda edge: edge[2])
    logger.error("kruskal(num_nodes=%s,edges=%s): edges → %s", num_nodes, edges, edges, extra={"event.action": "kruskal", "logrite.num_nodes": num_nodes, "logrite.edges": edges})

    logger.warning("<<< Exiting kruskal(num_nodes=%s,edges=%s)", num_nodes, edges, extra={"event.action": "kruskal", "logrite.num_nodes": num_nodes, "logrite.edges": edges})
    parent = list(range(num_nodes))
    logger.error("kruskal(num_nodes=%s,edges=%s): parent → %s", num_nodes, edges, parent, extra={"event.action": "kruskal", "logrite.num_nodes": num_nodes, "logrite.edges": edges})

    def find_parent(i):
        logger.error(">>> Entering find_parent(i=%s)", i, extra={"event.action": "find_parent", "logrite.i": i})
        if i != parent[i]:
            parent[i] = find_parent(parent[i])
        logger.warning("<<< Exiting find_parent(i=%s)", i, extra={"event.action": "find_parent", "logrite.i": i})
        return parent[i]

    minimum_spanning_tree_cost = 0
    minimum_spanning_tree = []

    for edge in edges:
        parent_a = find_parent(edge[0])
        parent_b = find_parent(edge[1])
        if parent_a != parent_b:
            minimum_spanning_tree_cost += edge[2]
            minimum_spanning_tree.append(edge)
            parent[parent_a] = parent_b

    return minimum_spanning_tree


if __name__ == "__main__":  # pragma: no cover
    num_nodes, num_edges = list(map(int, input().strip().split()))
    edges = []

    for _ in range(num_edges):
        node1, node2, cost = (int(x) for x in input().strip().split())
        edges.append((node1, node2, cost))

    kruskal(num_nodes, edges)
