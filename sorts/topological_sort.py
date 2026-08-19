import logging
logger = logging.getLogger(__name__)
"""Topological Sort."""

#     a
#    / \
#   b  c
#  / \
# d  e
edges: dict[str, list[str]] = {
    "a": ["c", "b"],
    "b": ["d", "e"],
    "c": [],
    "d": [],
    "e": [],
}
vertices: list[str] = ["a", "b", "c", "d", "e"]


def topological_sort(start: str, visited: list[str], sort: list[str]) -> list[str]:
    """Perform topological sort on a directed acyclic graph."""
    current = start
    # add current to visited
    visited.append(current)
    neighbors = edges[current]
    logger.debug("topological_sort(start=%s,visited=%s,sort=%s): neighbors → %s", start, visited, sort, neighbors)
    for neighbor in neighbors:
        # if neighbor not in visited, visit
        if neighbor not in visited:
            sort = topological_sort(neighbor, visited, sort)
    # if all neighbors visited add current to sort
    sort.append(current)
    # if all vertices haven't been visited select a new one to visit
    if len(visited) != len(vertices):
        for vertice in vertices:
            if vertice not in visited:
                sort = topological_sort(vertice, visited, sort)
                logger.debug("topological_sort(start=%s,visited=%s,sort=%s): sort → %s", start, visited, sort, sort)
    # return sort
    return sort


if __name__ == "__main__":
    sort = topological_sort("a", [], [])
    print(sort)
