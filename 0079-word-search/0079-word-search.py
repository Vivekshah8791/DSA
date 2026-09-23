class Solution:
    def solve(self,r,c,board,word,index,visited):
        if index==len(word):
            return True
        if r>=len(board) or c>=len(board[0]):
            return False
        visited[r][c]=0
        dir=[(0,1),(0,-1),(1,0),(-1,0)]
        for dx,dy in dir:
            nr,nc =r+dx,c+dy
            if 0<=nr<len(board) and 0<=nc<len(board[0]) and visited[nr][nc]==-1 and board[nr][nc]==word[index]:
                if self.solve(nr,nc,board,word,index+1,visited):
                    return True
        visited[r][c]=-1
        return False

    def exist(self, board: list[list[str]], word: str) -> bool:
        row=len(board)
        col=len(board[0])
        start=word[0]
        visited=[[-1 for _ in range(col)]for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if board[i][j]==start:
                    if self.solve(i,j,board,word,1,visited):
                        return True
        return False
