---
title: optional_theory_problems
date: 2020-04-27 11:18
---

1. Double Knapsacks Problem![Problem1](/Users/eve/repo/stanford_algorithms_specialization/greedy_algo_MST_Dynamic_Prog/week4/problem1.png)

2-3. Longest Common Substring ![Problem2_3](/Users/eve/repo/stanford_algorithms_specialization/greedy_algo_MST_Dynamic_Prog/week4/problem2_3.png)

4.Give a dynamic programming algorithm that computes an optimal binary search tree and runs in O(n^2) time.
See Theorem: 
`c(i,j) + c(i',j') <= c(i',j) + c(i,j') for i<=i'<=j<=j'`
its proof in [Efficient Dynamic Programming Using Quadrangle Inequalities, Yao 80]
Let r be 2-D array to store the root of alternative trees in the min function.
In the third iteration, we only need to scan the root alternatives from r[i, j-1] to r[i+1, j]. The optimality can be
proved by the above theorem. It needs to show that `c[i,k-1] + c[k+1, j] <= c[i, k] + c[k+2, j]`,
given `c[i,k-1] + c[k+1, j-1] <= c[i, k] + c[k+2, j-1]` and k is the optimal root for [i, j-1].
Since `k+1<=k+2<=j-1<=j`, `c[k+1, j-1] + c[k+2, j] <= c[k+1, j] + c[k+2, j-1]`
Add both sides of the above inequality to the given the inequality. QED.
O(N*2) can be proved by the recursive tree summing up the number of root comparisons for each level. 
 

