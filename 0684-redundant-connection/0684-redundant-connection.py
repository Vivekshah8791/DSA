class DisjointSetUnion:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return True
        self.parent[pu] = pv
        return False

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        dsu = DisjointSetUnion(n)
        for u, v in edges:
            if dsu.union(u, v):
                return [u, v]
        return []