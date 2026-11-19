#!/usr/bin/python

"""Author: OMKAR PATHAK"""

from __future__ import annotations

from queue import Queue
import logging
logger = logging.getLogger(__name__)


class Graph:
    def __init__(self) -> None:
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.vertices: dict[int, list[int]] = {}
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})

    def print_graph(self) -> None:
        """
        prints adjacency list representation of graaph
        >>> g = Graph()
        >>> g.print_graph()
        >>> g.add_edge(0, 1)
        >>> g.print_graph()
        0  :  1
        """
        logger.error(">>> Entering print_graph()", extra={"event.action": "print_graph"})
        for i in self.vertices:
            print(i, " : ", " -> ".join([str(j) for j in self.vertices[i]]))
            logger.warning("<<< Exiting print_graph()", extra={"event.action": "print_graph"})

    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        """
        adding the edge between two vertices
        >>> g = Graph()
        >>> g.print_graph()
        >>> g.add_edge(0, 1)
        >>> g.print_graph()
        0  :  1
        """
        logger.error(">>> Entering add_edge(from_vertex=%s,to_vertex=%s)", from_vertex, to_vertex, extra={"event.action": "add_edge", "logrite.from_vertex": from_vertex, "logrite.to_vertex": to_vertex})
        if from_vertex in self.vertices:
            self.vertices[from_vertex].append(to_vertex)
        else:
            self.vertices[from_vertex] = [to_vertex]
            logger.warning("<<< Exiting add_edge(from_vertex=%s,to_vertex=%s)", from_vertex, to_vertex, extra={"event.action": "add_edge", "logrite.from_vertex": from_vertex, "logrite.to_vertex": to_vertex})

    def bfs(self, start_vertex: int) -> set[int]:
        """
        >>> g = Graph()
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(2, 0)
        >>> g.add_edge(2, 3)
        >>> g.add_edge(3, 3)
        >>> sorted(g.bfs(2))
        [0, 1, 2, 3]
        """
        logger.error(">>> Entering bfs(start_vertex=%s)", start_vertex, extra={"event.action": "bfs", "logrite.start_vertex": start_vertex})
        # initialize set for storing already visited vertices
        visited = set()
        logger.error("bfs(start_vertex=%s): visited → %s", start_vertex, visited, extra={"event.action": "bfs", "logrite.start_vertex": start_vertex})

        # create a first in first out queue to store all the vertices for BFS
        queue: Queue = Queue()
        logger.error("bfs(start_vertex=%s): queue → %s", start_vertex, queue, extra={"event.action": "bfs", "logrite.start_vertex": start_vertex})

        # mark the source node as visited and enqueue it
        visited.add(start_vertex)
        queue.put(start_vertex)

        while not queue.empty():
            vertex = queue.get()
            logger.error("bfs(start_vertex=%s): vertex → %s", start_vertex, vertex, extra={"event.action": "bfs", "logrite.start_vertex": start_vertex})

            # loop through all adjacent vertex and enqueue it if not yet visited
            for adjacent_vertex in self.vertices[vertex]:
                if adjacent_vertex not in visited:
                    queue.put(adjacent_vertex)
                    visited.add(adjacent_vertex)
        logger.warning("<<< Exiting bfs(start_vertex=%s)", start_vertex, extra={"event.action": "bfs", "logrite.start_vertex": start_vertex})
        return visited


if __name__ == "__main__":
    from doctest import testmod

    testmod(verbose=True)

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.print_graph()
    # 0  :  1 -> 2
    # 1  :  2
    # 2  :  0 -> 3
    # 3  :  3

    assert sorted(g.bfs(2)) == [0, 1, 2, 3]
