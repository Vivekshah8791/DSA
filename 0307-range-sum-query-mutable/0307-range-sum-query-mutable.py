class NumArray:

    def __init__(self, nums: list[int]):
        self.nums=nums
        self.total=sum(nums)
        self.cache={}
        
    def update(self, index: int, val: int) -> None:
        self.total+=val-self.nums[index]
        self.nums[index]=val
        self.cache.clear()
    def sumRange(self, left: int, right: int) -> int:
        if (left,right) in self.cache:
            return self.cache[(left,right)]
        n=len(self.nums)
        if (right - left) >= n // 2:
            res = (self.total - sum(self.nums[:left])- sum(self.nums[right+1:]))
        else:
            res=sum(self.nums[left:right+1])
        self.cache[(left,right)]=res
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)