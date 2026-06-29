class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans=0
        for ch in patterns:
            if ch in word:
                ans+=1
        return ans