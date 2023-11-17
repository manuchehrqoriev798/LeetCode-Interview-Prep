class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Define the function for DFS
        def dfs(i, j, k):
            # Base case: If we've found all the characters in the word, return True
            if k == len(word):
                return True

            # Check if the current cell is out of bounds or the character doesn't match
            if i < 0 or i >= rows or j < 0 or j >= columns or board[i][j] != word[k]:
                return False

            # Save the current cell value and mark it as visited (to avoid reusing it)
            temp, board[i][j] = board[i][j], '/'

            # Explore the neighboring cells recursively
            result = (
                dfs(i + 1, j, k + 1)
                or dfs(i - 1, j, k + 1)
                or dfs(i, j + 1, k + 1)
                or dfs(i, j - 1, k + 1)
            )

            # Restore the original value of the cell
            board[i][j] = temp

            return result

        # Get the dimensions of the board
        rows, columns = len(board), len(board[0])

        # Iterate through each cell in the board
        for i in range(rows):
            for j in range(columns):
                # If the starting character matches, start DFS from that cell
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        # If no match is found, return False
        return False
