class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        first=float("-inf")
        second=float("-inf")
        third=float("-inf")
        min1=float("inf")
        min2=float("inf")
        for n in nums:
            if n>=first:
                third=second
                second=first
                first=n
            elif n>=second:
                third=second
                second=n
            elif n>=third:
                third=n
            if n<=min1:
                min2=min1
                min1=n
            elif n<=min2:
                min2=n
        return max(first*second*third,first*min1*min2) 