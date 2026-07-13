class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        ans = []
        for left in range(len(s)):
            for right in range(left, len(s)):
                num = int(s[left:right+1])
                if num > high:
                    break
                if num >= low:
                    ans.append(num)
        return sorted(ans)