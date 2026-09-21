class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        src=k
        adj=[[]for _ in range(n+1)]
        for u,v,w in times:
            adj[u].append([v,w])
        dist=[float("inf") for _ in range(n+1)]
        dist[0]=0
        dist[src]=0
        priority_queue=[[0,src]]
        while len(priority_queue)!=0:
            curr_dist,node=heapq.heappop(priority_queue)
            if curr_dist>dist[node]:
                continue
            for neigh,w in adj[node]:
                dist_trav=curr_dist+w
                if dist_trav<dist[neigh]:
                    dist[neigh]=dist_trav
                    heapq.heappush(priority_queue,[dist_trav,neigh])
        for i in range(len(dist)):
            if dist[i]==float("inf"):
                return -1
        return max(dist)