import time
import numpy as np
from os import path


def read_knapsacks(filename):
    i = 0
    knapsacks = list()

    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            if i == 0:
                _list = row.strip("\n").split(' ')
                capacity, n_knapsack = int(_list[0]), int(_list[1])
                i += 1
            else:
                _list = row.strip("\n").split(' ')
                knapsacks.append((int(_list[0]), int(_list[1])))

    assert len(knapsacks) == n_knapsack
    return knapsacks, capacity


def restruct_dp(knapsacks, capacity):
    n_knapsacks = len(knapsacks)
    sub_solutions = np.zeros((n_knapsacks + 1, capacity + 1))

    for i in range(1, n_knapsacks + 1):
        for j in range(0, capacity + 1):
            m = sub_solutions[i - 1][j]
            w_i = knapsacks[i - 1][1]
            v_i = knapsacks[i - 1][0]
            if j >= w_i and sub_solutions[i - 1][j - w_i] + v_i > m:
                m = sub_solutions[i - 1][j - w_i] + v_i
            sub_solutions[i][j] = m

    return sub_solutions[n_knapsacks][capacity]


def optimized_space_dp(knapsacks, capacity):
    knapsacks = sorted(knapsacks, key=lambda x: x[0], reverse=True)
    n_knapsacks = len(knapsacks)
    sub_solutions = np.zeros((2, capacity + 1))

    for i in range(1, n_knapsacks + 1):
        w_i = knapsacks[i - 1][1]
        v_i = knapsacks[i - 1][0]
        for j in range(w_i, capacity + 1):
            if sub_solutions[0][j - w_i] + v_i > sub_solutions[0][j]:
                sub_solutions[1][j] = sub_solutions[0][j - w_i] + v_i
        sub_solutions[0] = sub_solutions[1]

    return sub_solutions[1][capacity]


if __name__ == "__main__":
    knapsacks, capacity = read_knapsacks("knapsack1.txt")
    time_start = time.time()
    print(restruct_dp(knapsacks, capacity))
    print(time.time() - time_start)

    knapsacks, capacity = read_knapsacks("knapsack_big.txt")
    time_start = time.time()
    print(optimized_space_dp(knapsacks, capacity))
    print(time.time() - time_start)

