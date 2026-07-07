class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        visited=[-1]*n
        def dfs(node):
            visited[node]=1
            for neigh in graph[node]:
                if visited[neigh]==1:
                    return True
                else:
                    if visited[neigh]==-1:
                        if dfs(neigh):
                            return True
            visited[node]=0
            return False
        ans=[]
        for i in range(n):
            if not dfs(i):
                ans.append(i)
        return ans
        

