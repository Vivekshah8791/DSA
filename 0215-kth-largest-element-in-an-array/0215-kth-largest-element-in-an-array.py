class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq=[]
        n=len(nums)
        for i in range(k):
            heapq.heappush(pq,nums[i])
        
        for j in range(k,n):
            if nums[j]>pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq,nums[j])
        return pq[0]
