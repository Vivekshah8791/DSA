class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first=float("-inf")
        second=float("-inf")
        for n in nums:
            if n>=first:
                second=first
                first=n
            elif n>=second and n<first:
                second=n
        return (first-1)*(second-1)
