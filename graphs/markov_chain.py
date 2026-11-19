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
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.connections = {}
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})
        logger.debug("__init__(self=%s): self.connections → %s", self, self.connections, extra={"event.action": "__init__"})

    def add_node(self, node: str) -> None:
        logger.error(">>> Entering add_node(node=%s)", node, extra={"event.action": "add_node", "logrite.node": node})
        self.connections[node] = {}
        logger.warning("<<< Exiting add_node(node=%s)", node, extra={"event.action": "add_node", "logrite.node": node})

    def add_transition_probability(
        self, node1: str, node2: str, probability: float
    ) -> None:
        logger.error(">>> Entering add_transition_probability(node1=%s,node2=%s,probability=%s)", node1, node2, probability, extra={"event.action": "add_transition_probability", "logrite.node1": node1, "logrite.node2": node2, "logrite.probability": probability})
        if node1 not in self.connections:
            self.add_node(node1)
        if node2 not in self.connections:
            self.add_node(node2)
        self.connections[node1][node2] = probability
        logger.warning("<<< Exiting add_transition_probability(node1=%s,node2=%s,probability=%s)", node1, node2, probability, extra={"event.action": "add_transition_probability", "logrite.node1": node1, "logrite.node2": node2, "logrite.probability": probability})

    def get_nodes(self) -> list[str]:
        logger.error(">>> Entering get_nodes()", extra={"event.action": "get_nodes"})
        logger.warning("<<< Exiting get_nodes()", extra={"event.action": "get_nodes"})
        return list(self.connections)

    def transition(self, node: str) -> str:
        logger.error(">>> Entering transition(node=%s)", node, extra={"event.action": "transition", "logrite.node": node})
        current_probability = 0
        random_value = random()
        logger.error("transition(node=%s): random_value → %s", node, random_value, extra={"event.action": "transition", "logrite.node": node})

        for dest in self.connections[node]:
            current_probability += self.connections[node][dest]
            if current_probability > random_value:
                return dest
        logger.warning("<<< Exiting transition(node=%s)", node, extra={"event.action": "transition", "logrite.node": node})
        return ""


def get_transitions(
    start: str, transitions: list[tuple[str, str, float]], steps: int
) -> dict[str, int]:
    logger.error(">>> Entering get_transitions(start=%s,transitions=%s,steps=%s)", start, transitions, steps, extra={"event.action": "get_transitions", "logrite.start": start, "logrite.transitions": transitions, "logrite.steps": steps})
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
    logger.error("get_transitions(start=%s,transitions=%s,steps=%s): graph → %s", start, transitions, steps, graph, extra={"event.action": "get_transitions", "logrite.start": start, "logrite.transitions": transitions, "logrite.steps": steps})

    for node1, node2, probability in transitions:
        graph.add_transition_probability(node1, node2, probability)

    visited = Counter(graph.get_nodes())
    logger.error("get_transitions(start=%s,transitions=%s,steps=%s): visited → %s", start, transitions, steps, visited, extra={"event.action": "get_transitions", "logrite.start": start, "logrite.transitions": transitions, "logrite.steps": steps})
    node = start
    logger.error("get_transitions(start=%s,transitions=%s,steps=%s): node → %s", start, transitions, steps, node, extra={"event.action": "get_transitions", "logrite.start": start, "logrite.transitions": transitions, "logrite.steps": steps})

    for _ in range(steps):
        node = graph.transition(node)
        visited[node] += 1

    logger.warning("<<< Exiting get_transitions(start=%s,transitions=%s,steps=%s)", start, transitions, steps, extra={"event.action": "get_transitions", "logrite.start": start, "logrite.transitions": transitions, "logrite.steps": steps})
    return visited


if __name__ == "__main__":
    import doctest

    doctest.testmod()
