class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:

        adj = {}
        for u, v in tickets:
            adj.setdefault(u, []).append(v)
        for u in adj:
            adj[u].sort(reverse=True)
        ans = []
        def dfs(node):
            while adj.get(node):
                neigh = adj[node].pop()
                dfs(neigh)
            ans.append(node)
        dfs("JFK")
        return ans[::-1]