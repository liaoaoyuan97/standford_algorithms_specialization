import math
import random
from os import path


def read_clauses(filename):
    i = 0
    clauses = []

    with open(path.join('.', filename), 'r') as f:
        for row in f.readlines():
            if i == 0:
                n_clause = int(row.strip("\n"))
                i += 1
            else:
                _list = row.strip("\n").split(' ')
                clauses.append((int(_list[0]), int(_list[1]), False))

    assert len(clauses) == n_clause
    return n_clause, clauses


def reduce_clauses(clauses, assignment):
    while True:
        true_vars = set()
        false_vars = set()
        for i, c in enumerate(clauses):
            if assignment[abs(c[0])] is not None or assignment[abs(c[1])] is not None:
                clauses[i] = (c[0], c[1], True)
                continue

            if not c[2]:
                for v in c[:2]:
                    if v < 0:
                        false_vars.add(-v)
                    else:
                        true_vars.add(v)

        only_true = true_vars - false_vars
        only_false = false_vars - true_vars
        if len(only_true) == 0 and len(only_false) == 0:
            break

        for v in only_true:
            assignment[v] = True

        for v in only_false:
            assignment[v] = False

    clauses = [c for c in clauses if not c[2]]
    # print(len(clauses))
    return clauses, assignment


def is_satifisable(n_clause, clause):
    assignment = {i: None for i in range(1, n_clause + 1)}
    clause, assignment = reduce_clauses(clause, assignment)
    n_clause = len(clause)

    for i in range(math.ceil(math.log(n_clause)/math.log(2))):
        _ass = assignment.copy()

        for v in _ass:
            if _ass[v] is None:
                if random.random() < 0.5:
                    _ass[v] = True
                else:
                    _ass[v] = False

        j = 0
        while True:
            is_satifisable = 1
            for c in clause:
                if j < (2 * n_clause ** 2) and not (
                        (_ass[abs(c[0])] ^ (c[0] < 0)) or (_ass[abs(c[1])] ^ (c[1] < 0))):
                    if random.random() < 0.5:
                        _ass[abs(c[0])] = not _ass[abs(c[0])]
                    else:
                        _ass[abs(c[1])] = not _ass[abs(c[1])]
                    j += 1
                    is_satifisable = 0
                    break

            if j >= (2 * n_clause ** 2):
                return 0

            if is_satifisable:
                return is_satifisable


if __name__ == "__main__":
    res = []
    for i in range(1, 7):
        n, clauses = read_clauses("2sat{}.txt".format(i))
        res.append(str(is_satifisable(n, clauses)))

    print(''.join(res))
