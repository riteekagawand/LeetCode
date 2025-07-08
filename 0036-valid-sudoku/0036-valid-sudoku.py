class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:set() for i in range(9)}
        cols = {i:set() for i in range(9)}
        grid = {(i,j):set() for i in range(3) for j in range(3)}

        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val == ".":
                    continue
                if (val in rows[r] or 
                    val in cols[c] or 
                    val in grid[(r//3,c//3)]):
                    return False
                cols[c].add(val)
                rows[r].add(val)
                grid[r//3,c//3].add(val)
        return True