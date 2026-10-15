class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m=len(board)
        n=len(board[0])
        rows=[[] for _ in range(9)]
        cols=[[] for _ in range(9)]
        boxes=[[] for _ in range(9)]
        for i in range(m):
            for j in range(n):
                value=board[i][j]

                if value=='.':
                    continue

                box=((i//3)*3)+j//3

                if value in rows[i]:
                    return False
                elif value in cols[j]:
                    return False
                elif value in boxes[box]:
                    return False
                rows[i].append(value)
                cols[j].append(value)
                boxes[box].append(value)
        return True
    

        