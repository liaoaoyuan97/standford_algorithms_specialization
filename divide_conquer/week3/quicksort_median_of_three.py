from quicksort_first_pivot import read_input


def quicksort_median(arr, l, r):
    if (r - l) < 2:
        return 0

    threes = [l, r - 1, int((r - l + 1) / 2 - 1) + l]

    for i in range(2):
        for j in range(i + 1, 3):
            if arr[threes[i]] > arr[threes[j]]:
                t = threes[i]
                threes[i] = threes[j]
                threes[j] = t

    # print(threes, [arr[i] for i in threes])
    # import pdb;pdb.set_trace()
    if threes[1] != l:
        t = arr[threes[1]]
        arr[threes[1]] = arr[l]
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

    return r - l - 1 + quicksort_median(arr, l, i - 1) + quicksort_median(arr, i, r)

    # if (r - l) < 2:
    #     return 0
    #
    # threes = [l, r - 1, int((r - l) / 2)]
    # for i in range(2):
    #     for j in range(i + 1, 3):
    #         if arr[threes[i]] > arr[threes[j]]:
    #             t = threes[i]
    #             threes[i] = threes[j]
    #             threes[j] = t
    #
    # p_idx = threes[1]
    # p = arr[p_idx]
    # i = l
    #
    # for j in range(l, r):
    #     if j == threes[1]:
    #         continue
    #     if arr[j] < p:
    #         t = arr[j]
    #         arr[j] = arr[i]
    #         arr[i] = t
    #         if i == p_idx:
    #             p_idx = j
    #         i += 1
    #
    # if arr[i] != p:
    #     t = arr[i]
    #     arr[i] = p
    #     arr[p_idx] = t
    #     p_idx = i
    #
    # return r - l - 1 + quicksort_median(arr, l, p_idx) + quicksort_median(arr, p_idx + 1, r)


if __name__ == "__main__":
    input_arr = read_input('quicksort.txt')
    cmp_cnt = quicksort_median(input_arr, 0, len(input_arr))
    print(input_arr)
    print(cmp_cnt)
