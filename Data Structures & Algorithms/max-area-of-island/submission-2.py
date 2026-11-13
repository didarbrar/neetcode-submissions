class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        def dfs(row,col):
            if row<0 or row>=m or col<0 or col>=n:
                return 0

            if grid[row][col]==0:
                return 0
            
            grid[row][col]=0

            count=1

            count+=dfs(row-1,col)
            count+=dfs(row+1,col)
            count+=dfs(row,col-1)
            count+=dfs(row,col+1)

            return count

        result=0
        
        for row in range(m):
            for col in range(n):
                if grid[row][col]==1:
                    result=max(result,dfs(row,col))
        return result
        