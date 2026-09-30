class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.size=[1]*(n)

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
            self.parent[pu]=pv
            self.size[pv]+=self.size[pu]
        elif self.size[pu]>self.size[pv]:
            self.parent[pv]=pu
            self.size[pu]+=self.size[pv]
        else:
            self.parent[pv]=pu
            self.size[pu]+=self.size[pv]
        return True
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n=len(points)
        dsu=DisjointSet(len(points))
        pq=[]
        ans=0
        for i in range(n):
            for j in range(i+1,n):
                dist=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                heapq.heappush(pq,[dist,i,j])
        for i in range(len(pq)):
            cord=heapq.heappop(pq)
            u=cord[1]
            v=cord[2]
            if dsu.union(u,v):
                ans+=cord[0]
        return ans

                