class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l=len(words)
        word_len=len(words[0])
        w=Counter(words)
        ans=[]
        for k in range(word_len):
            left=k
            right=k
            curr=Counter()
            count=0
            while right+word_len <= len(s):
                news=s[right:right+word_len]
                right+=word_len
                if news in w:
                    curr[news]+=1
                    count+=1
                    while curr[news]>w[news]:
                        left_word=s[left:left+word_len]
                        left+=word_len
                        curr[left_word]-=1
                        count-=1
                    if count==l:
                        ans.append(left)

                        left_word = s[left:left + word_len]
                        curr[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    curr.clear()
                    count=0
                    left=right
        return ans
