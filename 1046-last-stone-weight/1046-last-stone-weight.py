class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        max_heap=[]
        for n in stones:
            heapq.heappush(max_heap,-n)
        while len(max_heap)>1:
            y=-heapq.heappop(max_heap)
            x=-heapq.heappop(max_heap)
            if x!=y:
                heapq.heappush(max_heap,-(y-x))
        return -max_heap[0] if max_heap else 0