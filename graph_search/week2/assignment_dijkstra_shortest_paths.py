import heapq
import time
from os import path
from math import floor


class Heap:
    def __init__(self):
        self.size = 0
        self.array = []
        self.v2index_map = {}

    def __get_parent_index(self, idx):
        return int(floor((idx - 1) / 2))

    def __get_left_child_index(self, idx):
        return 2 * idx + 1

    def __get_right_child_index(self, idx):
        return 2 * idx + 2

    def __swap_value(self, i, j):
        t = self.array[i]

        self.v2index_map[t[0]] = j
        self.v2index_map[self.array[j][0]] = i

        self.array[i] = self.array[j]
        self.array[j] = t

    def __bubble_up(self, idx):
        parent_idx = self.__get_parent_index(idx)
        while parent_idx >= 0:
            if self.array[parent_idx][1] <= self.array[idx][1]:
                break

            self.__swap_value(parent_idx, idx)
            idx = parent_idx
            parent_idx = self.__get_parent_index(idx)

    def __bubble_down(self, idx):
        left_idx = self.__get_left_child_index(idx)
        right_idx = self.__get_right_child_index(idx)

        while left_idx < self.size or right_idx < self.size:
            min_idx = left_idx
            if left_idx >= self.size or (right_idx < self.size and self.array[right_idx][1] < self.array[left_idx][1]):
                min_idx = right_idx

            if self.array[idx][1] < self.array[min_idx][1]:
                break

            self.__swap_value(idx, min_idx)
            idx = min_idx
            left_idx = self.__get_left_child_index(idx)
            right_idx = self.__get_right_child_index(idx)

    def get_vertex_key(self, v_id):
        return self.array[self.v2index_map[v_id]][1]

    def pop(self):
        if self.size < 1:
            raise IndexError

        min_node = self.array[0]
        self.size = self.size - 1
        self.__swap_value(0, self.size)
        self.array.pop()

        if self.size > 1:
            self.__bubble_down(0)

        del self.v2index_map[min_node[0]]

        return min_node

    def insert(self, node):
        self.array.append(node)
        self.v2index_map[node[0]] = self.size
        self.size = self.size + 1

        if self.size > 1:
            self.__bubble_up(self.size - 1)

    def modify_key(self, v_id, update_val):
        idx = self.v2index_map[v_id]
        self.array[idx] = (v_id, update_val)

        parent_idx = self.__get_parent_index(idx)
        if parent_idx >= 0 and self.array[idx][1] < self.array[parent_idx][1]:
            self.__bubble_up(idx)
        else:
            self.__bubble_down(idx)


def read_graph(filename):
    graph = dict()

    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            edges = row.strip('\t\n').split('\t')

            s = int(edges[0])
            graph[s] = []
            for i in range(1, len(edges)):
                edge = edges[i].split(',')
                graph[s].append((int(edge[0]), int(edge[1])))

    return graph


def get_shortest_paths_heapq(graph):
    heap = []
    heapq.heappush(heap, (0, 1))  # (dj_score, vertex_id)
    distances = {i: 1000000 for i in graph}
    distances[1] = 0
    X = []

    while heap:
        cur_distance, cur_v = heapq.heappop(heap)

        if cur_distance > distances[cur_v]:
            continue

        # added to X
        X.append(cur_v)
        for neighbor, weight in graph[cur_v]:
            dj_score = cur_distance + weight
            if dj_score < distances[neighbor]:
                distances[neighbor] = dj_score
                heapq.heappush(heap, (dj_score, neighbor))

    return distances, X


def get_shortest_paths_self_defined_heap(graph):
    heap = Heap()
    heap.insert((1, 0))  # (vertex_id, dj_score)
    for v in graph:
        if v != 1:
            heap.insert((v, 1000000))

    shortest_paths = dict()
    n_v = len(graph)

    while len(shortest_paths) < n_v:
        assert len(shortest_paths) + heap.size == n_v

        cur_v, v_score = heap.pop()
        shortest_paths[cur_v] = v_score

        for neighbor, weight in graph[cur_v]:
            dj_score = v_score + weight
            # import pdb;pdb.set_trace()
            if neighbor not in shortest_paths and dj_score < heap.get_vertex_key(neighbor):
                heap.modify_key(neighbor, dj_score)

    return shortest_paths


if __name__ == "__main__":
    # test case 1, output: {1: 0, 2: 1, 3: 2, 4: 2, 5: 3, 6: 4}
    # graph = {
    #     1: [(6, 7), (5, 3), (2, 1), (4, 2), (3, 3)],
    #     2: [(1, 1), (3, 1), (4, 1), (6, 6)],
    #     3: [(1, 3), (2, 1), (6, 2)],
    #     4: [(2, 1), (1, 2), (6, 5)],
    #     5: [(1, 3), (6, 3)],
    #     6: [(1, 7), (3, 2), (2, 6), (4, 5), (5, 3)]
    # }

    graph = read_graph("Dijkstra.txt")

    dedup_edges = set()
    for k, _ in graph.items():
        for v in _:
            dedup_edges.add((k, v[0], v[1]))
            dedup_edges.add((v[0], k, v[1]))
    assert len(dedup_edges) == sum([len(e) for e in graph.values()])

    # graph = {}

    # heap = Heap()
    # heap.insert((1,0))
    # heap.insert((2,0))
    # heap.pop()

    start_t = time.time()
    min_distances,X = get_shortest_paths_heapq(graph)
    print(time.time() - start_t)

    # print(min_distances)
    e = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    print(",".join([str(int(min_distances[i])) for i in e]))

    start_t = time.time()
    min_distances = get_shortest_paths_self_defined_heap(graph, X)
    print(time.time() - start_t)

    # print(min_distances)
    e = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    print(",".join([str(int(min_distances[i])) for i in e]))
