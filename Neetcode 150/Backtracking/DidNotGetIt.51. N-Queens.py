class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        COLUMNS = set()
        # Set to store occupied positive diagonals (r + c)
        posDiag = set()
        # Set to store occupied negative diagonals (r - c)
        negDiag = set()

        result = []

        # 2D board initialized with all dots
        board = []
        for _ in range(n):
            row = ["."] * n
            board.append(row)

        def backtrack(row):
            # If all queens are placed, add the current board to the result
            if row == n:
                # Create a copy of the current board and add it to the result
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            
            # Iterate over columns
            for col in range(n):
                # Skip if the current column, positive diagonal, or negative diagonal is occupied
                if col in COLUMNS or (row + col) in posDiag or (row - col) in negDiag:
                    continue
                
                # Occupy the current column, positive diagonal, and negative diagonal
                COLUMNS.add(col)
                posDiag.add(row + col)
                negDiag.add(row - col)
                board[row][col] = "Q"

                # Move to the next row
                backtrack(row + 1)

                # Undo the changes after exploring the subtree
                COLUMNS.remove(col)
                posDiag.remove(row + col)
                negDiag.remove(row - col)      
                board[row][col] = "."

        # Start the backtracking from the first row
        backtrack(0)
        return result







class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def create_board(cur_queen_pos):
            board = []
            for row in cur_queen_pos:
                board.append("".join(row))
            
            return board

        def backtrack(row, posDiag, negDiag, cols, cur_queen_pos):
            if row == n:
                res.append(create_board(cur_queen_pos))
                return
            
            for col in range(n):
                cur_d = row - col
                cur_anti_d = row + col
                if col in cols or cur_d in posDiag or cur_anti_d in negDiag:
                    continue
                
                cols.add(col)
                posDiag.add(cur_d)
                negDiag.add(cur_anti_d)
                cur_queen_pos[row][col] = "Q"

                backtrack(row + 1, posDiag, negDiag, cols, cur_queen_pos)

                cols.remove(col)
                posDiag.remove(cur_d)
                negDiag.remove(cur_anti_d)
                cur_queen_pos[row][col] = "."

        backtrack(0, set(), set(), set(), board)
        return res