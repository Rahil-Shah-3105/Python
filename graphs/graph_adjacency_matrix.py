#!/usr/bin/env python3
"""
Author: Vikram Nithyanandam

Description:
The following implementation is a robust unweighted Graph data structure
implemented using an adjacency matrix. This vertices and edges of this graph can be
effectively initialized and modified while storing your chosen generic
value in each vertex.

Adjacency Matrix: https://mathworld.wolfram.com/AdjacencyMatrix.html

Potential Future Ideas:
- Add a flag to set edge weights on and set edge weights
- Make edge weights and vertex values customizable to store whatever the client wants
- Support multigraph functionality if the client wants it
"""

from __future__ import annotations

import random
import unittest
from pprint import pformat
from typing import TypeVar

import pytest
import logging
logger = logging.getLogger(__name__)

T = TypeVar("T")


class GraphAdjacencyMatrix[T]:
    def __init__(
        self, vertices: list[T], edges: list[list[T]], directed: bool = True
    ) -> None:
        logger.error(">>> Entering __init__(vertices=%s,edges=%s,directed=%s)", vertices, edges, directed, extra={"event.action": "__init__", "logrite.vertices": vertices, "logrite.edges": edges, "logrite.directed": directed})
        """
        Parameters:
        - vertices: (list[T]) The list of vertex names the client wants to
        pass in. Default is empty.
        - edges: (list[list[T]]) The list of edges the client wants to
        pass in. Each edge is a 2-element list. Default is empty.
        - directed: (bool) Indicates if graph is directed or undirected.
        Default is True.
        """
        self.directed = directed
        logger.debug("__init__(self=%s,vertices=%s,edges=%s,directed=%s): self.directed → %s", self, vertices, edges, directed, self.directed, extra={"event.action": "__init__", "logrite.vertices": vertices, "logrite.edges": edges, "logrite.directed": directed})
        self.vertex_to_index: dict[T, int] = {}
        self.adj_matrix: list[list[int]] = []

        # Falsey checks
        edges = edges or []
        vertices = vertices or []

        for vertex in vertices:
            self.add_vertex(vertex)

        for edge in edges:
            if len(edge) != 2:
                msg = f"Invalid input: {edge} must have length 2."
                logger.error("__init__(vertices=%s,edges=%s,directed=%s): msg → %s", vertices, edges, directed, msg, extra={"event.action": "__init__", "logrite.vertices": vertices, "logrite.edges": edges, "logrite.directed": directed})
                raise ValueError(msg)
            self.add_edge(edge[0], edge[1])
            logger.warning("<<< Exiting __init__(vertices=%s,edges=%s,directed=%s)", vertices, edges, directed, extra={"event.action": "__init__", "logrite.vertices": vertices, "logrite.edges": edges, "logrite.directed": directed})

    def add_edge(self, source_vertex: T, destination_vertex: T) -> None:
        """
        Creates an edge from source vertex to destination vertex. If any
        given vertex doesn't exist or the edge already exists, a ValueError
        will be thrown.
        """
        logger.error(">>> Entering add_edge(source_vertex=%s,destination_vertex=%s)", source_vertex, destination_vertex, extra={"event.action": "add_edge", "logrite.source_vertex": source_vertex, "logrite.destination_vertex": destination_vertex})
        if not (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
        ):
            msg = (
                f"Incorrect input: Either {source_vertex} or "
                f"{destination_vertex} does not exist"
            )
            raise ValueError(msg)
        if self.contains_edge(source_vertex, destination_vertex):
            msg = (
                "Incorrect input: The edge already exists between "
                f"{source_vertex} and {destination_vertex}"
            )
            raise ValueError(msg)

        # Get the indices of the corresponding vertices and set their edge value to 1.
        u: int = self.vertex_to_index[source_vertex]
        v: int = self.vertex_to_index[destination_vertex]
        self.adj_matrix[u][v] = 1
        if not self.directed:
            self.adj_matrix[v][u] = 1
            logger.warning("<<< Exiting add_edge(source_vertex=%s,destination_vertex=%s)", source_vertex, destination_vertex, extra={"event.action": "add_edge", "logrite.source_vertex": source_vertex, "logrite.destination_vertex": destination_vertex})

    def remove_edge(self, source_vertex: T, destination_vertex: T) -> None:
        """
        Removes the edge between the two vertices. If any given vertex
        doesn't exist or the edge does not exist, a ValueError will be thrown.
        """
        logger.error(">>> Entering remove_edge(source_vertex=%s,destination_vertex=%s)", source_vertex, destination_vertex, extra={"event.action": "remove_edge", "logrite.source_vertex": source_vertex, "logrite.destination_vertex": destination_vertex})
        if not (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
        ):
            msg = (
                f"Incorrect input: Either {source_vertex} or "
                f"{destination_vertex} does not exist"
            )
            raise ValueError(msg)
        if not self.contains_edge(source_vertex, destination_vertex):
            msg = (
                "Incorrect input: The edge does NOT exist between "
                f"{source_vertex} and {destination_vertex}"
            )
            raise ValueError(msg)

        # Get the indices of the corresponding vertices and set their edge value to 0.
        u: int = self.vertex_to_index[source_vertex]
        v: int = self.vertex_to_index[destination_vertex]
        self.adj_matrix[u][v] = 0
        if not self.directed:
            self.adj_matrix[v][u] = 0
            logger.warning("<<< Exiting remove_edge(source_vertex=%s,destination_vertex=%s)", source_vertex, destination_vertex, extra={"event.action": "remove_edge", "logrite.source_vertex": source_vertex, "logrite.destination_vertex": destination_vertex})

    def add_vertex(self, vertex: T) -> None:
        """
        Adds a vertex to the graph. If the given vertex already exists,
        a ValueError will be thrown.
        """
        logger.error(">>> Entering add_vertex(vertex=%s)", vertex, extra={"event.action": "add_vertex", "logrite.vertex": vertex})
        if self.contains_vertex(vertex):
            msg = f"Incorrect input: {vertex} already exists in this graph."
            logger.error("add_vertex(vertex=%s): msg → %s", vertex, msg, extra={"event.action": "add_vertex", "logrite.vertex": vertex})
            raise ValueError(msg)

        # build column for vertex
        for row in self.adj_matrix:
            row.append(0)

        # build row for vertex and update other data structures
        self.adj_matrix.append([0] * (len(self.adj_matrix) + 1))
        self.vertex_to_index[vertex] = len(self.adj_matrix) - 1
        logger.warning("<<< Exiting add_vertex(vertex=%s)", vertex, extra={"event.action": "add_vertex", "logrite.vertex": vertex})

    def remove_vertex(self, vertex: T) -> None:
        """
        Removes the given vertex from the graph and deletes all incoming and
        outgoing edges from the given vertex as well. If the given vertex
        does not exist, a ValueError will be thrown.
        """
        logger.error(">>> Entering remove_vertex(vertex=%s)", vertex, extra={"event.action": "remove_vertex", "logrite.vertex": vertex})
        if not self.contains_vertex(vertex):
            msg = f"Incorrect input: {vertex} does not exist in this graph."
            logger.error("remove_vertex(vertex=%s): msg → %s", vertex, msg, extra={"event.action": "remove_vertex", "logrite.vertex": vertex})
            raise ValueError(msg)

        # first slide up the rows by deleting the row corresponding to
        # the vertex being deleted.
        start_index = self.vertex_to_index[vertex]
        self.adj_matrix.pop(start_index)

        # next, slide the columns to the left by deleting the values in
        # the column corresponding to the vertex being deleted
        for lst in self.adj_matrix:
            lst.pop(start_index)

        # final clean up
        self.vertex_to_index.pop(vertex)

        # decrement indices for vertices shifted by the deleted vertex in the adj matrix
        for inner_vertex in self.vertex_to_index:
            if self.vertex_to_index[inner_vertex] >= start_index:
                self.vertex_to_index[inner_vertex] = (
                    self.vertex_to_index[inner_vertex] - 1
                )
                logger.warning("<<< Exiting remove_vertex(vertex=%s)", vertex, extra={"event.action": "remove_vertex", "logrite.vertex": vertex})

    def contains_vertex(self, vertex: T) -> bool:
        """
        Returns True if the graph contains the vertex, False otherwise.
        """
        logger.error(">>> Entering contains_vertex(vertex=%s)", vertex, extra={"event.action": "contains_vertex", "logrite.vertex": vertex})
        logger.warning("<<< Exiting contains_vertex(vertex=%s)", vertex, extra={"event.action": "contains_vertex", "logrite.vertex": vertex})
        return vertex in self.vertex_to_index

    def contains_edge(self, source_vertex: T, destination_vertex: T) -> bool:
        """
        Returns True if the graph contains the edge from the source_vertex to the
        destination_vertex, False otherwise. If any given vertex doesn't exist, a
        ValueError will be thrown.
        """
        logger.error(">>> Entering contains_edge(source_vertex=%s,destination_vertex=%s)", source_vertex, destination_vertex, extra={"event.action": "contains_edge", "logrite.source_vertex": source_vertex, "logrite.destination_vertex": destination_vertex})
        if not (
            self.contains_vertex(source_vertex)
            and self.contains_vertex(destination_vertex)
        ):
            msg = (
                f"Incorrect input: Either {source_vertex} "
                f"or {destination_vertex} does not exist."
            )
            raise ValueError(msg)

        u = self.vertex_to_index[source_vertex]
        v = self.vertex_to_index[destination_vertex]
        logger.warning("<<< Exiting contains_edge(source_vertex=%s,destination_vertex=%s)", source_vertex, destination_vertex, extra={"event.action": "contains_edge", "logrite.source_vertex": source_vertex, "logrite.destination_vertex": destination_vertex})
        return self.adj_matrix[u][v] == 1

    def clear_graph(self) -> None:
        """
        Clears all vertices and edges.
        """
        logger.error(">>> Entering clear_graph()", extra={"event.action": "clear_graph"})
        self.vertex_to_index = {}
        logger.warning("<<< Exiting clear_graph()", extra={"event.action": "clear_graph"})
        logger.debug("clear_graph(self=%s): self.vertex_to_index → %s", self, self.vertex_to_index, extra={"event.action": "clear_graph"})
        self.adj_matrix = []
        logger.debug("clear_graph(self=%s): self.adj_matrix → %s", self, self.adj_matrix, extra={"event.action": "clear_graph"})

    def __repr__(self) -> str:
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        first = "Adj Matrix:\n" + pformat(self.adj_matrix)
        logger.error("__repr__(): first → %s", first, extra={"event.action": "__repr__"})
        second = "\nVertex to index mapping:\n" + pformat(self.vertex_to_index)
        logger.error("__repr__(): second → %s", second, extra={"event.action": "__repr__"})
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return first + second


class TestGraphMatrix(unittest.TestCase):
    def __assert_graph_edge_exists_check(
        self,
        undirected_graph: GraphAdjacencyMatrix,
        directed_graph: GraphAdjacencyMatrix,
        edge: list[int],
    ) -> None:
        assert undirected_graph.contains_edge(edge[0], edge[1])
        assert undirected_graph.contains_edge(edge[1], edge[0])
        assert directed_graph.contains_edge(edge[0], edge[1])

    def __assert_graph_edge_does_not_exist_check(
        self,
        undirected_graph: GraphAdjacencyMatrix,
        directed_graph: GraphAdjacencyMatrix,
        edge: list[int],
    ) -> None:
        logger.error(">>> Entering __assert_graph_edge_does_not_exist_check(undirected_graph=%s,directed_graph=%s,edge=%s)", undirected_graph, directed_graph, edge, extra={"event.action": "__assert_graph_edge_does_not_exist_check", "logrite.undirected_graph": undirected_graph, "logrite.directed_graph": directed_graph, "logrite.edge": edge})
        assert not undirected_graph.contains_edge(edge[0], edge[1])
        assert not undirected_graph.contains_edge(edge[1], edge[0])
        assert not directed_graph.contains_edge(edge[0], edge[1])
        logger.warning("<<< Exiting __assert_graph_edge_does_not_exist_check(undirected_graph=%s,directed_graph=%s,edge=%s)", undirected_graph, directed_graph, edge, extra={"event.action": "__assert_graph_edge_does_not_exist_check", "logrite.undirected_graph": undirected_graph, "logrite.directed_graph": directed_graph, "logrite.edge": edge})

    def __assert_graph_vertex_exists_check(
        self,
        undirected_graph: GraphAdjacencyMatrix,
        directed_graph: GraphAdjacencyMatrix,
        vertex: int,
    ) -> None:
        logger.error(">>> Entering __assert_graph_vertex_exists_check(undirected_graph=%s,directed_graph=%s,vertex=%s)", undirected_graph, directed_graph, vertex, extra={"event.action": "__assert_graph_vertex_exists_check", "logrite.undirected_graph": undirected_graph, "logrite.directed_graph": directed_graph, "logrite.vertex": vertex})
        assert undirected_graph.contains_vertex(vertex)
        assert directed_graph.contains_vertex(vertex)
        logger.warning("<<< Exiting __assert_graph_vertex_exists_check(undirected_graph=%s,directed_graph=%s,vertex=%s)", undirected_graph, directed_graph, vertex, extra={"event.action": "__assert_graph_vertex_exists_check", "logrite.undirected_graph": undirected_graph, "logrite.directed_graph": directed_graph, "logrite.vertex": vertex})

    def __assert_graph_vertex_does_not_exist_check(
        self,
        undirected_graph: GraphAdjacencyMatrix,
        directed_graph: GraphAdjacencyMatrix,
        vertex: int,
    ) -> None:
        logger.error(">>> Entering __assert_graph_vertex_does_not_exist_check(undirected_graph=%s,directed_graph=%s,vertex=%s)", undirected_graph, directed_graph, vertex, extra={"event.action": "__assert_graph_vertex_does_not_exist_check", "logrite.undirected_graph": undirected_graph, "logrite.directed_graph": directed_graph, "logrite.vertex": vertex})
        assert not undirected_graph.contains_vertex(vertex)
        assert not directed_graph.contains_vertex(vertex)
        logger.warning("<<< Exiting __assert_graph_vertex_does_not_exist_check(undirected_graph=%s,directed_graph=%s,vertex=%s)", undirected_graph, directed_graph, vertex, extra={"event.action": "__assert_graph_vertex_does_not_exist_check", "logrite.undirected_graph": undirected_graph, "logrite.directed_graph": directed_graph, "logrite.vertex": vertex})

    def __generate_random_edges(
        self, vertices: list[int], edge_pick_count: int
    ) -> list[list[int]]:
        logger.error(">>> Entering __generate_random_edges(vertices=%s,edge_pick_count=%s)", vertices, edge_pick_count, extra={"event.action": "__generate_random_edges", "logrite.vertices": vertices, "logrite.edge_pick_count": edge_pick_count})
        assert edge_pick_count <= len(vertices)

        random_source_vertices: list[int] = random.sample(
            vertices[0 : int(len(vertices) / 2)], edge_pick_count
        )
        random_destination_vertices: list[int] = random.sample(
            vertices[int(len(vertices) / 2) :], edge_pick_count
        )
        random_edges: list[list[int]] = []

        for source in random_source_vertices:
            for dest in random_destination_vertices:
                random_edges.append([source, dest])

        logger.warning("<<< Exiting __generate_random_edges(vertices=%s,edge_pick_count=%s)", vertices, edge_pick_count, extra={"event.action": "__generate_random_edges", "logrite.vertices": vertices, "logrite.edge_pick_count": edge_pick_count})
        return random_edges

    def __generate_graphs(
        self, vertex_count: int, min_val: int, max_val: int, edge_pick_count: int
    ) -> tuple[GraphAdjacencyMatrix, GraphAdjacencyMatrix, list[int], list[list[int]]]:
        logger.error(">>> Entering __generate_graphs(vertex_count=%s,min_val=%s,max_val=%s,edge_pick_count=%s)", vertex_count, min_val, max_val, edge_pick_count, extra={"event.action": "__generate_graphs", "logrite.vertex_count": vertex_count, "logrite.min_val": min_val, "logrite.max_val": max_val, "logrite.edge_pick_count": edge_pick_count})
        if max_val - min_val + 1 < vertex_count:
            raise ValueError(
                "Will result in duplicate vertices. Either increase "
                "range between min_val and max_val or decrease vertex count"
            )

        # generate graph input
        random_vertices: list[int] = random.sample(
            range(min_val, max_val + 1), vertex_count
        )
        random_edges: list[list[int]] = self.__generate_random_edges(
            random_vertices, edge_pick_count
        )

        # build graphs
        undirected_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=random_edges, directed=False
        )
        directed_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=random_edges, directed=True
        )

        logger.warning("<<< Exiting __generate_graphs(vertex_count=%s,min_val=%s,max_val=%s,edge_pick_count=%s)", vertex_count, min_val, max_val, edge_pick_count, extra={"event.action": "__generate_graphs", "logrite.vertex_count": vertex_count, "logrite.min_val": min_val, "logrite.max_val": max_val, "logrite.edge_pick_count": edge_pick_count})
        return undirected_graph, directed_graph, random_vertices, random_edges

    def test_init_check(self) -> None:
        logger.error(">>> Entering test_init_check()", extra={"event.action": "test_init_check"})
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        # test graph initialization with vertices and edges
        for num in random_vertices:
            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, num
            )

        for edge in random_edges:
            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, edge
            )

        assert not undirected_graph.directed
        assert directed_graph.directed
        logger.warning("<<< Exiting test_init_check()", extra={"event.action": "test_init_check"})

    def test_contains_vertex(self) -> None:
        logger.error(">>> Entering test_contains_vertex()", extra={"event.action": "test_contains_vertex"})
        random_vertices: list[int] = random.sample(range(101), 20)

        # Build graphs WITHOUT edges
        undirected_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=True
        )

        # Test contains_vertex
        for num in range(101):
            assert (num in random_vertices) == undirected_graph.contains_vertex(num)
            assert (num in random_vertices) == directed_graph.contains_vertex(num)
            logger.warning("<<< Exiting test_contains_vertex()", extra={"event.action": "test_contains_vertex"})

    def test_add_vertices(self) -> None:
        logger.error(">>> Entering test_add_vertices()", extra={"event.action": "test_add_vertices"})
        random_vertices: list[int] = random.sample(range(101), 20)

        # build empty graphs
        undirected_graph: GraphAdjacencyMatrix = GraphAdjacencyMatrix(
            vertices=[], edges=[], directed=False
        )
        directed_graph: GraphAdjacencyMatrix = GraphAdjacencyMatrix(
            vertices=[], edges=[], directed=True
        )

        # run add_vertex
        for num in random_vertices:
            undirected_graph.add_vertex(num)

        for num in random_vertices:
            directed_graph.add_vertex(num)

        # test add_vertex worked
        for num in random_vertices:
            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, num
            )
            logger.warning("<<< Exiting test_add_vertices()", extra={"event.action": "test_add_vertices"})

    def test_remove_vertices(self) -> None:
        logger.error(">>> Entering test_remove_vertices()", extra={"event.action": "test_remove_vertices"})
        random_vertices: list[int] = random.sample(range(101), 20)

        # build graphs WITHOUT edges
        undirected_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=True
        )

        # test remove_vertex worked
        for num in random_vertices:
            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, num
            )

            undirected_graph.remove_vertex(num)
            directed_graph.remove_vertex(num)

            self.__assert_graph_vertex_does_not_exist_check(
                undirected_graph, directed_graph, num
            )
            logger.warning("<<< Exiting test_remove_vertices()", extra={"event.action": "test_remove_vertices"})

    def test_add_and_remove_vertices_repeatedly(self) -> None:
        logger.error(">>> Entering test_add_and_remove_vertices_repeatedly()", extra={"event.action": "test_add_and_remove_vertices_repeatedly"})
        random_vertices1: list[int] = random.sample(range(51), 20)
        random_vertices2: list[int] = random.sample(range(51, 101), 20)

        # build graphs WITHOUT edges
        undirected_graph = GraphAdjacencyMatrix(
            vertices=random_vertices1, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyMatrix(
            vertices=random_vertices1, edges=[], directed=True
        )

        # test adding and removing vertices
        for i, _ in enumerate(random_vertices1):
            undirected_graph.add_vertex(random_vertices2[i])
            directed_graph.add_vertex(random_vertices2[i])

            self.__assert_graph_vertex_exists_check(
                undirected_graph, directed_graph, random_vertices2[i]
            )

            undirected_graph.remove_vertex(random_vertices1[i])
            directed_graph.remove_vertex(random_vertices1[i])

            self.__assert_graph_vertex_does_not_exist_check(
                undirected_graph, directed_graph, random_vertices1[i]
            )

        # remove all vertices
        for i, _ in enumerate(random_vertices1):
            undirected_graph.remove_vertex(random_vertices2[i])
            directed_graph.remove_vertex(random_vertices2[i])

            self.__assert_graph_vertex_does_not_exist_check(
                undirected_graph, directed_graph, random_vertices2[i]
            )
            logger.warning("<<< Exiting test_add_and_remove_vertices_repeatedly()", extra={"event.action": "test_add_and_remove_vertices_repeatedly"})

    def test_contains_edge(self) -> None:
        logger.error(">>> Entering test_contains_edge()", extra={"event.action": "test_contains_edge"})
        # generate graphs and graph input
        vertex_count = 20
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(vertex_count, 0, 100, 4)

        # generate all possible edges for testing
        all_possible_edges: list[list[int]] = []
        for i in range(vertex_count - 1):
            for j in range(i + 1, vertex_count):
                all_possible_edges.append([random_vertices[i], random_vertices[j]])
                all_possible_edges.append([random_vertices[j], random_vertices[i]])

        # test contains_edge function
        for edge in all_possible_edges:
            if edge in random_edges:
                self.__assert_graph_edge_exists_check(
                    undirected_graph, directed_graph, edge
                )
            elif [edge[1], edge[0]] in random_edges:
                # since this edge exists for undirected but the reverse may
                # not exist for directed
                self.__assert_graph_edge_exists_check(
                    undirected_graph, directed_graph, [edge[1], edge[0]]
                )
            else:
                self.__assert_graph_edge_does_not_exist_check(
                    undirected_graph, directed_graph, edge
                )
                logger.warning("<<< Exiting test_contains_edge()", extra={"event.action": "test_contains_edge"})

    def test_add_edge(self) -> None:
        logger.error(">>> Entering test_add_edge()", extra={"event.action": "test_add_edge"})
        # generate graph input
        random_vertices: list[int] = random.sample(range(101), 15)
        random_edges: list[list[int]] = self.__generate_random_edges(random_vertices, 4)

        # build graphs WITHOUT edges
        undirected_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=False
        )
        directed_graph = GraphAdjacencyMatrix(
            vertices=random_vertices, edges=[], directed=True
        )

        # run and test add_edge
        for edge in random_edges:
            undirected_graph.add_edge(edge[0], edge[1])
            directed_graph.add_edge(edge[0], edge[1])
            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, edge
            )
            logger.warning("<<< Exiting test_add_edge()", extra={"event.action": "test_add_edge"})

    def test_remove_edge(self) -> None:
        logger.error(">>> Entering test_remove_edge()", extra={"event.action": "test_remove_edge"})
        # generate graph input and graphs
        (
            undirected_graph,
            directed_graph,
            _random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        # run and test remove_edge
        for edge in random_edges:
            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, edge
            )
            undirected_graph.remove_edge(edge[0], edge[1])
            directed_graph.remove_edge(edge[0], edge[1])
            self.__assert_graph_edge_does_not_exist_check(
                undirected_graph, directed_graph, edge
            )
            logger.warning("<<< Exiting test_remove_edge()", extra={"event.action": "test_remove_edge"})

    def test_add_and_remove_edges_repeatedly(self) -> None:
        logger.error(">>> Entering test_add_and_remove_edges_repeatedly()", extra={"event.action": "test_add_and_remove_edges_repeatedly"})
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        # make some more edge options!
        more_random_edges: list[list[int]] = []

        while len(more_random_edges) != len(random_edges):
            edges: list[list[int]] = self.__generate_random_edges(random_vertices, 4)
            for edge in edges:
                if len(more_random_edges) == len(random_edges):
                    break
                elif edge not in more_random_edges and edge not in random_edges:
                    more_random_edges.append(edge)

        for i, _ in enumerate(random_edges):
            undirected_graph.add_edge(more_random_edges[i][0], more_random_edges[i][1])
            directed_graph.add_edge(more_random_edges[i][0], more_random_edges[i][1])

            self.__assert_graph_edge_exists_check(
                undirected_graph, directed_graph, more_random_edges[i]
            )

            undirected_graph.remove_edge(random_edges[i][0], random_edges[i][1])
            directed_graph.remove_edge(random_edges[i][0], random_edges[i][1])

            self.__assert_graph_edge_does_not_exist_check(
                undirected_graph, directed_graph, random_edges[i]
            )
            logger.warning("<<< Exiting test_add_and_remove_edges_repeatedly()", extra={"event.action": "test_add_and_remove_edges_repeatedly"})

    def test_add_vertex_exception_check(self) -> None:
        logger.error(">>> Entering test_add_vertex_exception_check()", extra={"event.action": "test_add_vertex_exception_check"})
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            _random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for vertex in random_vertices:
            with pytest.raises(ValueError):
                undirected_graph.add_vertex(vertex)
            with pytest.raises(ValueError):
                directed_graph.add_vertex(vertex)
                logger.warning("<<< Exiting test_add_vertex_exception_check()", extra={"event.action": "test_add_vertex_exception_check"})

    def test_remove_vertex_exception_check(self) -> None:
        logger.error(">>> Entering test_remove_vertex_exception_check()", extra={"event.action": "test_remove_vertex_exception_check"})
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            _random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for i in range(101):
            if i not in random_vertices:
                with pytest.raises(ValueError):
                    undirected_graph.remove_vertex(i)
                with pytest.raises(ValueError):
                    directed_graph.remove_vertex(i)
                    logger.warning("<<< Exiting test_remove_vertex_exception_check()", extra={"event.action": "test_remove_vertex_exception_check"})

    def test_add_edge_exception_check(self) -> None:
        logger.error(">>> Entering test_add_edge_exception_check()", extra={"event.action": "test_add_edge_exception_check"})
        (
            undirected_graph,
            directed_graph,
            _random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for edge in random_edges:
            with pytest.raises(ValueError):
                undirected_graph.add_edge(edge[0], edge[1])
            with pytest.raises(ValueError):
                directed_graph.add_edge(edge[0], edge[1])
                logger.warning("<<< Exiting test_add_edge_exception_check()", extra={"event.action": "test_add_edge_exception_check"})

    def test_remove_edge_exception_check(self) -> None:
        logger.error(">>> Entering test_remove_edge_exception_check()", extra={"event.action": "test_remove_edge_exception_check"})
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        more_random_edges: list[list[int]] = []

        while len(more_random_edges) != len(random_edges):
            edges: list[list[int]] = self.__generate_random_edges(random_vertices, 4)
            for edge in edges:
                if len(more_random_edges) == len(random_edges):
                    break
                elif edge not in more_random_edges and edge not in random_edges:
                    more_random_edges.append(edge)

        for edge in more_random_edges:
            with pytest.raises(ValueError):
                undirected_graph.remove_edge(edge[0], edge[1])
            with pytest.raises(ValueError):
                directed_graph.remove_edge(edge[0], edge[1])
                logger.warning("<<< Exiting test_remove_edge_exception_check()", extra={"event.action": "test_remove_edge_exception_check"})

    def test_contains_edge_exception_check(self) -> None:
        logger.error(">>> Entering test_contains_edge_exception_check()", extra={"event.action": "test_contains_edge_exception_check"})
        (
            undirected_graph,
            directed_graph,
            random_vertices,
            _random_edges,
        ) = self.__generate_graphs(20, 0, 100, 4)

        for vertex in random_vertices:
            with pytest.raises(ValueError):
                undirected_graph.contains_edge(vertex, 102)
            with pytest.raises(ValueError):
                directed_graph.contains_edge(vertex, 102)

        with pytest.raises(ValueError):
            undirected_graph.contains_edge(103, 102)
        with pytest.raises(ValueError):
            directed_graph.contains_edge(103, 102)
            logger.warning("<<< Exiting test_contains_edge_exception_check()", extra={"event.action": "test_contains_edge_exception_check"})


if __name__ == "__main__":
    unittest.main()
