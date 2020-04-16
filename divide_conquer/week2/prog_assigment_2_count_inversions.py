def merge_and_sort(arr_l, cnt_l, arr_r, cnt_r):
    len_l = len(arr_l)
    len_r = len(arr_r)

    sorted_arr = []
    l = 0
    r = 0
    merge_cnt = 0
    while l < len_l and r < len_r:
        if arr_l[l] < arr_r[r]:
            sorted_arr.append(arr_l[l])
            l += 1
        elif arr_l[l] > arr_r[r]:
            sorted_arr.append(arr_r[r])
            merge_cnt += len_l - l
            r += 1
        else:
            ValueError("Duplicate integers.")

    sorted_arr += arr_l[l:] + arr_r[r:]
    return sorted_arr, cnt_l + cnt_r + merge_cnt


def sort(arr, cnt):
    if len(arr) < 2:
        return arr, 0

    mid = int(len(arr) / 2)
    arr_l, cnt_l = sort(arr[:mid], cnt)
    arr_r, cnt_r = sort(arr[mid:], cnt)

    return merge_and_sort(arr_l, cnt_l, arr_r, cnt_r)


def main():
    with open('IntegerArray.txt', 'r') as f:
        array = []
        for line in f.readlines():
            array.append(int(line))

    sorted_arr, result = sort(array, 0)
    print(result)


if __name__ == "__main__":
    main()
