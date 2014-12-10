from __future__ import print_function

from graph import *

from collections import deque, defaultdict, namedtuple
import heapq
import sys


def breadth_first_search(vertex, node_callback, edge_callback):
    assert isinstance(vertex, Vertex)
    assert hasattr(node_callback, '__call__')
    assert hasattr(edge_callback, '__call__')

    explored = [vertex]
    queue = deque([vertex])
    node_callback(vertex)
    while queue:
        vertex = queue.popleft()
        for edge in vertex.edge_from:
            edge_callback(edge)
            if edge.vertex_to not in explored:
                node_callback(edge.vertex_to)
                explored.append(edge.vertex_to)
                queue.append(edge.vertex_to)


def _depth_first_search_rec(vertex, node_callback, edge_callback, explored):
    for edge in vertex.edge_from:
        edge_callback(edge)
        if edge.vertex_to not in explored:
            node_callback(edge.vertex_to)
            explored.add(edge.vertex_to)
            _depth_first_search_rec(edge.vertex_to, node_callback, edge_callback, explored)


def depth_first_search(vertex, node_callback, edge_callback):
    assert isinstance(vertex, Vertex)
    assert hasattr(node_callback, '__call__')
    assert hasattr(edge_callback, '__call__')

    _depth_first_search_rec(vertex, node_callback, edge_callback, set())


def _build_path(previous, start, end):
    path = [end]
    step = end
    while step != start:
        step = previous[step]
        path.append(step)

    return list(reversed(path))


def dijkstra(start, end):
    """
    Note: does not behave nicely if there is no path (infinite loop)
    """
    assert isinstance(start, Vertex)
    assert isinstance(end, Vertex)

    node = namedtuple('node', ['cost', 'vertex'])
    heap = []
    dists = {}
    previous = {}
    explored = set()
    top = start
    dist = 0
    while top != end:
        explored.add(top)
        for edge in top.edge_from:
            new_dist = dist + edge.weight
            if dists.get(edge.vertex_to, sys.maxint) > new_dist and edge.vertex_to not in explored:
                heapq.heappush(heap, node(new_dist, edge.vertex_to))
                previous[edge.vertex_to] = top
        dist, top = heapq.heappop(heap)

    return dist, _build_path(previous, start, end)


def bellman_ford(graph, start, end):
    assert isinstance(graph, Graph)
    assert isinstance(start, Vertex)

    vertices_count = len(graph.vertices)

    # initialize
    weight = {}
    for vertex in graph.vertices:
        if vertex == start:
            weight[vertex] = 0
        else:
            weight[vertex] = sys.maxint

    previous = {}

    # relax
    for _ in xrange(vertices_count):
        for edge in graph.edges:
            if weight[edge.vertex_from] + edge.weight < weight[edge.vertex_to]:
                previous[edge.vertex_to] = edge.vertex_from
                weight[edge.vertex_to] = weight[edge.vertex_from] + edge.weight

    # check for infinite cycles
    for edge in graph.edges:
        if weight[edge.vertex_from] + edge.weight < weight[edge.vertex_to]:
            raise Exception('graph contains a negative-weight cycle')

    return weight[end], _build_path(previous, start, end)


def a_star(graph, start, end, h_score):
    assert isinstance(graph, Graph)
    assert isinstance(start, Vertex)
    assert isinstance(end, Vertex)
    assert hasattr(h_score, '__call__')

    closed = set()
    previous = {}
    opened = [start]
    g_score = defaultdict(lambda: sys.maxint)
    g_score[start] = 0
    f_score = {start: h_score(start, end)}

    while opened:
        node = min(opened, key=lambda x: f_score[x])
        if node == end:
            return g_score[end], _build_path(previous, start, end)

        assert isinstance(node, Vertex)
        opened.remove(node)
        closed.add(node)

        current_g_score = g_score[node]

        for edge in node.edge_from:
            next_node = edge.vertex_to
            if next_node not in closed:
                new_g_score = current_g_score + edge.weight
                if new_g_score < g_score[next_node]:
                    previous[next_node] = node
                    g_score[next_node] = new_g_score
                    f_score[next_node] = new_g_score + h_score(next_node, end)
                    if next_node not in closed:
                        opened.append(next_node)


def main():
    bellman_ford_dist = dijkstra_dist = a_star_dist = 0
    while bellman_ford_dist == dijkstra_dist and bellman_ford_dist == a_star_dist:
        m_graph = random_graph(5, 3)

        # depth_first_search(graph.vertices[0], print, print)
        # breadth_first_search(graph.vertices[0], print, print)

        m_start = m_graph.vertices[0]
        m_end = m_graph.vertices[len(m_graph.vertices) - 1]
        dijkstra_dist, dijkstra_path = dijkstra(m_start, m_end)
        print(dijkstra_dist, dijkstra_path)

        bellman_ford_dist, bellman_ford_path = bellman_ford(m_graph, m_start, m_end)
        print(bellman_ford_dist, bellman_ford_path)

        # erroneous estimate can cause the wrong path to be selected
        # print(graph)
        def estimate(*_):
            return 1

        a_star_dist, a_star_path = a_star(m_graph, m_start, m_end, estimate)
        print(a_star_dist, a_star_path)

        sys.stdout.flush()


if __name__ == "__main__":
    main()
