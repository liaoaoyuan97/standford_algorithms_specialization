import numpy as np


def reconstruct_dp(knapsacks, capacity1, capacity2):
    n_knapsacks = len(knapsacks)
    sub_sols = np.zeros((n_knapsacks + 1, capacity1 + 1, capacity2 + 1))

    for i in range(1, n_knapsacks + 1):
        w = knapsacks[i - 1][1]
        v = knapsacks[i - 1][0]
        for c1 in range(0, capacity1 + 1):
            for c2 in range(0, capacity2 + 1):
                val1 = sub_sols[i - 1][c1][c2]
                if c1 >= w:
                    val1 = sub_sols[i - 1][c1 - w][c2] + v

                val2 = sub_sols[i - 1][c1][c2]
                if c2 >= w:
                    val2 = sub_sols[i - 1][c1][c2 - w] + v
                sub_sols[i][c1][c2] = max(val1, val2, sub_sols[i-1][c1][c2])
    return sub_sols[n_knapsacks][capacity1][capacity2]


if __name__ == "__main__":
    knapsacks = [(7, 1), (1, 3), (4, 4), (10, 8), (9, 15)]
    assert reconstruct_dp(knapsacks, 2, 29) == 30

    knapsacks = [(3, 3), (2, 2), (8, 8)]
    assert reconstruct_dp(knapsacks, 10, 3) == 13

    knapsacks = [(3, 3), (5, 5), (8, 8)]
    assert reconstruct_dp(knapsacks, 10, 3) == 11

