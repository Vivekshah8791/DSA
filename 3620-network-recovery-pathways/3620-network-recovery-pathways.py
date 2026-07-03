class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n=len(online)

        adj=[[]for _ in range(n)]
        indegree=[0]*n
        mx=float("-inf")
        for u,v,w in edges:
            adj[u].append((v,w))
            indegree[v]+=1
            mx=max(mx,w)
        q = deque()
        topo = []
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        while q:
            node=q.popleft()
            topo.append(node)
            for v,w in adj[node]:
                indegree[v]-=1
                if indegree[v]==0:
                    q.append(v)
        
        def check(limit):
            dp=[float("inf")]*n
            dp[0]=0
            for u in topo:
                if dp[u]==float("inf"):
                    continue
                for v,w in adj[u]:
                    if w<limit:
                        continue
                    if v!=n-1 and not online[v]:
                        continue
                    dp[v]=min(dp[v],dp[u]+w)
            return dp[n-1]<=k
        low=0
        high=mx
        ans=-1
        while low<=high:
            mid=low+(high-low)//2
            if check(mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans

