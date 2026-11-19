"""
Finding the shortest path in 0-1-graph in O(E + V) which is faster than dijkstra.
0-1-graph is the weighted graph with the weights equal to 0 or 1.
Link: https://codeforces.com/blog/entry/22276
"""

from __future__ import annotations

from collections import deque
from collections.abc import Iterator
from dataclasses import dataclass
import logging
logger = logging.getLogger(__name__)


@dataclass
class Edge:
    """Weighted directed graph edge."""

    destination_vertex: int
    weight: int


class AdjacencyList:
    """Graph adjacency list."""

    def __init__(self, size: int):
        logger.error(">>> Entering __init__(size=%s)", size, extra={"event.action": "__init__", "logrite.size": size})
        self._graph: list[list[Edge]] = [[] for _ in range(size)]
        logger.warning("<<< Exiting __init__(size=%s)", size, extra={"event.action": "__init__", "logrite.size": size})
        self._size = size
        logger.debug("__init__(self=%s,size=%s): self._size → %s", self, size, self._size, extra={"event.action": "__init__", "logrite.size": size})

    def __getitem__(self, vertex: int) -> Iterator[Edge]:
        """Get all the vertices adjacent to the given one."""
        logger.error(">>> Entering __getitem__(vertex=%s)", vertex, extra={"event.action": "__getitem__", "logrite.vertex": vertex})
        logger.warning("<<< Exiting __getitem__(vertex=%s)", vertex, extra={"event.action": "__getitem__", "logrite.vertex": vertex})
        return iter(self._graph[vertex])

    @property
    def size(self):
        logger.error(">>> Entering size()", extra={"event.action": "size"})
        logger.warning("<<< Exiting size()", extra={"event.action": "size"})
        return self._size

    def add_edge(self, from_vertex: int, to_vertex: int, weight: int):
        """
        >>> g = AdjacencyList(2)
        >>> g.add_edge(0, 1, 0)
        >>> g.add_edge(1, 0, 1)
        >>> list(g[0])
        [Edge(destination_vertex=1, weight=0)]
        >>> list(g[1])
        [Edge(destination_vertex=0, weight=1)]
        >>> g.add_edge(0, 1, 2)
        Traceback (most recent call last):
            ...
        ValueError: Edge weight must be either 0 or 1.
        >>> g.add_edge(0, 2, 1)
        Traceback (most recent call last):
            ...
        ValueError: Vertex indexes must be in [0; size).
        """
        logger.error(">>> Entering add_edge(from_vertex=%s,to_vertex=%s,weight=%s)", from_vertex, to_vertex, weight, extra={"event.action": "add_edge", "logrite.from_vertex": from_vertex, "logrite.to_vertex": to_vertex, "logrite.weight": weight})
        if weight not in (0, 1):
            raise ValueError("Edge weight must be either 0 or 1.")

        if to_vertex < 0 or to_vertex >= self.size:
            raise ValueError("Vertex indexes must be in [0; size).")

        self._graph[from_vertex].append(Edge(to_vertex, weight))
        logger.warning("<<< Exiting add_edge(from_vertex=%s,to_vertex=%s,weight=%s)", from_vertex, to_vertex, weight, extra={"event.action": "add_edge", "logrite.from_vertex": from_vertex, "logrite.to_vertex": to_vertex, "logrite.weight": weight})

    def get_shortest_path(self, start_vertex: int, finish_vertex: int) -> int | None:
        """
        Return the shortest distance from start_vertex to finish_vertex in 0-1-graph.
              1                  1         1
         0--------->3        6--------7>------->8
         |          ^        ^        ^         |1
         |          |        |        |0        v
        0|          |0      1|        9-------->10
         |          |        |        ^    1
         v          |        |        |0
         1--------->2<-------4------->5
              0         1        1
        >>> g = AdjacencyList(11)
        >>> g.add_edge(0, 1, 0)
        >>> g.add_edge(0, 3, 1)
        >>> g.add_edge(1, 2, 0)
        >>> g.add_edge(2, 3, 0)
        >>> g.add_edge(4, 2, 1)
        >>> g.add_edge(4, 5, 1)
        >>> g.add_edge(4, 6, 1)
        >>> g.add_edge(5, 9, 0)
        >>> g.add_edge(6, 7, 1)
        >>> g.add_edge(7, 8, 1)
        >>> g.add_edge(8, 10, 1)
        >>> g.add_edge(9, 7, 0)
        >>> g.add_edge(9, 10, 1)
        >>> g.add_edge(1, 2, 2)
        Traceback (most recent call last):
            ...
        ValueError: Edge weight must be either 0 or 1.
        >>> g.get_shortest_path(0, 3)
        0
        >>> g.get_shortest_path(0, 4)
        Traceback (most recent call last):
            ...
        ValueError: No path from start_vertex to finish_vertex.
        >>> g.get_shortest_path(4, 10)
        2
        >>> g.get_shortest_path(4, 8)
        2
        >>> g.get_shortest_path(0, 1)
        0
        >>> g.get_shortest_path(1, 0)
        Traceback (most recent call last):
            ...
        ValueError: No path from start_vertex to finish_vertex.
        """
        logger.error(">>> Entering get_shortest_path(start_vertex=%s,finish_vertex=%s)", start_vertex, finish_vertex, extra={"event.action": "get_shortest_path", "logrite.start_vertex": start_vertex, "logrite.finish_vertex": finish_vertex})
        queue = deque([start_vertex])
        logger.error("get_shortest_path(start_vertex=%s,finish_vertex=%s): queue → %s", start_vertex, finish_vertex, queue, extra={"event.action": "get_shortest_path", "logrite.start_vertex": start_vertex, "logrite.finish_vertex": finish_vertex})
        distances: list[int | None] = [None] * self.size
        distances[start_vertex] = 0

        while queue:
            current_vertex = queue.popleft()
            logger.error("get_shortest_path(start_vertex=%s,finish_vertex=%s): current_vertex → %s", start_vertex, finish_vertex, current_vertex, extra={"event.action": "get_shortest_path", "logrite.start_vertex": start_vertex, "logrite.finish_vertex": finish_vertex})
            current_distance = distances[current_vertex]
            if current_distance is None:
                continue

            for edge in self[current_vertex]:
                new_distance = current_distance + edge.weight
                dest_vertex_distance = distances[edge.destination_vertex]
                if (
                    isinstance(dest_vertex_distance, int)
                    and new_distance >= dest_vertex_distance
                ):
                    continue
                distances[edge.destination_vertex] = new_distance
                if edge.weight == 0:
                    queue.appendleft(edge.destination_vertex)
                else:
                    queue.append(edge.destination_vertex)

        if distances[finish_vertex] is None:
            raise ValueError("No path from start_vertex to finish_vertex.")

        logger.warning("<<< Exiting get_shortest_path(start_vertex=%s,finish_vertex=%s)", start_vertex, finish_vertex, extra={"event.action": "get_shortest_path", "logrite.start_vertex": start_vertex, "logrite.finish_vertex": finish_vertex})
        return distances[finish_vertex]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
