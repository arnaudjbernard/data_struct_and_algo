
class Graph(object):

    def __init__(self):
        super(Graph, self).__init__()
        self.vertices = []
        self.edges = []

    def add_vertex(self, value):
        vertex = Vertex(value)
        self.vertices.append(vertex)

    def add_edge(self, vertex_from, vertex_to, weight=1):
        for edge in vertex_from.edge_from:
            if edge.vertex_to == vertex_to:
                return
        edge = Edge(vertex_from, vertex_to, weight)
        vertex_from.add_edge(edge)
        vertex_to.add_edge(edge)
        self.edges.append(edge)

    def __repr__(self):
        res = "Vertices:\n"
        for vertex in self.vertices:
            res += repr(vertex) + "\n"
        res += "Edges:\n"
        for edge in self.edges:
            res += repr(edge) + "\n"
        return res


class Vertex(object):
    def __init__(self, value):
        super(Vertex, self).__init__()
        self.edge_from = []
        self.edge_to = []
        self.value = value

    def __repr__(self):
        return "Vertex(%s) ->%s %s->" % (self.value, len(self.edge_from), len(self.edge_to))

    def __str__(self):
        return "Vertex(%s)" % self.value

    def add_edge(self, edge):
        if edge.vertex_from == self:
            self.edge_from.append(edge)
        else:
            self.edge_to.append(edge)


class Edge(object):
    def __init__(self, vertex_from, vertex_to, weight=1):
        super(Edge, self).__init__()
        self.vertex_from = vertex_from
        self.vertex_to = vertex_to
        self.weight = weight

    def __repr__(self):
        return "%s -> %s %s" % (self.vertex_from, self.vertex_to, self.weight)


def random_graph(vertex_count=10, edge_count=5, connected=True):
    weights = xrange(1, 11)
    import random
    graph = Graph()
    for i in xrange(vertex_count):
        graph.add_vertex(i)
    if connected:
        for i in xrange(vertex_count - 1):
            graph.add_edge(graph.vertices[i], graph.vertices[i + 1], random.choice(weights))

    for i in xrange(edge_count):
        index_a = random.randrange(0, vertex_count)
        index_b = random.randrange(0, vertex_count)
        while index_b == index_a:
            index_b = random.randrange(0, vertex_count)
        graph.add_edge(graph.vertices[index_a], graph.vertices[index_b], random.choice(weights))

    return graph


def main():
    import pprint
    pprint.pprint(random_graph())


if __name__ == "__main__":
    main()