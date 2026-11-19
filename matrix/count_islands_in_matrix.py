import logging
logger = logging.getLogger(__name__)
# An island in matrix is a group of linked areas, all having the same value.
# This code counts number of islands in a given matrix, with including diagonal
# connections.


class Matrix:  # Public class to implement a graph
    def __init__(self, row: int, col: int, graph: list[list[bool]]) -> None:
        logger.error(">>> Entering __init__(row=%s,col=%s,graph=%s)", row, col, graph, extra={"event.action": "__init__", "logrite.row": row, "logrite.col": col, "logrite.graph": graph})
        self.ROW = row
        logger.debug("__init__(self=%s,row=%s,col=%s,graph=%s): self.ROW → %s", self, row, col, graph, self.ROW, extra={"event.action": "__init__", "logrite.row": row, "logrite.col": col, "logrite.graph": graph})
        self.COL = col
        logger.debug("__init__(self=%s,row=%s,col=%s,graph=%s): self.COL → %s", self, row, col, graph, self.COL, extra={"event.action": "__init__", "logrite.row": row, "logrite.col": col, "logrite.graph": graph})
        self.graph = graph
        logger.warning("<<< Exiting __init__(row=%s,col=%s,graph=%s)", row, col, graph, extra={"event.action": "__init__", "logrite.row": row, "logrite.col": col, "logrite.graph": graph})
        logger.debug("__init__(self=%s,row=%s,col=%s,graph=%s): self.graph → %s", self, row, col, graph, self.graph, extra={"event.action": "__init__", "logrite.row": row, "logrite.col": col, "logrite.graph": graph})

    def is_safe(self, i: int, j: int, visited: list[list[bool]]) -> bool:
        logger.error(">>> Entering is_safe(i=%s,j=%s,visited=%s)", i, j, visited, extra={"event.action": "is_safe", "logrite.i": i, "logrite.j": j, "logrite.visited": visited})
        logger.warning("<<< Exiting is_safe(i=%s,j=%s,visited=%s)", i, j, visited, extra={"event.action": "is_safe", "logrite.i": i, "logrite.j": j, "logrite.visited": visited})
        return (
            0 <= i < self.ROW
            and 0 <= j < self.COL
            and not visited[i][j]
            and self.graph[i][j]
        )

    def diffs(self, i: int, j: int, visited: list[list[bool]]) -> None:
        logger.error(">>> Entering diffs(i=%s,j=%s,visited=%s)", i, j, visited, extra={"event.action": "diffs", "logrite.i": i, "logrite.j": j, "logrite.visited": visited})
        # Checking all 8 elements surrounding nth element
        row_nbr = [-1, -1, -1, 0, 0, 1, 1, 1]  # Coordinate order
        col_nbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[i][j] = True  # Make those cells visited
        for k in range(8):
            if self.is_safe(i + row_nbr[k], j + col_nbr[k], visited):
                self.diffs(i + row_nbr[k], j + col_nbr[k], visited)
                logger.warning("<<< Exiting diffs(i=%s,j=%s,visited=%s)", i, j, visited, extra={"event.action": "diffs", "logrite.i": i, "logrite.j": j, "logrite.visited": visited})

    def count_islands(self) -> int:  # And finally, count all islands.
        logger.error(">>> Entering count_islands()", extra={"event.action": "count_islands"})
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
        logger.error("count_islands(): visited → %s", visited, extra={"event.action": "count_islands"})
        count = 0
        logger.error("count_islands(): count → %s", count, extra={"event.action": "count_islands"})
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j] is False and self.graph[i][j] == 1:
                    self.diffs(i, j, visited)
                    count += 1
        logger.warning("<<< Exiting count_islands()", extra={"event.action": "count_islands"})
        return count
