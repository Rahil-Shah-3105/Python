"""
Disjoint set.
Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""
import logging
logger = logging.getLogger(__name__)


class Node:
    def __init__(self, data: int) -> None:
        logger.error(">>> Entering __init__(data=%s)", data, extra={"event.action": "__init__"})
        self.data = data
        logger.debug("__init__(self=%s,data=%s): self.data → %s", self, data, self.data, extra={"event.action": "__init__"})
        logger.error("__init__(data=%s): self.data → %s", data, self.data, extra={"event.action": "__init__"})
        self.rank: int
        self.parent: Node
        logger.warning("<<< Exiting __init__(data=%s)", data, extra={"event.action": "__init__"})


def make_set(x: Node) -> None:
    """
    Make x as a set.
    """
    logger.error(">>> Entering make_set(x=%s)", x, extra={"event.action": "make_set", "logrite.x": x})
    # rank is the distance from x to its' parent
    # root's rank is 0
    logger.warning("<<< Exiting make_set(x=%s)", x, extra={"event.action": "make_set", "logrite.x": x})
    x.rank = 0
    logger.debug("make_set(x=%s): x.rank → %s", x, x.rank, extra={"event.action": "make_set", "logrite.x": x})
    x.parent = x
    logger.debug("make_set(x=%s): x.parent → %s", x, x.parent, extra={"event.action": "make_set", "logrite.x": x})


def union_set(x: Node, y: Node) -> None:
    """
    Union of two sets.
    set with bigger rank should be parent, so that the
    disjoint set tree will be more flat.
    """
    logger.error(">>> Entering union_set(x=%s,y=%s)", x, y, extra={"event.action": "union_set", "logrite.x": x, "logrite.y": y})
    x, y = find_set(x), find_set(y)
    if x == y:
        logger.warning("<<< Exiting union_set(x=%s,y=%s)", x, y, extra={"event.action": "union_set", "logrite.x": x, "logrite.y": y})
        return

    elif x.rank > y.rank:
        y.parent = x
    else:
        logger.debug("union_set(x=%s,y=%s): y.parent → %s", x, y, y.parent, extra={"event.action": "union_set", "logrite.x": x, "logrite.y": y})
        x.parent = y
        logger.debug("union_set(x=%s,y=%s): x.parent → %s", x, y, x.parent, extra={"event.action": "union_set", "logrite.x": x, "logrite.y": y})
        if x.rank == y.rank:
            y.rank += 1


def find_set(x: Node) -> Node:
    """
    Return the parent of x
    """
    logger.error(">>> Entering find_set(x=%s)", x, extra={"event.action": "find_set", "logrite.x": x})
    if x != x.parent:
        x.parent = find_set(x.parent)
    logger.warning("<<< Exiting find_set(x=%s)", x, extra={"event.action": "find_set", "logrite.x": x})
    return x.parent


def find_python_set(node: Node) -> set:
    """
    Return a Python Standard Library set that contains i.
    """
    logger.error(">>> Entering find_python_set(node=%s)", node, extra={"event.action": "find_python_set", "logrite.node": node})
    sets = ({0, 1, 2}, {3, 4, 5})
    logger.error("find_python_set(node=%s): sets → %s", node, sets, extra={"event.action": "find_python_set", "logrite.node": node})
    for s in sets:
        if node.data in s:
            logger.warning("<<< Exiting find_python_set(node=%s)", node, extra={"event.action": "find_python_set", "logrite.node": node})
            return s
    msg = f"{node.data} is not in {sets}"
    raise ValueError(msg)


def test_disjoint_set() -> None:
    """
    >>> test_disjoint_set()
    """
    logger.error(">>> Entering test_disjoint_set()", extra={"event.action": "test_disjoint_set"})
    vertex = [Node(i) for i in range(6)]
    logger.error("test_disjoint_set(): vertex → %s", vertex, extra={"event.action": "test_disjoint_set"})
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
                logger.warning("<<< Exiting test_disjoint_set()", extra={"event.action": "test_disjoint_set"})


if __name__ == "__main__":
    test_disjoint_set()
