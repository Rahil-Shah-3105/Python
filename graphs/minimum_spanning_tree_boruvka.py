import logging
logger = logging.getLogger(__name__)
class Graph:
    """
    Data structure to store graphs (based on adjacency lists)
    """

    def __init__(self):
        logger.debug(">>> Entering __init__()")
        self.num_vertices = 0
        logger.debug("__init__(self=%s): self.num_vertices → %s", self, self.num_vertices)
        self.num_edges = 0
        logger.debug("__init__(self=%s): self.num_edges → %s", self, self.num_edges)
        self.adjacency = {}
        logger.debug("__init__(self=%s): self.adjacency → %s", self, self.adjacency)
        logger.debug("<<< Exiting __init__()")

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph

        """
        logger.debug(">>> Entering add_vertex(vertex=%s)", vertex)
        if vertex not in self.adjacency:
            self.adjacency[vertex] = {}
            self.num_vertices += 1
            logger.debug("<<< Exiting add_vertex(vertex=%s)", vertex)

    def add_edge(self, head, tail, weight):
        """
        Adds an edge to the graph

        """
        logger.debug(">>> Entering add_edge(head=%s,tail=%s,weight=%s)", head, tail, weight)

        self.add_vertex(head)
        self.add_vertex(tail)

        if head == tail:
            logger.debug("<<< Exiting add_edge(head=%s,tail=%s,weight=%s)", head, tail, weight)
            return

        self.adjacency[head][tail] = weight
        self.adjacency[tail][head] = weight

    def distinct_weight(self):
        """
        For Boruvks's algorithm the weights should be distinct
        Converts the weights to be distinct

        """
        logger.debug(">>> Entering distinct_weight()")
        edges = self.get_edges()
        logger.debug("distinct_weight(self=%s): edges → %s", self, edges)
        logger.debug("distinct_weight(): edges → %s", edges)
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
            logger.debug("<<< Exiting distinct_weight()")

    def __str__(self):
        """
        Returns string representation of the graph
        """
        logger.debug(">>> Entering __str__()")
        string = ""
        logger.debug("__str__(): string → %s", string)
        for tail in self.adjacency:
            for head in self.adjacency[tail]:
                weight = self.adjacency[head][tail]
                logger.debug("__str__(self=%s): weight → %s", self, weight)
                string += f"{head} -> {tail} == {weight}\n"
        logger.debug("<<< Exiting __str__()")
        return string.rstrip("\n")

    def get_edges(self):
        """
        Returna all edges in the graph
        """
        logger.debug(">>> Entering get_edges()")
        output = []
        logger.debug("get_edges(self=%s): output → %s", self, output)
        for tail in self.adjacency:
            for head in self.adjacency[tail]:
                output.append((tail, head, self.adjacency[head][tail]))
        logger.debug("<<< Exiting get_edges()")
        return output

    def get_vertices(self):
        """
        Returns all vertices in the graph
        """
        logger.debug(">>> Entering get_vertices()")
        logger.debug("<<< Exiting get_vertices()")
        return self.adjacency.keys()

    @staticmethod
    def build(vertices=None, edges=None):
        """
        Builds a graph from the given set of vertices and edges

        """
        logger.debug(">>> Entering build(vertices=%s,edges=%s)", vertices, edges)
        g = Graph()
        logger.debug("build(vertices=%s,edges=%s): g → %s", vertices, edges, g)
        if vertices is None:
            vertices = []
        if edges is None:
            edge = []
            logger.debug("build(vertices=%s,edges=%s): edge → %s", vertices, edges, edge)
        for vertex in vertices:
            g.add_vertex(vertex)
        for edge in edges:
            g.add_edge(*edge)
        logger.debug("<<< Exiting build(vertices=%s,edges=%s)", vertices, edges)
        return g

    class UnionFind:
        """
        Disjoint set Union and Find for Boruvka's algorithm
        """

        def __init__(self):
            self.parent = {}
            self.rank = {}

        def __len__(self):
            logger.debug(">>> Entering __len__()")
            logger.debug("<<< Exiting __len__()")
            return len(self.parent)

        def make_set(self, item):
            logger.debug(">>> Entering make_set(item=%s)", item)
            if item in self.parent:
                return self.find(item)

            self.parent[item] = item
            self.rank[item] = 0
            logger.debug("<<< Exiting make_set(item=%s)", item)
            return item

        def find(self, item):
            logger.debug(">>> Entering find(item=%s)", item)
            if item not in self.parent:
                return self.make_set(item)
            if item != self.parent[item]:
                self.parent[item] = self.find(self.parent[item])
            logger.debug("<<< Exiting find(item=%s)", item)
            return self.parent[item]

        def union(self, item1, item2):
            logger.debug(">>> Entering union(item1=%s,item2=%s)", item1, item2)
            root1 = self.find(item1)
            logger.debug("union(item1=%s,item2=%s): root1 → %s", item1, item2, root1)
            root2 = self.find(item2)
            logger.debug("union(item1=%s,item2=%s): root2 → %s", item1, item2, root2)
            logger.debug("union(self=%s,item1=%s,item2=%s): root2 → %s", self, item1, item2, root2)

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
            logger.debug("<<< Exiting union(item1=%s,item2=%s)", item1, item2)
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
        logger.debug(">>> Entering boruvka_mst(graph=%s)", graph)
        num_components = graph.num_vertices
        logger.debug("boruvka_mst(graph=%s): num_components → %s", graph, num_components)

        union_find = Graph.UnionFind()
        logger.debug("boruvka_mst(graph=%s): union_find → %s", graph, union_find)
        mst_edges = []
        logger.debug("boruvka_mst(graph=%s): mst_edges → %s", graph, mst_edges)
        while num_components > 1:
            cheap_edge = {}
            logger.debug("boruvka_mst(graph=%s): cheap_edge → %s", graph, cheap_edge)
            for vertex in graph.get_vertices():
                cheap_edge[vertex] = -1

            edges = graph.get_edges()
            logger.debug("boruvka_mst(graph=%s): edges → %s", graph, edges)
            for edge in edges:
                head, tail, weight = edge
                edges.remove((tail, head, weight))
            for edge in edges:
                head, tail, weight = edge
                set1 = union_find.find(head)
                logger.debug("boruvka_mst(graph=%s): set1 → %s", graph, set1)
                set2 = union_find.find(tail)
                logger.debug("boruvka_mst(graph=%s): set2 → %s", graph, set2)
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
        logger.debug("boruvka_mst(graph=%s): mst → %s", graph, mst)
        logger.debug("<<< Exiting boruvka_mst(graph=%s)", graph)
        return mst
