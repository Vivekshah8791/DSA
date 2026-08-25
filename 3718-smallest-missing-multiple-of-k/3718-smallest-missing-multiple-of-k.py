class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        new_nums=set(nums)
        pro=k
        while pro in new_nums:
            pro+=k
        return pro