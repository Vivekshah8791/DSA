class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n=len(s)
        i=0
        count=0
        while i<n:
            found=False
            for centre in range(i,n):
                prev=centre
                next=centre
                while prev>=i and next<n and s[prev]==s[next]:
                    if next-prev+1>=k:
                        count+=1
                        i=next+1
                        found=True
                        break
                    prev-=1
                    next+=1
                
                if found:
                    break
                prev=centre
                next=centre+1
                while prev>=i and next<n and s[prev]==s[next]:
                    if next-prev+1>=k:
                        count+=1
                        i=next+1
                        found=True
                        break
                    prev-=1
                    next+=1
                if found:
                    break
            if not found:
                break
        return count
            