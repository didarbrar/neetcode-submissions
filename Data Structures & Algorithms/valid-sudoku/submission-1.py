class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m=len(board)
        n=len(board[0])
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
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
                rows[i].add(value)
                cols[j].add(value)
                boxes[box].add(value)
        return True
    

        