class Solution {
public:
bool isSafe(vector<vector<char>>& board,int row,int col,char digit){
    //horizontal
    for(int j=0;j<9;j++){
        if(board[row][j]==digit){
            return false;
        }
    }
    //vertical
    for(int i=0;i<9;i++){
        if(board[i][col]==digit){
            return false;
        }
    }
    //grid
    int strow=(row/3)*3;
    int stcol=(col/3)*3;
    for(int i = strow; i <= strow + 2; i++){
    for(int j = stcol; j <= stcol + 2; j++){
        if(board[i][j] == digit){
            return false;
        }
    }
}

    return true;

}
bool helper(vector<vector<char>>& board,int row ,int col){
    if(row==9){
        return true;
    }
    int nextrow=row;
    int nextcol=col+1;
    if(nextcol==9){
        nextrow=row+1;
        nextcol=0;
    }
    if(board[row][col]!='.'){
        return helper(board,nextrow,nextcol);
    }
    for(char i='1';i<='9';i++){
        if(isSafe(board,row,col,i)){
            board[row][col]=i;
            if(helper(board,nextrow,nextcol)){
                return true;
            }
            board[row][col]='.';
        }
    }
    return false;
}
    void solveSudoku(vector<vector<char>>& board) {
        helper(board,0,0);
        
    }
};