class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        n=len(tokens)
        left=0
        right=n-1
        score=0
        ans=0
        while left<=right:
            if power>=tokens[left]:
                score+=1
                power-=tokens[left]
                left+=1
                ans=max(ans,score)
            elif score>0:
                power+=tokens[right]
                score-=1
                right-=1
            else:
                break
        return ans
