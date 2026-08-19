from __future__ import annotations
import logging
logger = logging.getLogger(__name__)


def dfs(u):
    logger.debug(">>> Entering dfs(u=%s)", u)
    global graph, reversed_graph, scc, component, visit, stack
    if visit[u]:
        logger.debug("<<< Exiting dfs(u=%s)", u)
        return
    visit[u] = True
    for v in graph[u]:
        dfs(v)
    stack.append(u)


def dfs2(u):
    logger.debug(">>> Entering dfs2(u=%s)", u)
    global graph, reversed_graph, scc, component, visit, stack
    if visit[u]:
        logger.debug("<<< Exiting dfs2(u=%s)", u)
        return
    visit[u] = True
    component.append(u)
    for v in reversed_graph[u]:
        dfs2(v)


def kosaraju():
    logger.debug(">>> Entering kosaraju()")
    global graph, reversed_graph, scc, component, visit, stack
    for i in range(n):
        dfs(i)
    visit = [False] * n
    logger.debug("kosaraju(): visit → %s", visit)
    for i in stack[::-1]:
        if visit[i]:
            continue
        component = []
        logger.debug("kosaraju(): component → %s", component)
        dfs2(i)
        scc.append(component)
    logger.debug("<<< Exiting kosaraju()")
    return scc


if __name__ == "__main__":
    # n - no of nodes, m - no of edges
    n, m = list(map(int, input().strip().split()))

    graph: list[list[int]] = [[] for _ in range(n)]  # graph
    reversed_graph: list[list[int]] = [[] for i in range(n)]  # reversed graph
    # input graph data (edges)
    for _ in range(m):
        u, v = list(map(int, input().strip().split()))
        graph[u].append(v)
        reversed_graph[v].append(u)

    stack: list[int] = []
    visit: list[bool] = [False] * n
    scc: list[int] = []
    component: list[int] = []
    print(kosaraju())
