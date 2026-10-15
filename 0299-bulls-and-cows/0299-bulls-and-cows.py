class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        freq1 = {}
        freq2 = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                freq1[secret[i]] = freq1.get(secret[i], 0) + 1
                freq2[guess[i]] = freq2.get(guess[i], 0) + 1
        for ch in freq1:
            if ch in freq2:
                cows += min(freq1[ch], freq2[ch])
        return str(bulls) + "A" + str(cows) + "B"