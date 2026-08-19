from collections import deque
from math import floor
from random import random
from time import time
import logging
logger = logging.getLogger(__name__)

# the default weight is 1 if not assigned but all the implementation is weighted


class DirectedGraph:
    def __init__(self):
        logger.debug(">>> Entering __init__()")
        self.graph = {}
        logger.debug("__init__(self=%s): self.graph → %s", self, self.graph)
        logger.debug("<<< Exiting __init__()")

    # adding vertices and edges
    # adding the weight is optional
    # handles repetition
    def add_pair(self, u, v, w=1):
        if self.graph.get(u):
            if self.graph[u].count([w, v]) == 0:
                self.graph[u].append([w, v])
        else:
            self.graph[u] = [[w, v]]
        if not self.graph.get(v):
            self.graph[v] = []
            logger.debug(">>> Entering add_pair(u=%s,v=%s,w=%s)", u, v, w)
            logger.debug("<<< Exiting add_pair(u=%s,v=%s,w=%s)", u, v, w)

    def all_nodes(self):
        logger.debug(">>> Entering all_nodes()")
        logger.debug("<<< Exiting all_nodes()")
        return list(self.graph)

    # handles if the input does not exist
    def remove_pair(self, u, v):
        if self.graph.get(u):
            for _ in self.graph[u]:
                if _[1] == v:
                    self.graph[u].remove(_)

    logger.debug(">>> Entering remove_pair(u=%s,v=%s)", u, v)
    logger.debug("<<< Exiting remove_pair(u=%s,v=%s)", u, v)
    # if no destination is meant the default value is -1
    def dfs(self, s=-2, d=-1):
        logger.debug(">>> Entering dfs(s=%s,d=%s)", s, d)
        if s == d:
            return []
        stack = []
        logger.debug("dfs(self=%s,s=%s,d=%s): stack → %s", self, s, d, stack)
        visited = []
        logger.debug("dfs(self=%s,s=%s,d=%s): visited → %s", self, s, d, visited)
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
                logger.debug("<<< Exiting dfs(s=%s,d=%s)", s, d)
                return visited

    # c is the count of nodes you want and if you leave it or pass -1 to the function
    # the count will be random from 10 to 10000
    def fill_graph_randomly(self, c=-1):
        logger.debug(">>> Entering fill_graph_randomly(c=%s)", c)
        if c == -1:
            c = floor(random() * 10000) + 10
            logger.debug("fill_graph_randomly(c=%s): c → %s", c, c)
        for i in range(c):
            # every vertex has max 100 edges
            for _ in range(floor(random() * 102) + 1):
                n = floor(random() * c) + 1
                logger.debug("fill_graph_randomly(c=%s): n → %s", c, n)
                if n != i:
                    self.add_pair(i, n, 1)
                    logger.debug("<<< Exiting fill_graph_randomly(c=%s)", c)

    def bfs(self, s=-2):
        logger.debug(">>> Entering bfs(s=%s)", s)
        d = deque()
        logger.debug("bfs(s=%s): d → %s", s, d)
        visited = []
        logger.debug("bfs(self=%s,s=%s): visited → %s", self, s, visited)
        if s == -2:
            s = next(iter(self.graph))
            logger.debug("bfs(s=%s): s → %s", s, s)
        d.append(s)
        visited.append(s)
        while d:
            s = d.popleft()
            if len(self.graph[s]) != 0:
                for node in self.graph[s]:
                    if visited.count(node[1]) < 1:
                        d.append(node[1])
                        visited.append(node[1])
        logger.debug("<<< Exiting bfs(s=%s)", s)
        return visited

    def in_degree(self, u):
        logger.debug(">>> Entering in_degree(u=%s)", u)
        count = 0
        logger.debug("in_degree(u=%s): count → %s", u, count)
        logger.debug("in_degree(self=%s,u=%s): count → %s", self, u, count)
        for x in self.graph:
            for y in self.graph[x]:
                if y[1] == u:
                    count += 1
        logger.debug("<<< Exiting in_degree(u=%s)", u)
        return count

    def out_degree(self, u):
        logger.debug(">>> Entering out_degree(u=%s)", u)
        logger.debug("<<< Exiting out_degree(u=%s)", u)
        return len(self.graph[u])

    def topological_sort(self, s=-2):
        logger.debug(">>> Entering topological_sort(s=%s)", s)
        stack = []
        logger.debug("topological_sort(self=%s,s=%s): stack → %s", self, s, stack)
        visited = []
        logger.debug("topological_sort(self=%s,s=%s): visited → %s", self, s, visited)
        if s == -2:
            s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        ss = s
        sorted_nodes = []
        logger.debug("topological_sort(self=%s,s=%s): sorted_nodes → %s", self, s, sorted_nodes)

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
                logger.debug("<<< Exiting topological_sort(s=%s)", s)
                return sorted_nodes

    def cycle_nodes(self):
        logger.debug(">>> Entering cycle_nodes()")
        stack = []
        logger.debug("cycle_nodes(self=%s): stack → %s", self, stack)
        visited = []
        logger.debug("cycle_nodes(self=%s): visited → %s", self, visited)
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        logger.debug("cycle_nodes(self=%s): parent → %s", self, parent)
        indirect_parents = []
        logger.debug("cycle_nodes(self=%s): indirect_parents → %s", self, indirect_parents)
        ss = s
        on_the_way_back = False
        logger.debug("cycle_nodes(self=%s): on_the_way_back → %s", self, on_the_way_back)
        anticipating_nodes = set()
        logger.debug("cycle_nodes(self=%s): anticipating_nodes → %s", self, anticipating_nodes)
        logger.debug("cycle_nodes(): anticipating_nodes → %s", anticipating_nodes)

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
                        logger.debug("cycle_nodes(self=%s): len_stack → %s", self, len_stack)
                        logger.debug("cycle_nodes(): len_stack → %s", len_stack)
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
                logger.debug("<<< Exiting cycle_nodes()")
                return list(anticipating_nodes)

    def has_cycle(self):
        logger.debug(">>> Entering has_cycle()")
        stack = []
        logger.debug("has_cycle(self=%s): stack → %s", self, stack)
        visited = []
        logger.debug("has_cycle(self=%s): visited → %s", self, visited)
        s = next(iter(self.graph))
        stack.append(s)
        visited.append(s)
        parent = -2
        logger.debug("has_cycle(self=%s): parent → %s", self, parent)
        indirect_parents = []
        logger.debug("has_cycle(self=%s): indirect_parents → %s", self, indirect_parents)
        ss = s
        on_the_way_back = False
        logger.debug("has_cycle(self=%s): on_the_way_back → %s", self, on_the_way_back)
        anticipating_nodes = set()
        logger.debug("has_cycle(self=%s): anticipating_nodes → %s", self, anticipating_nodes)
        logger.debug("has_cycle(): anticipating_nodes → %s", anticipating_nodes)

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
                        logger.debug("has_cycle(self=%s): len_stack_minus_one → %s", self, len_stack_minus_one)
                        logger.debug("has_cycle(): len_stack_minus_one → %s", len_stack_minus_one)
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
                logger.debug("<<< Exiting has_cycle()")
                return False

    def dfs_time(self, s=-2, e=-1):
        logger.debug(">>> Entering dfs_time(s=%s,e=%s)", s, e)
        logger.debug("dfs_time(self=%s,s=%s,e=%s): end → %s", self, s, e, end)
        logger.debug("dfs_time(s=%s,e=%s): end → %s", s, e, end)
        begin = time()
        logger.debug("dfs_time(s=%s,e=%s): begin → %s", s, e, begin)
        logger.debug("dfs_time(self=%s,s=%s,e=%s): begin → %s", self, s, e, begin)
        self.dfs(s, e)
        end = time()
        logger.debug("<<< Exiting dfs_time(s=%s,e=%s)", s, e)
        return end - begin

    def bfs_time(self, s=-2):
        logger.debug(">>> Entering bfs_time(s=%s)", s)
        logger.debug("bfs_time(self=%s,s=%s): end → %s", self, s, end)
        logger.debug("bfs_time(s=%s): end → %s", s, end)
        begin = time()
        logger.debug("bfs_time(s=%s): begin → %s", s, begin)
        logger.debug("bfs_time(self=%s,s=%s): begin → %s", self, s, begin)
        self.bfs(s)
        end = time()
        logger.debug("<<< Exiting bfs_time(s=%s)", s)
        return end - begin


class Graph:
    def __init__(self):
        self.graph = {}

    # adding vertices and edges
    # adding the weight is optional
    # handles repetition
    def add_pair(self, u, v, w=1):
        logger.debug(">>> Entering add_pair(u=%s,v=%s,w=%s)", u, v, w)
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
        logger.debug(">>> Entering remove_pair(u=%s,v=%s)", u, v)
        if self.graph.get(u):
            for _ in self.graph[u]:
                if _[1] == v:
                    self.graph[u].remove(_)
        # the other way round
        if self.graph.get(v):
            for _ in self.graph[v]:
                if _[1] == u:
                    self.graph[v].remove(_)
                    logger.debug("<<< Exiting remove_pair(u=%s,v=%s)", u, v)

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
        logger.debug(">>> Entering degree(u=%s)", u)
        logger.debug("<<< Exiting degree(u=%s)", u)
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
