from quicksort_first_pivot import read_input


def quicksort_last_pivot(arr, l, r):
    if (r - l) < 2:
        return 0

    t = arr[r - 1]
    arr[r - 1] = arr[l]
    arr[l] = t

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

    return r - l - 1 + quicksort_last_pivot(arr, l, i - 1) + quicksort_last_pivot(arr, i, r)

    # if (r - l) < 2:
    #     return 0
    #
    # p = arr[r - 1]
    # i = l
    #
    # for j in range(l, r - 1):
    #     if arr[j] < p:
    #         t = arr[j]
    #         arr[j] = arr[i]
    #         arr[i] = t
    #         i += 1
    #
    # if arr[i] != p:
    #     t = arr[i]
    #     arr[i] = p
    #     arr[r - 1] = t
    # return r - l - 1 + quicksort_last_pivot(arr, l, i) + quicksort_last_pivot(arr, i + 1, r)


if __name__ == "__main__":
    input_arr = read_input('quicksort.txt')
    cmp_cnt = quicksort_last_pivot(input_arr, 0, len(input_arr))
    # print(input_arr)
    print(cmp_cnt)
