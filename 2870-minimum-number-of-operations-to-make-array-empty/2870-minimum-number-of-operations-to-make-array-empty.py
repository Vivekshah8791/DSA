class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq=Counter(nums)
        count=0
        print(freq)
        for key,val in freq.items():
            if val==1:
                return -1
            elif val%3==0:
                count+=val//3
            elif val%2==0:
                count+=min(val//2,val//3+1)
            else:
                count+=val//3+1
        return count
        