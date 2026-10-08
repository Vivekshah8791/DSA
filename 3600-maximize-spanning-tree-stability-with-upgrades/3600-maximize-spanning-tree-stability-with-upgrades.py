class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.size=[ 1 for _ in range(n)]
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
        if self.size[pu]<self.size[pv]:
            pu,pv=pv,pu

        self.parent[pv]=pu
        self.size[pu]+=self.size[pv]
        return True
class Solution:
    def solve(self,edges,limit,n,k):
        dsu=DisjointSet(n)
        count=0
        for u,v,w,m in edges:
            if m==1:
                if w<limit:
                    return False
                if not dsu.union(u,v):
                    return False
                count+=1
        for u,v,w,m in edges:
            if m==0:
                if w>=limit:
                    if dsu.union(u,v):
                        count+=1
        for u,v,w,m in edges:
            if m==0:
                if w<limit and 2*w>=limit and k>0:
                    if dsu.union(u,v):
                        count+=1
                        k-=1
        return count==n-1
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x:[x[2],-x[3]])
        left=float("inf")
        right=float("-inf")
        for u,v,w,m in edges:
            if w<left:
                left=w
            if w>right:
                right=w
        right=2*right
        ans=-1
        while left<=right:
            mid=left+(right-left)//2
            if self.solve(edges,mid,n,k):
                ans=mid
                left=mid+1
            else:
                right=mid-1
        return ans