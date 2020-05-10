import time
import math
from itertools import combinations
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
                vertices.append((float(_list[0]), float(_list[1])))

    assert len(vertices) == n_vertex
    return n_vertex, vertices


def compute_min_cost_permutation(n_vertex, vertices):
    cost_dict = {1: {0: 0}}

    for m in range(2, n_vertex + 1):
        print(m)
        for s in combinations([i for i in range(1, n_vertex)], m - 1):
            s_st = ["0"] * n_vertex
            s_st[-1] = "1"
            for i in s:
                s_st[n_vertex - 1 - i] = "1"
            for j in s:
                _st = s_st.copy()
                _st[n_vertex - 1 - j] = "0"
                set_sub_j = int("".join(_st), 2)
                if set_sub_j in cost_dict:
                    min_cost = float('inf')
                    for k in range(0, len(_st)):
                        if _st[k] == "1" and (len(s) == 1 or k != n_vertex - 1):
                            k = n_vertex - 1 - k
                            if cost_dict[set_sub_j][k] + math.sqrt(
                                    (vertices[j][0] - vertices[k][0]) ** 2 + (vertices[j][1] - vertices[k][1]) ** 2
                            ) < min_cost:
                                min_cost = cost_dict[set_sub_j][k] + math.sqrt(
                                    (vertices[j][0] - vertices[k][0]) ** 2 + (vertices[j][1] - vertices[k][1]) ** 2)

                    if min_cost != float('inf'):
                        s_int = int("".join(s_st), 2)
                        if s_int not in cost_dict:
                            cost_dict[s_int] = {}
                        cost_dict[s_int][j] = min_cost

    m = float('inf')
    max_s = 2 ** n_vertex - 1
    full_s = cost_dict[max_s]
    for j in full_s:
        if m > full_s[j] + math.sqrt(
                (vertices[j][0] - vertices[0][0]) ** 2 + (vertices[j][1] - vertices[0][1]) ** 2):
            m = full_s[j] + math.sqrt(
                (vertices[j][0] - vertices[0][0]) ** 2 + (vertices[j][1] - vertices[0][1]) ** 2)

    return m


if __name__ == "__main__":
    n_vertex, vertices = read_graph('tsp.txt')
    time_start = time.time()
    print(compute_min_cost_permutation(n_vertex, vertices))
    print(time.time() - time_start)
