from os import path


def read_nodes(filename):
    i = 0
    weights = list()

    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            if i == 0:
                n_nodes = int(row.strip("\n"))
                i += 1
            else:
                weights.append(float(row.strip("\n")))

    assert len(weights) == n_nodes
    return n_nodes, weights


def compute_mwis(weights):
    n_nodes = len(weights)
    weight_sum = [0] * (n_nodes + 1)
    node_set = set()
    weight_sum[1] = weights[0]

    for i in range(2, n_nodes + 1):
        weight_sum_i_included = weight_sum[i - 2] + weights[i - 1]
        if weight_sum[i - 1] < weight_sum_i_included:
            weight_sum[i] = weight_sum_i_included
        else:
            weight_sum[i] = weight_sum[i - 1]

    i = n_nodes
    while i > 1:
        if weight_sum[i - 2] + weights[i - 1] > weight_sum[i - 1]:
            node_set.add(i)
            i = i - 2
        else:
            i = i - 1
    if i == 1:
        node_set.add(1)

    # print(node_set)
    output = ""
    for i in [1, 2, 3, 4, 17, 117, 517, 997]:
        if i in node_set:
            output += "1"
        else:
            output += "0"

    print(output)


if __name__ == "__main__":
    n_nodes, weights = read_nodes("mwis.txt")
    # weights = [1,4,5,4] # output: 8
    compute_mwis(weights)
