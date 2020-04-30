# O(n^2)

import numpy as np


def compute_optimal_avg_cost_bst(nodes):
    sorted_nodes = sorted(nodes, key=lambda x: x[0])
    n_nodes = len(sorted_nodes)
    result = np.ones((n_nodes, n_nodes)) * float('Inf')
    r = np.zeros((n_nodes, n_nodes))
    for i in range(n_nodes):
        r[i][i] = i
        result[i][i] = sorted_nodes[i][1]

    for s in range(1, n_nodes):
        for i in range(0, n_nodes - 1):
            start = i
            end = i + s
            if end < n_nodes:
                print(start, end)
                # import pdb;pdb.set_trace()

                m = float('inf')
                for k in range(int(r[start][end - 1]), int(r[start + 1][end] + 1)):
                    print(k)
                    val_lt = 0
                    val_rt = 0
                    if start <= k-1:
                        val_lt = result[start][k - 1]
                    if k + 1 <= end:
                        val_rt = result[k + 1, end]

                    if val_lt + val_rt < m:
                        m = val_lt + val_rt
                        opt_r = k

                r[start][end] = opt_r
                result[start][end] = sum([sorted_nodes[i][1] for i in range(start, end + 1)]) + m

    return result[0][n_nodes - 1]


if __name__ == "__main__":
    nodes = [(4, 4), (3, 3), (2, 2), (1, 1)]
    assert compute_optimal_avg_cost_bst(nodes) == 18
