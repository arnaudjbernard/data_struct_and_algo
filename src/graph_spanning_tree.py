from graph import random_graph
from operator import attrgetter
from set_util import DisjointSet


def kruskal(graph):

    # initialize the sets with each vertex in its own set
    disjoint_set = DisjointSet()
    for vertex in graph.vertices:
        disjoint_set.make_set(vertex)

    sorted_edges = sorted(graph.edges, key=attrgetter("weight"))

    min_spanning_tree = []
    for edge in sorted_edges:
        if disjoint_set.find(edge.vertex_from) != disjoint_set.find(edge.vertex_to):
            min_spanning_tree.append(edge)
            disjoint_set.union(edge.vertex_from, edge.vertex_to)

    return min_spanning_tree

def prims(graph):
    assert len(graph.vertices) > 0

    vertices_in_tree = set([graph.vertices[0]])
    vertices_count = len(graph.vertices)

    min_spanning_tree = []

    while len(vertices_in_tree) < vertices_count:
        filtered_edges = [edge
                          for edge in graph.edges
                          if edge.vertex_from not in vertices_in_tree and edge.vertex_to in vertices_in_tree
                              or edge.vertex_from in vertices_in_tree and edge.vertex_to not in vertices_in_tree]

        smallest_edge = min(filtered_edges, key=attrgetter("weight"))

        vertices_in_tree.add(smallest_edge.vertex_from)
        vertices_in_tree.add(smallest_edge.vertex_to)

        min_spanning_tree.append(smallest_edge)

    return min_spanning_tree


def main():
    for i in xrange(100):
        m_graph = random_graph(5, 3)

        k = kruskal(m_graph)
        p = prims(m_graph)

        print k
        print p

        k_total_weight = reduce(lambda s, edge: edge.weight + s, k, 0)
        p_total_weight = reduce(lambda s, edge: edge.weight + s, p, 0)

        assert k_total_weight == p_total_weight


if __name__ == "__main__":
    main()
