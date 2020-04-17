import heapq
import time
from os import path


def read_edges(filename):
    graph = dict()
    i = 0

    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            if i == 0:
                n, m = tuple(int(j) for j in row.strip("\n").split(' '))
                i += 1
            else:
                edge = row.strip("\n").split(' ')
                u, v, cost = int(edge[0]), int(edge[1]), float(edge[2])
                if u not in graph:
                    graph[u] = [(v, cost)]
                else:
                    graph[u].append((v, cost))

                if v not in graph:
                    graph[v] = [(u, cost)]
                else:
                    graph[v].append((u, cost))

    assert len(graph) == n
    assert sum([len(edge) for _, edge in graph.items()]) == 2 * m
    return graph


def compute_min_cost_MST(graph):
    connected_vs = set()
    heap = []
    heapq.heappush(heap, (0, 1))  # (cost, vertex_id)
    n_vertices = len(graph)
    distances = {i: float('+inf') for i in graph}
    distances[1] = 0
    min_cost = 0

    while len(connected_vs) < n_vertices:
        # import pdb;pdb.set_trace()
        cur_cost, cur_v = heapq.heappop(heap)

        if cur_v in connected_vs:
            continue

        connected_vs.add(cur_v)
        # print(cur_v, cur_cost)
        min_cost += cur_cost

        for neighbor, cost in graph[cur_v]:
            if neighbor not in connected_vs and cost < distances[neighbor]:
                distances[neighbor] = cost
                heapq.heappush(heap, (cost, neighbor))

    return min_cost


if __name__ == "__main__":
    graph = read_edges("edges.txt")
    # graph = {1: [(2, 2),(4, 1)], 2:[{1, 2}, (3,3)],3:[(2,3), (4,4)], 4:[(1,4)] }

    time_start = time.time()
    print(compute_min_cost_MST(graph))
    print(time.time() - time_start)
