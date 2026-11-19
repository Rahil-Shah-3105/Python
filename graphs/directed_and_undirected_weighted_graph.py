from collections import deque
from math import floor
from random import random
from time import time
import logging
logger = logging.getLogger(__name__)

# the default weight is 1 if not assigned but all the implementation is weighted


class DirectedGraph:
    def __init__(self):
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.graph = {}
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})
        logger.debug("__init__(self=%s): self.graph → %s", self, self.graph, extra={"event.action": "__init__"})

    # adding vertices and edges
    # adding the weight is optional
    # handles repetition
    def add_pair(self, u, v, w=1):
        logger.error(">>> Entering add_pair(u=%s,v=%s,w=%s)", u, v, w, extra={"event.action": "add_pair", "logrite.u": u, "logrite.v": v})
        if self.graph.get(u):
            if self.graph[u].count([w, v]) == 0:
                self.graph[u].append([w, v])
        else:
            self.graph[u] = [[w, v]]
        if not self.graph.get(v):
            self.graph[v] = []
            logger.warning("<<< Exiting add_pair(u=%s,v=%s,w=%s)", u, v, w, extra={"event.action": "add_pair", "logrite.u": u, "logrite.v": v})

    def all_nodes(self):
        logger.error(">>> Entering all_nodes()", extra={"event.action": "all_nodes"})
        logger.warning("<<< Exiting all_nodes()", extra={"event.action": "all_nodes"})
        return list(self.graph)

    # handles if the input does not exist
    def remove_pair(self, u, v):
        logger.error(">>> Entering remove_pair(u=%s,v=%s)", u, v, extra={"event.action": "remove_pair", "logrite.u": u, "logrite.v": v})
        if self.graph.get(u):
            for _ in self.graph[u]:
                if _[1] == v:
                    self.graph[u].remove(_)
                    logger.warning("<<< Exiting remove_pair(u=%s,v=%s)", u, v, extra={"event.action": "remove_pair", "logrite.u": u, "logrite.v": v})

    # if no destination is meant the default value is -1
    def dfs(self, s=-2, d=-1):
        logger.error(">>> Entering dfs(s=%s,d=%s)", s, d, extra={"event.action": "dfs", "logrite.s": s, "logrite.d": d})
        if s == d:
            return []
        stack = []
        visited = []
        if s == -2:
            s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        ss = s

        while True:
            # check if there is any non isolated nodes
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if visited.count(node[1]) < 1:
                        if node[1] == d:
                            visited.append(d)
                            return visited
                        else:
                            stack.append(node[1])
                            visited.append(node[1])
                            ss = node[1]
                            break

            # check if all the children are visited
            if s == ss:
                stack.pop()
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                s = ss

            # check if se have reached the starting point
            if len(stack) == 0:
                logger.warning("<<< Exiting dfs(s=%s,d=%s)", s, d, extra={"event.action": "dfs", "logrite.s": s, "logrite.d": d})
                return visited

    # c is the count of nodes you want and if you leave it or pass -1 to the function
    # the count will be random from 10 to 10000
    def fill_graph_randomly(self, c=-1):
        logger.error(">>> Entering fill_graph_randomly(c=%s)", c, extra={"event.action": "fill_graph_randomly", "logrite.c": c})
        if c == -1:
            c = floor(random() * 10000) + 10
            logger.error("fill_graph_randomly(c=%s): c → %s", c, c, extra={"event.action": "fill_graph_randomly", "logrite.c": c})
        for i in range(c):
            # every vertex has max 100 edges
            for _ in range(floor(random() * 102) + 1):
                n = floor(random() * c) + 1
                logger.error("fill_graph_randomly(c=%s): n → %s", c, n, extra={"event.action": "fill_graph_randomly", "logrite.c": c})
                if n != i:
                    self.add_pair(i, n, 1)
                    logger.warning("<<< Exiting fill_graph_randomly(c=%s)", c, extra={"event.action": "fill_graph_randomly", "logrite.c": c})

    def bfs(self, s=-2):
        logger.error(">>> Entering bfs(s=%s)", s, extra={"event.action": "bfs", "logrite.s": s})
        d = deque()
        logger.error("bfs(s=%s): d → %s", s, d, extra={"event.action": "bfs", "logrite.s": s})
        visited = []
        if s == -2:
            s = next(iter(self.graph))
            logger.error("bfs(s=%s): s → %s", s, s, extra={"event.action": "bfs", "logrite.s": s})
        d.append(s)
        visited.append(s)
        while d:
            s = d.popleft()
            if len(self.graph[s]) != 0:
                for node in self.graph[s]:
                    if visited.count(node[1]) < 1:
                        d.append(node[1])
                        visited.append(node[1])
        logger.warning("<<< Exiting bfs(s=%s)", s, extra={"event.action": "bfs", "logrite.s": s})
        return visited

    def in_degree(self, u):
        logger.error(">>> Entering in_degree(u=%s)", u, extra={"event.action": "in_degree", "logrite.u": u})
        count = 0
        logger.error("in_degree(u=%s): count → %s", u, count, extra={"event.action": "in_degree", "logrite.u": u})
        for x in self.graph:
            for y in self.graph[x]:
                if y[1] == u:
                    count += 1
        logger.warning("<<< Exiting in_degree(u=%s)", u, extra={"event.action": "in_degree", "logrite.u": u})
        return count

    def out_degree(self, u):
        logger.error(">>> Entering out_degree(u=%s)", u, extra={"event.action": "out_degree", "logrite.u": u})
        logger.warning("<<< Exiting out_degree(u=%s)", u, extra={"event.action": "out_degree", "logrite.u": u})
        return len(self.graph[u])

    def topological_sort(self, s=-2):
        logger.error(">>> Entering topological_sort(s=%s)", s, extra={"event.action": "topological_sort", "logrite.s": s})
        stack = []
        visited = []
        if s == -2:
            s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        ss = s
        sorted_nodes = []

        while True:
            # check if there is any non isolated nodes
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break

            # check if all the children are visited
            if s == ss:
                sorted_nodes.append(stack.pop())
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                s = ss

            # check if se have reached the starting point
            if len(stack) == 0:
                logger.warning("<<< Exiting topological_sort(s=%s)", s, extra={"event.action": "topological_sort", "logrite.s": s})
                return sorted_nodes

    def cycle_nodes(self):
        logger.error(">>> Entering cycle_nodes()", extra={"event.action": "cycle_nodes"})
        stack = []
        visited = []
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        indirect_parents = []
        ss = s
        on_the_way_back = False
        anticipating_nodes = set()
        logger.error("cycle_nodes(): anticipating_nodes → %s", anticipating_nodes, extra={"event.action": "cycle_nodes"})

        while True:
            # check if there is any non isolated nodes
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if (
                        visited.count(node[1]) > 0
                        and node[1] != parent
                        and indirect_parents.count(node[1]) > 0
                        and not on_the_way_back
                    ):
                        len_stack = len(stack) - 1
                        logger.error("cycle_nodes(): len_stack → %s", len_stack, extra={"event.action": "cycle_nodes"})
                        while len_stack >= 0:
                            if stack[len_stack] == node[1]:
                                anticipating_nodes.add(node[1])
                                break
                            else:
                                anticipating_nodes.add(stack[len_stack])
                                len_stack -= 1
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break

            # check if all the children are visited
            if s == ss:
                stack.pop()
                on_the_way_back = True
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                on_the_way_back = False
                indirect_parents.append(parent)
                parent = s
                s = ss

            # check if se have reached the starting point
            if len(stack) == 0:
                logger.warning("<<< Exiting cycle_nodes()", extra={"event.action": "cycle_nodes"})
                return list(anticipating_nodes)

    def has_cycle(self):
        logger.error(">>> Entering has_cycle()", extra={"event.action": "has_cycle"})
        stack = []
        visited = []
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        indirect_parents = []
        ss = s
        on_the_way_back = False
        anticipating_nodes = set()
        logger.error("has_cycle(): anticipating_nodes → %s", anticipating_nodes, extra={"event.action": "has_cycle"})

        while True:
            # check if there is any non isolated nodes
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if (
                        visited.count(node[1]) > 0
                        and node[1] != parent
                        and indirect_parents.count(node[1]) > 0
                        and not on_the_way_back
                    ):
                        len_stack_minus_one = len(stack) - 1
                        logger.error("has_cycle(): len_stack_minus_one → %s", len_stack_minus_one, extra={"event.action": "has_cycle"})
                        while len_stack_minus_one >= 0:
                            if stack[len_stack_minus_one] == node[1]:
                                anticipating_nodes.add(node[1])
                                break
                            else:
                                return True
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break

            # check if all the children are visited
            if s == ss:
                stack.pop()
                on_the_way_back = True
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                on_the_way_back = False
                indirect_parents.append(parent)
                parent = s
                s = ss

            # check if se have reached the starting point
            if len(stack) == 0:
                logger.warning("<<< Exiting has_cycle()", extra={"event.action": "has_cycle"})
                return False

    def dfs_time(self, s=-2, e=-1):
        logger.error(">>> Entering dfs_time(s=%s,e=%s)", s, e, extra={"event.action": "dfs_time", "logrite.s": s, "logrite.e": e})
        begin = time()
        logger.error("dfs_time(s=%s,e=%s): begin → %s", s, e, begin, extra={"event.action": "dfs_time", "logrite.s": s, "logrite.e": e})
        self.dfs(s, e)
        end = time()
        logger.error("dfs_time(s=%s,e=%s): end → %s", s, e, end, extra={"event.action": "dfs_time", "logrite.s": s, "logrite.e": e})
        logger.warning("<<< Exiting dfs_time(s=%s,e=%s)", s, e, extra={"event.action": "dfs_time", "logrite.s": s, "logrite.e": e})
        return end - begin

    def bfs_time(self, s=-2):
        logger.error(">>> Entering bfs_time(s=%s)", s, extra={"event.action": "bfs_time", "logrite.s": s})
        begin = time()
        logger.error("bfs_time(s=%s): begin → %s", s, begin, extra={"event.action": "bfs_time", "logrite.s": s})
        self.bfs(s)
        end = time()
        logger.error("bfs_time(s=%s): end → %s", s, end, extra={"event.action": "bfs_time", "logrite.s": s})
        logger.warning("<<< Exiting bfs_time(s=%s)", s, extra={"event.action": "bfs_time", "logrite.s": s})
        return end - begin


class Graph:
    def __init__(self):
        self.graph = {}

    # adding vertices and edges
    # adding the weight is optional
    # handles repetition
    def add_pair(self, u, v, w=1):
        # check if the u exists
        if self.graph.get(u):
            # if there already is a edge
            if self.graph[u].count([w, v]) == 0:
                self.graph[u].append([w, v])
        else:
            # if u does not exist
            self.graph[u] = [[w, v]]
        # add the other way
        if self.graph.get(v):
            # if there already is a edge
            if self.graph[v].count([w, u]) == 0:
                self.graph[v].append([w, u])
        else:
            # if u does not exist
            self.graph[v] = [[w, u]]

    # handles if the input does not exist
    def remove_pair(self, u, v):
        if self.graph.get(u):
            for _ in self.graph[u]:
                if _[1] == v:
                    self.graph[u].remove(_)
        # the other way round
        if self.graph.get(v):
            for _ in self.graph[v]:
                if _[1] == u:
                    self.graph[v].remove(_)

    # if no destination is meant the default value is -1
    def dfs(self, s=-2, d=-1):
        if s == d:
            return []
        stack = []
        visited = []
        if s == -2:
            s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        ss = s

        while True:
            # check if there is any non isolated nodes
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if visited.count(node[1]) < 1:
                        if node[1] == d:
                            visited.append(d)
                            return visited
                        else:
                            stack.append(node[1])
                            visited.append(node[1])
                            ss = node[1]
                            break

            # check if all the children are visited
            if s == ss:
                stack.pop()
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                s = ss

            # check if se have reached the starting point
            if len(stack) == 0:
                return visited

    # c is the count of nodes you want and if you leave it or pass -1 to the function
    # the count will be random from 10 to 10000
    def fill_graph_randomly(self, c=-1):
        if c == -1:
            c = floor(random() * 10000) + 10
        for i in range(c):
            # every vertex has max 100 edges
            for _ in range(floor(random() * 102) + 1):
                n = floor(random() * c) + 1
                if n != i:
                    self.add_pair(i, n, 1)

    def bfs(self, s=-2):
        d = deque()
        visited = []
        if s == -2:
            s = next(iter(self.graph))
        d.append(s)
        visited.append(s)
        while d:
            s = d.popleft()
            if len(self.graph[s]) != 0:
                for node in self.graph[s]:
                    if visited.count(node[1]) < 1:
                        d.append(node[1])
                        visited.append(node[1])
        return visited

    def degree(self, u):
        logger.error(">>> Entering degree(u=%s)", u, extra={"event.action": "degree", "logrite.u": u})
        logger.warning("<<< Exiting degree(u=%s)", u, extra={"event.action": "degree", "logrite.u": u})
        return len(self.graph[u])

    def cycle_nodes(self):
        stack = []
        visited = []
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        indirect_parents = []
        ss = s
        on_the_way_back = False
        anticipating_nodes = set()

        while True:
            # check if there is any non isolated nodes
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if (
                        visited.count(node[1]) > 0
                        and node[1] != parent
                        and indirect_parents.count(node[1]) > 0
                        and not on_the_way_back
                    ):
                        len_stack = len(stack) - 1
                        while len_stack >= 0:
                            if stack[len_stack] == node[1]:
                                anticipating_nodes.add(node[1])
                                break
                            else:
                                anticipating_nodes.add(stack[len_stack])
                                len_stack -= 1
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break

            # check if all the children are visited
            if s == ss:
                stack.pop()
                on_the_way_back = True
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                on_the_way_back = False
                indirect_parents.append(parent)
                parent = s
                s = ss

            # check if se have reached the starting point
            if len(stack) == 0:
                return list(anticipating_nodes)

    def has_cycle(self):
        stack = []
        visited = []
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        indirect_parents = []
        ss = s
        on_the_way_back = False
        anticipating_nodes = set()

        while True:
            # check if there is any non isolated nodes
            if len(self.graph[s]) != 0:
                ss = s
                for node in self.graph[s]:
                    if (
                        visited.count(node[1]) > 0
                        and node[1] != parent
                        and indirect_parents.count(node[1]) > 0
                        and not on_the_way_back
                    ):
                        len_stack_minus_one = len(stack) - 1
                        while len_stack_minus_one >= 0:
                            if stack[len_stack_minus_one] == node[1]:
                                anticipating_nodes.add(node[1])
                                break
                            else:
                                return True
                    if visited.count(node[1]) < 1:
                        stack.append(node[1])
                        visited.append(node[1])
                        ss = node[1]
                        break

            # check if all the children are visited
            if s == ss:
                stack.pop()
                on_the_way_back = True
                if len(stack) != 0:
                    s = stack[len(stack) - 1]
            else:
                on_the_way_back = False
                indirect_parents.append(parent)
                parent = s
                s = ss

            # check if se have reached the starting point
            if len(stack) == 0:
                return False

    def all_nodes(self):
        return list(self.graph)

    def dfs_time(self, s=-2, e=-1):
        begin = time()
        self.dfs(s, e)
        end = time()
        return end - begin

    def bfs_time(self, s=-2):
        begin = time()
        self.bfs(s)
        end = time()
        return end - begin
