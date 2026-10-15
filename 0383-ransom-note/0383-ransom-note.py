class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq={}
        freq2={}
        for ch in ransomNote:
            freq[ch]=freq.get(ch,0)+1
        for ch in magazine:
            freq2[ch]=freq2.get(ch,0)+1
        for ch in ransomNote:
            if ch not in freq2 or freq2[ch]<freq[ch]:
                return False
        return True
        