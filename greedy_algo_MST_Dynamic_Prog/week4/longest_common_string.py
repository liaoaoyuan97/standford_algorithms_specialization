import numpy as np


def compute_lcs_length_no_consecutive_needed(x, y):
    len_x = len(x)
    len_y = len(y)
    sub_sol = np.zeros((len_x + 1, len_y + 1))

    for i in range(1, len_x + 1):
        for j in range(1, len_y + 1):
            if x[i - 1] == y[j - 1]:
                sub_sol[i][j] = sub_sol[i - 1][j - 1] + 1
            else:
                sub_sol[i][j] = max(sub_sol[i - 1][j], sub_sol[i][j - 1])

    return sub_sol[len_x][len_y]


def compute_lcs_length_consecutive_needed(x, y):
    len_x = len(x)
    len_y = len(y)
    sub_sol = np.zeros((len_x + 1, len_y + 1, 3))

    for i in range(1, len_x + 1):
        for j in range(1, len_y + 1):
            if x[i - 1] == y[j - 1]:
                last_matched_l = 1
                if sub_sol[i - 1][j - 1][1] and sub_sol[i - 1][j - 1][2]:
                    last_matched_l += sub_sol[i - 1][j - 1][0]
                m = (last_matched_l, True, True)
                if sub_sol[i - 1][j][0] > m[0]:
                    m = (sub_sol[i - 1][j][0], False, sub_sol[i - 1][j][2])
                if sub_sol[i][j - 1][0] > m[0]:
                    m = (sub_sol[i][j - 1][0], sub_sol[i][j - 1][1], False)
            else:
                m = (sub_sol[i - 1][j][0], False, sub_sol[i - 1][j][2])
                if sub_sol[i][j - 1][0] > m[0]:
                    m = (sub_sol[i][j - 1][0], sub_sol[i][j - 1][1], False)

            sub_sol[i][j] = m

    return sub_sol[len_x][len_y][0]


if __name__ == "__main__":
    assert compute_lcs_length_no_consecutive_needed("abcdgh", "aedfhr") == 3
    assert compute_lcs_length_no_consecutive_needed("aggtab", "gxtxayb") == 4

    assert compute_lcs_length_consecutive_needed("abcdgh", "acdfhr") == 2
