import heapq
from collections.abc import Hashable
import logging
logger = logging.getLogger(__name__)

Node = Hashable
edge = tuple[Node, Node, float]
adjacency = dict[Node, list[tuple[Node, float]]]


def _collect_nodes_and_edges(graph: adjacency) -> tuple[list[Node], list[edge]]:
    logger.debug(">>> Entering _collect_nodes_and_edges(graph=%s)", graph)
    nodes = set()
    logger.debug("_collect_nodes_and_edges(graph=%s): nodes → %s", graph, nodes)
    edges: list[edge] = []
    for u, neighbors in graph.items():
        nodes.add(u)
        for v, w in neighbors:
            nodes.add(v)
            edges.append((u, v, w))
    logger.debug("<<< Exiting _collect_nodes_and_edges(graph=%s)", graph)
    return list(nodes), edges


def _bellman_ford(nodes: list[Node], edges: list[edge]) -> dict[Node, float]:
    """
    Bellman-Ford relaxation to compute potentials h[v] for all vertices.
    Raises ValueError if a negative weight cycle exists.
    """
    logger.debug(">>> Entering _bellman_ford(nodes=%s,edges=%s)", nodes, edges)
    dist: dict[Node, float] = dict.fromkeys(nodes, 0.0)
    n = len(nodes)
    logger.debug("_bellman_ford(nodes=%s,edges=%s): n → %s", nodes, edges, n)

    for _ in range(n - 1):
        updated = False
        logger.debug("_bellman_ford(nodes=%s,edges=%s): updated → %s", nodes, edges, updated)
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break
    else:
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                raise ValueError("Negative weight cycle detected")
    logger.debug("<<< Exiting _bellman_ford(nodes=%s,edges=%s)", nodes, edges)
    return dist


def _dijkstra(
    start: Node,
    nodes: list[Node],
    graph: adjacency,
    potentials: dict[Node, float],
) -> dict[Node, float]:
    """
    Dijkstra over reweighted graph, using potentials h to make weights non-negative.
    Returns distances from start in the reweighted space.
    """
    inf = float("inf")
    dist: dict[Node, float] = dict.fromkeys(nodes, inf)
    dist[start] = 0.0
    heap: list[tuple[float, Node]] = [(0.0, start)]

    while heap:
        d_u, u = heapq.heappop(heap)
        if d_u > dist[u]:
            continue
        for v, w in graph.get(u, []):
            w_prime = w + potentials[u] - potentials[v]
            if w_prime < 0:
                raise ValueError(
                    "Negative edge weight after reweighting: numeric error"
                )
            new_dist = d_u + w_prime
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))
    return dist


def johnson(graph: adjacency) -> dict[Node, dict[Node, float]]:
    """
    Compute all-pairs shortest paths using Johnson's algorithm.

    Reference:
        https://en.wikipedia.org/wiki/Johnson%27s_algorithm

    Args:
        graph: adjacency list {u: [(v, weight), ...], ...}

    Returns:
        dict of dicts: dist[u][v] = shortest distance from u to v

    Raises:
        ValueError: if a negative weight cycle is detected

    Example:
    >>> g = {
    ...     0: [(1, 3), (2, 8), (4, -4)],
    ...     1: [(3, 1), (4, 7)],
    ...     2: [(1, 4)],
    ...     3: [(0, 2), (2, -5)],
    ...     4: [(3, 6)],
    ... }
    >>> round(johnson(g)[0][3], 2)
    2.0
    """
    logger.debug(">>> Entering johnson(graph=%s)", graph)
    nodes, edges = _collect_nodes_and_edges(graph)
    potentials = _bellman_ford(nodes, edges)
    logger.debug("johnson(graph=%s): potentials → %s", graph, potentials)

    all_pairs: dict[Node, dict[Node, float]] = {}
    inf = float("inf")
    logger.debug("johnson(graph=%s): inf → %s", graph, inf)
    for s in nodes:
        dist_reweighted = _dijkstra(s, nodes, graph, potentials)
        logger.debug("johnson(graph=%s): dist_reweighted → %s", graph, dist_reweighted)
        dists_orig: dict[Node, float] = {}
        for v in nodes:
            d_prime = dist_reweighted[v]
            logger.debug("johnson(graph=%s): d_prime → %s", graph, d_prime)
            if d_prime < inf:
                dists_orig[v] = d_prime - potentials[s] + potentials[v]
            else:
                dists_orig[v] = inf
        all_pairs[s] = dists_orig

    logger.debug("<<< Exiting johnson(graph=%s)", graph)
    return all_pairs
