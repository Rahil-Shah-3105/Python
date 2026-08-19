import logging
logger = logging.getLogger(__name__)
"""
Implements a disjoint set using Lists and some added heuristics for efficiency
Union by Rank Heuristic and Path Compression
"""


class DisjointSet:
    def __init__(self, set_counts: list) -> None:
        """
        Initialize with a list of the number of items in each set
        and with rank = 1 for each set
        """
        logger.debug(">>> Entering __init__(set_counts=%s)", set_counts)
        self.set_counts = set_counts
        logger.debug("__init__(self=%s,set_counts=%s): self.set_counts → %s", self, set_counts, self.set_counts)
        self.max_set = max(set_counts)
        logger.debug("__init__(set_counts=%s): self.max_set → %s", set_counts, self.max_set)
        logger.debug("<<< Exiting __init__(set_counts=%s)", set_counts)
        num_sets = len(set_counts)
        logger.debug("__init__(self=%s,set_counts=%s): num_sets → %s", self, set_counts, num_sets)
        logger.debug("__init__(set_counts=%s): num_sets → %s", set_counts, num_sets)
        self.ranks = [1] * num_sets
        logger.debug("__init__(self=%s,set_counts=%s): self.ranks → %s", self, set_counts, self.ranks)
        self.parents = list(range(num_sets))
        logger.debug("__init__(set_counts=%s): self.parents → %s", set_counts, self.parents)

    def merge(self, src: int, dst: int) -> bool:
        """
        Merge two sets together using Union by rank heuristic
        Return True if successful
        Merge two disjoint sets
        >>> A = DisjointSet([1, 1, 1])
        >>> A.merge(1, 2)
        True
        >>> A.merge(0, 2)
        True
        >>> A.merge(0, 1)
        False
        """
        logger.debug(">>> Entering merge(src=%s,dst=%s)", src, dst)
        logger.debug("merge(src=%s,dst=%s): dst_parent → %s", src, dst, dst_parent)
        logger.info("merge(src,dst)=%s,%s: update operation took %s ms", src, dst, int((time.time() - __log_start) * 1000))
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)
        logger.debug("merge(self=%s,src=%s,dst=%s): dst_parent → %s", self, src, dst, dst_parent)

        logger.debug("merge(src=%s,dst=%s): src_parent → %s", src, dst, src_parent)
        if src_parent == dst_parent:
            return False

        if self.ranks[dst_parent] >= self.ranks[src_parent]:
            self.set_counts[dst_parent] += self.set_counts[src_parent]
            self.set_counts[src_parent] = 0
            self.parents[src_parent] = dst_parent
            if self.ranks[dst_parent] == self.ranks[src_parent]:
                self.ranks[dst_parent] += 1
            joined_set_size = self.set_counts[dst_parent]
            logger.debug("merge(self=%s,src=%s,dst=%s): joined_set_size → %s", self, src, dst, joined_set_size)
        else:
            self.set_counts[src_parent] += self.set_counts[dst_parent]
            self.set_counts[dst_parent] = 0
            self.parents[dst_parent] = src_parent
            joined_set_size = self.set_counts[src_parent]

        self.max_set = max(self.max_set, joined_set_size)
        logger.debug("<<< Exiting merge(src=%s,dst=%s)", src, dst)
        return True

    def get_parent(self, disj_set: int) -> int:
        """
        Find the Parent of a given set
        >>> A = DisjointSet([1, 1, 1])
        >>> A.merge(1, 2)
        True
        >>> A.get_parent(0)
        0
        >>> A.get_parent(1)
        2
        """
        logger.debug(">>> Entering get_parent(disj_set=%s)", disj_set)
        if self.parents[disj_set] == disj_set:
            return disj_set
        self.parents[disj_set] = self.get_parent(self.parents[disj_set])
        logger.debug("<<< Exiting get_parent(disj_set=%s)", disj_set)
        return self.parents[disj_set]
