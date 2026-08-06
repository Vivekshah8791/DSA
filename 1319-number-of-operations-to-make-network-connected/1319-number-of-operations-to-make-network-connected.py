class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
    def find(self,x):
        if x==self.parent[x]:
            return x
        self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    def union(self,u,v):

        pu=self.find(u)
        pv=self.find(v)

        if pu==pv:
            return False
        if self.rank[pu]<self.rank[pv]:
            self.parent[pu]=pv
        elif self.rank[pu]>self.rank[pv]:
            self.parent[pv]=pu
        else:
            self.parent[pv]=pu
            self.rank[pu]+=1
        return True

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        dsu=DisjointSet(n)
        extra=0
        for u,v in connections:
            if not dsu.union(u,v):
                extra+=1
        seen=set()
        for i in range(n):
            fin=dsu.find(i)
            if fin not in seen:
                seen.add(fin)
        return len(seen)-1 if extra>=(len(seen)-1) else -1
        