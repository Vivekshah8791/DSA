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
    def findCriticalAndPseudoCriticalEdges(self,n:int,edges:list[list[int]])->list[list[int]]:
        new_edges=[]
        for i in range(len(edges)):
            u,v,w=edges[i]
            new_edges.append([u,v,w,i])
        new_edges.sort(key=lambda x:x[2])
        dsu=DisjointSet(n)
        weight=0
        count=0
        for u,v,w,idx in new_edges:
            if dsu.union(u,v):
                weight+=w
                count+=1
        critical_edges=[]
        for i in range(len(new_edges)):
            dsu=DisjointSet(n)
            new_weight=0
            count=0
            for j in range(len(new_edges)):
                if i==j:
                    continue
                u,v,w,idx=new_edges[j]
                if dsu.union(u,v):
                    new_weight+=w
                    count+=1
            if count!=n-1 or new_weight>weight:
                critical_edges.append(new_edges[i][3])
        pseudo=[]
        for i in range(len(new_edges)):
            dsu=DisjointSet(n)
            u,v,w,idx=new_edges[i]
            dsu.union(u,v)
            new_weight=w
            count=1
            for j in range(len(new_edges)):
                if i==j:
                    continue
                u2,v2,w2,idx2=new_edges[j]
                if dsu.union(u2,v2):
                    new_weight+=w2
                    count+=1
            if count==n-1 and new_weight==weight and idx not in critical_edges:
                pseudo.append(idx)
        return [critical_edges,pseudo]