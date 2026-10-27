class Solution:
    def solve(self,path,graph,node,last,ans):
        path.append(node)
        if node==last:
            ans.append(list(path))
        else:
            for neigh in graph[node]:
                self.solve(path,graph,neigh,last,ans)
        path.pop()
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        ans=[]
        n=len(graph)
        self.solve([],graph,0,n-1,ans)
        return ans