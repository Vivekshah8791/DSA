class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=[[]for _ in range(numCourses)]
        indegree=[0 for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
            indegree[u]+=1
        queue=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        res=[]
        while queue:
            node=queue.popleft()
            res.append(node)
            for n in adj[node]:
                indegree[n]-=1
                if indegree[n]==0:
                    queue.append(n)
        if len(res)==numCourses:
            return res
        return []