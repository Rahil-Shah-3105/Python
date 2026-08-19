import sys
from collections import defaultdict
import logging
logger = logging.getLogger(__name__)


class Heap:
    def __init__(self):
        logger.debug(">>> Entering __init__()")
        self.node_position = []
        logger.debug("__init__(self=%s): self.node_position → %s", self, self.node_position)
        logger.debug("<<< Exiting __init__()")

    def get_position(self, vertex):
        logger.debug(">>> Entering get_position(vertex=%s)", vertex)
        logger.debug("<<< Exiting get_position(vertex=%s)", vertex)
        return self.node_position[vertex]

    def set_position(self, vertex, pos):
        logger.debug(">>> Entering set_position(vertex=%s,pos=%s)", vertex, pos)
        self.node_position[vertex] = pos
        logger.debug("<<< Exiting set_position(vertex=%s,pos=%s)", vertex, pos)

    def top_to_bottom(self, heap, start, size, positions):
        logger.debug(">>> Entering top_to_bottom(heap=%s,start=%s,size=%s,positions=%s)", heap, start, size, positions)
        if start > size // 2 - 1:
            return
            logger.debug("<<< Exiting top_to_bottom(heap=%s,start=%s,size=%s,positions=%s)", heap, start, size, positions)
        else:
            if 2 * start + 2 >= size:  # noqa: SIM114
                smallest_child = 2 * start + 1
                logger.debug("top_to_bottom(self=%s,heap=%s,start=%s,size=%s,positions=%s): smallest_child → %s", self, heap, start, size, positions, smallest_child)
            elif heap[2 * start + 1] < heap[2 * start + 2]:
                smallest_child = 2 * start + 1
            else:
                smallest_child = 2 * start + 2
            if heap[smallest_child] < heap[start]:
                temp, temp1 = heap[smallest_child], positions[smallest_child]
                heap[smallest_child], positions[smallest_child] = (
                    heap[start],
                    positions[start],
                )
                heap[start], positions[start] = temp, temp1

                temp = self.get_position(positions[smallest_child])
                self.set_position(
                    positions[smallest_child], self.get_position(positions[start])
                )
                self.set_position(positions[start], temp)

                self.top_to_bottom(heap, smallest_child, size, positions)

    # Update function if value of any node in min-heap decreases
    def bottom_to_top(self, val, index, heap, position):
        logger.debug(">>> Entering bottom_to_top(val=%s,index=%s,heap=%s,position=%s)", val, index, heap, position)
        temp = position[index]

        while index != 0:
            parent = int((index - 2) / 2) if index % 2 == 0 else int((index - 1) / 2)
            logger.debug("bottom_to_top(val=%s,index=%s,heap=%s,position=%s): parent → %s", val, index, heap, position, parent)

            if val < heap[parent]:
                heap[index] = heap[parent]
                position[index] = position[parent]
                self.set_position(position[parent], index)
            else:
                heap[index] = val
                position[index] = temp
                self.set_position(temp, index)
                break
            index = parent
        else:
            heap[0] = val
            position[0] = temp
            self.set_position(temp, 0)
            logger.debug("<<< Exiting bottom_to_top(val=%s,index=%s,heap=%s,position=%s)", val, index, heap, position)

    def heapify(self, heap, positions):
        logger.debug(">>> Entering heapify(heap=%s,positions=%s)", heap, positions)
        start = len(heap) // 2 - 1
        logger.debug("heapify(self=%s,heap=%s,positions=%s): start → %s", self, heap, positions, start)
        for i in range(start, -1, -1):
            self.top_to_bottom(heap, i, len(heap), positions)
            logger.debug("<<< Exiting heapify(heap=%s,positions=%s)", heap, positions)

    def delete_minimum(self, heap, positions):
        logger.debug(">>> Entering delete_minimum(heap=%s,positions=%s)", heap, positions)
        temp = positions[0]
        heap[0] = sys.maxsize
        self.top_to_bottom(heap, 0, len(heap), positions)
        logger.debug("<<< Exiting delete_minimum(heap=%s,positions=%s)", heap, positions)
        return temp


def prisms_algorithm(adjacency_list):
    """
    >>> adjacency_list = {0: [[1, 1], [3, 3]],
    ...                   1: [[0, 1], [2, 6], [3, 5], [4, 1]],
    ...                   2: [[1, 6], [4, 5], [5, 2]],
    ...                   3: [[0, 3], [1, 5], [4, 1]],
    ...                   4: [[1, 1], [2, 5], [3, 1], [5, 4]],
    ...                   5: [[2, 2], [4, 4]]}
    >>> prisms_algorithm(adjacency_list)
    [(0, 1), (1, 4), (4, 3), (4, 5), (5, 2)]
    """
    logger.debug(">>> Entering prisms_algorithm(adjacency_list=%s)", adjacency_list)

    heap = Heap()
    logger.debug("prisms_algorithm(adjacency_list=%s): heap → %s", adjacency_list, heap)

    visited = [0] * len(adjacency_list)
    logger.debug("prisms_algorithm(adjacency_list=%s): visited → %s", adjacency_list, visited)
    nbr_tv = [-1] * len(adjacency_list)  # Neighboring Tree Vertex of selected vertex
    logger.debug("prisms_algorithm(adjacency_list=%s): nbr_tv → %s", adjacency_list, nbr_tv)
    # Minimum Distance of explored vertex with neighboring vertex of partial tree
    # formed in graph
    distance_tv = []  # Heap of Distance of vertices from their neighboring vertex
    logger.debug("prisms_algorithm(adjacency_list=%s): distance_tv → %s", adjacency_list, distance_tv)
    positions = []
    logger.debug("prisms_algorithm(adjacency_list=%s): positions → %s", adjacency_list, positions)

    for vertex in range(len(adjacency_list)):
        distance_tv.append(sys.maxsize)
        positions.append(vertex)
        heap.node_position.append(vertex)

    tree_edges = []
    logger.debug("prisms_algorithm(adjacency_list=%s): tree_edges → %s", adjacency_list, tree_edges)
    visited[0] = 1
    distance_tv[0] = sys.maxsize
    for neighbor, distance in adjacency_list[0]:
        nbr_tv[neighbor] = 0
        distance_tv[neighbor] = distance
    heap.heapify(distance_tv, positions)

    for _ in range(1, len(adjacency_list)):
        vertex = heap.delete_minimum(distance_tv, positions)
        logger.debug("prisms_algorithm(adjacency_list=%s): vertex → %s", adjacency_list, vertex)
        if visited[vertex] == 0:
            tree_edges.append((nbr_tv[vertex], vertex))
            visited[vertex] = 1
            for neighbor, distance in adjacency_list[vertex]:
                if (
                    visited[neighbor] == 0
                    and distance < distance_tv[heap.get_position(neighbor)]
                ):
                    distance_tv[heap.get_position(neighbor)] = distance
                    heap.bottom_to_top(
                        distance, heap.get_position(neighbor), distance_tv, positions
                    )
                    nbr_tv[neighbor] = vertex
    logger.debug("<<< Exiting prisms_algorithm(adjacency_list=%s)", adjacency_list)
    return tree_edges


if __name__ == "__main__":  # pragma: no cover
    # < --------- Prims Algorithm --------- >
    edges_number = int(input("Enter number of edges: ").strip())
    adjacency_list = defaultdict(list)
    for _ in range(edges_number):
        edge = [int(x) for x in input().strip().split()]
        adjacency_list[edge[0]].append([edge[1], edge[2]])
        adjacency_list[edge[1]].append([edge[0], edge[2]])
    print(prisms_algorithm(adjacency_list))
