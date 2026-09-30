class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        n=max(max(u,v) for u,v in edges)
        adj=[[]for _ in range(n+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            if len(adj[u])==n-1:
                return u
            if len(adj[v])==n-1:
                return v
        
