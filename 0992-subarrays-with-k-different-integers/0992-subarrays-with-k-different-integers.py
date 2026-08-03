class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def solve(nums,k):
            l=0
            r=0
            freq=defaultdict(int)
            ans=0
            while r<len(nums):
                freq[nums[r]]+=1
                while len(freq)>k:
                    freq[nums[l]]-=1
                    if freq[nums[l]]==0:
                        del freq[nums[l]]
                    l+=1
                ans+=r-l+1
                r+=1
            return ans
        return solve(nums,k)-solve(nums,k-1)