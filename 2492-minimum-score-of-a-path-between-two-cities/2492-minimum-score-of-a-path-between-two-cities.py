class Solution:
    def dfs(self,adj,start,visited):
        visited[start]=1
        for v,w in adj[start]:
            self.ans=min(self.ans,w)
            if visited[v]==-1:
                self.dfs(adj,v,visited)

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj=[[]for _ in range(n+1)]
        for u,v,w in roads:
            adj[u].append([v,w])
            adj[v].append([u,w])
        start=1
        self.ans=float("inf")
        visited=[-1]*(n+1)
        self.dfs(adj,start,visited)
        return self.ans