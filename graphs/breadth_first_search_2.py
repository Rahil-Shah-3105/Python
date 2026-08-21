"""
https://en.wikipedia.org/wiki/Breadth-first_search
pseudo-code:
breadth_first_search(graph G, start vertex s):
// all nodes initially unexplored
mark s as explored
let Q = queue data structure, initialized with s
while Q is non-empty:
    remove the first node of Q, call it v
    for each edge(v, w):  // for w in graph[v]
        if w unexplored:
            mark w as explored
            add w to Q (at the end)
"""

from __future__ import annotations

from collections import deque
from queue import Queue
from timeit import timeit
import logging
logger = logging.getLogger(__name__)

G = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}


def breadth_first_search(graph: dict, start: str) -> list[str]:
    """
    Implementation of breadth first search using queue.Queue.

    >>> ''.join(breadth_first_search(G, 'A'))
    'ABCDEF'
    """
    explored = {start}
    result = [start]
    queue: Queue = Queue()
    logger.debug("breadth_first_search(graph=%s,start=%s): queue → %s", graph, start, queue)
    queue.put(start)
    while not queue.empty():
        v = queue.get()
        logger.debug("breadth_first_search(graph=%s,start=%s): v → %s", graph, start, v)
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                result.append(w)
                queue.put(w)
    return result


def breadth_first_search_with_deque(graph: dict, start: str) -> list[str]:
    """
    Implementation of breadth first search using collection.queue.

    >>> ''.join(breadth_first_search_with_deque(G, 'A'))
    'ABCDEF'
    """
    visited = {start}
    result = [start]
    queue = deque([start])
    logger.debug("breadth_first_search_with_deque(graph=%s,start=%s): queue → %s", graph, start, queue)
    while queue:
        v = queue.popleft()
        logger.debug("breadth_first_search_with_deque(graph=%s,start=%s): v → %s", graph, start, v)
        for child in graph[v]:
            if child not in visited:
                visited.add(child)
                result.append(child)
                queue.append(child)
    return result


def benchmark_function(name: str) -> None:
    logger.debug(">>> Entering benchmark_function(name=%s)", name)
    setup = f"from __main__ import G, {name}"
    logger.debug("benchmark_function(name=%s): setup → %s", name, setup)
    number = 10000
    res = timeit(f"{name}(G, 'A')", setup=setup, number=number)
    logger.debug("benchmark_function(name=%s): number → %s", name, number)
    logger.debug("benchmark_function(name=%s): res → %s", name, res)
    print(f"{name:<35} finished {number} runs in {res:.5f} seconds")
    logger.debug("<<< Exiting benchmark_function(name=%s)", name)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    benchmark_function("breadth_first_search")
    benchmark_function("breadth_first_search_with_deque")
    # breadth_first_search                finished 10000 runs in 0.20999 seconds
    # breadth_first_search_with_deque     finished 10000 runs in 0.01421 seconds
