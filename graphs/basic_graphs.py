from collections import deque
import logging
logger = logging.getLogger(__name__)


def _input(message):
    logger.debug(">>> Entering _input(message=%s)", message)
    logger.debug("<<< Exiting _input(message=%s)", message)
    return input(message).strip().split(" ")


def initialize_unweighted_directed_graph(
    node_count: int, edge_count: int
) -> dict[int, list[int]]:
    graph: dict[int, list[int]] = {}
    for i in range(node_count):
        graph[i + 1] = []

    for e in range(edge_count):
        x, y = (int(i) for i in _input(f"Edge {e + 1}: <node1> <node2> "))
        graph[x].append(y)
    return graph


def initialize_unweighted_undirected_graph(
    node_count: int, edge_count: int
) -> dict[int, list[int]]:
    graph: dict[int, list[int]] = {}
    for i in range(node_count):
        graph[i + 1] = []

    for e in range(edge_count):
        x, y = (int(i) for i in _input(f"Edge {e + 1}: <node1> <node2> "))
        graph[x].append(y)
        graph[y].append(x)
    return graph


def initialize_weighted_undirected_graph(
    node_count: int, edge_count: int
) -> dict[int, list[tuple[int, int]]]:
    graph: dict[int, list[tuple[int, int]]] = {}
    for i in range(node_count):
        graph[i + 1] = []

    for e in range(edge_count):
        x, y, w = (int(i) for i in _input(f"Edge {e + 1}: <node1> <node2> <weight> "))
        graph[x].append((y, w))
        graph[y].append((x, w))
    return graph


if __name__ == "__main__":
    n, m = (int(i) for i in _input("Number of nodes and edges: "))

    graph_choice = int(
        _input(
            "Press 1 or 2 or 3 \n"
            "1. Unweighted directed \n"
            "2. Unweighted undirected \n"
            "3. Weighted undirected \n"
        )[0]
    )

    g = {
        1: initialize_unweighted_directed_graph,
        2: initialize_unweighted_undirected_graph,
        3: initialize_weighted_undirected_graph,
    }[graph_choice](n, m)


"""
--------------------------------------------------------------------------------
    Depth First Search.
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  vis - Set of visited nodes
                S - Traversal Stack
--------------------------------------------------------------------------------
"""


def dfs(g, s):
    """
    >>> dfs({1: [2, 3], 2: [4, 5], 3: [], 4: [], 5: []}, 1)
    1
    2
    4
    5
    3
    """
    logger.debug(">>> Entering dfs(g=%s,s=%s)", g, s)
    vis, _s = {s}, [s]
    print(s)
    while _s:
        flag = 0
        logger.debug("dfs(g=%s,s=%s): flag → %s", g, s, flag)
        for i in g[_s[-1]]:
            if i not in vis:
                _s.append(i)
                vis.add(i)
                flag = 1
                print(i)
                break
        if not flag:
            _s.pop()
            logger.debug("<<< Exiting dfs(g=%s,s=%s)", g, s)


"""
--------------------------------------------------------------------------------
    Breadth First Search.
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  vis - Set of visited nodes
                Q - Traversal Stack
--------------------------------------------------------------------------------
"""


def bfs(g, s):
    """
    >>> bfs({1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [], 5: [8], 6: [], 7: [], 8: []}, 1)
    1
    2
    3
    4
    5
    6
    7
    8
    """
    logger.debug(">>> Entering bfs(g=%s,s=%s)", g, s)
    vis, q = {s}, deque([s])
    print(s)
    while q:
        u = q.popleft()
        logger.debug("bfs(g=%s,s=%s): u → %s", g, s, u)
        for v in g[u]:
            if v not in vis:
                vis.add(v)
                q.append(v)
                print(v)
                logger.debug("<<< Exiting bfs(g=%s,s=%s)", g, s)


"""
--------------------------------------------------------------------------------
    Dijkstra's shortest path Algorithm
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  dist - Dictionary storing shortest distance from s to every other node
                known - Set of knows nodes
                path - Preceding node in path
--------------------------------------------------------------------------------
"""


def dijk(g, s):
    """
    dijk({1: [(2, 7), (3, 9), (6, 14)],
        2: [(1, 7), (3, 10), (4, 15)],
        3: [(1, 9), (2, 10), (4, 11), (6, 2)],
        4: [(2, 15), (3, 11), (5, 6)],
        5: [(4, 6), (6, 9)],
        6: [(1, 14), (3, 2), (5, 9)]}, 1)
    7
    9
    11
    20
    20
    """
    logger.debug(">>> Entering dijk(g=%s,s=%s)", g, s)
    dist, known, path = {s: 0}, set(), {s: 0}
    while True:
        if len(known) == len(g) - 1:
            break
        mini = 100000
        logger.debug("dijk(g=%s,s=%s): mini → %s", g, s, mini)
        for key, value in dist:
            if key not in known and value < mini:
                mini = value
                u = key
        known.add(u)
        for v in g[u]:
            if v[0] not in known and dist[u] + v[1] < dist.get(v[0], 100000):
                dist[v[0]] = dist[u] + v[1]
                path[v[0]] = u
    for key, value in dist.items():
        if key != s:
            print(value)
            logger.debug("<<< Exiting dijk(g=%s,s=%s)", g, s)


"""
--------------------------------------------------------------------------------
    Topological Sort
--------------------------------------------------------------------------------
"""


def topo(g, ind=None, q=None):
    logger.debug(">>> Entering topo(g=%s,ind=%s,q=%s)", g, ind, q)
    if q is None:
        q = [1]
        logger.debug("topo(g=%s,ind=%s,q=%s): q → %s", g, ind, q, q)
    if ind is None:
        ind = [0] * (len(g) + 1)  # SInce oth Index is ignored
        logger.debug("topo(g=%s,ind=%s,q=%s): ind → %s", g, ind, q, ind)
        for u in g:
            for v in g[u]:
                ind[v] += 1
        q = deque()
        for i in g:
            if ind[i] == 0:
                q.append(i)
    if len(q) == 0:
        logger.debug("<<< Exiting topo(g=%s,ind=%s,q=%s)", g, ind, q)
        return
    v = q.popleft()
    print(v)
    for w in g[v]:
        ind[w] -= 1
        if ind[w] == 0:
            q.append(w)
    topo(g, ind, q)


"""
--------------------------------------------------------------------------------
    Reading an Adjacency matrix
--------------------------------------------------------------------------------
"""


def adjm():
    r"""
    Reading an Adjacency matrix

    Parameters:
        None

    Returns:
        tuple: A tuple containing a list of edges and number of edges

    Example:
    >>> # Simulate user input for 3 nodes
    >>> input_data = "4\n0 1 0 1\n1 0 1 0\n0 1 0 1\n1 0 1 0\n"
    >>> import sys,io
    >>> original_input = sys.stdin
    >>> sys.stdin = io.StringIO(input_data)  # Redirect stdin for testing
    >>> adjm()
    ([(0, 1, 0, 1), (1, 0, 1, 0), (0, 1, 0, 1), (1, 0, 1, 0)], 4)
    >>> sys.stdin = original_input  # Restore original stdin
    """
    logger.debug(">>> Entering adjm()")
    n = int(input().strip())
    logger.debug("adjm(): n → %s", n)
    a = []
    for _ in range(n):
        a.append(tuple(map(int, input().strip().split())))
    logger.debug("<<< Exiting adjm()")
    return a, n


"""
--------------------------------------------------------------------------------
    Floyd Warshall's algorithm
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  dist - Dictionary storing shortest distance from s to every other node
                known - Set of knows nodes
                path - Preceding node in path

--------------------------------------------------------------------------------
"""


def floy(a_and_n):
    logger.debug(">>> Entering floy(a_and_n=%s)", a_and_n)
    (a, n) = a_and_n
    dist = list(a)
    logger.debug("floy(a_and_n=%s): dist → %s", a_and_n, dist)
    path = [[0] * n for i in range(n)]
    logger.debug("floy(a_and_n=%s): path → %s", a_and_n, path)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][k] = k
    print(dist)
    logger.debug("<<< Exiting floy(a_and_n=%s)", a_and_n)


"""
--------------------------------------------------------------------------------
    Prim's MST Algorithm
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  dist - Dictionary storing shortest distance from s to nearest node
                known - Set of knows nodes
                path - Preceding node in path
--------------------------------------------------------------------------------
"""


def prim(g, s):
    logger.debug(">>> Entering prim(g=%s,s=%s)", g, s)
    dist, known, path = {s: 0}, set(), {s: 0}
    while True:
        if len(known) == len(g) - 1:
            break
        mini = 100000
        logger.debug("prim(g=%s,s=%s): mini → %s", g, s, mini)
        for key, value in dist.items():
            if key not in known and value < mini:
                mini = value
                u = key
        known.add(u)
        for v in g[u]:
            if v[0] not in known and v[1] < dist.get(v[0], 100000):
                dist[v[0]] = v[1]
                path[v[0]] = u
    logger.debug("<<< Exiting prim(g=%s,s=%s)", g, s)
    return dist


"""
--------------------------------------------------------------------------------
    Accepting Edge list
        Vars :  n - Number of nodes
                m - Number of edges
        Returns : l - Edge list
                n - Number of Nodes
--------------------------------------------------------------------------------
"""


def edglist():
    r"""
    Get the edges and number of edges from the user

    Parameters:
        None

    Returns:
        tuple: A tuple containing a list of edges and number of edges

    Example:
    >>> # Simulate user input for 3 edges and 4 vertices: (1, 2), (2, 3), (3, 4)
    >>> input_data = "4 3\n1 2\n2 3\n3 4\n"
    >>> import sys,io
    >>> original_input = sys.stdin
    >>> sys.stdin = io.StringIO(input_data)  # Redirect stdin for testing
    >>> edglist()
    ([(1, 2), (2, 3), (3, 4)], 4)
    >>> sys.stdin = original_input  # Restore original stdin
    """
    logger.debug(">>> Entering edglist()")
    n, m = tuple(map(int, input().split(" ")))
    edges = []
    logger.debug("edglist(): edges → %s", edges)
    for _ in range(m):
        edges.append(tuple(map(int, input().split(" "))))
    logger.debug("<<< Exiting edglist()")
    return edges, n


"""
--------------------------------------------------------------------------------
    Kruskal's MST Algorithm
        Args :  E - Edge list
                n - Number of Nodes
        Vars :  s - Set of all nodes as unique disjoint sets (initially)
--------------------------------------------------------------------------------
"""


def krusk(e_and_n):
    """
    Sort edges on the basis of distance
    """
    logger.debug(">>> Entering krusk(e_and_n=%s)", e_and_n)
    (e, n) = e_and_n
    e.sort(reverse=True, key=lambda x: x[2])
    s = [{i} for i in range(1, n + 1)]
    logger.debug("krusk(e_and_n=%s): s → %s", e_and_n, s)
    while True:
        if len(s) == 1:
            break
        print(s)
        x = e.pop()
        logger.debug("krusk(e_and_n=%s): x → %s", e_and_n, x)
        for i in range(len(s)):
            if x[0] in s[i]:
                break
        for j in range(len(s)):
            if x[1] in s[j]:
                if i == j:
                    break
                s[j].update(s[i])
                s.pop(i)
                logger.debug("<<< Exiting krusk(e_and_n=%s)", e_and_n)
                break


def find_isolated_nodes(graph):
    """
    Find the isolated node in the graph

    Parameters:
    graph (dict): A dictionary representing a graph.

    Returns:
    list: A list of isolated nodes.

    Examples:
    >>> graph1 = {1: [2, 3], 2: [1, 3], 3: [1, 2], 4: []}
    >>> find_isolated_nodes(graph1)
    [4]

    >>> graph2 = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A'], 'D': []}
    >>> find_isolated_nodes(graph2)
    ['D']

    >>> graph3 = {'X': [], 'Y': [], 'Z': []}
    >>> find_isolated_nodes(graph3)
    ['X', 'Y', 'Z']

    >>> graph4 = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    >>> find_isolated_nodes(graph4)
    []

    >>> graph5 = {}
    >>> find_isolated_nodes(graph5)
    []
    """
    logger.debug(">>> Entering find_isolated_nodes(graph=%s)", graph)
    isolated = []
    logger.debug("find_isolated_nodes(graph=%s): isolated → %s", graph, isolated)
    for node in graph:
        if not graph[node]:
            isolated.append(node)
    logger.debug("<<< Exiting find_isolated_nodes(graph=%s)", graph)
    return isolated
