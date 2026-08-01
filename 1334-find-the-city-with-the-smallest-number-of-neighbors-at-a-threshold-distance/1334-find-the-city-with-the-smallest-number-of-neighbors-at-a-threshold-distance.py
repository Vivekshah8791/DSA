class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adjmat=[[float("inf") for _ in range(n)] for _ in range(n)]
        for u,v,w in edges:
            adjmat[u][v]=w
            adjmat[v][u]=w
            adjmat[u][u]=0
            adjmat[v][v]=0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if adjmat[i][k]!=float("inf") and adjmat[k][j]!=float("inf"):
                        dist=adjmat[i][k]+adjmat[k][j]
                        adjmat[i][j]=min(adjmat[i][j],dist)
        ans=0
        mini=float("inf")
        for i in range(n):
            count=0
            for j in range(n):
                if i != j and adjmat[i][j] <= distanceThreshold:
                    count+=1
            if count<=mini:
                mini=count
                ans=i
        return ans

