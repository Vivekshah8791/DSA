class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj=[[]for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=[-1]*(n)
        queue=deque()
        queue.append(source)
        visited[source]=1
        while queue:
            node=queue.popleft()
            if node==destination:
                return True
            for neigh in adj[node]:
                if visited[neigh]==-1:
                    queue.append(neigh)
                    visited[neigh]=1
        return False