from os import path


def read_edges(filename):
    i = 0
    edges = list()

    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            if i == 0:
                n_nodes = int(row.strip("\n"))
                i += 1
            else:
                edge = [j for j in row.strip("\n").split(' ')]
                edges.append((int(edge[0]), int(edge[1]), float(edge[2])))

    assert len(set([i[0] for i in edges] + [i[1] for i in edges])) == n_nodes

    return n_nodes, edges


def get_max_spacing_k_cluster(k, n_nodes, edges):
    sorted_edges = sorted(edges, key=lambda x: x[2])
    leader_arr = [i for i in range(n_nodes)]
    size_dict = {i: {i} for i in range(n_nodes)}

    for edge in sorted_edges:
        u, v = edge[0], edge[1]
        # import pdb;pdb.set_trace()
        leader_u, leader_v = leader_arr[u - 1], leader_arr[v - 1]
        if leader_u == leader_v:
            continue

        if len(size_dict) <= k:
            return edge[2]

        min_leader = leader_u; max_leader = leader_v
        if len(size_dict[leader_u]) < len(size_dict[leader_v]):
            min_leader = leader_v; max_leader = leader_u

        for i in size_dict[min_leader]:
            leader_arr[i] = max_leader
        size_dict[max_leader] = size_dict[max_leader].union(size_dict[min_leader])
        del size_dict[min_leader]


if __name__ == "__main__":
    n_nodes, edges = read_edges("clustering1.txt")
    print(get_max_spacing_k_cluster(4, n_nodes, edges))

