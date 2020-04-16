# You are a given a unimodal array of n distinct elements, meaning that its entries are in increasing order up until its maximum element,
# after which its elements are in decreasing order.
# Give an algorithm to compute the maximum element that runs in O(log n) time.


def find_max(arr):
    if len(arr) < 2:
        return arr[0]

    mid = int(len(arr) / 2) - 1
    if arr[mid] < arr[mid+1]:
        return find_max(arr[mid+1: len(arr)])
    elif arr[mid] > arr[mid+1]:
        return find_max(arr[:mid+1])
    else:
        ValueError("Duplicate numbers!")

if __name__ == "__main__":
    input_arr = [1, 2, 5, 4, 3]
    print(find_max(input_arr))
