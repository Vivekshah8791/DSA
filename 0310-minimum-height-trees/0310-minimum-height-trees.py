class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n==1:
            return [0]
        adj=[[]for _ in range(n)]
        degree=[0 for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degree[u]+=1
            degree[v]+=1
        queue=deque()
        for i in range(len(degree)):
            if degree[i]==1:
                queue.append(i)
        remain=n
        while remain>2:
            size=len(queue)
            remain-=size
            for _ in range(size):
                node=queue.popleft()
                for neigh in adj[node]:
                    degree[neigh]-=1
                    if degree[neigh]==1:
                        queue.append(neigh)
        return list(queue)

        


