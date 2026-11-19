import heapq
import sys

import numpy as np
import logging
logger = logging.getLogger(__name__)

TPos = tuple[int, int]


class PriorityQueue:
    def __init__(self):
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.elements = []
        logger.debug("__init__(self=%s): self.elements → %s", self, self.elements, extra={"event.action": "__init__"})
        self.set = set()
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})
        logger.error("__init__(): self.set → %s", self.set, extra={"event.action": "__init__"})

    def minkey(self):
        logger.error(">>> Entering minkey()", extra={"event.action": "minkey"})
        if not self.empty():
            return self.elements[0][0]
        else:
            logger.warning("<<< Exiting minkey()", extra={"event.action": "minkey"})
            return float("inf")

    def empty(self):
        logger.error(">>> Entering empty()", extra={"event.action": "empty"})
        logger.warning("<<< Exiting empty()", extra={"event.action": "empty"})
        return len(self.elements) == 0

    def put(self, item, priority):
        logger.error(">>> Entering put(item=%s,priority=%s)", item, priority, extra={"event.action": "put", "logrite.item": item, "logrite.priority": priority})
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
                logger.warning("<<< Exiting put(item=%s,priority=%s)", item, priority, extra={"event.action": "put", "logrite.item": item, "logrite.priority": priority})

    def remove_element(self, item):
        logger.error(">>> Entering remove_element(item=%s)", item, extra={"event.action": "remove_element", "logrite.item": item})
        if item in self.set:
            self.set.remove(item)
            temp = []
            (pro, x) = heapq.heappop(self.elements)
            while x != item:
                temp.append((pro, x))
                (pro, x) = heapq.heappop(self.elements)
            for prito, yyy in temp:
                heapq.heappush(self.elements, (prito, yyy))
                logger.warning("<<< Exiting remove_element(item=%s)", item, extra={"event.action": "remove_element", "logrite.item": item})

    def top_show(self):
        logger.error(">>> Entering top_show()", extra={"event.action": "top_show"})
        logger.warning("<<< Exiting top_show()", extra={"event.action": "top_show"})
        return self.elements[0][1]

    def get(self):
        logger.error(">>> Entering get()", extra={"event.action": "get"})
        (priority, item) = heapq.heappop(self.elements)
        self.set.remove(item)
        logger.warning("<<< Exiting get()", extra={"event.action": "get"})
        return (priority, item)


def consistent_heuristic(p: TPos, goal: TPos):
    logger.error(">>> Entering consistent_heuristic(p=%s,goal=%s)", p, goal, extra={"event.action": "consistent_heuristic", "logrite.p": p, "logrite.goal": goal})
    # euclidean distance
    a = np.array(p)
    logger.error("consistent_heuristic(p=%s,goal=%s): a → %s", p, goal, a, extra={"event.action": "consistent_heuristic", "logrite.p": p, "logrite.goal": goal})
    b = np.array(goal)
    logger.error("consistent_heuristic(p=%s,goal=%s): b → %s", p, goal, b, extra={"event.action": "consistent_heuristic", "logrite.p": p, "logrite.goal": goal})
    logger.warning("<<< Exiting consistent_heuristic(p=%s,goal=%s)", p, goal, extra={"event.action": "consistent_heuristic", "logrite.p": p, "logrite.goal": goal})
    return np.linalg.norm(a - b)


def heuristic_2(p: TPos, goal: TPos):
    logger.error(">>> Entering heuristic_2(p=%s,goal=%s)", p, goal, extra={"event.action": "heuristic_2", "logrite.p": p, "logrite.goal": goal})
    # integer division by time variable
    logger.warning("<<< Exiting heuristic_2(p=%s,goal=%s)", p, goal, extra={"event.action": "heuristic_2", "logrite.p": p, "logrite.goal": goal})
    return consistent_heuristic(p, goal) // t


def heuristic_1(p: TPos, goal: TPos):
    logger.error(">>> Entering heuristic_1(p=%s,goal=%s)", p, goal, extra={"event.action": "heuristic_1", "logrite.p": p, "logrite.goal": goal})
    # manhattan distance
    logger.warning("<<< Exiting heuristic_1(p=%s,goal=%s)", p, goal, extra={"event.action": "heuristic_1", "logrite.p": p, "logrite.goal": goal})
    return abs(p[0] - goal[0]) + abs(p[1] - goal[1])


def key(start: TPos, i: int, goal: TPos, g_function: dict[TPos, float]):
    logger.error(">>> Entering key(start=%s,i=%s,goal=%s,g_function=%s)", start, i, goal, g_function, extra={"event.action": "key", "logrite.start": start, "logrite.i": i, "logrite.goal": goal, "logrite.g_function": g_function})
    ans = g_function[start] + W1 * heuristics[i](start, goal)
    logger.error("key(start=%s,i=%s,goal=%s,g_function=%s): ans → %s", start, i, goal, g_function, ans, extra={"event.action": "key", "logrite.start": start, "logrite.i": i, "logrite.goal": goal, "logrite.g_function": g_function})
    logger.warning("<<< Exiting key(start=%s,i=%s,goal=%s,g_function=%s)", start, i, goal, g_function, extra={"event.action": "key", "logrite.start": start, "logrite.i": i, "logrite.goal": goal, "logrite.g_function": g_function})
    return ans


def do_something(back_pointer, goal, start):
    logger.error(">>> Entering do_something(back_pointer=%s,goal=%s,start=%s)", back_pointer, goal, start, extra={"event.action": "do_something", "logrite.back_pointer": back_pointer, "logrite.goal": goal, "logrite.start": start})
    grid = np.char.chararray((n, n))
    logger.error("do_something(back_pointer=%s,goal=%s,start=%s): grid → %s", back_pointer, goal, start, grid, extra={"event.action": "do_something", "logrite.back_pointer": back_pointer, "logrite.goal": goal, "logrite.start": start})
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
    logger.warning("<<< Exiting do_something(back_pointer=%s,goal=%s,start=%s)", back_pointer, goal, start, extra={"event.action": "do_something", "logrite.back_pointer": back_pointer, "logrite.goal": goal, "logrite.start": start})


def valid(p: TPos):
    logger.error(">>> Entering valid(p=%s)", p, extra={"event.action": "valid", "logrite.p": p})
    if p[0] < 0 or p[0] > n - 1:
        return False
    logger.warning("<<< Exiting valid(p=%s)", p, extra={"event.action": "valid", "logrite.p": p})
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
    logger.error(">>> Entering expand_state(s=%s,j=%s,visited=%s,g_function=%s,close_list_anchor=%s,close_list_inad=%s,open_list=%s,back_pointer=%s)", s, j, visited, g_function, close_list_anchor, close_list_inad, open_list, back_pointer, extra={"event.action": "expand_state", "logrite.s": s, "logrite.j": j, "logrite.visited": visited, "logrite.g_function": g_function, "logrite.close_list_anchor": close_list_anchor, "logrite.close_list_inad": close_list_inad, "logrite.open_list": open_list, "logrite.back_pointer": back_pointer})
    for itera in range(n_heuristic):
        open_list[itera].remove_element(s)
    # print("s", s)
    # print("j", j)
    (x, y) = s
    left = (x - 1, y)
    logger.error("expand_state(s=%s,j=%s,visited=%s,g_function=%s,close_list_anchor=%s,close_list_inad=%s,open_list=%s,back_pointer=%s): left → %s", s, j, visited, g_function, close_list_anchor, close_list_inad, open_list, back_pointer, left, extra={"event.action": "expand_state", "logrite.s": s, "logrite.j": j, "logrite.visited": visited, "logrite.g_function": g_function, "logrite.close_list_anchor": close_list_anchor, "logrite.close_list_inad": close_list_inad, "logrite.open_list": open_list, "logrite.back_pointer": back_pointer})
    right = (x + 1, y)
    logger.error("expand_state(s=%s,j=%s,visited=%s,g_function=%s,close_list_anchor=%s,close_list_inad=%s,open_list=%s,back_pointer=%s): right → %s", s, j, visited, g_function, close_list_anchor, close_list_inad, open_list, back_pointer, right, extra={"event.action": "expand_state", "logrite.s": s, "logrite.j": j, "logrite.visited": visited, "logrite.g_function": g_function, "logrite.close_list_anchor": close_list_anchor, "logrite.close_list_inad": close_list_inad, "logrite.open_list": open_list, "logrite.back_pointer": back_pointer})
    up = (x, y + 1)
    logger.error("expand_state(s=%s,j=%s,visited=%s,g_function=%s,close_list_anchor=%s,close_list_inad=%s,open_list=%s,back_pointer=%s): up → %s", s, j, visited, g_function, close_list_anchor, close_list_inad, open_list, back_pointer, up, extra={"event.action": "expand_state", "logrite.s": s, "logrite.j": j, "logrite.visited": visited, "logrite.g_function": g_function, "logrite.close_list_anchor": close_list_anchor, "logrite.close_list_inad": close_list_inad, "logrite.open_list": open_list, "logrite.back_pointer": back_pointer})
    down = (x, y - 1)
    logger.error("expand_state(s=%s,j=%s,visited=%s,g_function=%s,close_list_anchor=%s,close_list_inad=%s,open_list=%s,back_pointer=%s): down → %s", s, j, visited, g_function, close_list_anchor, close_list_inad, open_list, back_pointer, down, extra={"event.action": "expand_state", "logrite.s": s, "logrite.j": j, "logrite.visited": visited, "logrite.g_function": g_function, "logrite.close_list_anchor": close_list_anchor, "logrite.close_list_inad": close_list_inad, "logrite.open_list": open_list, "logrite.back_pointer": back_pointer})

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
                                logger.warning("<<< Exiting expand_state(s=%s,j=%s,visited=%s,g_function=%s,close_list_anchor=%s,close_list_inad=%s,open_list=%s,back_pointer=%s)", s, j, visited, g_function, close_list_anchor, close_list_inad, open_list, back_pointer, extra={"event.action": "expand_state", "logrite.s": s, "logrite.j": j, "logrite.visited": visited, "logrite.g_function": g_function, "logrite.close_list_anchor": close_list_anchor, "logrite.close_list_inad": close_list_inad, "logrite.open_list": open_list, "logrite.back_pointer": back_pointer})


def make_common_ground():
    logger.error(">>> Entering make_common_ground()", extra={"event.action": "make_common_ground"})
    some_list = []
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
    logger.warning("<<< Exiting make_common_ground()", extra={"event.action": "make_common_ground"})
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
    logger.error(">>> Entering multi_a_star(start=%s,goal=%s,n_heuristic=%s)", start, goal, n_heuristic, extra={"event.action": "multi_a_star", "logrite.start": start, "logrite.goal": goal, "logrite.n_heuristic": n_heuristic})
    g_function = {start: 0, goal: float("inf")}
    logger.error("multi_a_star(start=%s,goal=%s,n_heuristic=%s): g_function → %s", start, goal, n_heuristic, g_function, extra={"event.action": "multi_a_star", "logrite.start": start, "logrite.goal": goal, "logrite.n_heuristic": n_heuristic})
    back_pointer = {start: -1, goal: -1}
    open_list = []
    visited = set()
    logger.error("multi_a_star(start=%s,goal=%s,n_heuristic=%s): visited → %s", start, goal, n_heuristic, visited, extra={"event.action": "multi_a_star", "logrite.start": start, "logrite.goal": goal, "logrite.n_heuristic": n_heuristic})

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
                logger.error("multi_a_star(start=%s,goal=%s,n_heuristic=%s): get_s → %s", start, goal, n_heuristic, get_s, extra={"event.action": "multi_a_star", "logrite.start": start, "logrite.goal": goal, "logrite.n_heuristic": n_heuristic})
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
    logger.warning("<<< Exiting multi_a_star(start=%s,goal=%s,n_heuristic=%s)", start, goal, n_heuristic, extra={"event.action": "multi_a_star", "logrite.start": start, "logrite.goal": goal, "logrite.n_heuristic": n_heuristic})


if __name__ == "__main__":
    multi_a_star(start, goal, n_heuristic)
