import logging
logger = logging.getLogger(__name__)
"""
Author: https://github.com/bhushan-borole
"""

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
        logger.debug(">>> Entering __init__(name=%s)", name)
        self.name = name
        logger.debug("__init__(name=%s): self.name → %s", name, self.name)
        logger.debug("__init__(self=%s,name=%s): self.name → %s", self, name, self.name)
        self.inbound = []
        logger.debug("__init__(self=%s,name=%s): self.inbound → %s", self, name, self.inbound)
        self.outbound = []
        logger.debug("__init__(self=%s,name=%s): self.outbound → %s", self, name, self.outbound)
        logger.debug("<<< Exiting __init__(name=%s)", name)

    def add_inbound(self, node):
        self.inbound.append(node)
        logger.debug(">>> Entering add_inbound(node=%s)", node)
        logger.debug("<<< Exiting add_inbound(node=%s)", node)

    def add_outbound(self, node):
        logger.debug(">>> Entering add_outbound(node=%s)", node)
        self.outbound.append(node)
        logger.debug("<<< Exiting add_outbound(node=%s)", node)

    def __repr__(self):
        logger.debug(">>> Entering __repr__()")
        logger.debug("<<< Exiting __repr__()")
        return f"<node={self.name} inbound={self.inbound} outbound={self.outbound}>"


def page_rank(nodes, limit=3, d=0.85):
    logger.debug(">>> Entering page_rank(nodes=%s,limit=%s,d=%s)", nodes, limit, d)
    ranks = {}
    logger.debug("page_rank(nodes=%s,limit=%s,d=%s): ranks → %s", nodes, limit, d, ranks)
    for node in nodes:
        ranks[node.name] = 1

    outbounds = {}
    logger.debug("page_rank(nodes=%s,limit=%s,d=%s): outbounds → %s", nodes, limit, d, outbounds)
    for node in nodes:
        outbounds[node.name] = len(node.outbound)

    for i in range(limit):
        print(f"======= Iteration {i + 1} =======")
        for _, node in enumerate(nodes):
            ranks[node.name] = (1 - d) + d * sum(
                ranks[ib] / outbounds[ib] for ib in node.inbound
            )
        print(ranks)
        logger.debug("<<< Exiting page_rank(nodes=%s,limit=%s,d=%s)", nodes, limit, d)


def main():
    logger.debug(">>> Entering main()")
    names = list(input("Enter Names of the Nodes: ").split())
    logger.debug("main(): names → %s", names)

    nodes = [Node(name) for name in names]
    logger.debug("main(): nodes → %s", nodes)

    for ri, row in enumerate(graph):
        for ci, col in enumerate(row):
            if col == 1:
                nodes[ci].add_inbound(names[ri])
                nodes[ri].add_outbound(names[ci])

    print("======= Nodes =======")
    for node in nodes:
        print(node)

    page_rank(nodes)
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    main()
