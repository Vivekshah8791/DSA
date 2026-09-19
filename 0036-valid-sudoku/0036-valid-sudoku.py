class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row=len(board)
        col=len(board[0])
        for i in range(row):
            seen=set()
            for j in range(col):
                if board[i][j] in seen:
                    return False
                if board[i][j].isdigit():
                    seen.add(board[i][j])
        
        for j in range(col):
            seen=set()
            for i in range(row):
                if board[i][j] in seen:
                    return False
                if board[i][j].isdigit():
                    seen.add(board[i][j])
        for i in range(0,row,3):
            for j in range(0,col,3):
                seen=set()
                for r in range(i,i+3):
                    for c in range(j,j+3):
                        if board[r][c] in seen:
                            return False
                        if board[r][c].isdigit():
                            seen.add(board[r][c])
        return True
