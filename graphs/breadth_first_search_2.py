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
    logger.error(">>> Entering breadth_first_search(graph=%s,start=%s)", graph, start, extra={"event.action": "breadth_first_search", "logrite.graph": graph, "logrite.start": start})
    explored = {start}
    result = [start]
    logger.error("breadth_first_search(graph=%s,start=%s): result → %s", graph, start, result, extra={"event.action": "breadth_first_search", "logrite.graph": graph, "logrite.start": start})
    queue: Queue = Queue()
    logger.error("breadth_first_search(graph=%s,start=%s): queue → %s", graph, start, queue, extra={"event.action": "breadth_first_search", "logrite.graph": graph, "logrite.start": start})
    queue.put(start)
    while not queue.empty():
        v = queue.get()
        logger.error("breadth_first_search(graph=%s,start=%s): v → %s", graph, start, v, extra={"event.action": "breadth_first_search", "logrite.graph": graph, "logrite.start": start})
        for w in graph[v]:
            if w not in explored:
                explored.add(w)
                result.append(w)
                queue.put(w)
    logger.warning("<<< Exiting breadth_first_search(graph=%s,start=%s)", graph, start, extra={"event.action": "breadth_first_search", "logrite.graph": graph, "logrite.start": start})
    return result


def breadth_first_search_with_deque(graph: dict, start: str) -> list[str]:
    """
    Implementation of breadth first search using collection.queue.

    >>> ''.join(breadth_first_search_with_deque(G, 'A'))
    'ABCDEF'
    """
    logger.error(">>> Entering breadth_first_search_with_deque(graph=%s,start=%s)", graph, start, extra={"event.action": "breadth_first_search_with_deque", "logrite.graph": graph, "logrite.start": start})
    visited = {start}
    result = [start]
    logger.error("breadth_first_search_with_deque(graph=%s,start=%s): result → %s", graph, start, result, extra={"event.action": "breadth_first_search_with_deque", "logrite.graph": graph, "logrite.start": start})
    queue = deque([start])
    logger.error("breadth_first_search_with_deque(graph=%s,start=%s): queue → %s", graph, start, queue, extra={"event.action": "breadth_first_search_with_deque", "logrite.graph": graph, "logrite.start": start})
    while queue:
        v = queue.popleft()
        logger.error("breadth_first_search_with_deque(graph=%s,start=%s): v → %s", graph, start, v, extra={"event.action": "breadth_first_search_with_deque", "logrite.graph": graph, "logrite.start": start})
        for child in graph[v]:
            if child not in visited:
                visited.add(child)
                result.append(child)
                queue.append(child)
    logger.warning("<<< Exiting breadth_first_search_with_deque(graph=%s,start=%s)", graph, start, extra={"event.action": "breadth_first_search_with_deque", "logrite.graph": graph, "logrite.start": start})
    return result


def benchmark_function(name: str) -> None:
    logger.error(">>> Entering benchmark_function(name=%s)", name, extra={"event.action": "benchmark_function", "logrite.name": name})
    setup = f"from __main__ import G, {name}"
    logger.error("benchmark_function(name=%s): setup → %s", name, setup, extra={"event.action": "benchmark_function", "logrite.name": name})
    number = 10000
    res = timeit(f"{name}(G, 'A')", setup=setup, number=number)
    logger.error("benchmark_function(name=%s): res → %s", name, res, extra={"event.action": "benchmark_function", "logrite.name": name})
    print(f"{name:<35} finished {number} runs in {res:.5f} seconds")
    logger.warning("<<< Exiting benchmark_function(name=%s)", name, extra={"event.action": "benchmark_function", "logrite.name": name})


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    benchmark_function("breadth_first_search")
    benchmark_function("breadth_first_search_with_deque")
    # breadth_first_search                finished 10000 runs in 0.20999 seconds
    # breadth_first_search_with_deque     finished 10000 runs in 0.01421 seconds
