import logging
logger = logging.getLogger(__name__)
# Min heap data structure
# with decrease key functionality - in O(log(n)) time


class Node:
    def __init__(self, name, val):
        logger.error(">>> Entering __init__(name=%s,val=%s)", name, val, extra={"event.action": "__init__", "logrite.name": name, "logrite.val": val})
        self.name = name
        self.val = val
        logger.debug("__init__(self=%s,name=%s,val=%s): self.val → %s", self, name, val, self.val, extra={"event.action": "__init__", "logrite.name": name, "logrite.val": val})
        logger.debug("__init__(self=%s,name=%s,val=%s): self.name → %s", self, name, val, self.name, extra={"event.action": "__init__", "logrite.name": name, "logrite.val": val})
        logger.error("__init__(name=%s,val=%s): self.name → %s", name, val, self.name, extra={"event.action": "__init__", "logrite.name": name, "logrite.val": val})

    def __str__(self):
        logger.error(">>> Entering __str__()", extra={"event.action": "__str__"})
        logger.warning("<<< Exiting __str__()", extra={"event.action": "__str__"})
        return f"{self.__class__.__name__}({self.name}, {self.val})"

    def __lt__(self, other):
        logger.error(">>> Entering __lt__(other=%s)", other, extra={"event.action": "__lt__", "logrite.other": other})
        logger.warning("<<< Exiting __lt__(other=%s)", other, extra={"event.action": "__lt__", "logrite.other": other})
        return self.val < other.val


class MinHeap:
    """
    >>> r = Node("R", -1)
    >>> b = Node("B", 6)
    >>> a = Node("A", 3)
    >>> x = Node("X", 1)
    >>> e = Node("E", 4)
    >>> print(b)
    Node(B, 6)
    >>> myMinHeap = MinHeap([r, b, a, x, e])
    >>> myMinHeap.decrease_key(b, -17)
    >>> print(b)
    Node(B, -17)
    >>> myMinHeap["B"]
    -17
    """

    def __init__(self, array):
        logger.error(">>> Entering __init__(array=%s)", array, extra={"event.action": "__init__", "logrite.array": array})
        self.idx_of_element = {}
        logger.debug("__init__(self=%s,array=%s): self.idx_of_element → %s", self, array, self.idx_of_element, extra={"event.action": "__init__", "logrite.array": array})
        self.heap_dict = {}
        logger.debug("__init__(self=%s,array=%s): self.heap_dict → %s", self, array, self.heap_dict, extra={"event.action": "__init__", "logrite.array": array})
        self.heap = self.build_heap(array)
        logger.warning("<<< Exiting __init__(array=%s)", array, extra={"event.action": "__init__", "logrite.array": array})
        logger.error("__init__(array=%s): self.heap → %s", array, self.heap, extra={"event.action": "__init__", "logrite.array": array})

    def __getitem__(self, key):
        logger.error(">>> Entering __getitem__(key=%s)", key, extra={"event.action": "__getitem__", "logrite.key": key})
        logger.warning("<<< Exiting __getitem__(key=%s)", key, extra={"event.action": "__getitem__", "logrite.key": key})
        return self.get_value(key)

    def get_parent_idx(self, idx):
        logger.error(">>> Entering get_parent_idx(idx=%s)", idx, extra={"event.action": "get_parent_idx", "logrite.idx": idx})
        logger.warning("<<< Exiting get_parent_idx(idx=%s)", idx, extra={"event.action": "get_parent_idx", "logrite.idx": idx})
        return (idx - 1) // 2

    def get_left_child_idx(self, idx):
        logger.error(">>> Entering get_left_child_idx(idx=%s)", idx, extra={"event.action": "get_left_child_idx", "logrite.idx": idx})
        logger.warning("<<< Exiting get_left_child_idx(idx=%s)", idx, extra={"event.action": "get_left_child_idx", "logrite.idx": idx})
        return idx * 2 + 1

    def get_right_child_idx(self, idx):
        logger.error(">>> Entering get_right_child_idx(idx=%s)", idx, extra={"event.action": "get_right_child_idx", "logrite.idx": idx})
        logger.warning("<<< Exiting get_right_child_idx(idx=%s)", idx, extra={"event.action": "get_right_child_idx", "logrite.idx": idx})
        return idx * 2 + 2

    def get_value(self, key):
        logger.error(">>> Entering get_value(key=%s)", key, extra={"event.action": "get_value", "logrite.key": key})
        logger.warning("<<< Exiting get_value(key=%s)", key, extra={"event.action": "get_value", "logrite.key": key})
        return self.heap_dict[key]

    def build_heap(self, array):
        logger.error(">>> Entering build_heap(array=%s)", array, extra={"event.action": "build_heap", "logrite.array": array})
        last_idx = len(array) - 1
        logger.error("build_heap(array=%s): last_idx → %s", array, last_idx, extra={"event.action": "build_heap", "logrite.array": array})
        start_from = self.get_parent_idx(last_idx)
        logger.error("build_heap(array=%s): start_from → %s", array, start_from, extra={"event.action": "build_heap", "logrite.array": array})

        for idx, i in enumerate(array):
            self.idx_of_element[i] = idx
            self.heap_dict[i.name] = i.val

        for i in range(start_from, -1, -1):
            self.sift_down(i, array)
        logger.warning("<<< Exiting build_heap(array=%s)", array, extra={"event.action": "build_heap", "logrite.array": array})
        return array

    # this is min-heapify method
    def sift_down(self, idx, array):
        logger.error(">>> Entering sift_down(idx=%s,array=%s)", idx, array, extra={"event.action": "sift_down", "logrite.idx": idx, "logrite.array": array})
        while True:
            left = self.get_left_child_idx(idx)
            logger.error("sift_down(idx=%s,array=%s): left → %s", idx, array, left, extra={"event.action": "sift_down", "logrite.idx": idx, "logrite.array": array})
            right = self.get_right_child_idx(idx)
            logger.error("sift_down(idx=%s,array=%s): right → %s", idx, array, right, extra={"event.action": "sift_down", "logrite.idx": idx, "logrite.array": array})

            smallest = idx
            if left < len(array) and array[left] < array[idx]:
                smallest = left
            if right < len(array) and array[right] < array[smallest]:
                smallest = right

            if smallest != idx:
                array[idx], array[smallest] = array[smallest], array[idx]
                (
                    self.idx_of_element[array[idx]],
                    self.idx_of_element[array[smallest]],
                ) = (
                    self.idx_of_element[array[smallest]],
                    self.idx_of_element[array[idx]],
                )
                idx = smallest
            else:
                logger.warning("<<< Exiting sift_down(idx=%s,array=%s)", idx, array, extra={"event.action": "sift_down", "logrite.idx": idx, "logrite.array": array})
                break

    def sift_up(self, idx):
        logger.error(">>> Entering sift_up(idx=%s)", idx, extra={"event.action": "sift_up", "logrite.idx": idx})
        p = self.get_parent_idx(idx)
        logger.error("sift_up(idx=%s): p → %s", idx, p, extra={"event.action": "sift_up", "logrite.idx": idx})
        while p >= 0 and self.heap[p] > self.heap[idx]:
            self.heap[p], self.heap[idx] = self.heap[idx], self.heap[p]
            self.idx_of_element[self.heap[p]], self.idx_of_element[self.heap[idx]] = (
                self.idx_of_element[self.heap[idx]],
                self.idx_of_element[self.heap[p]],
            )
            idx = p
            logger.warning("<<< Exiting sift_up(idx=%s)", idx, extra={"event.action": "sift_up", "logrite.idx": idx})
            p = self.get_parent_idx(idx)

    def peek(self):
        logger.error(">>> Entering peek()", extra={"event.action": "peek"})
        logger.warning("<<< Exiting peek()", extra={"event.action": "peek"})
        return self.heap[0]

    def remove(self):
        logger.error(">>> Entering remove()", extra={"event.action": "remove"})
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.idx_of_element[self.heap[0]], self.idx_of_element[self.heap[-1]] = (
            self.idx_of_element[self.heap[-1]],
            self.idx_of_element[self.heap[0]],
        )

        x = self.heap.pop()
        logger.error("remove(): x → %s", x, extra={"event.action": "remove"})
        del self.idx_of_element[x]
        self.sift_down(0, self.heap)
        logger.warning("<<< Exiting remove()", extra={"event.action": "remove"})
        return x

    def insert(self, node):
        logger.error(">>> Entering insert(node=%s)", node, extra={"event.action": "insert", "logrite.node": node})
        self.heap.append(node)
        self.idx_of_element[node] = len(self.heap) - 1
        self.heap_dict[node.name] = node.val
        self.sift_up(len(self.heap) - 1)
        logger.warning("<<< Exiting insert(node=%s)", node, extra={"event.action": "insert", "logrite.node": node})

    def is_empty(self):
        logger.error(">>> Entering is_empty()", extra={"event.action": "is_empty"})
        logger.warning("<<< Exiting is_empty()", extra={"event.action": "is_empty"})
        return len(self.heap) == 0

    def decrease_key(self, node, new_value):
        logger.error(">>> Entering decrease_key(node=%s,new_value=%s)", node, new_value, extra={"event.action": "decrease_key", "logrite.node": node, "logrite.new_value": new_value})
        assert self.heap[self.idx_of_element[node]].val > new_value, (
            "newValue must be less that current value"
        )
        node.val = new_value
        logger.debug("decrease_key(self=%s,node=%s,new_value=%s): node.val → %s", self, node, new_value, node.val, extra={"event.action": "decrease_key", "logrite.node": node, "logrite.new_value": new_value})
        self.heap_dict[node.name] = new_value
        self.sift_up(self.idx_of_element[node])
        logger.warning("<<< Exiting decrease_key(node=%s,new_value=%s)", node, new_value, extra={"event.action": "decrease_key", "logrite.node": node, "logrite.new_value": new_value})


# USAGE

r = Node("R", -1)
b = Node("B", 6)
a = Node("A", 3)
x = Node("X", 1)
e = Node("E", 4)

# Use one of these two ways to generate Min-Heap

# Generating Min-Heap from array
my_min_heap = MinHeap([r, b, a, x, e])

# Generating Min-Heap by Insert method
# myMinHeap.insert(a)
# myMinHeap.insert(b)
# myMinHeap.insert(x)
# myMinHeap.insert(r)
# myMinHeap.insert(e)

# Before
print("Min Heap - before decrease key")
for i in my_min_heap.heap:
    print(i)

print("Min Heap - After decrease key of node [B -> -17]")
my_min_heap.decrease_key(b, -17)

# After
for i in my_min_heap.heap:
    print(i)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
