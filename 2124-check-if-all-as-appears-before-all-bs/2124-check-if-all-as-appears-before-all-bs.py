class Solution:
    def checkString(self, s: str) -> bool:
        bseen=False
        for ch in s:
            if ch=='a':
                if bseen:
                    return False
            else:
                bseen=True
        return True
