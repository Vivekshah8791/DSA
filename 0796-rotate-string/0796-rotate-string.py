class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        n=len(goal)
        s=s+s
        for i in range(len(s)):
            if s[i:i+n]==goal:
                return True
        return False