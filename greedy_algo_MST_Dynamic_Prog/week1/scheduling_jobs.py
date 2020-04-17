from os import path
from functools import reduce


def read_jobs(filename):
    i = 0
    jobs = list()

    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            if i == 0:
                n_jobs = int(row.strip("\n"))
                i += 1
            else:
                job = [float(j) for j in row.strip("\n").split(' ')]
                jobs.append((job[0], job[1]))

    assert len(jobs) == n_jobs

    return jobs


def min_weighted_sum_by_diff_greedy(jobs):
    sorted_by_diff = sorted(jobs, key=lambda x: (x[0] - x[1], x[0]), reverse=True)
    # import pdb;pdb.set_trace()

    completion_ts = [sorted_by_diff[0]]
    for i in range(1, len(sorted_by_diff)):
        completion_ts.append((sorted_by_diff[i][0], sorted_by_diff[i][1] + completion_ts[i - 1][1]))

    return reduce(lambda pre, cur: pre + cur[0] * cur[1], completion_ts, 0)


def min_weighted_sum_by_ratio_greedy(jobs):
    sorted_by_ratio = sorted(jobs, key=lambda x: 1.0 * x[0] / x[1], reverse=True)

    completion_ts = [sorted_by_ratio[0]]
    for i in range(1, len(sorted_by_ratio)):
        completion_ts.append((sorted_by_ratio[i][0], sorted_by_ratio[i][1] + completion_ts[i - 1][1]))

    return reduce(lambda pre, cur: pre + cur[0] * cur[1], completion_ts, 0)


if __name__ == "__main__":
    jobs = read_jobs('jobs.txt')

    # jobs = [(3,5), (1,2)]
    min_completion_time = min_weighted_sum_by_diff_greedy(jobs)
    print("by diff:", min_completion_time)

    min_completion_time = min_weighted_sum_by_ratio_greedy(jobs)
    print("by ratio:", min_completion_time)
