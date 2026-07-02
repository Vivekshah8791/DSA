class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[]for _ in range(numCourses)]
        indegree=[0 for _ in range(numCourses)]
        for u,v in prerequisites:
            adj[u].append(v)
            indegree[v]+=1
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
            return True
        return False