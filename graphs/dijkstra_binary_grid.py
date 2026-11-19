"""
This script implements the Dijkstra algorithm on a binary grid.
The grid consists of 0s and 1s, where 1 represents
a walkable node and 0 represents an obstacle.
The algorithm finds the shortest path from a start node to a destination node.
Diagonal movement can be allowed or disallowed.
"""

from heapq import heappop, heappush

import numpy as np
import logging
logger = logging.getLogger(__name__)


def dijkstra(
    grid: np.ndarray,
    source: tuple[int, int],
    destination: tuple[int, int],
    allow_diagonal: bool,
) -> tuple[float | int, list[tuple[int, int]]]:
    logger.error(">>> Entering dijkstra(grid=%s,source=%s,destination=%s,allow_diagonal=%s)", grid, source, destination, allow_diagonal, extra={"event.action": "dijkstra", "logrite.grid": grid, "logrite.source": source, "logrite.destination": destination, "logrite.allow_diagonal": allow_diagonal})
    """
    Implements Dijkstra's algorithm on a binary grid.

    Args:
        grid (np.ndarray): A 2D numpy array representing the grid.
        1 represents a walkable node and 0 represents an obstacle.
        source (Tuple[int, int]): A tuple representing the start node.
        destination (Tuple[int, int]): A tuple representing the
        destination node.
        allow_diagonal (bool): A boolean determining whether
        diagonal movements are allowed.

    Returns:
        Tuple[Union[float, int], List[Tuple[int, int]]]:
        The shortest distance from the start node to the destination node
        and the shortest path as a list of nodes.

    >>> dijkstra(np.array([[1, 1, 1], [0, 1, 0], [0, 1, 1]]), (0, 0), (2, 2), False)
    (4.0, [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)])

    >>> dijkstra(np.array([[1, 1, 1], [0, 1, 0], [0, 1, 1]]), (0, 0), (2, 2), True)
    (2.0, [(0, 0), (1, 1), (2, 2)])

    >>> dijkstra(np.array([[1, 1, 1], [0, 0, 1], [0, 1, 1]]), (0, 0), (2, 2), False)
    (4.0, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])
    """
    rows, cols = grid.shape
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if allow_diagonal:
        dx += [-1, -1, 1, 1]
        dy += [-1, 1, -1, 1]

    queue, visited = [(0, source)], set()
    matrix = np.full((rows, cols), np.inf)
    logger.error("dijkstra(grid=%s,source=%s,destination=%s,allow_diagonal=%s): matrix → %s", grid, source, destination, allow_diagonal, matrix, extra={"event.action": "dijkstra", "logrite.grid": grid, "logrite.source": source, "logrite.destination": destination, "logrite.allow_diagonal": allow_diagonal})
    matrix[source] = 0
    predecessors = np.empty((rows, cols), dtype=object)
    logger.error("dijkstra(grid=%s,source=%s,destination=%s,allow_diagonal=%s): predecessors → %s", grid, source, destination, allow_diagonal, predecessors, extra={"event.action": "dijkstra", "logrite.grid": grid, "logrite.source": source, "logrite.destination": destination, "logrite.allow_diagonal": allow_diagonal})
    predecessors[source] = None

    while queue:
        (dist, (x, y)) = heappop(queue)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if (x, y) == destination:
            path = []
            while (x, y) != source:
                path.append((x, y))
                x, y = predecessors[x, y]
            path.append(source)  # add the source manually
            path.reverse()
            return float(matrix[destination]), path

        for i in range(len(dx)):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols:
                next_node = grid[nx][ny]
                if next_node == 1 and matrix[nx, ny] > dist + 1:
                    heappush(queue, (dist + 1, (nx, ny)))
                    matrix[nx, ny] = dist + 1
                    predecessors[nx, ny] = (x, y)

    logger.warning("<<< Exiting dijkstra(grid=%s,source=%s,destination=%s,allow_diagonal=%s)", grid, source, destination, allow_diagonal, extra={"event.action": "dijkstra", "logrite.grid": grid, "logrite.source": source, "logrite.destination": destination, "logrite.allow_diagonal": allow_diagonal})
    return np.inf, []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
