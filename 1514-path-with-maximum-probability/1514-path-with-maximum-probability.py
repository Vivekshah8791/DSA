class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        adj=[[]for _ in range(n)]
        i=0
        for u,v in edges:
            adj[u].append([v,succProb[i]])
            adj[v].append([u,succProb[i]])
            i+=1
        dist=[float("-inf") for _ in range(n)]
        dist[start_node]=0
        pq=[[0,start_node]]
        while pq:
            d,node=heapq.heappop(pq)
            d=-d
            if d<dist[node]:
                continue
            for neigh ,w in adj[node]:
                if w==0:
                    continue
                curr=d+math.log(w)
                if curr>dist[neigh]:
                    dist[neigh]=curr
                    heapq.heappush(pq,[-curr,neigh])
        return math.exp(dist[end_node]) if dist[end_node] != float("-inf") else 0
            