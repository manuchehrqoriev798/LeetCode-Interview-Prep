class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            if i == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= columns or board[r][c] != word[i]:
                return False

            # Save the current value of the cell at board[r][c] in the variable temp
            temp = board[r][c]

            # Mark the current cell as visited by updating its value to 'tmp'
            board[r][c] = 'tmp'

            # Explore the neighboring cells recursively
            result = (
                dfs(r + 1, c, i + 1)
                or dfs(r - 1, c, i + 1)
                or dfs(r, c + 1, i + 1)
                or dfs(r, c - 1, i + 1)
            )

            # Restore the original value of the cell
            board[r][c] = temp

            return result

        # Get the dimensions of the board
        ROWS, COLUMNS = len(board), len(board[0])

        # Iterate through each cell in the board
        for r in range(ROWS):
            for c in range(COLUMNS):
                # If the starting character matches, start DFS from that cell
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False














class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLUMNS = len(board), len(board[0])
        
        # Set to keep track of visited cells
        path = set()

        # Depth-first search (DFS) function
        def dfs(r, c, i):
            # If the entire word has been found, return True
            if i == len(word):
                return True

            # Check for conditions where DFS should not proceed
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLUMNS or 
                board[r][c] != word[i] or
                (r, c) in path):
                return False

            # Mark the current cell as visited
            path.add((r, c))

            # Explore neighboring cells recursively
            result = (
                dfs(r + 1, c, i + 1) or 
                dfs(r - 1, c, i + 1) or 
                dfs(r, c + 1, i + 1) or 
                dfs(r, c - 1, i + 1)
            )

            # Backtrack: Unmark the current cell as visited
            path.remove((r, c))

            return result

        # Iterate through each cell in the board
        for r in range(ROWS):
            for c in range(COLUMNS):
                # If the starting character matches, start DFS from that cell
                if dfs(r, c, 0):
                    return True

        return False
