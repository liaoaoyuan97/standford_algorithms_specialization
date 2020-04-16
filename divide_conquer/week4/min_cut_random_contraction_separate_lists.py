import math
import random
from os import path


def read_graph(filename):
    edges = dict()
    vertices_set = set()
    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            # vertices = row.strip('\t\r\n').split('\t')
            vertices = row.strip('\n').split(' ')
            vertices_set.add(vertices[0])

            for v in vertices[1:]:
                if v < vertices[0]:
                    h, t = v, vertices[0]
                else:
                    h, t = vertices[0], v

                if (h, t) not in edges:
                    edges[(h, t)] = 1
                else:
                    edges[(h, t)] = edges[(h, t)] + 1

    return {e: c/2 for e, c in edges.items()}, vertices_set


def random_contraction(edges, vertices):
    n_vertices = len(edges)
    min_edge_cnt = sum([c for c in edges.values()])
    for _ in range(int(n_vertices ** 2 * math.log(n_vertices))):
        _edges = edges.copy()
        _vertices = vertices.copy()
        while len(_vertices) > 2:
            merge_vertex_x, merge_vertex_y = random.choice(list(_edges.keys()))
            del _edges[(merge_vertex_x, merge_vertex_y)]

            for h, t in _edges.keys():
                if h != merge_vertex_y and t != merge_vertex_y:
                    continue

                if h == merge_vertex_y:
                    relabel_e = (merge_vertex_x, t)
                elif t == merge_vertex_y:
                    if merge_vertex_x > h:
                        relabel_e = (h, merge_vertex_x)
                    else:
                        relabel_e = (merge_vertex_x, h)

                if relabel_e in _edges:
                    _edges[relabel_e] = _edges[relabel_e] + _edges[(h, t)]
                else:
                    _edges[relabel_e] = _edges[(h, t)]
                del _edges[(h, t)]

            _vertices.remove(merge_vertex_y)
            # import pdb;pdb.set_trace()

        # print(test)
        trial_edge_cnt = sum(list(_edges.values()))
        if trial_edge_cnt < min_edge_cnt:
            min_edge_cnt = trial_edge_cnt
    return min_edge_cnt


def get_cross_edge_cnt_for_min_cut(edges, vertices):
    min_edge_cnt = sum([c for c in edges.values()])
    for seed in (2019,):
        random.seed(seed)
        # print('seed', seed)
        _cnt = random_contraction(edges, vertices)
        if _cnt < min_edge_cnt:
            min_edge_cnt = _cnt
        print(min_edge_cnt)
    return min_edge_cnt


if __name__ == '__main__':
    edges, vertices = read_graph('input_random_18_75.txt')
    # import pdb;pdb.set_trace()

    import time
    start = time.time()
    print(get_cross_edge_cnt_for_min_cut(edges, vertices))
    print((time.time()-start) / 60)
