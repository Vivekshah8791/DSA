class Solution:
    def countingSort(self,arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 10

        for num in arr:
            digit = (num // exp) % 10
            count[digit] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        for i in range(n - 1, -1, -1):
            digit = (arr[i] // exp) % 10
            output[count[digit] - 1] = arr[i]
            count[digit] -= 1

        for i in range(n):
            arr[i] = output[i]

    def maximumGap(self, nums: list[int]) -> int:
        if len(nums)<2:
            return 0
        max_num = max(nums)
        exp = 1
        while max_num // exp > 0:
            self.countingSort(nums, exp)
            exp *= 10
        maxi=float("-inf")
        for i in range(len(nums)-1):
            maxi=max(maxi,nums[i+1]-nums[i])
        return maxi