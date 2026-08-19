import logging
logger = logging.getLogger(__name__)
"""
Disjoint set.
Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""


class Node:
    def __init__(self, data: int) -> None:
        logger.debug(">>> Entering __init__(data=%s)", data)
        self.data = data
        logger.debug("__init__(data=%s): self.data → %s", data, self.data)
        logger.debug("__init__(self=%s,data=%s): self.data → %s", self, data, self.data)
        self.rank: int
        self.parent: Node
        logger.debug("<<< Exiting __init__(data=%s)", data)


def make_set(x: Node) -> None:
    """
    Make x as a set.
    """
    logger.debug(">>> Entering make_set(x=%s)", x)
    # rank is the distance from x to its' parent
    # root's rank is 0
    logger.debug("<<< Exiting make_set(x=%s)", x)
    x.rank = 0
    logger.debug("make_set(x=%s): x.rank → %s", x, x.rank)
    x.parent = x
    logger.debug("make_set(x=%s): x.parent → %s", x, x.parent)


def union_set(x: Node, y: Node) -> None:
    """
    Union of two sets.
    set with bigger rank should be parent, so that the
    disjoint set tree will be more flat.
    """
    logger.debug(">>> Entering union_set(x=%s,y=%s)", x, y)
    x, y = find_set(x), find_set(y)
    if x == y:
        logger.debug("<<< Exiting union_set(x=%s,y=%s)", x, y)
        return

    elif x.rank > y.rank:
        y.parent = x
        logger.debug("union_set(x=%s,y=%s): y.parent → %s", x, y, y.parent)
    else:
        x.parent = y
        logger.debug("union_set(x=%s,y=%s): x.parent → %s", x, y, x.parent)
        if x.rank == y.rank:
            y.rank += 1


def find_set(x: Node) -> Node:
    """
    Return the parent of x
    """
    logger.debug(">>> Entering find_set(x=%s)", x)
    if x != x.parent:
        x.parent = find_set(x.parent)
    logger.debug("<<< Exiting find_set(x=%s)", x)
    return x.parent


def find_python_set(node: Node) -> set:
    """
    Return a Python Standard Library set that contains i.
    """
    logger.debug(">>> Entering find_python_set(node=%s)", node)
    sets = ({0, 1, 2}, {3, 4, 5})
    logger.debug("find_python_set(node=%s): sets → %s", node, sets)
    for s in sets:
        if node.data in s:
            logger.debug("<<< Exiting find_python_set(node=%s)", node)
            logger.debug("find_python_set(node=%s): msg → %s", node, msg)
            return s
    msg = f"{node.data} is not in {sets}"
    raise ValueError(msg)


def test_disjoint_set() -> None:
    """
    >>> test_disjoint_set()
    """
    logger.debug(">>> Entering test_disjoint_set()")
    vertex = [Node(i) for i in range(6)]
    logger.debug("test_disjoint_set(): vertex → %s", vertex)
    for v in vertex:
        make_set(v)

    union_set(vertex[0], vertex[1])
    union_set(vertex[1], vertex[2])
    union_set(vertex[3], vertex[4])
    union_set(vertex[3], vertex[5])

    for node0 in vertex:
        for node1 in vertex:
            if find_python_set(node0).isdisjoint(find_python_set(node1)):
                assert find_set(node0) != find_set(node1)
            else:
                assert find_set(node0) == find_set(node1)
                logger.debug("<<< Exiting test_disjoint_set()")


if __name__ == "__main__":
    test_disjoint_set()
