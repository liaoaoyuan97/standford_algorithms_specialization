import statistics


# O(m)
def compute_order_statistic(costs, n, order):
    if n == 1:
        return costs[0]

    grps = []
    for i in range(0, n, 5):
        grps.append(statistics.median(costs[i: i + 5]))

    p = compute_order_statistic(grps, len(grps), int(len(grps) / 2))

    j = 0
    for i in range(0, n):
        if costs[i] < p:
            t = costs[j]
            costs[j] = costs[i]
            costs[i] = t
            j += 1

    if (order + 1) == j:
        return costs[j]
    elif (order + 1) < j:
        return compute_order_statistic(costs[:j], j, order)
    else:
        return compute_order_statistic(costs[j:], n - j - 1, order - j - 1)


def compute_minimum_bottleneck_spanning_tree(edges, connected_vs, n_nodes, spanning_tree):
    median_cost = compute_order_statistic([t[2] for t in edges], len(edges), int(len(edges) / 2))
    below_median = list(); below_connected_nodes = set()
    at_least_median = list()
    for edge in edges:
        if edge[2] < median_cost:
            below_median.append(edge)
            below_connected_nodes.add(edge[0])
            below_connected_nodes.add(edge[1])
        else:
            at_least_median.append(edge)

    connected_vs = connected_vs.union(below_connected_nodes)
    if len(connected_vs) == n_nodes:
        return spanning_tree + below_median

    spanning_tree = spanning_tree + below_median
    return compute_minimum_bottleneck_spanning_tree(at_least_median, connected_vs, n_nodes, spanning_tree)


if __name__ == "__main__":
    n_nodes = 7
    edges = [(1, 2, 7), (2, 3, 8), (1, 4, 5), (2, 4, 9), (2, 5, 7),
             (3, 5, 5), (4, 5, 15), (4, 6, 6), (6, 5, 8), (5, 7, 7), (6, 7, 11)]
    connected_vs = set()
    spanning_tree = list()
    print(compute_minimum_bottleneck_spanning_tree(edges, connected_vs, n_nodes, spanning_tree))