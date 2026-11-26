class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False
        n -= 10
        play = 9
        turn = 0
        while play > 0:
            if play > n:
                return turn == 0
            n -= play
            play -= 1
            turn = 1 - turn
        return turn == 0