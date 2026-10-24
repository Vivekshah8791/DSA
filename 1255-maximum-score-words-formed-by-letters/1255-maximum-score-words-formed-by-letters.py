class Solution:
    def solve(self,words,index,letters,score,total):
        if index==len(words):
            self.maxi=max(self.maxi,total)
            return
        word=words[index]
        value=0
        self.solve(words,index+1,letters,score,total)
        freq=[0]*26
        possible=True
        for ch in word:
            x=ord(ch)-ord("a")
            freq[x]+=1
            value+=score[x]
            if freq[x]>letters[x]:
                possible=False
                break
        if possible:
            for i in range(26):
                letters[i]-=freq[i]
            self.solve(words,index+1,letters,score,total+value)
            for i in range(26):
                letters[i]+=freq[i]

    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        freq=[0]*26
        for ch in letters:
            index=ord(ch)-ord("a")
            freq[index]+=1
        self.maxi=float("-inf")
        self.solve(words,0,freq,score,0)
        return self.maxi