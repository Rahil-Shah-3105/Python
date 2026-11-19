from __future__ import annotations

from typing import TypeVar
import logging
logger = logging.getLogger(__name__)

T = TypeVar("T")


class DisjointSetTreeNode[T]:
    # Disjoint Set Node to store the parent and rank
    def __init__(self, data: T) -> None:
        logger.error(">>> Entering __init__(data=%s)", data, extra={"event.action": "__init__"})
        self.data = data
        logger.debug("__init__(self=%s,data=%s): self.data → %s", self, data, self.data, extra={"event.action": "__init__"})
        logger.error("__init__(data=%s): self.data → %s", data, self.data, extra={"event.action": "__init__"})
        self.parent = self
        self.rank = 0
        logger.debug("__init__(self=%s,data=%s): self.rank → %s", self, data, self.rank, extra={"event.action": "__init__"})
        logger.debug("__init__(self=%s,data=%s): self.parent → %s", self, data, self.parent, extra={"event.action": "__init__"})

        logger.warning("<<< Exiting __init__(data=%s)", data, extra={"event.action": "__init__"})

class DisjointSetTree[T]:
    # Disjoint Set DataStructure
    def __init__(self) -> None:
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        # map from node name to the node object
        self.map: dict[T, DisjointSetTreeNode[T]] = {}
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})

    def make_set(self, data: T) -> None:
        logger.error(">>> Entering make_set(data=%s)", data, extra={"event.action": "make_set"})
        # create a new set with x as its member
        self.map[data] = DisjointSetTreeNode(data)
        logger.warning("<<< Exiting make_set(data=%s)", data, extra={"event.action": "make_set"})

    def find_set(self, data: T) -> DisjointSetTreeNode[T]:
        logger.error(">>> Entering find_set(data=%s)", data, extra={"event.action": "find_set"})
        # find the set x belongs to (with path-compression)
        elem_ref = self.map[data]
        if elem_ref != elem_ref.parent:
            elem_ref.parent = self.find_set(elem_ref.parent.data)
        logger.warning("<<< Exiting find_set(data=%s)", data, extra={"event.action": "find_set"})
        return elem_ref.parent

    def link(
        self, node1: DisjointSetTreeNode[T], node2: DisjointSetTreeNode[T]
    ) -> None:
        logger.error(">>> Entering link(node1=%s,node2=%s)", node1, node2, extra={"event.action": "link", "logrite.node1": node1, "logrite.node2": node2})
        # helper function for union operation
        if node1.rank > node2.rank:
            node2.parent = node1
        else:
            logger.debug("link(self=%s,node1=%s,node2=%s): node2.parent → %s", self, node1, node2, node2.parent, extra={"event.action": "link", "logrite.node1": node1, "logrite.node2": node2})
            node1.parent = node2
            logger.debug("link(self=%s,node1=%s,node2=%s): node1.parent → %s", self, node1, node2, node1.parent, extra={"event.action": "link", "logrite.node1": node1, "logrite.node2": node2})
            if node1.rank == node2.rank:
                node2.rank += 1
                logger.warning("<<< Exiting link(node1=%s,node2=%s)", node1, node2, extra={"event.action": "link", "logrite.node1": node1, "logrite.node2": node2})

    def union(self, data1: T, data2: T) -> None:
        logger.error(">>> Entering union(data1=%s,data2=%s)", data1, data2, extra={"event.action": "union", "logrite.data1": data1, "logrite.data2": data2})
        # merge 2 disjoint sets
        self.link(self.find_set(data1), self.find_set(data2))
        logger.warning("<<< Exiting union(data1=%s,data2=%s)", data1, data2, extra={"event.action": "union", "logrite.data1": data1, "logrite.data2": data2})


class GraphUndirectedWeighted[T]:
    def __init__(self) -> None:
        # connections: map from the node to the neighbouring nodes (with weights)
        self.connections: dict[T, dict[T, int]] = {}

    def add_node(self, node: T) -> None:
        logger.error(">>> Entering add_node(node=%s)", node, extra={"event.action": "add_node", "logrite.node": node})
        # add a node ONLY if its not present in the graph
        if node not in self.connections:
            self.connections[node] = {}
            logger.warning("<<< Exiting add_node(node=%s)", node, extra={"event.action": "add_node", "logrite.node": node})

    def add_edge(self, node1: T, node2: T, weight: int) -> None:
        logger.error(">>> Entering add_edge(node1=%s,node2=%s,weight=%s)", node1, node2, weight, extra={"event.action": "add_edge", "logrite.node1": node1, "logrite.node2": node2, "logrite.weight": weight})
        # add an edge with the given weight
        self.add_node(node1)
        self.add_node(node2)
        self.connections[node1][node2] = weight
        self.connections[node2][node1] = weight
        logger.warning("<<< Exiting add_edge(node1=%s,node2=%s,weight=%s)", node1, node2, weight, extra={"event.action": "add_edge", "logrite.node1": node1, "logrite.node2": node2, "logrite.weight": weight})

    def kruskal(self) -> GraphUndirectedWeighted[T]:
        logger.error(">>> Entering kruskal()", extra={"event.action": "kruskal"})
        # Kruskal's Algorithm to generate a Minimum Spanning Tree (MST) of a graph
        """
        Details: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm

        Example:
        >>> g1 = GraphUndirectedWeighted[int]()
        >>> g1.add_edge(1, 2, 1)
        >>> g1.add_edge(2, 3, 2)
        >>> g1.add_edge(3, 4, 1)
        >>> g1.add_edge(3, 5, 100) # Removed in MST
        >>> g1.add_edge(4, 5, 5)
        >>> assert 5 in g1.connections[3]
        >>> mst = g1.kruskal()
        >>> assert 5 not in mst.connections[3]

        >>> g2 = GraphUndirectedWeighted[str]()
        >>> g2.add_edge('A', 'B', 1)
        >>> g2.add_edge('B', 'C', 2)
        >>> g2.add_edge('C', 'D', 1)
        >>> g2.add_edge('C', 'E', 100) # Removed in MST
        >>> g2.add_edge('D', 'E', 5)
        >>> assert 'E' in g2.connections["C"]
        >>> mst = g2.kruskal()
        >>> assert 'E' not in mst.connections['C']
        """

        # getting the edges in ascending order of weights
        edges = []
        seen = set()
        logger.error("kruskal(): seen → %s", seen, extra={"event.action": "kruskal"})
        for start in self.connections:
            for end in self.connections[start]:
                if (start, end) not in seen:
                    seen.add((end, start))
                    edges.append((start, end, self.connections[start][end]))
        edges.sort(key=lambda x: x[2])

        # creating the disjoint set
        disjoint_set = DisjointSetTree[T]()
        logger.error("kruskal(): disjoint_set → %s", disjoint_set, extra={"event.action": "kruskal"})
        for node in self.connections:
            disjoint_set.make_set(node)

        # MST generation
        num_edges = 0
        index = 0
        graph = GraphUndirectedWeighted[T]()
        logger.error("kruskal(): graph → %s", graph, extra={"event.action": "kruskal"})
        while num_edges < len(self.connections) - 1:
            u, v, w = edges[index]
            index += 1
            parent_u = disjoint_set.find_set(u)
            logger.error("kruskal(): parent_u → %s", parent_u, extra={"event.action": "kruskal"})
            parent_v = disjoint_set.find_set(v)
            logger.error("kruskal(): parent_v → %s", parent_v, extra={"event.action": "kruskal"})
            if parent_u != parent_v:
                num_edges += 1
                graph.add_edge(u, v, w)
                disjoint_set.union(u, v)
        logger.warning("<<< Exiting kruskal()", extra={"event.action": "kruskal"})
        return graph
