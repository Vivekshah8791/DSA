class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[]for _ in range(n)]
        for u,v,w in flights:
            adj[u].append([v,w])
        dist=[float("inf")for _ in range(n)]
        dist[src]=0
        queue=deque()
        queue.append([0,src,0])
        while queue:
            stop,node,d=queue.popleft()
            for neigh,w in adj[node]:
                if d+w<dist[neigh]:
                    if stop+1==k+1:
                        if neigh!=dst:  
                            continue
                    dist[neigh]=d+w
                    queue.append([stop+1,neigh,d+w])

        if dist[dst]==float("inf"):
            return -1
        return dist[dst]