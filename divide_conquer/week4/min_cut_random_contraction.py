import math
import random
from os import path

# O(mn^2logn)

def read_graph(filename):
    graph = dict()
    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            vertices = row.strip('\t\r\n').split('\t')
            graph[vertices[0]] = vertices[1:]
    return graph


def random_contraction(graph):
    n_vertices = len(graph)
    min_edge_cnt = sum([len(edges) for edges in graph.values()])
    for _ in range(int(n_vertices ** 2 * math.log(n_vertices))):
            #10000):
        _graph = graph.copy()
        test = []
        while len(_graph) > 2:
            merge_vertex_x = random.choice(list(_graph.keys()))
            _x_adj_vertices = _graph[merge_vertex_x]
            test.append(merge_vertex_x)

            merge_vertex_y = _x_adj_vertices[random.randint(0, len(_x_adj_vertices) - 1)]
            _y_adj_vertices = _graph[merge_vertex_y]
            _x_adj_vertices = [v for v in _x_adj_vertices if v != merge_vertex_y]
            _y_adj_vertices = [v for v in _y_adj_vertices if v != merge_vertex_x]

            # relabel
            for _adj_vertex in _y_adj_vertices:
                _graph[_adj_vertex] = [merge_vertex_x if v == merge_vertex_y else v for v in _graph[_adj_vertex]]

            merged_adj_vertices = _x_adj_vertices + _y_adj_vertices
            _graph[merge_vertex_x] = merged_adj_vertices
            del _graph[merge_vertex_y]

        trial_edge_cnt = sum([len(adj_edges) for adj_edges in _graph.values()]) / 2
        if trial_edge_cnt < min_edge_cnt:
            min_edge_cnt = trial_edge_cnt
    return min_edge_cnt


def get_cross_edge_cnt_for_min_cut(graph):
    min_edge_cnt = sum([len(edges) for edges in graph.values()])
    for seed in (8,):
        random.seed(seed)
        _cnt = random_contraction(graph)
        if _cnt < min_edge_cnt:
            min_edge_cnt = _cnt
        print(min_edge_cnt)
    return min_edge_cnt


if __name__ == '__main__':
    graph = read_graph('KargerMinCut.txt')
    assert sum([len(adj_vertices) == 0 for adj_vertices in graph.values()]) == 0

    import time
    start = time.time()
    print(get_cross_edge_cnt_for_min_cut(graph))
    print((time.time()-start) / 60)
