class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited=[-1 for _ in range(len(rooms))]
        def solve(node):
            visited[node]=1
            for neigh in rooms[node]:
                if visited[neigh]==-1:
                    solve(neigh)
        solve(0)
        for x in visited:
            if x==-1:
                return False
        return True