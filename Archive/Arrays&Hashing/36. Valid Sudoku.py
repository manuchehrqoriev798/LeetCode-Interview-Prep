class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize dictionaries to keep track of values in each column, row, and 3x3 subgrid.
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # Each subgrid is identified by (r//3, c//3)

        # Iterate through each cell in the 9x9 Sudoku board.
        for r in range(9):
            for c in range(9):
                # Skip empty cells denoted by '.'.
                if board[r][c] == '.':
                    continue

                # Check if the current value is already present in the corresponding row, column, or subgrid.
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[(r//3, c//3)]):
                    return False  # Return False if the Sudoku board is not valid.

                # Add the current value to the sets of the corresponding column, row, and subgrid.
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])

        # If the entire board has been checked without finding any violations, return True.
        return True






        # # Initialize a regular dictionary
        # cols = {}
        # rows = {}
        # squares = {}

        # # Iterate through each cell in the 9x9 Sudoku board.
        # for r in range(9):
        #     for c in range(9):
        #         # Skip empty cells denoted by '.'.
        #         if board[r][c] == '.':
        #             continue

        #         # Check if the current value is already present in the corresponding row, column, or subgrid.
        #         if (board[r][c] in rows.get(r, set()) or 
        #             board[r][c] in cols.get(c, set()) or 
        #             board[r][c] in squares.get((r//3, c//3), set())):
        #             return False  # Return False if the Sudoku board is not valid.

        #         # Add the current value to the sets of the corresponding column, row, and subgrid.
        #         cols[c] = cols.get(c, set())
        #         rows[r] = rows.get(r, set())
        #         squares[(r//3, c//3)] = squares.get((r//3, c//3), set())
        #         cols[c].add(board[r][c])
        #         rows[r].add(board[r][c])
        #         squares[(r//3, c//3)].add(board[r][c])

        # # If the entire board has been checked without finding any violations, return True.
        # return True
