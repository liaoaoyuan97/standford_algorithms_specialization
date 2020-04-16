import time
import heapq
from os import path
from bintrees import RBTree


def read_array(filename):
    result = list()

    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            result.append(int(row.strip("\n")))

    assert len(result) == 10000
    assert min(result) == 1
    assert max(result) == 10000

    return result


def median_maintenance_heaps(arr):
    sum_median = arr[0]
    heap_low = []; heap_high = []

    if arr[0] > arr[1]:
        heapq.heappush(heap_low, -arr[1])
        heapq.heappush(heap_high, arr[0])
        sum_median += arr[1]
    else:
        heapq.heappush(heap_low, -arr[0])
        heapq.heappush(heap_high, arr[1])
        sum_median += arr[0]

    i = 3

    for cur_num in arr[2:]:
        max_heap_low = -heap_low[0]
        min_heap_high = heap_high[0]
        # import pdb;pdb.set_trace()
        if i % 2 == 1:
            if max_heap_low <= cur_num <= min_heap_high:
                sum_median += cur_num
                # print(cur_num)
                heapq.heappush(heap_low, -cur_num)
            elif cur_num < max_heap_low:
                heapq.heappush(heap_low, -cur_num)
                # print(-heap_low[0])
                sum_median += -heap_low[0]
            else:
                heapq.heappush(heap_high, cur_num)
                # print(heap_high[0])
                sum_median += heap_high[0]
        else:
            if cur_num < max_heap_low:
                heapq.heappush(heap_low, -cur_num)
            else:
                heapq.heappush(heap_high, cur_num)

            if len(heap_low) > len(heap_high):
                heapq.heappush(heap_high, - heapq.heappop(heap_low))
            elif len(heap_low) < len(heap_high):
                heapq.heappush(heap_low, - heapq.heappop(heap_high))

            # print(-heapq.heappop(heap_low))
            sum_median += -heap_low[0]
        i += 1

    assert len(heap_high) + len(heap_low) == len(arr)
    return sum_median


def post_order_traverse(cur):
    """
    O(n) to calculate the size of tree rooted by each node. Alternative optimization is to move it to the insert
    method. In terms of time, I didn't overwrite the method in bintrees module.
    """
    if cur is not None:
        if cur.left is None and cur.right is None:
            cur.value = 1
            return

        left_size = 0
        if cur.left is not None:
            post_order_traverse(cur.left)
            left_size = cur.left.value

        right_size = 0
        if cur.right is not None:
            post_order_traverse(cur.right)
            right_size = cur.right.value

        cur.value = left_size + right_size + 1


# O(logn)
def select_order_statisic(subtree_root, i):
    # print(subtree_root.val)
    # assert subtree_root.value >= i

    if subtree_root is not None:
        if subtree_root.left is None:
            if i == 1:
                return subtree_root.key
            else:
                return select_order_statisic(subtree_root.right, i - 1)

        if subtree_root.right is None:
            if i == (subtree_root.left.value + 1):
                return subtree_root.key
            else:
                return select_order_statisic(subtree_root.left, i)

        left_tree_size = subtree_root.left.value
        if i == (left_tree_size + 1):
            return subtree_root.key
        elif i <= left_tree_size:
            return select_order_statisic(subtree_root.left, i)
        else:
            return select_order_statisic(subtree_root.right, i - left_tree_size - 1)


def median_maintenance_rbtree(arr):
    median_sum = arr[0]
    rbtree = RBTree([(arr[0], 1)])  # (number, subtree_size)

    for i in range(1, len(arr)):
        ele = arr[i]
        rbtree.insert(ele, 1)
        post_order_traverse(rbtree._root)
        # assert rbtree._root.value == (i+1)
        median_order = int(i / 2) + 1
        median_sum += select_order_statisic(rbtree._root, median_order)

    return median_sum


if __name__ == "__main__":
    input_arr = read_array("median_maintenance.txt")

    time_start = time.time()
    print(median_maintenance_heaps(input_arr) % 10000)
    print(time.time() - time_start)

    time_start = time.time()
    # input_arr = [1,2,3,4]
    print(median_maintenance_rbtree(input_arr) % 10000)
    print(time.time() - time_start)
