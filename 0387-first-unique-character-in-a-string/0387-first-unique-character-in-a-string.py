class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq=OrderedDict()
        for i,ch in enumerate(s):
            if ch not in freq:
                freq[ch]=[i,1]
            else:
                freq[ch][1]+=1
        for key,value in freq.items():
            if value[1]==1:
                return value[0]
        return -1
                