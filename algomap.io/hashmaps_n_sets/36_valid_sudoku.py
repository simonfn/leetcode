class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        DOT = '.'
        LOC =  [(0,0), (0,3), (0,6),
                (3,0), (3,3), (3,6),
                (6,0), (6,3), (6,6)]
        
        for i in range(N):
            set_row, set_col = set(), set()
            for j in range(N):
                cell_row, cell_col = board[i][j], board[j][i]
                if cell_row in set_row or cell_col in set_col :
                    return False
                if cell_row != DOT:
                    set_row.add(cell_row)
                if cell_col != DOT:
                    set_col.add(cell_col)

        for k in range(N):
            sqr_y, sqr_x = LOC[k]
            set_sqr = set()
            for i in range(3):
                for j in range(3):
                    cell = board[sqr_y + i][sqr_x + j]
                    if cell in set_sqr :
                        return False
                    if cell != DOT:
                        set_sqr.add(cell)
        
        return True