from os import path


def read_input(filename):
    result = []
    with open(path.join('.', filename), 'r') as f:
        for i in f.readlines():
            ele = int(i)
            result.append(ele)
    return result


def quicksort_first_pivot(arr, l, r):
    if (r - l) < 2:
        return 0

    p = arr[l]
    i = l + 1

    for j in range(l + 1, r):
        if arr[j] < p:
            t = arr[j]
            arr[j] = arr[i]
            arr[i] = t
            i += 1

    if arr[i - 1] != p:
        t = arr[i - 1]
        arr[i - 1] = arr[l]
        arr[l] = t

    return r - l - 1 + quicksort_first_pivot(arr, l, i - 1) + quicksort_first_pivot(arr, i, r)


if __name__ == "__main__":
    input_arr = read_input('quicksort.txt')
    cmp_cnt = quicksort_first_pivot(input_arr, 0, len(input_arr))
    print(cmp_cnt)
    # print(input_arr)
