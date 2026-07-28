class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD=10**9+7
        adj=[[]for _ in range(n)]
        for u,v,w in roads:
            adj[u].append([v,w])
            adj[v].append([u,w])
        dist=[float("inf")for _ in range(n)]
        ways=[0 for _ in range(n)]
        dist[0]=0
        ways[0]=1
        pq=[]
        pq.append([0,0])
        while pq:
            d,node=heapq.heappop(pq)
            for neigh,w in adj[node]:
                nd=d+w
                if nd<dist[neigh]:
                    dist[neigh]=nd
                    heapq.heappush(pq,[nd,neigh])
                    ways[neigh]=(ways[node])%MOD
                elif nd==dist[neigh]:
                    ways[neigh]+=ways[node]
        return ways[n-1]%MOD
        
