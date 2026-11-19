import logging
logger = logging.getLogger(__name__)
class Graph:
    """
    Data structure to store graphs (based on adjacency lists)
    """

    def __init__(self):
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.num_vertices = 0
        logger.debug("__init__(self=%s): self.num_vertices → %s", self, self.num_vertices, extra={"event.action": "__init__"})
        self.num_edges = 0
        logger.debug("__init__(self=%s): self.num_edges → %s", self, self.num_edges, extra={"event.action": "__init__"})
        self.adjacency = {}
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})
        logger.debug("__init__(self=%s): self.adjacency → %s", self, self.adjacency, extra={"event.action": "__init__"})

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph

        """
        logger.error(">>> Entering add_vertex(vertex=%s)", vertex, extra={"event.action": "add_vertex", "logrite.vertex": vertex})
        if vertex not in self.adjacency:
            self.adjacency[vertex] = {}
            self.num_vertices += 1
            logger.warning("<<< Exiting add_vertex(vertex=%s)", vertex, extra={"event.action": "add_vertex", "logrite.vertex": vertex})

    def add_edge(self, head, tail, weight):
        """
        Adds an edge to the graph

        """
        logger.error(">>> Entering add_edge(head=%s,tail=%s,weight=%s)", head, tail, weight, extra={"event.action": "add_edge", "logrite.head": head, "logrite.tail": tail, "logrite.weight": weight})

        self.add_vertex(head)
        self.add_vertex(tail)

        if head == tail:
            logger.warning("<<< Exiting add_edge(head=%s,tail=%s,weight=%s)", head, tail, weight, extra={"event.action": "add_edge", "logrite.head": head, "logrite.tail": tail, "logrite.weight": weight})
            return

        self.adjacency[head][tail] = weight
        self.adjacency[tail][head] = weight

    def distinct_weight(self):
        """
        For Boruvks's algorithm the weights should be distinct
        Converts the weights to be distinct

        """
        logger.error(">>> Entering distinct_weight()", extra={"event.action": "distinct_weight"})
        edges = self.get_edges()
        logger.error("distinct_weight(): edges → %s", edges, extra={"event.action": "distinct_weight"})
        for edge in edges:
            head, tail, weight = edge
            edges.remove((tail, head, weight))
        for i in range(len(edges)):
            edges[i] = list(edges[i])

        edges.sort(key=lambda e: e[2])
        for i in range(len(edges) - 1):
            if edges[i][2] >= edges[i + 1][2]:
                edges[i + 1][2] = edges[i][2] + 1
        for edge in edges:
            head, tail, weight = edge
            self.adjacency[head][tail] = weight
            self.adjacency[tail][head] = weight
            logger.warning("<<< Exiting distinct_weight()", extra={"event.action": "distinct_weight"})

    def __str__(self):
        """
        Returns string representation of the graph
        """
        logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
        string = ""
        logger.error("__str__(): string → %s", string, extra={"event.action": "__str__"})
        for tail in self.adjacency:
            for head in self.adjacency[tail]:
                weight = self.adjacency[head][tail]
                string += f"{head} -> {tail} == {weight}\n"
        logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
        return string.rstrip("\n")

    def get_edges(self):
        """
        Returna all edges in the graph
        """
        logger.error(">>> Entering get_edges()", extra={"event.action": "get_edges"})
        output = []
        for tail in self.adjacency:
            for head in self.adjacency[tail]:
                output.append((tail, head, self.adjacency[head][tail]))
        logger.warning("<<< Exiting get_edges()", extra={"event.action": "get_edges"})
        return output

    def get_vertices(self):
        """
        Returns all vertices in the graph
        """
        logger.error(">>> Entering get_vertices()", extra={"event.action": "get_vertices"})
        logger.warning("<<< Exiting get_vertices()", extra={"event.action": "get_vertices"})
        return self.adjacency.keys()

    @staticmethod
    def build(vertices=None, edges=None):
        """
        Builds a graph from the given set of vertices and edges

        """
        logger.error(">>> Entering build(vertices=%s,edges=%s)", vertices, edges, extra={"event.action": "build", "logrite.vertices": vertices, "logrite.edges": edges})
        g = Graph()
        logger.error("build(vertices=%s,edges=%s): g → %s", vertices, edges, g, extra={"event.action": "build", "logrite.vertices": vertices, "logrite.edges": edges})
        if vertices is None:
            vertices = []
        if edges is None:
            edge = []
        for vertex in vertices:
            g.add_vertex(vertex)
        for edge in edges:
            g.add_edge(*edge)
        logger.warning("<<< Exiting build(vertices=%s,edges=%s)", vertices, edges, extra={"event.action": "build", "logrite.vertices": vertices, "logrite.edges": edges})
        return g

    class UnionFind:
        """
        Disjoint set Union and Find for Boruvka's algorithm
        """

        def __init__(self):
            self.parent = {}
            logger.debug("__init__(self=%s): self.parent → %s", self, self.parent, extra={"event.action": "__init__"})
            self.rank = {}
            logger.debug("__init__(self=%s): self.rank → %s", self, self.rank, extra={"event.action": "__init__"})

        def __len__(self):
            logger.error(">>> Entering __len__()", extra={"event.action": "__len__"})
            logger.warning("<<< Exiting __len__()", extra={"event.action": "__len__"})
            return len(self.parent)

        def make_set(self, item):
            logger.error(">>> Entering make_set(item=%s)", item, extra={"event.action": "make_set", "logrite.item": item})
            if item in self.parent:
                return self.find(item)

            self.parent[item] = item
            self.rank[item] = 0
            logger.warning("<<< Exiting make_set(item=%s)", item, extra={"event.action": "make_set", "logrite.item": item})
            return item

        def find(self, item):
            logger.error(">>> Entering find(item=%s)", item, extra={"event.action": "find", "logrite.item": item})
            if item not in self.parent:
                return self.make_set(item)
            if item != self.parent[item]:
                self.parent[item] = self.find(self.parent[item])
            logger.warning("<<< Exiting find(item=%s)", item, extra={"event.action": "find", "logrite.item": item})
            return self.parent[item]

        def union(self, item1, item2):
            logger.error(">>> Entering union(item1=%s,item2=%s)", item1, item2, extra={"event.action": "union", "logrite.item1": item1, "logrite.item2": item2})
            root1 = self.find(item1)
            logger.error("union(item1=%s,item2=%s): root1 → %s", item1, item2, root1, extra={"event.action": "union", "logrite.item1": item1, "logrite.item2": item2})
            root2 = self.find(item2)
            logger.error("union(item1=%s,item2=%s): root2 → %s", item1, item2, root2, extra={"event.action": "union", "logrite.item1": item1, "logrite.item2": item2})

            if root1 == root2:
                return root1

            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
                return root1

            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
                return root2

            if self.rank[root1] == self.rank[root2]:
                self.rank[root1] += 1
                self.parent[root2] = root1
                return root1
            logger.warning("<<< Exiting union(item1=%s,item2=%s)", item1, item2, extra={"event.action": "union", "logrite.item1": item1, "logrite.item2": item2})
            return None

    @staticmethod
    def boruvka_mst(graph):
        """
        Implementation of Boruvka's algorithm
        >>> g = Graph()
        >>> g = Graph.build([0, 1, 2, 3], [[0, 1, 1], [0, 2, 1],[2, 3, 1]])
        >>> g.distinct_weight()
        >>> bg = Graph.boruvka_mst(g)
        >>> print(bg)
        1 -> 0 == 1
        2 -> 0 == 2
        0 -> 1 == 1
        0 -> 2 == 2
        3 -> 2 == 3
        2 -> 3 == 3
        """
        logger.error(">>> Entering boruvka_mst(graph=%s)", graph, extra={"event.action": "boruvka_mst", "logrite.graph": graph})
        num_components = graph.num_vertices

        union_find = Graph.UnionFind()
        logger.error("boruvka_mst(graph=%s): union_find → %s", graph, union_find, extra={"event.action": "boruvka_mst", "logrite.graph": graph})
        mst_edges = []
        while num_components > 1:
            cheap_edge = {}
            for vertex in graph.get_vertices():
                cheap_edge[vertex] = -1

            edges = graph.get_edges()
            logger.error("boruvka_mst(graph=%s): edges → %s", graph, edges, extra={"event.action": "boruvka_mst", "logrite.graph": graph})
            for edge in edges:
                head, tail, weight = edge
                edges.remove((tail, head, weight))
            for edge in edges:
                head, tail, weight = edge
                set1 = union_find.find(head)
                logger.error("boruvka_mst(graph=%s): set1 → %s", graph, set1, extra={"event.action": "boruvka_mst", "logrite.graph": graph})
                set2 = union_find.find(tail)
                logger.error("boruvka_mst(graph=%s): set2 → %s", graph, set2, extra={"event.action": "boruvka_mst", "logrite.graph": graph})
                if set1 != set2:
                    if cheap_edge[set1] == -1 or cheap_edge[set1][2] > weight:
                        cheap_edge[set1] = [head, tail, weight]

                    if cheap_edge[set2] == -1 or cheap_edge[set2][2] > weight:
                        cheap_edge[set2] = [head, tail, weight]
            for head_tail_weight in cheap_edge.values():
                if head_tail_weight != -1:
                    head, tail, weight = head_tail_weight
                    if union_find.find(head) != union_find.find(tail):
                        union_find.union(head, tail)
                        mst_edges.append(head_tail_weight)
                        num_components = num_components - 1
        mst = Graph.build(edges=mst_edges)
        logger.error("boruvka_mst(graph=%s): mst → %s", graph, mst, extra={"event.action": "boruvka_mst", "logrite.graph": graph})
        logger.warning("<<< Exiting boruvka_mst(graph=%s)", graph, extra={"event.action": "boruvka_mst", "logrite.graph": graph})
        return mst
