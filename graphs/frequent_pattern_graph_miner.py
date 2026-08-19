import logging
logger = logging.getLogger(__name__)
"""
FP-GraphMiner - A Fast Frequent Pattern Mining Algorithm for Network Graphs

A novel Frequent Pattern Graph Mining algorithm, FP-GraphMiner, that compactly
represents a set of network graphs as a Frequent Pattern Graph (or FP-Graph).
This graph can be used to efficiently mine frequent subgraphs including maximal
frequent subgraphs and maximum common subgraphs.

URL: https://www.researchgate.net/publication/235255851
"""

# fmt: off
edge_array = [
    ['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'be-e6', 'bh-e12', 'cd-e2', 'ce-e4',
     'de-e1', 'df-e8', 'dg-e5', 'dh-e10', 'ef-e3', 'eg-e2', 'fg-e6', 'gh-e6', 'hi-e3'],
    ['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'be-e6', 'cd-e2', 'de-e1', 'df-e8',
     'ef-e3', 'eg-e2', 'fg-e6'],
    ['ab-e1', 'ac-e3', 'bc-e4', 'bd-e2', 'de-e1', 'df-e8', 'dg-e5', 'ef-e3', 'eg-e2',
     'eh-e12', 'fg-e6', 'fh-e10', 'gh-e6'],
    ['ab-e1', 'ac-e3', 'bc-e4', 'bd-e2', 'bh-e12', 'cd-e2', 'df-e8', 'dh-e10'],
    ['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'cd-e2', 'ce-e4', 'de-e1', 'df-e8',
     'dg-e5', 'ef-e3', 'eg-e2', 'fg-e6']
]
# fmt: on


def get_distinct_edge(edge_array):
    """
    Return Distinct edges from edge array of multiple graphs
    >>> sorted(get_distinct_edge(edge_array))
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    """
    logger.debug(">>> Entering get_distinct_edge(edge_array=%s)", edge_array)
    distinct_edge = set()
    logger.debug("get_distinct_edge(edge_array=%s): distinct_edge → %s", edge_array, distinct_edge)
    for row in edge_array:
        for item in row:
            distinct_edge.add(item[0])
    logger.debug("<<< Exiting get_distinct_edge(edge_array=%s)", edge_array)
    return list(distinct_edge)


def get_bitcode(edge_array, distinct_edge):
    """
    Return bitcode of distinct_edge
    """
    logger.debug(">>> Entering get_bitcode(edge_array=%s,distinct_edge=%s)", edge_array, distinct_edge)
    bitcode = ["0"] * len(edge_array)
    logger.debug("get_bitcode(edge_array=%s,distinct_edge=%s): bitcode → %s", edge_array, distinct_edge, bitcode)
    for i, row in enumerate(edge_array):
        for item in row:
            if distinct_edge in item[0]:
                bitcode[i] = "1"
                break
    logger.debug("<<< Exiting get_bitcode(edge_array=%s,distinct_edge=%s)", edge_array, distinct_edge)
    return "".join(bitcode)


def get_frequency_table(edge_array):
    """
    Returns Frequency Table
    """
    logger.debug(">>> Entering get_frequency_table(edge_array=%s)", edge_array)
    distinct_edge = get_distinct_edge(edge_array)
    logger.debug("get_frequency_table(edge_array=%s): distinct_edge → %s", edge_array, distinct_edge)
    frequency_table = {}
    logger.debug("get_frequency_table(edge_array=%s): frequency_table → %s", edge_array, frequency_table)

    for item in distinct_edge:
        bit = get_bitcode(edge_array, item)
        logger.debug("get_frequency_table(edge_array=%s): bit → %s", edge_array, bit)
        # print('bit',bit)
        # bt=''.join(bit)
        s = bit.count("1")
        logger.debug("get_frequency_table(edge_array=%s): s → %s", edge_array, s)
        frequency_table[item] = [s, bit]
    # Store [Distinct edge, WT(Bitcode), Bitcode] in descending order
    sorted_frequency_table = [
    logger.debug("get_frequency_table(edge_array=%s): sorted_frequency_table → %s", edge_array, sorted_frequency_table)
        [k, v[0], v[1]]
        for k, v in sorted(frequency_table.items(), key=lambda v: v[1][0], reverse=True)
    ]
    logger.debug("<<< Exiting get_frequency_table(edge_array=%s)", edge_array)
    return sorted_frequency_table


def get_nodes(frequency_table):
    """
    Returns nodes
    format nodes={bitcode:edges that represent the bitcode}
    >>> get_nodes([['ab', 5, '11111'], ['ac', 5, '11111'], ['df', 5, '11111'],
    ...            ['bd', 5, '11111'], ['bc', 5, '11111']])
    {'11111': ['ab', 'ac', 'df', 'bd', 'bc']}
    """
    nodes = {}
    for _, item in enumerate(frequency_table):
        nodes.setdefault(item[2], []).append(item[0])
    return nodes


def get_cluster(nodes):
    """
    Returns cluster
    format cluster:{WT(bitcode):nodes with same WT}
    """
    logger.debug(">>> Entering get_cluster(nodes=%s)", nodes)
    cluster = {}
    logger.debug("get_cluster(nodes=%s): cluster → %s", nodes, cluster)
    for key, value in nodes.items():
        cluster.setdefault(key.count("1"), {})[key] = value
    logger.debug("<<< Exiting get_cluster(nodes=%s)", nodes)
    return cluster


def get_support(cluster):
    """
    Returns support
    >>> get_support({5: {'11111': ['ab', 'ac', 'df', 'bd', 'bc']},
    ...              4: {'11101': ['ef', 'eg', 'de', 'fg'], '11011': ['cd']},
    ...              3: {'11001': ['ad'], '10101': ['dg']},
    ...              2: {'10010': ['dh', 'bh'], '11000': ['be'], '10100': ['gh'],
    ...                  '10001': ['ce']},
    ...              1: {'00100': ['fh', 'eh'], '10000': ['hi']}})
    [100.0, 80.0, 60.0, 40.0, 20.0]
    """
    logger.debug(">>> Entering get_support(cluster=%s)", cluster)
    logger.debug("<<< Exiting get_support(cluster=%s)", cluster)
    return [i * 100 / len(cluster) for i in cluster]


def print_all() -> None:
    logger.debug(">>> Entering print_all()")
    print("\nNodes\n")
    for key, value in nodes.items():
        print(key, value)
    print("\nSupport\n")
    print(support)
    print("\n Cluster \n")
    for key, value in sorted(cluster.items(), reverse=True):
        print(key, value)
    print("\n Graph\n")
    for key, value in graph.items():
        print(key, value)
    print("\n Edge List of Frequent subgraphs \n")
    for edge_list in freq_subgraph_edge_list:
        print(edge_list)
        logger.debug("<<< Exiting print_all()")


def create_edge(nodes, graph, cluster, c1):
    """
    create edge between the nodes
    """
    logger.debug(">>> Entering create_edge(nodes=%s,graph=%s,cluster=%s,c1=%s)", nodes, graph, cluster, c1)
    for i in cluster[c1]:
        count = 0
        logger.debug("create_edge(nodes=%s,graph=%s,cluster=%s,c1=%s): count → %s", nodes, graph, cluster, c1, count)
        c2 = c1 + 1
        while c2 < max(cluster.keys()):
            for j in cluster[c2]:
                """
                creates edge only if the condition satisfies
                """
                if int(i, 2) & int(j, 2) == int(i, 2):
                    if tuple(nodes[i]) in graph:
                        graph[tuple(nodes[i])].append(nodes[j])
                    else:
                        graph[tuple(nodes[i])] = [nodes[j]]
                    count += 1
            if count == 0:
                c2 = c2 + 1
            else:
                logger.debug("<<< Exiting create_edge(nodes=%s,graph=%s,cluster=%s,c1=%s)", nodes, graph, cluster, c1)
                break


def construct_graph(cluster, nodes):
    logger.debug(">>> Entering construct_graph(cluster=%s,nodes=%s)", cluster, nodes)
    x = cluster[max(cluster.keys())]
    logger.debug("construct_graph(cluster=%s,nodes=%s): x → %s", cluster, nodes, x)
    cluster[max(cluster.keys()) + 1] = "Header"
    graph = {}
    logger.debug("construct_graph(cluster=%s,nodes=%s): graph → %s", cluster, nodes, graph)
    for i in x:
        if (["Header"],) in graph:
            graph[(["Header"],)].append(x[i])
        else:
            graph[(["Header"],)] = [x[i]]
    for i in x:
        graph[(x[i],)] = [["Header"]]
    i = 1
    while i < max(cluster) - 1:
        create_edge(nodes, graph, cluster, i)
        i = i + 1
    logger.debug("<<< Exiting construct_graph(cluster=%s,nodes=%s)", cluster, nodes)
    return graph


def my_dfs(graph, start, end, path=None):
    """
    find different DFS walk from given node to Header node
    """
    logger.debug(">>> Entering my_dfs(graph=%s,start=%s,end=%s,path=%s)", graph, start, end, path)
    path = (path or []) + [start]
    logger.debug("my_dfs(graph=%s,start=%s,end=%s,path=%s): path → %s", graph, start, end, path, path)
    if start == end:
        paths.append(path)
    for node in graph[start]:
        if tuple(node) not in path:
            my_dfs(graph, tuple(node), end, path)
            logger.debug("<<< Exiting my_dfs(graph=%s,start=%s,end=%s,path=%s)", graph, start, end, path)


def find_freq_subgraph_given_support(s, cluster, graph):
    """
    find edges of multiple frequent subgraphs
    """
    logger.debug(">>> Entering find_freq_subgraph_given_support(s=%s,cluster=%s,graph=%s)", s, cluster, graph)
    k = int(s / 100 * (len(cluster) - 1))
    for i in cluster[k]:
        my_dfs(graph, tuple(cluster[k][i]), (["Header"],))
        logger.debug("<<< Exiting find_freq_subgraph_given_support(s=%s,cluster=%s,graph=%s)", s, cluster, graph)


def freq_subgraphs_edge_list(paths):
    """
    returns Edge list for frequent subgraphs
    """
    logger.debug(">>> Entering freq_subgraphs_edge_list(paths=%s)", paths)
    freq_sub_el = []
    logger.debug("freq_subgraphs_edge_list(paths=%s): freq_sub_el → %s", paths, freq_sub_el)
    for edges in paths:
        el = []
        for j in range(len(edges) - 1):
            temp = list(edges[j])
            for e in temp:
                edge = (e[0], e[1])
                logger.debug("freq_subgraphs_edge_list(paths=%s): edge → %s", paths, edge)
                el.append(edge)
        freq_sub_el.append(el)
    logger.debug("<<< Exiting freq_subgraphs_edge_list(paths=%s)", paths)
    return freq_sub_el


def preprocess(edge_array):
    """
    Preprocess the edge array
    >>> preprocess([['ab-e1', 'ac-e3', 'ad-e5', 'bc-e4', 'bd-e2', 'be-e6', 'bh-e12',
    ...              'cd-e2', 'ce-e4', 'de-e1', 'df-e8', 'dg-e5', 'dh-e10', 'ef-e3',
    ...              'eg-e2', 'fg-e6', 'gh-e6', 'hi-e3']])

    """
    logger.debug(">>> Entering preprocess(edge_array=%s)", edge_array)
    for i in range(len(edge_array)):
        for j in range(len(edge_array[i])):
            t = edge_array[i][j].split("-")
            logger.debug("preprocess(edge_array=%s): t → %s", edge_array, t)
            edge_array[i][j] = t
            logger.debug("<<< Exiting preprocess(edge_array=%s)", edge_array)


if __name__ == "__main__":
    preprocess(edge_array)
    frequency_table = get_frequency_table(edge_array)
    nodes = get_nodes(frequency_table)
    cluster = get_cluster(nodes)
    support = get_support(cluster)
    graph = construct_graph(cluster, nodes)
    find_freq_subgraph_given_support(60, cluster, graph)
    paths: list = []
    freq_subgraph_edge_list = freq_subgraphs_edge_list(paths)
    print_all()
