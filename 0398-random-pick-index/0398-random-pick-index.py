class Solution:

    def __init__(self, nums: list[int]):
        self.nums=nums
        self.dict={}
        for i in range(len(self.nums)):
            if self.nums[i] not in self.dict:
                self.dict[nums[i]]=[i]
            else:
                self.dict[self.nums[i]].append(i)
    def pick(self, target: int) -> int:
        for key,val in self.dict.items():
            if key==target:
                if len(val)==1:
                    return val[0]
                else:
                    return random.choice(val)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)