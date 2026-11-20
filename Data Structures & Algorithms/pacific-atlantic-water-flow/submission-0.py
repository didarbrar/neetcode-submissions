class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m=len(heights)
        n=len(heights[0])

        pacific=set()
        atlantic=set()

        directions = [(1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)]

        def dfs(row,col,visited):

            if (row,col) in visited:
                return 
            visited.add((row,col))

            for dr,dc in directions:
                new_row=row+dr
                new_col=col+dc

                if ( new_row<0 or new_row>=m or new_col<0 or new_col>=n):
                        continue
                
                if heights[new_row][new_col]<heights[row][col]:
                    continue
                
                dfs(new_row,new_col,visited)
        
        for col in range(n):
            dfs(0,col,pacific)
        
        for row in range(m):
            dfs(row,0,pacific)
        
        # atlantic

        for col in range(n):
            dfs(m-1,col,atlantic)
        
        for row in range(m):
            dfs(row,n-1,atlantic)

        
        result = []

        for row in range(m):
            for col in range(n):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result

    
    



        