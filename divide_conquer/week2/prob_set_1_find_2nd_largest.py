# You are given as input an unsorted array of n distinct numbers, where n is a power of 2. Give an algorithm that identifies the second-largest number in the array,
# and that uses at most n +\log_2 n −2 comparisons.


def find_maximum(arr, cmp_idxs):
    if len(arr) < 3:
        cmp_idxs[arr[1]].add(arr[0])
        cmp_idxs[arr[0]].add(arr[1])
        if arr[0] > arr[1]:
            return arr[0], cmp_idxs
        elif arr[1] > arr[0]:
            return arr[1], cmp_idxs
        else:
            ValueError("Duplicate numbers")

    if len(arr) % 2 != 0:
        ValueError("Length of array is not 2^k.")

    n_pairs = int(len(arr) / 2)
    start = 0
    next_arr = []
    for i in range(n_pairs):
        _maximum, _cmp_idxs = find_maximum(arr[start:start+2], cmp_idxs)
        for k in _cmp_idxs:
            cmp_idxs[k] = cmp_idxs[k].union(_cmp_idxs[k])
        next_arr.append(_maximum)
        start = start + 2

    return find_maximum(next_arr, cmp_idxs)

if __name__ == "__main__":
    input_arr = [10, 20, 1, 2, 12, 23, 50, 6]
    cmp_idxs = dict()
    for k in input_arr:
        cmp_idxs[k] = set()

    maximum, cmp_idxs = find_maximum(input_arr, cmp_idxs)
    cmp_len = len(cmp_idxs[maximum])
    results = list(cmp_idxs[maximum])
    result = results[0]
    for i in results[1:cmp_len]:
        if i > result:
            result = i

    print(result)