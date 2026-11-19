from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        queue=deque()
        fresh=0
        minutes=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        directions = [(1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)]


        while queue and fresh>0 :

            for _ in range(len(queue)):

                row,col=queue.popleft()

                for dr,dc in directions:
                    new_row=row+dr
                    new_col=col+dc

                    if ( new_row<0 or new_row>=m or new_col<0 or new_col>=n):
                        continue
                    
                    if grid[new_row][new_col]!=1:
                        continue
                    
                    grid[new_row][new_col]=2

                    fresh-=1

                    queue.append((new_row,new_col))

            minutes+=1
        
        return minutes if fresh==0 else -1
        
        