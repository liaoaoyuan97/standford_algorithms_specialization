import time
from os import path
from itertools import combinations
from networkx.utils.union_find import UnionFind


def read_nodes(filename):
    i = 0
    nodes = list()

    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            if i == 0:
                _list = row.strip("\n").split(' ')
                n_nodes, n_bits = int(_list[0]), int(_list[1])
                i += 1
            else:
                bits = ''.join(row.strip("\n").split(' '))
                assert len(bits) == n_bits
                nodes.append(int(bits, 2))

    return n_nodes, n_bits, nodes


def get_mask_by_bit_diff(n_bits, n_diff):
    comb = combinations([i for i in range(n_bits)], n_diff)
    masks = list()

    for idxs in list(comb):
        comb_val = ["0"] * n_bits
        for i in idxs:
            comb_val[i] = "1"
        masks.append(int("".join(comb_val), 2))

    return masks


def union_find_by_dist(node, bit_masks, union_find, nodes):
    for mask in bit_masks:
        dist_node = node ^ mask
        if dist_node in nodes and union_find[dist_node] != union_find[node]:
            union_find.union(node, dist_node)


def get_n_clusters_with_spacing_at_least_3(n_bits, nodes):
    nodes_set = set(nodes)
    union_find = UnionFind(list(nodes_set))
    one_bit_mask = get_mask_by_bit_diff(n_bits, 1)
    two_bit_mask = get_mask_by_bit_diff(n_bits, 2)

    for node in nodes_set:
        union_find_by_dist(node, one_bit_mask, union_find, nodes_set)
        union_find_by_dist(node, two_bit_mask, union_find, nodes_set)

    leader_set = set([union_find[i] for i in nodes_set])
    return len(leader_set)


if __name__ == "__main__":
    n_nodes, n_bits, nodes = read_nodes("clustering_big.txt")

    time_start = time.time()
    print(get_n_clusters_with_spacing_at_least_3(n_bits, nodes))
    print(time.time() - time_start)
