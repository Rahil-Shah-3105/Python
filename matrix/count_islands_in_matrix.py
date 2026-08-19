import logging
logger = logging.getLogger(__name__)
# An island in matrix is a group of linked areas, all having the same value.
# This code counts number of islands in a given matrix, with including diagonal
# connections.


class Matrix:  # Public class to implement a graph
    def __init__(self, row: int, col: int, graph: list[list[bool]]) -> None:
        logger.debug(">>> Entering __init__(row=%s,col=%s,graph=%s)", row, col, graph)
        self.ROW = row
        logger.debug("__init__(self=%s,row=%s,col=%s,graph=%s): self.ROW → %s", self, row, col, graph, self.ROW)
        self.COL = col
        logger.debug("__init__(self=%s,row=%s,col=%s,graph=%s): self.COL → %s", self, row, col, graph, self.COL)
        self.graph = graph
        logger.debug("__init__(self=%s,row=%s,col=%s,graph=%s): self.graph → %s", self, row, col, graph, self.graph)
        logger.debug("<<< Exiting __init__(row=%s,col=%s,graph=%s)", row, col, graph)

    def is_safe(self, i: int, j: int, visited: list[list[bool]]) -> bool:
        logger.debug(">>> Entering is_safe(i=%s,j=%s,visited=%s)", i, j, visited)
        logger.debug("<<< Exiting is_safe(i=%s,j=%s,visited=%s)", i, j, visited)
        return (
            0 <= i < self.ROW
            and 0 <= j < self.COL
            and not visited[i][j]
            and self.graph[i][j]
        )

    def diffs(self, i: int, j: int, visited: list[list[bool]]) -> None:
        logger.debug(">>> Entering diffs(i=%s,j=%s,visited=%s)", i, j, visited)
        # Checking all 8 elements surrounding nth element
        row_nbr = [-1, -1, -1, 0, 0, 1, 1, 1]  # Coordinate order
        logger.debug("diffs(self=%s,i=%s,j=%s,visited=%s): row_nbr → %s", self, i, j, visited, row_nbr)
        col_nbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        logger.debug("diffs(self=%s,i=%s,j=%s,visited=%s): col_nbr → %s", self, i, j, visited, col_nbr)
        visited[i][j] = True  # Make those cells visited
        for k in range(8):
            if self.is_safe(i + row_nbr[k], j + col_nbr[k], visited):
                self.diffs(i + row_nbr[k], j + col_nbr[k], visited)
                logger.debug("<<< Exiting diffs(i=%s,j=%s,visited=%s)", i, j, visited)

    def count_islands(self) -> int:  # And finally, count all islands.
        logger.debug(">>> Entering count_islands()")
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
        logger.debug("count_islands(): visited → %s", visited)
        logger.debug("count_islands(self=%s): visited → %s", self, visited)
        count = 0
        logger.debug("count_islands(): count → %s", count)
        logger.debug("count_islands(self=%s): count → %s", self, count)
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j] is False and self.graph[i][j] == 1:
                    self.diffs(i, j, visited)
                    count += 1
        logger.debug("<<< Exiting count_islands()")
        return count
