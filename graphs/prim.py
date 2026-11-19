"""Prim's Algorithm.

Determines the minimum spanning tree(MST) of a graph using the Prim's Algorithm.

Details: https://en.wikipedia.org/wiki/Prim%27s_algorithm
"""

import heapq as hq
import math
from collections.abc import Iterator
import logging
logger = logging.getLogger(__name__)


class Vertex:
    """Class Vertex."""

    def __init__(self, id_):
        """
        Arguments:
            id - input an id to identify the vertex
        Attributes:
            neighbors - a list of the vertices it is linked to
            edges     - a dict to store the edges's weight
        """
        logger.error(">>> Entering __init__(id_=%s)", id_, extra={"event.action": "__init__", "logrite.id_": id_})
        self.id = str(id_)
        logger.warning("<<< Exiting __init__(id_=%s)", id_, extra={"event.action": "__init__", "logrite.id_": id_})
        logger.error("__init__(id_=%s): self.id → %s", id_, self.id, extra={"event.action": "__init__", "logrite.id_": id_})
        self.key = None
        self.pi = None
        logger.debug("__init__(self=%s,id_=%s): self.key → %s", self, id_, self.key, extra={"event.action": "__init__", "logrite.id_": id_})
        logger.error("__init__(id_=%s): self.key → %s", id_, self.key, extra={"event.action": "__init__", "logrite.id_": id_})
        logger.debug("__init__(self=%s,id_=%s): self.pi → %s", self, id_, self.pi, extra={"event.action": "__init__", "logrite.id_": id_})
        self.neighbors = []
        self.edges = {}  # {vertex:distance}
        logger.debug("__init__(self=%s,id_=%s): self.edges → %s", self, id_, self.edges, extra={"event.action": "__init__", "logrite.id_": id_})

    def __lt__(self, other):
        """Comparison rule to < operator."""
        logger.error(">>> Entering __lt__(other=%s)", other, extra={"event.action": "__lt__", "logrite.other": other})
        logger.warning("<<< Exiting __lt__(other=%s)", other, extra={"event.action": "__lt__", "logrite.other": other})
        return self.key < other.key

    def __repr__(self):
        """Return the vertex id."""
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return self.id

    def add_neighbor(self, vertex):
        """Add a pointer to a vertex at neighbor's list."""
        logger.error(">>> Entering add_neighbor(vertex=%s)", vertex, extra={"event.action": "add_neighbor", "logrite.vertex": vertex})
        self.neighbors.append(vertex)
        logger.warning("<<< Exiting add_neighbor(vertex=%s)", vertex, extra={"event.action": "add_neighbor", "logrite.vertex": vertex})

    def add_edge(self, vertex, weight):
        """Destination vertex and weight."""
        logger.error(">>> Entering add_edge(vertex=%s,weight=%s)", vertex, weight, extra={"event.action": "add_edge", "logrite.vertex": vertex, "logrite.weight": weight})
        self.edges[vertex.id] = weight
        logger.warning("<<< Exiting add_edge(vertex=%s,weight=%s)", vertex, weight, extra={"event.action": "add_edge", "logrite.vertex": vertex, "logrite.weight": weight})


def connect(graph, a, b, edge):
    logger.error(">>> Entering connect(graph=%s,a=%s,b=%s,edge=%s)", graph, a, b, edge, extra={"event.action": "connect", "logrite.graph": graph, "logrite.a": a, "logrite.b": b, "logrite.edge": edge})
    # add the neighbors:
    graph[a - 1].add_neighbor(graph[b - 1])
    graph[b - 1].add_neighbor(graph[a - 1])
    # add the edges:
    graph[a - 1].add_edge(graph[b - 1], edge)
    graph[b - 1].add_edge(graph[a - 1], edge)
    logger.warning("<<< Exiting connect(graph=%s,a=%s,b=%s,edge=%s)", graph, a, b, edge, extra={"event.action": "connect", "logrite.graph": graph, "logrite.a": a, "logrite.b": b, "logrite.edge": edge})


def prim(graph: list, root: Vertex) -> list:
    """Prim's Algorithm.

    Runtime:
        O(mn) with `m` edges and `n` vertices

    Return:
        List with the edges of a Minimum Spanning Tree

    Usage:
        prim(graph, graph[0])
    """
    logger.error(">>> Entering prim(graph=%s,root=%s)", graph, root, extra={"event.action": "prim", "logrite.graph": graph, "logrite.root": root})
    a = []
    for u in graph:
        u.key = math.inf
        logger.debug("prim(graph=%s,root=%s): u.key → %s", graph, root, u.key, extra={"event.action": "prim", "logrite.graph": graph, "logrite.root": root})
        u.pi = None
        logger.debug("prim(graph=%s,root=%s): u.pi → %s", graph, root, u.pi, extra={"event.action": "prim", "logrite.graph": graph, "logrite.root": root})
    root.key = 0
    logger.debug("prim(graph=%s,root=%s): root.key → %s", graph, root, root.key, extra={"event.action": "prim", "logrite.graph": graph, "logrite.root": root})
    q = graph[:]
    while q:
        u = min(q)
        logger.error("prim(graph=%s,root=%s): u → %s", graph, root, u, extra={"event.action": "prim", "logrite.graph": graph, "logrite.root": root})
        q.remove(u)
        for v in u.neighbors:
            if (v in q) and (u.edges[v.id] < v.key):
                v.pi = u
                logger.debug("prim(graph=%s,root=%s): v.pi → %s", graph, root, v.pi, extra={"event.action": "prim", "logrite.graph": graph, "logrite.root": root})
                v.key = u.edges[v.id]
                logger.debug("prim(graph=%s,root=%s): v.key → %s", graph, root, v.key, extra={"event.action": "prim", "logrite.graph": graph, "logrite.root": root})
    for i in range(1, len(graph)):
        a.append((int(graph[i].id) + 1, int(graph[i].pi.id) + 1))
    logger.warning("<<< Exiting prim(graph=%s,root=%s)", graph, root, extra={"event.action": "prim", "logrite.graph": graph, "logrite.root": root})
    return a


def prim_heap(graph: list, root: Vertex) -> Iterator[tuple]:
    """Prim's Algorithm with min heap.

    Runtime:
        O((m + n)log n) with `m` edges and `n` vertices

    Yield:
        Edges of a Minimum Spanning Tree

    Usage:
        prim(graph, graph[0])
    """
    logger.error(">>> Entering prim_heap(graph=%s,root=%s)", graph, root, extra={"event.action": "prim_heap", "logrite.graph": graph, "logrite.root": root})
    for u in graph:
        u.key = math.inf
        logger.debug("prim_heap(graph=%s,root=%s): u.key → %s", graph, root, u.key, extra={"event.action": "prim_heap", "logrite.graph": graph, "logrite.root": root})
        u.pi = None
        logger.debug("prim_heap(graph=%s,root=%s): u.pi → %s", graph, root, u.pi, extra={"event.action": "prim_heap", "logrite.graph": graph, "logrite.root": root})
    root.key = 0
    logger.debug("prim_heap(graph=%s,root=%s): root.key → %s", graph, root, root.key, extra={"event.action": "prim_heap", "logrite.graph": graph, "logrite.root": root})

    h = list(graph)
    logger.error("prim_heap(graph=%s,root=%s): h → %s", graph, root, h, extra={"event.action": "prim_heap", "logrite.graph": graph, "logrite.root": root})
    hq.heapify(h)

    while h:
        u = hq.heappop(h)
        logger.error("prim_heap(graph=%s,root=%s): u → %s", graph, root, u, extra={"event.action": "prim_heap", "logrite.graph": graph, "logrite.root": root})
        for v in u.neighbors:
            if (v in h) and (u.edges[v.id] < v.key):
                v.pi = u
                logger.debug("prim_heap(graph=%s,root=%s): v.pi → %s", graph, root, v.pi, extra={"event.action": "prim_heap", "logrite.graph": graph, "logrite.root": root})
                v.key = u.edges[v.id]
                logger.debug("prim_heap(graph=%s,root=%s): v.key → %s", graph, root, v.key, extra={"event.action": "prim_heap", "logrite.graph": graph, "logrite.root": root})
                hq.heapify(h)

    for i in range(1, len(graph)):
        yield (int(graph[i].id) + 1, int(graph[i].pi.id) + 1)
        logger.warning("<<< Exiting prim_heap(graph=%s,root=%s)", graph, root, extra={"event.action": "prim_heap", "logrite.graph": graph, "logrite.root": root})


def test_vector() -> None:
    """
    # Creates a list to store x vertices.
    >>> x = 5
    >>> G = [Vertex(n) for n in range(x)]

    >>> connect(G, 1, 2, 15)
    >>> connect(G, 1, 3, 12)
    >>> connect(G, 2, 4, 13)
    >>> connect(G, 2, 5, 5)
    >>> connect(G, 3, 2, 6)
    >>> connect(G, 3, 4, 6)
    >>> connect(G, 0, 0, 0)  # Generate the minimum spanning tree:
    >>> G_heap = G[:]
    >>> MST = prim(G, G[0])
    >>> MST_heap = prim_heap(G, G[0])
    >>> for i in MST:
    ...     print(i)
    (2, 3)
    (3, 1)
    (4, 3)
    (5, 2)
    >>> for i in MST_heap:
    ...     print(i)
    (2, 3)
    (3, 1)
    (4, 3)
    (5, 2)
    """
    logger.error(">>> Entering test_vector()", extra={"event.action": "test_vector"})

    logger.warning("<<< Exiting test_vector()", extra={"event.action": "test_vector"})

if __name__ == "__main__":
    import doctest

    doctest.testmod()
