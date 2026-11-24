class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m=len(board)
        n=len(board[0])


        
        def dfs(row,col):

            if row<0 or row>=m or col<0 or col>=n:
                return 
            
            if board[row][col]!='O':
                return
            
            # Mark boundary-connected O as safe
            board[row][col] = "T"

            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        
        for col in range(n):
            if board[0][col] == "O":
                dfs(0,col)
            if board[m-1][col] == "O":
                dfs(m-1,col)
        for row in range(m):
            if board[row][0] == "O":
                dfs(row,0)
            if board[row][n-1] == "O":
                dfs(row,n-1)
        

        for i in range(m):
            for j in range(n):
                if board[i][j]=='O':
                    board[i][j]='X'
                
                elif board[i][j]=='T':
                    board[i][j]='O'

    





        

        