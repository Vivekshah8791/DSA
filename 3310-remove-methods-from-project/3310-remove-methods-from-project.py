class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj=[[]for _ in range(n)]
        for u,v in invocations:
            adj[u].append(v)
        visited=[-1]*n
        suspicious=set()
        nonsus=set()
        def dfs(node):
            visited[node]=1
            suspicious.add(node)
            for neigh in adj[node]:
                if visited[neigh]==-1:
                    dfs(neigh)
        dfs(k)

        sus=True
        for u,v in invocations:
            if u not in suspicious and v in suspicious:
                sus=False
                break   
        if sus:
            return [i for i in range(n) if i not in suspicious]
        else:
            return list(range(n))
        


                
