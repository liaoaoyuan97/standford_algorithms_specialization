import time
import bisect
from os import path


def read_array(filename):
    num_set = set()

    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            num = int(row.strip("\n"))
            num_set.add(num)

    return num_set


# too slow
def print_number_of_target_values_odd_even(even_set, odd_set):
    num_targets = 0
    min_target = -10000
    max_target = 10000
    sorted_nums = sorted(even_set.union(odd_set))

    min_target = max(min_target, sorted_nums[0] + sorted_nums[1])
    max_target = min(max_target, sorted_nums[-1] + sorted_nums[-2])

    for t in range(min_target, max_target + 1):
        if t % 2 == 1:
            for x in odd_set:
                if (t - x) in even_set:
                    num_targets += 1
                    break
        else:
            is_t_valid = False
            for x in even_set:
                if (t - x) != x and (t - x) in even_set:
                    num_targets += 1
                    is_t_valid = True
                    break

            if not is_t_valid:
                for x in odd_set:
                    if (t - x) != x and (t - x) in odd_set:
                        num_targets += 1
                        break

    print(num_targets)


def print_number_of_target_values(num_set):
    target_set = set()
    sorted_nums = sorted(num_set)

    for x in num_set:
        low_bound = bisect.bisect_left(sorted_nums, -10000 - x)
        up_bound = bisect.bisect_right(sorted_nums, 10000 - x)
        for i in range(low_bound, up_bound):
            if sorted_nums[i] != x:
                target_set.add(sorted_nums[i] + x)

    print(len(target_set))


if __name__ == "__main__":
    num_set = read_array("two_sum.txt")
    # num_set = {-3, -1, 1, 2, 9, 11, 7, 6, 2}
    # num_set = {-2, 0, 0, 4}

    time_start = time.time()
    print_number_of_target_values(num_set)
    print(time.time() - time_start)
