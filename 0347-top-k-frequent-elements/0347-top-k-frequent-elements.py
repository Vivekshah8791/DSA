import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        min_heap=[]
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        for key,value in freq.items():
            heapq.heappush(min_heap,[value,key])
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        ans=[]
        for c,v in min_heap:
            ans.append(v)
        return ans
            