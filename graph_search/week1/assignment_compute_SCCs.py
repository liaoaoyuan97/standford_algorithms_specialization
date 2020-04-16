from os import path
from collections import deque
from collections import Counter


class SCCGraph:
    def __init__(self):
        self.fw_edges = dict()
        self.bt_edges = dict()
        self.v_set = set()

    def add_edge(self, head, tail):
        if head not in self.fw_edges:
            self.fw_edges[head] = [tail]
        else:
            self.fw_edges[head].append(tail)

        if tail not in self.bt_edges:
            self.bt_edges[tail] = [head]
        else:
            self.bt_edges[tail].append(head)

    def get_vertex_set(self):
        return set(self.fw_edges.keys()).union(set(self.bt_edges.keys()))

    def dfs_stack_two_passes(self, edges_dict, explored_v_set, cur_leader, leaders_dict, f, finish_time):
        stack = deque()
        stack.append(cur_leader)
        explored_v_set.add(cur_leader)

        while len(stack) != 0:
            v = stack[-1]

            _has_child_to_explore = False
            for t in edges_dict.get(v, []):
                if t not in explored_v_set:
                    _has_child_to_explore = True
                    stack.append(t)
                    explored_v_set.add(t)
                    break

            if not _has_child_to_explore:
                v = stack.pop()
                leaders_dict[v] = cur_leader
                finish_time[v] = f
                f += 1

        return f

    def compute_scc(self):
        # 1st pass
        _explored_set = set()
        finishing_time = dict()
        _leaders_dict = dict()
        f = 1

        for v in self.v_set:
            if v not in _explored_set:
                f = self.dfs_stack_two_passes(
                    self.fw_edges,
                    _explored_set, v, _leaders_dict, f, finishing_time
                )

        assert f == (len(_explored_set) + 1)

        # 2nd pass
        _explored_set = set()
        leaders_dict = dict()
        _finishing_time = dict()
        _f = 1

        # print("2nd pass", sorted(finishing_time, key=finishing_time.get, reverse=True))
        for v in sorted(finishing_time, key=finishing_time.get, reverse=True):
            if v not in _explored_set:
                self.dfs_stack_two_passes(
                    self.bt_edges,
                    _explored_set, v, leaders_dict, _f, _finishing_time
                )
        assert f == (len(_explored_set) + 1)
        return leaders_dict


def read_graph(filename, graph):
    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            vertices = row.strip('\t\r\n').split(' ')
            graph.add_edge(int(vertices[0]), int(vertices[1]))


def max_5_scc_size(graph):
    leaders_dict = graph.compute_scc()
    sizes = Counter(list(leaders_dict.values()))
    return [t[1] for t in sizes.most_common(5)]


if __name__ == "__main__":
    graph = SCCGraph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.add_edge(5, 4)
    graph.v_set = graph.get_vertex_set()
    assert max_5_scc_size(graph) == [3, 1, 1]

    graph = SCCGraph()
    graph.add_edge(4, 5)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(5, 3)
    graph.add_edge(2, 1)
    graph.v_set = graph.get_vertex_set()
    assert max_5_scc_size(graph) == [3, 1, 1]

    graph = SCCGraph()
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 1)
    graph.add_edge(1, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(6, 4)
    graph.v_set = graph.get_vertex_set()
    assert max_5_scc_size(graph) == [3, 3]

    graph = SCCGraph()
    graph.add_edge(2, 3)
    graph.add_edge(3, 2)
    graph.add_edge(2, 4)
    graph.add_edge(4, 2)
    graph.add_edge(2, 1)
    graph.add_edge(1, 2)
    graph.add_edge(3, 1)
    graph.add_edge(4, 1)
    graph.add_edge(4, 4)
    graph.add_edge(4, 3)
    graph.v_set = graph.get_vertex_set()
    assert max_5_scc_size(graph) == [4]

    read_graph("SCC.txt", graph)
    graph.v_set = set([v for v in range(1, 875715)])
    print(max_5_scc_size(graph))
