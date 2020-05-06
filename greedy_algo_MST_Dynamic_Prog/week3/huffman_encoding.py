from os import path
from collections import deque


class TreeNode:
    def __init__(self, idx, value):
        self.idx = idx
        self.value = value
        self.parent = None
        self.left_child = None
        self.right_child = None


def read_nodes(filename):
    i = 0
    nodes = list()

    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            if i == 0:
                n_nodes = int(row.strip("\n"))
                i += 1
            else:
                nodes.append(float(row.strip("\n")))

    assert len(nodes) == n_nodes
    return n_nodes, nodes


def bfs_binary_tree(root, tree_size):
    min_depth, max_depth = float("+inf"), 0
    node_queue = deque([root])
    dists = {i: 0 for i in range(tree_size)}

    while len(node_queue) > 0:
        cur = node_queue.pop()
        left = cur.left_child
        right = cur.right_child

        if left is not None:
            node_queue.append(left)
            dists[left.idx] = dists[cur.idx] + 1

        if right is not None:
            node_queue.append(right)
            dists[right.idx] = dists[cur.idx] + 1

        if left is None and right is None:
            if dists[cur.idx] < min_depth:
                min_depth = dists[cur.idx]
            if dists[cur.idx] > max_depth:
                max_depth = dists[cur.idx]

    return min_depth, max_depth


def build_huffman_tree(nodes):
    sorted_nodes = sorted(nodes)
    node_queue = deque()
    i = 0
    for node in sorted_nodes:
        node_queue.append(TreeNode(i, node))
        i += 1

    merged_nodes = deque()
    while len(node_queue) + len(merged_nodes) > 1:
        single_node_1 = None; single_node_2 = None
        if len(node_queue) > 0:
            single_node_1 = node_queue.popleft()
        if len(node_queue) > 0:
            single_node_2 = node_queue.popleft()

        merger_1 = None; merger_2 = None
        if len(merged_nodes) > 0:
            merger_1 = merged_nodes.popleft()
        if len(merged_nodes) > 0:
            merger_2 = merged_nodes.popleft()

        if merger_1 is None or (single_node_2 is not None and single_node_2.value < merger_1.value):
            new_merger = TreeNode(i, single_node_1.value + single_node_2.value)
            new_merger.left_child = single_node_1
            new_merger.right_child = single_node_2
            merged_nodes.append(new_merger)

            if merger_1 is not None:
                merged_nodes.appendleft(merger_1)
            if merger_2 is not None:
                merged_nodes.appendleft(merger_2)

            i += 1
            continue

        if single_node_1 is None or (merger_2 is not None and merger_2.value < single_node_1.value):
            new_merger = TreeNode(i, merger_1.value + merger_2.value)
            new_merger.left_child = merger_1
            new_merger.right_child = merger_2
            merged_nodes.append(new_merger)

            if single_node_1 is not None:
                node_queue.appendleft(single_node_1)
            if single_node_2 is not None:
                node_queue.appendleft(single_node_2)

            i += 1
            continue

        new_merger = TreeNode(i, single_node_1.value + merger_1.value)
        new_merger.left_child = single_node_1
        new_merger.right_child = merger_1
        merged_nodes.append(new_merger)

        if merger_2 is not None:
            merged_nodes.appendleft(merger_2)
        if single_node_2 is not None:
            node_queue.appendleft(single_node_2)

        i += 1

    min_depth, max_depth = bfs_binary_tree(new_merger, i)
    print(min_depth, max_depth)


if __name__ == "__main__":
    n_nodes, nodes = read_nodes("huffman.txt")
    build_huffman_tree(nodes)

