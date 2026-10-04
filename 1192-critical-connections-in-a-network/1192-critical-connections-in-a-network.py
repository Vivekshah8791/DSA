class Solution:
    def criticalConnections(self, n: int, connections: list[list[int]]) -> list[list[int]]:
        ans=[]
        adj=[[] for _ in range(n)]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        visited=[-1]*n
        self.time=0
        dt=[0]*n
        low=[0]*n
        def dfs(node,parent):
            visited[node]=1
            self.time+=1
            low[node]=dt[node]=self.time
            for neigh in adj[node]:
                if visited[neigh]==-1:
                    visited[neigh]=1
                    dfs(neigh,node)
                    low[node]=min(low[node],low[neigh])
                    if low[neigh]>dt[node]:
                        ans.append([node,neigh])
                elif neigh!=parent:
                    low[node]=min(low[node],dt[neigh])
        dfs(0,-1)
        return ans