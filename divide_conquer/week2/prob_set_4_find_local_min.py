# You are given an n by n grid of distinct numbers.
# A number is a local minimum if it is smaller than all of its neighbors.
# (A neighbor of a number is one immediately above, below, to the left, or the right. Most numbers have four neighbors;
# numbers on the side have three; the four corners have two.)
# Use the divide-and-conquer algorithm design paradigm to compute a local minimum with only O(n) comparisons between pairs of numbers.
# (Note: since there are n^2 numbers in the input, you cannot afford to look at all of them.
# Hint: Think about what types of recurrences would give you the desired upper bound.)

import numpy as np


def find_local_max(matrix):
    n_rows = len(matrix)
    n_cols = len(matrix[0])

    if n_rows <= 3 or n_cols <= 3:
        return max(matrix.flatten())

    mid_row = int(n_rows / 2)
    mid_col = int(n_cols / 2)

    wind_dict = dict()
    row_idxs = (0, mid_row, n_rows - 1)
    col_idxs = (0, mid_col, n_cols - 1)
    for i in row_idxs:
        for j in range(n_cols):
            wind_dict[(i, j)] = matrix[i, j]

    for i in col_idxs:
        for j in range(n_rows):
            wind_dict[(j, i)] = matrix[j, i]

    max_idx = max(wind_dict, key=wind_dict.get)
    maximum = wind_dict[max_idx]
    left_idx = max_idx[1] - 1
    right_idx = max_idx[1] + 1
    up_idx = max_idx[0] - 1
    down_idx = max_idx[0] + 1
    if ((left_idx < 0 or matrix[max_idx[0], left_idx] < maximum) and
        (right_idx > n_cols or matrix[max_idx[0], right_idx] < maximum)) and (
            (up_idx < 0 or matrix[up_idx, max_idx[1]] < maximum) and
            (down_idx > n_rows or matrix[down_idx, max_idx[1]] < maximum)):
        return maximum
    elif left_idx >= 0 and matrix[max_idx[0], left_idx] > maximum and (max_idx[0], left_idx) not in wind_dict:
        c_start = max([c if c < left_idx else -1 for c in col_idxs])
        r_start = max([r if r < max_idx[0] else -1 for r in row_idxs])
        r_end = min([r if r > max_idx[0] else n_rows + 1 for r in row_idxs])
        return find_local_max(matrix[r_start+1:r_end, c_start+1:left_idx+1])
    elif right_idx <= n_cols and matrix[max_idx[0], right_idx] > maximum and (max_idx[0], right_idx) not in wind_dict:
        c_end = min([c if c > right_idx else n_cols + 1 for c in col_idxs])
        r_start = max([r if r < max_idx[0] else -1 for r in row_idxs])
        r_end = min([r if r > max_idx[0] else n_rows + 1 for r in row_idxs])
        return find_local_max(matrix[r_start+1:r_end, right_idx:c_end])
    elif up_idx >= 0 and matrix[up_idx, max_idx[1]] > maximum and (up_idx, max_idx[1]) not in wind_dict:
        r_start = max([r if r < up_idx else -1 for r in row_idxs])
        c_start = max([c if c < max_idx[1] else -1 for c in col_idxs])
        c_end = min([c if c > max_idx[1] else n_cols + 1 for c in col_idxs])
        return find_local_max(matrix[r_start+1:up_idx+1, c_start+1:c_end])
    elif down_idx <= n_rows and matrix[down_idx, max_idx[1]] > maximum and (down_idx, max_idx[1]) not in wind_dict:
        r_end = min([r if r > max_idx[0] else n_rows + 1 for r in row_idxs])
        c_start = max([c if c < max_idx[1] else -1 for c in col_idxs])
        c_end = min([c if c > max_idx[1] else n_cols + 1 for c in col_idxs])
        return find_local_max(matrix[down_idx:r_end, c_start+1:c_end])


if __name__ == "__main__":
    matrix = np.array([[0, 1, 2, 3, 4, 5],
                       [19, 35, 20, 24, 32, 6],
                       [31, 34, 21, 27, 33, 7],
                       [17, 30, 22, 25, 18, 8],
                       [16, 28, 23, 26, 29, 9],
                       [15, 14, 13, 12, 11, 10]])
    print(find_local_max(matrix))
