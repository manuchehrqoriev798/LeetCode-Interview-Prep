class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])


        def dfs(matrix, r, c):
            if (r < 0 or c >= len(matrix[0])) or (c < 0 or r >= len(matrix)):
                return 

            if matrix[r][c] == "0":
                return

            matrix[r][c] = "0"

            dfs(matrix, r + 1, c)
            dfs(matrix, r - 1, c)
            dfs(matrix, r, c + 1)
            dfs(matrix, r , c - 1)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" :
                    islands += 1
                    dfs(grid, r, c)
            
                    
        return islands