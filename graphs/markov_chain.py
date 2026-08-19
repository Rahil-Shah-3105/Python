from __future__ import annotations

from collections import Counter
from random import random
import logging
logger = logging.getLogger(__name__)


class MarkovChainGraphUndirectedUnweighted:
    """
    Undirected Unweighted Graph for running Markov Chain Algorithm
    """

    def __init__(self):
        logger.debug(">>> Entering __init__()")
        self.connections = {}
        logger.debug("__init__(self=%s): self.connections → %s", self, self.connections)
        logger.debug("<<< Exiting __init__()")

    def add_node(self, node: str) -> None:
        logger.debug(">>> Entering add_node(node=%s)", node)
        self.connections[node] = {}
        logger.debug("<<< Exiting add_node(node=%s)", node)

    def add_transition_probability(
        self, node1: str, node2: str, probability: float
    ) -> None:
        if node1 not in self.connections:
            self.add_node(node1)
        if node2 not in self.connections:
            self.add_node(node2)
        self.connections[node1][node2] = probability

    def get_nodes(self) -> list[str]:
        logger.debug(">>> Entering get_nodes()")
        logger.debug("<<< Exiting get_nodes()")
        return list(self.connections)

    def transition(self, node: str) -> str:
        logger.debug(">>> Entering transition(node=%s)", node)
        current_probability = 0
        logger.debug("transition(self=%s,node=%s): current_probability → %s", self, node, current_probability)
        random_value = random()
        logger.debug("transition(node=%s): random_value → %s", node, random_value)
        logger.debug("transition(self=%s,node=%s): random_value → %s", self, node, random_value)

        for dest in self.connections[node]:
            current_probability += self.connections[node][dest]
            if current_probability > random_value:
                return dest
        logger.debug("<<< Exiting transition(node=%s)", node)
        return ""


def get_transitions(
    start: str, transitions: list[tuple[str, str, float]], steps: int
) -> dict[str, int]:
    """
    Running Markov Chain algorithm and calculating the number of times each node is
    visited

    >>> transitions = [
    ... ('a', 'a', 0.9),
    ... ('a', 'b', 0.075),
    ... ('a', 'c', 0.025),
    ... ('b', 'a', 0.15),
    ... ('b', 'b', 0.8),
    ... ('b', 'c', 0.05),
    ... ('c', 'a', 0.25),
    ... ('c', 'b', 0.25),
    ... ('c', 'c', 0.5)
    ... ]

    >>> result = get_transitions('a', transitions, 5000)

    >>> result['a'] > result['b'] > result['c']
    True
    """

    graph = MarkovChainGraphUndirectedUnweighted()

    for node1, node2, probability in transitions:
        graph.add_transition_probability(node1, node2, probability)

    visited = Counter(graph.get_nodes())
    node = start

    for _ in range(steps):
        node = graph.transition(node)
        visited[node] += 1

    return visited


if __name__ == "__main__":
    import doctest

    doctest.testmod()
