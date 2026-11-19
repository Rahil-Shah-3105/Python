import logging
logger = logging.getLogger(__name__)
class FlowNetwork:
    def __init__(self, graph, sources, sinks):
        logger.error(">>> Entering __init__(graph=%s,sources=%s,sinks=%s)", graph, sources, sinks, extra={"event.action": "__init__", "logrite.graph": graph, "logrite.sources": sources, "logrite.sinks": sinks})
        self.source_index = None
        logger.debug("__init__(self=%s,graph=%s,sources=%s,sinks=%s): self.source_index → %s", self, graph, sources, sinks, self.source_index, extra={"event.action": "__init__", "logrite.graph": graph, "logrite.sources": sources, "logrite.sinks": sinks})
        self.sink_index = None
        logger.debug("__init__(self=%s,graph=%s,sources=%s,sinks=%s): self.sink_index → %s", self, graph, sources, sinks, self.sink_index, extra={"event.action": "__init__", "logrite.graph": graph, "logrite.sources": sources, "logrite.sinks": sinks})
        self.graph = graph
        logger.debug("__init__(self=%s,graph=%s,sources=%s,sinks=%s): self.graph → %s", self, graph, sources, sinks, self.graph, extra={"event.action": "__init__", "logrite.graph": graph, "logrite.sources": sources, "logrite.sinks": sinks})

        self._normalize_graph(sources, sinks)
        logger.warning("<<< Exiting __init__(graph=%s,sources=%s,sinks=%s)", graph, sources, sinks, extra={"event.action": "__init__", "logrite.graph": graph, "logrite.sources": sources, "logrite.sinks": sinks})
        self.vertices_count = len(graph)
        logger.error("__init__(graph=%s,sources=%s,sinks=%s): self.vertices_count → %s", graph, sources, sinks, self.vertices_count, extra={"event.action": "__init__", "logrite.graph": graph, "logrite.sources": sources, "logrite.sinks": sinks})
        self.maximum_flow_algorithm = None
        logger.debug("__init__(self=%s,graph=%s,sources=%s,sinks=%s): self.maximum_flow_algorithm → %s", self, graph, sources, sinks, self.maximum_flow_algorithm, extra={"event.action": "__init__", "logrite.graph": graph, "logrite.sources": sources, "logrite.sinks": sinks})

    # make only one source and one sink
    def _normalize_graph(self, sources, sinks):
        logger.error(">>> Entering _normalize_graph(sources=%s,sinks=%s)", sources, sinks, extra={"event.action": "_normalize_graph", "logrite.sources": sources, "logrite.sinks": sinks})
        if sources is int:
            sources = [sources]
        if sinks is int:
            sinks = [sinks]

        if len(sources) == 0 or len(sinks) == 0:
            logger.warning("<<< Exiting _normalize_graph(sources=%s,sinks=%s)", sources, sinks, extra={"event.action": "_normalize_graph", "logrite.sources": sources, "logrite.sinks": sinks})
            return

        self.source_index = sources[0]
        logger.debug("_normalize_graph(self=%s,sources=%s,sinks=%s): self.source_index → %s", self, sources, sinks, self.source_index, extra={"event.action": "_normalize_graph", "logrite.sources": sources, "logrite.sinks": sinks})
        self.sink_index = sinks[0]
        logger.debug("_normalize_graph(self=%s,sources=%s,sinks=%s): self.sink_index → %s", self, sources, sinks, self.sink_index, extra={"event.action": "_normalize_graph", "logrite.sources": sources, "logrite.sinks": sinks})

        # make fake vertex if there are more
        # than one source or sink
        if len(sources) > 1 or len(sinks) > 1:
            max_input_flow = 0
            for i in sources:
                max_input_flow += sum(self.graph[i])

            size = len(self.graph) + 1
            for room in self.graph:
                room.insert(0, 0)
            self.graph.insert(0, [0] * size)
            for i in sources:
                self.graph[0][i + 1] = max_input_flow
            self.source_index = 0

            size = len(self.graph) + 1
            for room in self.graph:
                room.append(0)
            self.graph.append([0] * size)
            for i in sinks:
                self.graph[i + 1][size - 1] = max_input_flow
            self.sink_index = size - 1

    def find_maximum_flow(self):
        logger.error(">>> Entering find_maximum_flow()", extra={"event.action": "find_maximum_flow"})
        if self.maximum_flow_algorithm is None:
            raise Exception("You need to set maximum flow algorithm before.")
        if self.source_index is None or self.sink_index is None:
            return 0

        self.maximum_flow_algorithm.execute()
        logger.warning("<<< Exiting find_maximum_flow()", extra={"event.action": "find_maximum_flow"})
        return self.maximum_flow_algorithm.getMaximumFlow()

    def set_maximum_flow_algorithm(self, algorithm):
        logger.error(">>> Entering set_maximum_flow_algorithm(algorithm=%s)", algorithm, extra={"event.action": "set_maximum_flow_algorithm", "logrite.algorithm": algorithm})
        self.maximum_flow_algorithm = algorithm(self)
        logger.warning("<<< Exiting set_maximum_flow_algorithm(algorithm=%s)", algorithm, extra={"event.action": "set_maximum_flow_algorithm", "logrite.algorithm": algorithm})
        logger.error("set_maximum_flow_algorithm(algorithm=%s): self.maximum_flow_algorithm → %s", algorithm, self.maximum_flow_algorithm, extra={"event.action": "set_maximum_flow_algorithm", "logrite.algorithm": algorithm})


class FlowNetworkAlgorithmExecutor:
    def __init__(self, flow_network):
        logger.error(">>> Entering __init__(flow_network=%s)", flow_network, extra={"event.action": "__init__", "logrite.flow_network": flow_network})
        self.flow_network = flow_network
        logger.debug("__init__(self=%s,flow_network=%s): self.flow_network → %s", self, flow_network, self.flow_network, extra={"event.action": "__init__", "logrite.flow_network": flow_network})
        self.verticies_count = flow_network.verticesCount
        logger.debug("__init__(self=%s,flow_network=%s): self.verticies_count → %s", self, flow_network, self.verticies_count, extra={"event.action": "__init__", "logrite.flow_network": flow_network})
        self.source_index = flow_network.sourceIndex
        logger.debug("__init__(self=%s,flow_network=%s): self.source_index → %s", self, flow_network, self.source_index, extra={"event.action": "__init__", "logrite.flow_network": flow_network})
        self.sink_index = flow_network.sinkIndex
        logger.debug("__init__(self=%s,flow_network=%s): self.sink_index → %s", self, flow_network, self.sink_index, extra={"event.action": "__init__", "logrite.flow_network": flow_network})
        # it's just a reference, so you shouldn't change
        # it in your algorithms, use deep copy before doing that
        logger.warning("<<< Exiting __init__(flow_network=%s)", flow_network, extra={"event.action": "__init__", "logrite.flow_network": flow_network})
        self.graph = flow_network.graph
        logger.debug("__init__(self=%s,flow_network=%s): self.graph → %s", self, flow_network, self.graph, extra={"event.action": "__init__", "logrite.flow_network": flow_network})
        self.executed = False
        logger.debug("__init__(self=%s,flow_network=%s): self.executed → %s", self, flow_network, self.executed, extra={"event.action": "__init__", "logrite.flow_network": flow_network})

    def execute(self):
        logger.error(">>> Entering execute()", extra={"event.action": "execute"})
        if not self.executed:
            self._algorithm()
            logger.warning("<<< Exiting execute()", extra={"event.action": "execute"})
            self.executed = True
            logger.debug("execute(self=%s): self.executed → %s", self, self.executed, extra={"event.action": "execute"})

    # You should override it
    def _algorithm(self):
        logger.error(">>> Entering _algorithm()", extra={"event.action": "_algorithm"})
        pass
        logger.warning("<<< Exiting _algorithm()", extra={"event.action": "_algorithm"})


class MaximumFlowAlgorithmExecutor(FlowNetworkAlgorithmExecutor):
    def __init__(self, flow_network):
        super().__init__(flow_network)
        # use this to save your result
        self.maximum_flow = -1
        logger.debug("__init__(self=%s,flow_network=%s): self.maximum_flow → %s", self, flow_network, self.maximum_flow, extra={"event.action": "__init__", "logrite.flow_network": flow_network})

    def get_maximum_flow(self):
        logger.error(">>> Entering get_maximum_flow()", extra={"event.action": "get_maximum_flow"})
        if not self.executed:
            raise Exception("You should execute algorithm before using its result!")

        logger.warning("<<< Exiting get_maximum_flow()", extra={"event.action": "get_maximum_flow"})
        return self.maximum_flow


class PushRelabelExecutor(MaximumFlowAlgorithmExecutor):
    def __init__(self, flow_network):
        super().__init__(flow_network)

        self.preflow = [[0] * self.verticies_count for i in range(self.verticies_count)]
        logger.error("__init__(flow_network=%s): self.preflow → %s", flow_network, self.preflow, extra={"event.action": "__init__", "logrite.flow_network": flow_network})

        self.heights = [0] * self.verticies_count
        logger.debug("__init__(self=%s,flow_network=%s): self.heights → %s", self, flow_network, self.heights, extra={"event.action": "__init__", "logrite.flow_network": flow_network})
        self.excesses = [0] * self.verticies_count
        logger.debug("__init__(self=%s,flow_network=%s): self.excesses → %s", self, flow_network, self.excesses, extra={"event.action": "__init__", "logrite.flow_network": flow_network})

    def _algorithm(self):
        self.heights[self.source_index] = self.verticies_count

        # push some substance to graph
        for nextvertex_index, bandwidth in enumerate(self.graph[self.source_index]):
            self.preflow[self.source_index][nextvertex_index] += bandwidth
            self.preflow[nextvertex_index][self.source_index] -= bandwidth
            self.excesses[nextvertex_index] += bandwidth

        # Relabel-to-front selection rule
        vertices_list = [
            i
            for i in range(self.verticies_count)
            if i not in {self.source_index, self.sink_index}
        ]

        # move through list
        i = 0
        while i < len(vertices_list):
            vertex_index = vertices_list[i]
            previous_height = self.heights[vertex_index]
            self.process_vertex(vertex_index)
            if self.heights[vertex_index] > previous_height:
                # if it was relabeled, swap elements
                # and start from 0 index
                vertices_list.insert(0, vertices_list.pop(i))
                i = 0
            else:
                i += 1

        self.maximum_flow = sum(self.preflow[self.source_index])
        logger.error("_algorithm(): self.maximum_flow → %s", self.maximum_flow, extra={"event.action": "_algorithm"})

    def process_vertex(self, vertex_index):
        logger.error(">>> Entering process_vertex(vertex_index=%s)", vertex_index, extra={"event.action": "process_vertex", "logrite.vertex_index": vertex_index})
        while self.excesses[vertex_index] > 0:
            for neighbour_index in range(self.verticies_count):
                # if it's neighbour and current vertex is higher
                if (
                    self.graph[vertex_index][neighbour_index]
                    - self.preflow[vertex_index][neighbour_index]
                    > 0
                    and self.heights[vertex_index] > self.heights[neighbour_index]
                ):
                    self.push(vertex_index, neighbour_index)

            self.relabel(vertex_index)
            logger.warning("<<< Exiting process_vertex(vertex_index=%s)", vertex_index, extra={"event.action": "process_vertex", "logrite.vertex_index": vertex_index})

    def push(self, from_index, to_index):
        logger.error(">>> Entering push(from_index=%s,to_index=%s)", from_index, to_index, extra={"event.action": "push", "logrite.from_index": from_index, "logrite.to_index": to_index})
        preflow_delta = min(
            self.excesses[from_index],
            self.graph[from_index][to_index] - self.preflow[from_index][to_index],
        )
        self.preflow[from_index][to_index] += preflow_delta
        self.preflow[to_index][from_index] -= preflow_delta
        self.excesses[from_index] -= preflow_delta
        self.excesses[to_index] += preflow_delta
        logger.warning("<<< Exiting push(from_index=%s,to_index=%s)", from_index, to_index, extra={"event.action": "push", "logrite.from_index": from_index, "logrite.to_index": to_index})

    def relabel(self, vertex_index):
        logger.error(">>> Entering relabel(vertex_index=%s)", vertex_index, extra={"event.action": "relabel", "logrite.vertex_index": vertex_index})
        min_height = None
        for to_index in range(self.verticies_count):
            if (
                self.graph[vertex_index][to_index]
                - self.preflow[vertex_index][to_index]
                > 0
            ) and (min_height is None or self.heights[to_index] < min_height):
                min_height = self.heights[to_index]

        if min_height is not None:
            self.heights[vertex_index] = min_height + 1
            logger.warning("<<< Exiting relabel(vertex_index=%s)", vertex_index, extra={"event.action": "relabel", "logrite.vertex_index": vertex_index})


if __name__ == "__main__":
    entrances = [0]
    exits = [3]
    # graph = [
    #     [0, 0, 4, 6, 0, 0],
    #     [0, 0, 5, 2, 0, 0],
    #     [0, 0, 0, 0, 4, 4],
    #     [0, 0, 0, 0, 6, 6],
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0],
    # ]
    graph = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]

    # prepare our network
    flow_network = FlowNetwork(graph, entrances, exits)
    # set algorithm
    flow_network.set_maximum_flow_algorithm(PushRelabelExecutor)
    # and calculate
    maximum_flow = flow_network.find_maximum_flow()

    print(f"maximum flow is {maximum_flow}")
