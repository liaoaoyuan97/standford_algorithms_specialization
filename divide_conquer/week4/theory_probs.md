![Problems](/Users/eve/repo/algorithms_stanford/divide_conquer/week4/problems.png)
1. As proved before, every comparison-based sorting algorithm has worst-case running time Omega(nlogn), so:
    suppose there are m pivot choices(p1, p2,..., pm),
    E(T(p)) = sum from i=1 to m P(p=pi)\*T(p=pi)
            >= 1/m sum from i=1 to m ci\*nlogn
            >= 1/m sum from i=1 to m min(ci,..,cm)\*nlogn
            >= min(ci,..,cm)\*nlogn
            = Omega(nlogn)
            
2. groups of 7:
    T(n) <= cn + T(n/7) + T(?)
    T(?) <= T(5/7n) by the grid
    Let a=7c, prove T(n) <= an for all
    when a=1, T(1) = 1 <= a since a >= 1
    we have T(k) <= ak when k < n,
    then T(n) <= cn + T(n/7) + T(5/7n)
              <= cn + an/7 + an\*5/7
              <= (c + c + 5c)n
              <= an
    
    groups of 3:
    T(n) <= cn + T(n/3) + T(?)
    T(?) <= T(2/3n) by the grid
    T(n) <= cn + T(n/3) + T(2/3n)
    By recurrence tree, we can see that the depth of the tree is related to n.
    T(n) = O(nlogn)
    
3.  DWeightSelect(x, n, w):
    1. if n==1: return x[1]
    2. Split x into groups of 5, sort each group --O(n)
    3. c = the n/5 middle elements --O(n)
    4. chose the pivot as p=DSelect(x, n/5, n/10) --O(n)
    5. partition x around p, index of p is j
       if sum of w when x<p == w/2, return p and DSelect(x[j+1:], n-j, 1) --O(n-j)
       elif sum of w when x<p < w/2, return DWeightSelect(x[j:], n-j+1, w/2 - sum of w when x<p)
       else return DWeightSelect(x[:j-1], j-1, w/2) 
    
    T(n) <= O(n) + T(7/10n)
    By the master method, T(n) = O(n)

4. Proof as the same as the undirected graph, P(output=(Ai, Bi)) >= 2/(n(n-1)) holds and the disjoint events hold

5. ![Problem5](/Users/eve/repo/algorithms_stanford/divide_conquer/week4/theory_prob_5.jpeg)
    
    