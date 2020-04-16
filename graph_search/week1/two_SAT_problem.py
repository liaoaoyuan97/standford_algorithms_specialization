# In the 2SAT problem, you are given a set of clauses, where each clause is the disjunction of two literals (a literal
# is a Boolean variable or the negation of a Boolean variable). You are looking for a way to assign a value "true" or
# "false" to each of the variables so that all clauses are satisfied --- that is, there is at least one true literal in
# each clause. For this problem, design an algorithm that determines whether or not a given 2SAT instance has
# a satisfying assignment. (Your algorithm does not need to exhibit a satisfying assignment,
# just decide whether or not one exists.)
# Your algorithm should run in O(m+n) time, where m and n are the number of clauses and variables, respectively.
# [Hint: strongly connected components.]

# // The CNF being handled is:
# // '+' implies 'OR' and '*' implies 'AND'
# // (x1+x2)*(x2’+x3)*(x1’+x2’)*(x3+x4)*(x3’+x5)*
# // (x4’+x5’)*(x3’+x4)
# int a[] = {1, -2, -1, 3, -3, -4, -3};
# int b[] = {2, 3, -2, 4, 5, -5, 4};

from assignment_compute_SCCs import SCCGraph


class Graph(SCCGraph):

    def dfs1_recursive(self, explored_v_set, v, desc_order):
        explored_v_set.add(v)

        for t in self.fw_edges.get(v, []):
            if t not in explored_v_set:
                self.dfs1_recursive(explored_v_set, t, desc_order)

        desc_order.append(v)

    def dfs2_recursive(self, explored_v_set, s, v, leaders):
        explored_v_set.add(v)

        for t in self.bt_edges.get(v, []):
            if t not in explored_v_set:
                self.dfs2_recursive(explored_v_set, s, t, leaders)

        leaders[v] = s


def is_formula_satisfiable(f_bools, l_bools):
    graph = Graph()

    if len(f_bools) != len(l_bools):
        raise ValueError("Wrong input format.")

    for i in range(len(f_bools)):
        f_i = f_bools[i]
        l_i = l_bools[i]
        graph.add_edge(-f_i, l_i)
        graph.add_edge(-l_i, f_i)

    graph.v_set = graph.get_vertex_set()
    v_by_desc = list()
    explored_v_set = set()

    for v in graph.v_set:
        if v not in explored_v_set:
            graph.dfs1_recursive(explored_v_set, v, v_by_desc)

    leaders = dict()
    explored_v_set = set()

    for v in v_by_desc[::-1]:
        if v not in explored_v_set:
            s = v
            graph.dfs2_recursive(explored_v_set, s, v, leaders)

    for v in leaders:
        if leaders[v] == leaders[-v]:
            return False

    return True


if __name__ == "__main__":
    assert is_formula_satisfiable([1, 2, -1],
                                  [2, -1, -2]) is True

    assert is_formula_satisfiable([1, -1, 1, -1],
                                  [2, 2, -2, -2]) is False
