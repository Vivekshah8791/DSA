class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append([v, w])
        queue = [(0, 0, 1)]
        dist = [[float("inf") for _ in range(k + 1)] for _ in range(n)]
        dist[0][1] = 0
        while queue:
            d, node, count = heapq.heappop(queue)
            if d != dist[node][count]:
                continue
            if node == n - 1:
                return d
            for neigh, w in adj[node]:
                if labels[node] == labels[neigh]:
                    new_count = count + 1
                else:
                    new_count = 1
                if new_count > k:
                    continue
                if d + w < dist[neigh][new_count]:
                    dist[neigh][new_count] = d + w
                    heapq.heappush(
                        queue,
                        (d + w, neigh, new_count)
                    )
        return -1