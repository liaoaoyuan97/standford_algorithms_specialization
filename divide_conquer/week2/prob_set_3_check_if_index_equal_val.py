# You are given a sorted (from smallest to largest) array A of n distinct integers which can be positive, negative, or zero.
# You want to decide whether or not there is an index i such that A[i] = i.
# Design the fastest algorithm that you can for solving this problem.

import math


def check_if_idx_equal_val(arr):
    len_a = len(arr)
    if len_a == 1:
        return arr[0] == 0
    elif len_a < 1:
        return False

    mid = int(len_a / 2)
    if arr[mid] == mid:
        return True
    elif arr[mid] < mid:
        l = max(0, math.ceil(arr[mid]))
        r = mid
    else:
        r = min(len_a, int(arr[mid]))
        l = mid

    return check_if_idx_equal_val(arr[0: l]) or check_if_idx_equal_val([i-r-1 for i in arr[r+1: len_a]])


if __name__ == "__main__":
    input_arr = [-2, -1.5, 2, 2.5, 3, 4.5, 6]
    print(check_if_idx_equal_val(input_arr))
