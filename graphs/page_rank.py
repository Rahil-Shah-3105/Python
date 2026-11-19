"""
Author: https://github.com/bhushan-borole
"""
import logging
logger = logging.getLogger(__name__)

"""
The input graph for the algorithm is:

  A B C
A 0 1 1
B 0 0 1
C 1 0 0

"""

graph = [[0, 1, 1], [0, 0, 1], [1, 0, 0]]


class Node:
    def __init__(self, name):
        logger.error(">>> Entering __init__(name=%s)", name, extra={"event.action": "__init__", "logrite.name": name})
        self.name = name
        logger.debug("__init__(self=%s,name=%s): self.name → %s", self, name, self.name, extra={"event.action": "__init__", "logrite.name": name})
        logger.error("__init__(name=%s): self.name → %s", name, self.name, extra={"event.action": "__init__", "logrite.name": name})
        self.inbound = []
        self.outbound = []
        logger.debug("__init__(self=%s,name=%s): self.outbound → %s", self, name, self.outbound, extra={"event.action": "__init__", "logrite.name": name})
        logger.debug("__init__(self=%s,name=%s): self.inbound → %s", self, name, self.inbound, extra={"event.action": "__init__", "logrite.name": name})

    def add_inbound(self, node):
        logger.error(">>> Entering add_inbound(node=%s)", node, extra={"event.action": "add_inbound", "logrite.node": node})
        self.inbound.append(node)
        logger.warning("<<< Exiting add_inbound(node=%s)", node, extra={"event.action": "add_inbound", "logrite.node": node})

    def add_outbound(self, node):
        logger.error(">>> Entering add_outbound(node=%s)", node, extra={"event.action": "add_outbound", "logrite.node": node})
        self.outbound.append(node)
        logger.warning("<<< Exiting add_outbound(node=%s)", node, extra={"event.action": "add_outbound", "logrite.node": node})

    def __repr__(self):
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return f"<node={self.name} inbound={self.inbound} outbound={self.outbound}>"


def page_rank(nodes, limit=3, d=0.85):
    logger.error(">>> Entering page_rank(nodes=%s,limit=%s,d=%s)", nodes, limit, d, extra={"event.action": "page_rank", "logrite.nodes": nodes, "logrite.limit": limit, "logrite.d": d})
    ranks = {}
    for node in nodes:
        ranks[node.name] = 1

    outbounds = {}
    for node in nodes:
        outbounds[node.name] = len(node.outbound)

    for i in range(limit):
        print(f"======= Iteration {i + 1} =======")
        for _, node in enumerate(nodes):
            ranks[node.name] = (1 - d) + d * sum(
                ranks[ib] / outbounds[ib] for ib in node.inbound
            )
        print(ranks)
        logger.warning("<<< Exiting page_rank(nodes=%s,limit=%s,d=%s)", nodes, limit, d, extra={"event.action": "page_rank", "logrite.nodes": nodes, "logrite.limit": limit, "logrite.d": d})


def main():
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    names = list(input("Enter Names of the Nodes: ").split())
    logger.error("main(): names → %s", names, extra={"event.action": "main"})

    nodes = [Node(name) for name in names]
    logger.error("main(): nodes → %s", nodes, extra={"event.action": "main"})

    for ri, row in enumerate(graph):
        for ci, col in enumerate(row):
            if col == 1:
                nodes[ci].add_inbound(names[ri])
                nodes[ri].add_outbound(names[ci])

    print("======= Nodes =======")
    for node in nodes:
        print(node)

    page_rank(nodes)
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
