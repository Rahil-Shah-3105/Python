import heapq
import sys

import numpy as np
import logging
logger = logging.getLogger(__name__)

TPos = tuple[int, int]


class PriorityQueue:
    def __init__(self):
        logger.debug(">>> Entering __init__()")
        self.elements = []
        logger.debug("__init__(self=%s): self.elements → %s", self, self.elements)
        self.set = set()
        logger.debug("__init__(): self.set → %s", self.set)
        logger.debug("<<< Exiting __init__()")

    def minkey(self):
        logger.debug(">>> Entering minkey()")
        if not self.empty():
            return self.elements[0][0]
        else:
            logger.debug("<<< Exiting minkey()")
            return float("inf")

    def empty(self):
        logger.debug(">>> Entering empty()")
        logger.debug("<<< Exiting empty()")
        return len(self.elements) == 0

    def put(self, item, priority):
        logger.debug(">>> Entering put(item=%s,priority=%s)", item, priority)
        if item not in self.set:
            heapq.heappush(self.elements, (priority, item))
            self.set.add(item)
        else:
            # update
            # print("update", item)
            temp = []
            (pri, x) = heapq.heappop(self.elements)
            while x != item:
                temp.append((pri, x))
                (pri, x) = heapq.heappop(self.elements)
            temp.append((priority, item))
            for pro, xxx in temp:
                heapq.heappush(self.elements, (pro, xxx))
                logger.debug("<<< Exiting put(item=%s,priority=%s)", item, priority)

    def remove_element(self, item):
        logger.debug(">>> Entering remove_element(item=%s)", item)
        if item in self.set:
            self.set.remove(item)
            temp = []
            (pro, x) = heapq.heappop(self.elements)
            while x != item:
                temp.append((pro, x))
                (pro, x) = heapq.heappop(self.elements)
            for prito, yyy in temp:
                heapq.heappush(self.elements, (prito, yyy))
                logger.debug("<<< Exiting remove_element(item=%s)", item)

    def top_show(self):
        logger.debug(">>> Entering top_show()")
        logger.debug("<<< Exiting top_show()")
        return self.elements[0][1]

    def get(self):
        logger.debug(">>> Entering get()")
        (priority, item) = heapq.heappop(self.elements)
        self.set.remove(item)
        logger.debug("<<< Exiting get()")
        return (priority, item)


def consistent_heuristic(p: TPos, goal: TPos):
    logger.debug(">>> Entering consistent_heuristic(p=%s,goal=%s)", p, goal)
    # euclidean distance
    a = np.array(p)
    logger.debug("consistent_heuristic(p=%s,goal=%s): a → %s", p, goal, a)
    b = np.array(goal)
    logger.debug("consistent_heuristic(p=%s,goal=%s): b → %s", p, goal, b)
    logger.debug("<<< Exiting consistent_heuristic(p=%s,goal=%s)", p, goal)
    return np.linalg.norm(a - b)


def heuristic_2(p: TPos, goal: TPos):
    logger.debug(">>> Entering heuristic_2(p=%s,goal=%s)", p, goal)
    # integer division by time variable
    logger.debug("<<< Exiting heuristic_2(p=%s,goal=%s)", p, goal)
    return consistent_heuristic(p, goal) // t


def heuristic_1(p: TPos, goal: TPos):
    logger.debug(">>> Entering heuristic_1(p=%s,goal=%s)", p, goal)
    # manhattan distance
    logger.debug("<<< Exiting heuristic_1(p=%s,goal=%s)", p, goal)
    return abs(p[0] - goal[0]) + abs(p[1] - goal[1])


def key(start: TPos, i: int, goal: TPos, g_function: dict[TPos, float]):
    logger.debug(">>> Entering key(start=%s,i=%s,goal=%s,g_function=%s)", start, i, goal, g_function)
    ans = g_function[start] + W1 * heuristics[i](start, goal)
    logger.debug("key(start=%s,i=%s,goal=%s,g_function=%s): ans → %s", start, i, goal, g_function, ans)
    logger.debug("<<< Exiting key(start=%s,i=%s,goal=%s,g_function=%s)", start, i, goal, g_function)
    return ans


def do_something(back_pointer, goal, start):
    logger.debug(">>> Entering do_something(back_pointer=%s,goal=%s,start=%s)", back_pointer, goal, start)
    grid = np.char.chararray((n, n))
    logger.debug("do_something(back_pointer=%s,goal=%s,start=%s): grid → %s", back_pointer, goal, start, grid)
    for i in range(n):
        for j in range(n):
            grid[i][j] = "*"

    for i in range(n):
        for j in range(n):
            if (j, (n - 1) - i) in blocks:
                grid[i][j] = "#"

    grid[0][(n - 1)] = "-"
    x = back_pointer[goal]
    while x != start:
        (x_c, y_c) = x
        # print(x)
        grid[(n - 1) - y_c][x_c] = "-"
        x = back_pointer[x]
    grid[(n - 1)][0] = "-"

    for i in range(n):
        for j in range(n):
            if (i, j) == (0, n - 1):
                print(grid[i][j], end=" ")
                print("<-- End position", end=" ")
            else:
                print(grid[i][j], end=" ")
        print()
    print("^")
    print("Start position")
    print()
    print("# is an obstacle")
    print("- is the path taken by algorithm")
    print("PATH TAKEN BY THE ALGORITHM IS:-")
    x = back_pointer[goal]
    while x != start:
        print(x, end=" ")
        x = back_pointer[x]
    print(x)
    sys.exit()
    logger.debug("<<< Exiting do_something(back_pointer=%s,goal=%s,start=%s)", back_pointer, goal, start)


def valid(p: TPos):
    logger.debug(">>> Entering valid(p=%s)", p)
    if p[0] < 0 or p[0] > n - 1:
        return False
    logger.debug("<<< Exiting valid(p=%s)", p)
    return not (p[1] < 0 or p[1] > n - 1)


def expand_state(
    s,
    j,
    visited,
    g_function,
    close_list_anchor,
    close_list_inad,
    open_list,
    back_pointer,
):
    for itera in range(n_heuristic):
        open_list[itera].remove_element(s)
    # print("s", s)
    # print("j", j)
    (x, y) = s
    left = (x - 1, y)
    right = (x + 1, y)
    up = (x, y + 1)
    down = (x, y - 1)

    for neighbours in [left, right, up, down]:
        if neighbours not in blocks:
            if valid(neighbours) and neighbours not in visited:
                # print("neighbour", neighbours)
                visited.add(neighbours)
                back_pointer[neighbours] = -1
                g_function[neighbours] = float("inf")

            if valid(neighbours) and g_function[neighbours] > g_function[s] + 1:
                g_function[neighbours] = g_function[s] + 1
                back_pointer[neighbours] = s
                if neighbours not in close_list_anchor:
                    open_list[0].put(neighbours, key(neighbours, 0, goal, g_function))
                    if neighbours not in close_list_inad:
                        for var in range(1, n_heuristic):
                            if key(neighbours, var, goal, g_function) <= W2 * key(
                                neighbours, 0, goal, g_function
                            ):
                                open_list[j].put(
                                    neighbours, key(neighbours, var, goal, g_function)
                                )


def make_common_ground():
    logger.debug(">>> Entering make_common_ground()")
    some_list = []
    logger.debug("make_common_ground(): some_list → %s", some_list)
    for x in range(1, 5):
        for y in range(1, 6):
            some_list.append((x, y))

    for x in range(15, 20):
        some_list.append((x, 17))

    for x in range(10, 19):
        for y in range(1, 15):
            some_list.append((x, y))

    # L block
    for x in range(1, 4):
        for y in range(12, 19):
            some_list.append((x, y))
    for x in range(3, 13):
        for y in range(16, 19):
            some_list.append((x, y))
    logger.debug("<<< Exiting make_common_ground()")
    return some_list


heuristics = {0: consistent_heuristic, 1: heuristic_1, 2: heuristic_2}

blocks_blk = [
    (0, 1),
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 1),
    (5, 1),
    (6, 1),
    (7, 1),
    (8, 1),
    (9, 1),
    (10, 1),
    (11, 1),
    (12, 1),
    (13, 1),
    (14, 1),
    (15, 1),
    (16, 1),
    (17, 1),
    (18, 1),
    (19, 1),
]
blocks_all = make_common_ground()


blocks = blocks_blk
# hyper parameters
W1 = 1
W2 = 1
n = 20
n_heuristic = 3  # one consistent and two other inconsistent

# start and end destination
start = (0, 0)
goal = (n - 1, n - 1)

t = 1


def multi_a_star(start: TPos, goal: TPos, n_heuristic: int):
    logger.debug(">>> Entering multi_a_star(start=%s,goal=%s,n_heuristic=%s)", start, goal, n_heuristic)
    g_function = {start: 0, goal: float("inf")}
    logger.debug("multi_a_star(start=%s,goal=%s,n_heuristic=%s): g_function → %s", start, goal, n_heuristic, g_function)
    back_pointer = {start: -1, goal: -1}
    open_list = []
    logger.debug("multi_a_star(start=%s,goal=%s,n_heuristic=%s): back_pointer → %s", start, goal, n_heuristic, back_pointer)
    logger.debug("multi_a_star(start=%s,goal=%s,n_heuristic=%s): open_list → %s", start, goal, n_heuristic, open_list)
    visited = set()
    logger.debug("multi_a_star(start=%s,goal=%s,n_heuristic=%s): visited → %s", start, goal, n_heuristic, visited)

    for i in range(n_heuristic):
        open_list.append(PriorityQueue())
        open_list[i].put(start, key(start, i, goal, g_function))

    close_list_anchor: list[int] = []
    close_list_inad: list[int] = []
    while open_list[0].minkey() < float("inf"):
        for i in range(1, n_heuristic):
            # print(open_list[0].minkey(), open_list[i].minkey())
            if open_list[i].minkey() <= W2 * open_list[0].minkey():
                global t
                t += 1
                if g_function[goal] <= open_list[i].minkey():
                    if g_function[goal] < float("inf"):
                        do_something(back_pointer, goal, start)
                else:
                    _, get_s = open_list[i].top_show()
                    visited.add(get_s)
                    expand_state(
                        get_s,
                        i,
                        visited,
                        g_function,
                        close_list_anchor,
                        close_list_inad,
                        open_list,
                        back_pointer,
                    )
                    close_list_inad.append(get_s)
            elif g_function[goal] <= open_list[0].minkey():
                if g_function[goal] < float("inf"):
                    do_something(back_pointer, goal, start)
            else:
                get_s = open_list[0].top_show()
                logger.debug("multi_a_star(start=%s,goal=%s,n_heuristic=%s): get_s → %s", start, goal, n_heuristic, get_s)
                visited.add(get_s)
                expand_state(
                    get_s,
                    0,
                    visited,
                    g_function,
                    close_list_anchor,
                    close_list_inad,
                    open_list,
                    back_pointer,
                )
                close_list_anchor.append(get_s)
    print("No path found to goal")
    print()
    for i in range(n - 1, -1, -1):
        for j in range(n):
            if (j, i) in blocks:
                print("#", end=" ")
            elif (j, i) in back_pointer:
                if (j, i) == (n - 1, n - 1):
                    print("*", end=" ")
                else:
                    print("-", end=" ")
            else:
                print("*", end=" ")
            if (j, i) == (n - 1, n - 1):
                print("<-- End position", end=" ")
        print()
    print("^")
    print("Start position")
    print()
    print("# is an obstacle")
    print("- is the path taken by algorithm")
    logger.debug("<<< Exiting multi_a_star(start=%s,goal=%s,n_heuristic=%s)", start, goal, n_heuristic)


if __name__ == "__main__":
    multi_a_star(start, goal, n_heuristic)
