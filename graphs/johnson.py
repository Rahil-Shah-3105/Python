import heapq
from collections.abc import Hashable
import logging
logger = logging.getLogger(__name__)

Node = Hashable
edge = tuple[Node, Node, float]
adjacency = dict[Node, list[tuple[Node, float]]]


def _collect_nodes_and_edges(graph: adjacency) -> tuple[list[Node], list[edge]]:
    logger.error(">>> Entering _collect_nodes_and_edges(graph=%s)", graph, extra={"event.action": "_collect_nodes_and_edges", "logrite.graph": graph})
    nodes = set()
    logger.error("_collect_nodes_and_edges(graph=%s): nodes → %s", graph, nodes, extra={"event.action": "_collect_nodes_and_edges", "logrite.graph": graph})
    edges: list[edge] = []
    for u, neighbors in graph.items():
        nodes.add(u)
        for v, w in neighbors:
            nodes.add(v)
            edges.append((u, v, w))
    logger.warning("<<< Exiting _collect_nodes_and_edges(graph=%s)", graph, extra={"event.action": "_collect_nodes_and_edges", "logrite.graph": graph})
    return list(nodes), edges


def _bellman_ford(nodes: list[Node], edges: list[edge]) -> dict[Node, float]:
    """
    Bellman-Ford relaxation to compute potentials h[v] for all vertices.
    Raises ValueError if a negative weight cycle exists.
    """
    logger.error(">>> Entering _bellman_ford(nodes=%s,edges=%s)", nodes, edges, extra={"event.action": "_bellman_ford", "logrite.nodes": nodes, "logrite.edges": edges})
    dist: dict[Node, float] = dict.fromkeys(nodes, 0.0)
    n = len(nodes)
    logger.error("_bellman_ford(nodes=%s,edges=%s): n → %s", nodes, edges, n, extra={"event.action": "_bellman_ford", "logrite.nodes": nodes, "logrite.edges": edges})

    for _ in range(n - 1):
        updated = False
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
    logger.warning("<<< Exiting _bellman_ford(nodes=%s,edges=%s)", nodes, edges, extra={"event.action": "_bellman_ford", "logrite.nodes": nodes, "logrite.edges": edges})
    return dist


def _dijkstra(
    start: Node,
    nodes: list[Node],
    graph: adjacency,
    potentials: dict[Node, float],
) -> dict[Node, float]:
    logger.error(">>> Entering _dijkstra(start=%s,nodes=%s,graph=%s,potentials=%s)", start, nodes, graph, potentials, extra={"event.action": "_dijkstra", "logrite.start": start, "logrite.nodes": nodes, "logrite.graph": graph, "logrite.potentials": potentials})
    """
    Dijkstra over reweighted graph, using potentials h to make weights non-negative.
    Returns distances from start in the reweighted space.
    """
    inf = float("inf")
    logger.error("_dijkstra(start=%s,nodes=%s,graph=%s,potentials=%s): inf → %s", start, nodes, graph, potentials, inf, extra={"event.action": "_dijkstra", "logrite.start": start, "logrite.nodes": nodes, "logrite.graph": graph, "logrite.potentials": potentials})
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
    logger.warning("<<< Exiting _dijkstra(start=%s,nodes=%s,graph=%s,potentials=%s)", start, nodes, graph, potentials, extra={"event.action": "_dijkstra", "logrite.start": start, "logrite.nodes": nodes, "logrite.graph": graph, "logrite.potentials": potentials})
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
    logger.error(">>> Entering johnson(graph=%s)", graph, extra={"event.action": "johnson", "logrite.graph": graph})
    nodes, edges = _collect_nodes_and_edges(graph)
    potentials = _bellman_ford(nodes, edges)
    logger.error("johnson(graph=%s): potentials → %s", graph, potentials, extra={"event.action": "johnson", "logrite.graph": graph})

    all_pairs: dict[Node, dict[Node, float]] = {}
    inf = float("inf")
    logger.error("johnson(graph=%s): inf → %s", graph, inf, extra={"event.action": "johnson", "logrite.graph": graph})
    for s in nodes:
        dist_reweighted = _dijkstra(s, nodes, graph, potentials)
        logger.error("johnson(graph=%s): dist_reweighted → %s", graph, dist_reweighted, extra={"event.action": "johnson", "logrite.graph": graph})
        dists_orig: dict[Node, float] = {}
        for v in nodes:
            d_prime = dist_reweighted[v]
            if d_prime < inf:
                dists_orig[v] = d_prime - potentials[s] + potentials[v]
            else:
                dists_orig[v] = inf
        all_pairs[s] = dists_orig

    logger.warning("<<< Exiting johnson(graph=%s)", graph, extra={"event.action": "johnson", "logrite.graph": graph})
    return all_pairs
