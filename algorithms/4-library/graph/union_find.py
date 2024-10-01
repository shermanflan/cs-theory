"""
A.k.a. merge-find set. This is a useful algorithm to know as it helps solve many problems involving
disjoint sets or disconnected graphs.

TODO: Implementation
https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3881/
"""
class UnionFind:
    def __init__(self, size):
        """Initialize parents to selves with rank 0"""
        self.parent = [i for i in range(size)]
        self.rank = [1]*size

    def find(self, node):
        """
        Find root parent by recursing up parent chain with path 
        compression optimization.
        """
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union_set(self, x, y):
        """
        Merge sets: smaller into larger and update combined
        rank. Rank corresponds to height and is essential in keeping
        the trees more "bushy" and hence more efficiently structured
        (i.e. less lookup times).
        """
        xSet, ySet = self.find(x), self.find(y)

        if xSet == ySet:
            return
        elif self.rank[xSet] < self.rank[ySet]:
            self.parent[xSet] = ySet
        elif self.rank[xSet] > self.rank[ySet]:
            self.parent[ySet] = xSet
        else:
            self.parent[ySet] = xSet
            self.rank[xSet] += 1
