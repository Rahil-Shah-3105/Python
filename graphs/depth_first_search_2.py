import logging
logger = logging.getLogger(__name__)
#!/usr/bin/python

"""Author: OMKAR PATHAK"""


class Graph:
    def __init__(self):
        logger.debug(">>> Entering __init__()")
        self.vertex = {}
        logger.debug("__init__(self=%s): self.vertex → %s", self, self.vertex)
        logger.debug("<<< Exiting __init__()")

    # for printing the Graph vertices
    def print_graph(self) -> None:
        """
        Print the graph vertices.

        Example:
        >>> g = Graph()
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(2, 0)
        >>> g.add_edge(2, 3)
        >>> g.add_edge(3, 3)
        >>> g.print_graph()
        {0: [1, 2], 1: [2], 2: [0, 3], 3: [3]}
        0  ->  1 -> 2
        1  ->  2
        2  ->  0 -> 3
        3  ->  3
        """
        logger.debug(">>> Entering print_graph()")
        print(self.vertex)
        for i in self.vertex:
            print(i, " -> ", " -> ".join([str(j) for j in self.vertex[i]]))
            logger.debug("<<< Exiting print_graph()")

    # for adding the edge between two vertices
    def add_edge(self, from_vertex: int, to_vertex: int) -> None:
        """
        Add an edge between two vertices.

        :param from_vertex: The source vertex.
        :param to_vertex: The destination vertex.

        Example:
        >>> g = Graph()
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.print_graph()
        {0: [1, 2]}
        0  ->  1 -> 2
        """
        logger.debug(">>> Entering add_edge(from_vertex=%s,to_vertex=%s)", from_vertex, to_vertex)
        # check if vertex is already present,
        if from_vertex in self.vertex:
            self.vertex[from_vertex].append(to_vertex)
        else:
            # else make a new vertex
            self.vertex[from_vertex] = [to_vertex]
            logger.debug("<<< Exiting add_edge(from_vertex=%s,to_vertex=%s)", from_vertex, to_vertex)

    def dfs(self) -> None:
        """
        Perform depth-first search (DFS) traversal on the graph
        and print the visited vertices.

        Example:
        >>> g = Graph()
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(2, 0)
        >>> g.add_edge(2, 3)
        >>> g.add_edge(3, 3)
        >>> g.dfs()
        0 1 2 3
        """
        logger.debug(">>> Entering dfs()")
        # visited array for storing already visited nodes
        visited = [False] * len(self.vertex)
        logger.debug("dfs(self=%s): visited → %s", self, visited)

        # call the recursive helper function
        for i in range(len(self.vertex)):
            if not visited[i]:
                self.dfs_recursive(i, visited)
                logger.debug("<<< Exiting dfs()")

    def dfs_recursive(self, start_vertex: int, visited: list) -> None:
        """
        Perform a recursive depth-first search (DFS) traversal on the graph.

        :param start_vertex: The starting vertex for the traversal.
        :param visited: A list to track visited vertices.

        Example:
        >>> g = Graph()
        >>> g.add_edge(0, 1)
        >>> g.add_edge(0, 2)
        >>> g.add_edge(1, 2)
        >>> g.add_edge(2, 0)
        >>> g.add_edge(2, 3)
        >>> g.add_edge(3, 3)
        >>> visited = [False] * len(g.vertex)
        >>> g.dfs_recursive(0, visited)
        0 1 2 3
        """
        logger.debug(">>> Entering dfs_recursive(start_vertex=%s,visited=%s)", start_vertex, visited)
        # mark start vertex as visited
        visited[start_vertex] = True

        print(start_vertex, end="")

        # Recur for all the vertices that are adjacent to this node
        for i in self.vertex:
            if not visited[i]:
                print(" ", end="")
                self.dfs_recursive(i, visited)
                logger.debug("<<< Exiting dfs_recursive(start_vertex=%s,visited=%s)", start_vertex, visited)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.print_graph()
    print("DFS:")
    g.dfs()
