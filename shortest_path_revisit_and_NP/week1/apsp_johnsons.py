import time
import numpy as np
from os import path


def read_graph(filename):
    i = 0

    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            if i == 0:
                _list = row.strip("\n").split(' ')
                n_vertex, n_edge = int(_list[0]), int(_list[1])
                shortest_paths = np.ones((n_vertex + 1, n_vertex + 1, n_vertex + 1)) * float('inf')
                i += 1
            else:
                _list = row.strip("\n").split(' ')
                shortest_paths[int(_list[0])][int(_list[1])][0] = float(_list[2])

    for i in range(1, n_vertex + 1):
        shortest_paths[i][i][0] = 0

    return n_vertex, shortest_paths


def compute_apsp(n_vertex, shortest_paths):
    for k in range(1, n_vertex + 1):
        for i in range(1, n_vertex + 1):
            for j in range(1, n_vertex + 1):
                if shortest_paths[i][j][k - 1] > (shortest_paths[i][k][k - 1] + shortest_paths[k][j][k - 1]):
                    shortest_paths[i][j][k] = shortest_paths[i][k][k - 1] + shortest_paths[k][j][k - 1]
                else:
                    shortest_paths[i][j][k] = shortest_paths[i][j][k - 1]

    for i in range(1, n_vertex + 1):
        if shortest_paths[i][i][n_vertex] < 0:
            return None

    m = shortest_paths[1][2][n_vertex]
    for i in range(1, n_vertex + 1):
        for j in range(1, n_vertex + 1):
            if i != j and shortest_paths[i][j][n_vertex] < m:
                m = shortest_paths[i][j][n_vertex]

    return m


if __name__ == "__main__":
    time_start = time.time()
    n_vertex, shortest_paths = read_graph("grh1.txt")
    print(compute_apsp(n_vertex, shortest_paths))
    print(time.time() - time_start)

    time_start = time.time()
    n_vertex, shortest_paths = read_graph("grh2.txt")
    print(compute_apsp(n_vertex, shortest_paths))
    print(time.time() - time_start)

    time_start = time.time()
    n_vertex, shortest_paths = read_graph("grh3.txt")
    print(compute_apsp(n_vertex, shortest_paths))
    print(time.time() - time_start)
