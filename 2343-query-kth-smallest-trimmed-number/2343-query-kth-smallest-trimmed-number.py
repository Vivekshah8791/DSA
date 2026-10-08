class Solution:
    def smallestTrimmedNumbers(self, nums: list[str], queries: list[list[int]]) -> list[int]:
        ans=[]
        for k,trim in queries:
            maxheap=[]
            for i,n in enumerate(nums):
                heapq.heappush(maxheap,[-int(n[-trim:]),-i])
                if len(maxheap)>k:
                    heapq.heappop(maxheap)
            val,index=heapq.heappop(maxheap)
            ans.append(-index)
        return ans

