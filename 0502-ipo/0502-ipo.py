import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        projects = []
        for i in range(len(profits)):
            heapq.heappush(projects, (capital[i], profits[i]))
        available = []
        while k > 0:
            while projects and projects[0][0] <= w:
                cap, pro = heapq.heappop(projects)
                heapq.heappush(available, -pro)
            if not available:
                break
            w += -heapq.heappop(available)
            k -= 1
        return w