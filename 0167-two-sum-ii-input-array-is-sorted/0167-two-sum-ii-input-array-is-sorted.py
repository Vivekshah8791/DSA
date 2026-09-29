class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        index={}
        for i,n in enumerate(numbers):
            diff=target-n
            if diff in index:
                return [index[diff]+1,i+1]
            index[n]=i