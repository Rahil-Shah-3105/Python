import logging
logger = logging.getLogger(__name__)
# Min heap data structure
# with decrease key functionality - in O(log(n)) time


class Node:
    def __init__(self, name, val):
        logger.debug(">>> Entering __init__(name=%s,val=%s)", name, val)
        self.name = name
        logger.debug("__init__(name=%s,val=%s): self.name → %s", name, val, self.name)
        logger.debug("__init__(self=%s,name=%s,val=%s): self.name → %s", self, name, val, self.name)
        self.val = val
        logger.debug("__init__(self=%s,name=%s,val=%s): self.val → %s", self, name, val, self.val)
        logger.debug("<<< Exiting __init__(name=%s,val=%s)", name, val)
        logger.debug(">>> Entering __init__(array=%s)", array)
        logger.debug("__init__(self=%s,array=%s): self.idx_of_element → %s", self, array, self.idx_of_element)
        logger.debug("__init__(self=%s,array=%s): self.heap_dict → %s", self, array, self.heap_dict)
        logger.debug("<<< Exiting __init__(array=%s)", array)

    def __str__(self):
        logger.debug(">>> Entering __str__()")
        logger.debug("<<< Exiting __str__()")
        return f"{self.__class__.__name__}({self.name}, {self.val})"

    def __lt__(self, other):
        logger.debug(">>> Entering __lt__(other=%s)", other)
        logger.debug("<<< Exiting __lt__(other=%s)", other)
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
        self.idx_of_element = {}
        self.heap_dict = {}
        self.heap = self.build_heap(array)
        logger.debug("__init__(array=%s): self.heap → %s", array, self.heap)

    def __getitem__(self, key):
        logger.debug(">>> Entering __getitem__(key=%s)", key)
        logger.debug("<<< Exiting __getitem__(key=%s)", key)
        return self.get_value(key)

    def get_parent_idx(self, idx):
        logger.debug(">>> Entering get_parent_idx(idx=%s)", idx)
        logger.debug("<<< Exiting get_parent_idx(idx=%s)", idx)
        return (idx - 1) // 2

    def get_left_child_idx(self, idx):
        logger.debug(">>> Entering get_left_child_idx(idx=%s)", idx)
        logger.debug("<<< Exiting get_left_child_idx(idx=%s)", idx)
        return idx * 2 + 1

    def get_right_child_idx(self, idx):
        logger.debug(">>> Entering get_right_child_idx(idx=%s)", idx)
        logger.debug("<<< Exiting get_right_child_idx(idx=%s)", idx)
        return idx * 2 + 2

    def get_value(self, key):
        logger.debug(">>> Entering get_value(key=%s)", key)
        logger.debug("<<< Exiting get_value(key=%s)", key)
        return self.heap_dict[key]

    def build_heap(self, array):
        logger.debug(">>> Entering build_heap(array=%s)", array)
        last_idx = len(array) - 1
        logger.debug("build_heap(array=%s): last_idx → %s", array, last_idx)
        logger.debug("build_heap(self=%s,array=%s): last_idx → %s", self, array, last_idx)
        start_from = self.get_parent_idx(last_idx)
        logger.debug("build_heap(array=%s): start_from → %s", array, start_from)
        logger.debug("build_heap(self=%s,array=%s): start_from → %s", self, array, start_from)

        for idx, i in enumerate(array):
            self.idx_of_element[i] = idx
            self.heap_dict[i.name] = i.val

        for i in range(start_from, -1, -1):
            self.sift_down(i, array)
        logger.debug("<<< Exiting build_heap(array=%s)", array)
        return array

    # this is min-heapify method
    def sift_down(self, idx, array):
        logger.debug(">>> Entering sift_down(idx=%s,array=%s)", idx, array)
        logger.debug("sift_down(idx=%s,array=%s): left → %s", idx, array, left)
        logger.debug("sift_down(self=%s,idx=%s,array=%s): left → %s", self, idx, array, left)
        logger.debug("sift_down(self=%s,idx=%s,array=%s): right → %s", self, idx, array, right)
        logger.debug("sift_down(idx=%s,array=%s): right → %s", idx, array, right)
        logger.debug("sift_down(self=%s,idx=%s,array=%s): smallest → %s", self, idx, array, smallest)
        while True:
            left = self.get_left_child_idx(idx)
            right = self.get_right_child_idx(idx)

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
                logger.debug("<<< Exiting sift_down(idx=%s,array=%s)", idx, array)
                break

    def sift_up(self, idx):
        logger.debug(">>> Entering sift_up(idx=%s)", idx)
        p = self.get_parent_idx(idx)
        logger.debug("sift_up(idx=%s): p → %s", idx, p)
        while p >= 0 and self.heap[p] > self.heap[idx]:
            self.heap[p], self.heap[idx] = self.heap[idx], self.heap[p]
            self.idx_of_element[self.heap[p]], self.idx_of_element[self.heap[idx]] = (
                self.idx_of_element[self.heap[idx]],
                self.idx_of_element[self.heap[p]],
            )
            idx = p
            logger.debug("<<< Exiting sift_up(idx=%s)", idx)
            p = self.get_parent_idx(idx)

    def peek(self):
        logger.debug(">>> Entering peek()")
        logger.debug("<<< Exiting peek()")
        return self.heap[0]

    def remove(self):
        logger.debug(">>> Entering remove()")
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.idx_of_element[self.heap[0]], self.idx_of_element[self.heap[-1]] = (
            self.idx_of_element[self.heap[-1]],
            self.idx_of_element[self.heap[0]],
        )

        x = self.heap.pop()
        logger.debug("remove(): x → %s", x)
        del self.idx_of_element[x]
        self.sift_down(0, self.heap)
        logger.debug("<<< Exiting remove()")
        return x

    def insert(self, node):
        logger.debug(">>> Entering insert(node=%s)", node)
        self.heap.append(node)
        self.idx_of_element[node] = len(self.heap) - 1
        self.heap_dict[node.name] = node.val
        self.sift_up(len(self.heap) - 1)
        logger.debug("<<< Exiting insert(node=%s)", node)

    def is_empty(self):
        logger.debug(">>> Entering is_empty()")
        logger.debug("<<< Exiting is_empty()")
        return len(self.heap) == 0

    def decrease_key(self, node, new_value):
        logger.debug(">>> Entering decrease_key(node=%s,new_value=%s)", node, new_value)
        assert self.heap[self.idx_of_element[node]].val > new_value, (
            "newValue must be less that current value"
        )
        node.val = new_value
        logger.debug("decrease_key(self=%s,node=%s,new_value=%s): node.val → %s", self, node, new_value, node.val)
        self.heap_dict[node.name] = new_value
        self.sift_up(self.idx_of_element[node])
        logger.debug("<<< Exiting decrease_key(node=%s,new_value=%s)", node, new_value)


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
