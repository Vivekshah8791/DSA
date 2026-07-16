class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        newgraph = [[] for _ in range(n)]
        indegree=[0]*n
        for node in range(n):
            for adjnode in graph[node]:
                newgraph[adjnode].append(node)
        for node in range(len(newgraph)):
            for adjnode in newgraph[node]:
                indegree[adjnode]+=1
        queue=deque()
        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
        res=[]
        while queue:
            node=queue.popleft();
            res.append(node)

            for neigh in newgraph[node]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    queue.append(neigh)
        res.sort()
        return res
