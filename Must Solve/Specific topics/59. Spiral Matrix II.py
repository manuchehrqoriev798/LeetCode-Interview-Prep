class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        res = []
        
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        
        while top <= bottom and left <= right:
            # Traverse top row
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            
            # Traverse right column
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            # Check if there is a bottom row
            if top <= bottom:
                # Traverse bottom row
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            
            # Check if there is a left column
            if left <= right:
                # Traverse left column
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res