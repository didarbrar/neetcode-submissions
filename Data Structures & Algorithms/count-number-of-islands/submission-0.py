class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])

        def dfs(row,col):
            if row<0 or row>=m or col<0 or col>=n:
                return False

            if grid[row][col]=='0':
                return False
            
            grid[row][col]='0'

            found=(
                dfs(row-1,col) or
                dfs(row+1,col) or
                dfs(row,col-1) or
                dfs(row,col+1)
            )

            return found

        count=0
        
        for row in range(m):
            for col in range(n):
                if grid[row][col]=='1':
                    dfs(row,col)
                    count+=1
        return count
        