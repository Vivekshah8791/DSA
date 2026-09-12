class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        index=defaultdict(list)
        for i , n in enumerate(nums):
            index[n].append(i)
        count=0
        for num,in_list in index.items():
            if len(in_list)==3:
                if in_list[1]-in_list[0]==in_list[2]-in_list[1]:
                    count+=1
        return count
                