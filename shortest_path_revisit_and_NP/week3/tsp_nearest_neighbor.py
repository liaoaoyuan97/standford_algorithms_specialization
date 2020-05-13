import time
import math
from os import path


def read_graph(filename):
    i = 0
    vertices = []

    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            if i == 0:
                n_vertex = int(row.strip("\n"))
                i += 1
            else:
                _list = row.strip("\n").split(' ')
                vertices.append((float(_list[1]), float(_list[2])))

    assert len(vertices) == n_vertex
    return n_vertex, vertices


def compute_min_cost(n_vertex, vertices):
    set_to_explore = set([i for i in range(1, n_vertex)])
    pre_point = vertices[0]
    res = 0

    while len(set_to_explore) > 1:
        m = float('inf')
        min_i = None
        for i in set_to_explore:
            dist = (pre_point[0] - vertices[i][0]) ** 2 + (pre_point[1] - vertices[i][1]) ** 2
            if dist < m:
                min_i = i
                m = dist

        if min_i is not None:
            res += math.sqrt(m)
            set_to_explore.remove(min_i)
            pre_point = vertices[min_i]

    last_i = set_to_explore.pop()
    res += math.sqrt((pre_point[0] - vertices[last_i][0]) ** 2 + (pre_point[1] - vertices[last_i][1]) ** 2)
    res += math.sqrt((vertices[0][0] - vertices[last_i][0]) ** 2 + (vertices[0][1] - vertices[last_i][1]) ** 2)

    return res


if __name__ == "__main__":
    time_start = time.time()
    n, vertices = read_graph("tsp.txt")
    print(compute_min_cost(n, vertices))
    print(time.time() - time_start)
