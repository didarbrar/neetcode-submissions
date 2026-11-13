from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return 
        
        m=len(grid)
        n=len(grid[0])
        INF=2147483647

        queue=deque()


        for row in range(m):
            for col in range(n):
                if grid[row][col]==0:
                    queue.append((row,col))
            
        directions=[
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        while queue:

            row,col=queue.popleft()

            for dr, dc in directions:
                new_row=row+dr
                new_col=col+dc

                if new_row<0 or new_row>=m  or new_col<0 or new_col>=n:
                    continue
                
                if grid[new_row][new_col]!=INF:
                    continue
                
                grid[new_row][new_col]=grid[row][col]+1

                queue.append((new_row,new_col))







            