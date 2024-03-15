class Solution(object):
    def rotate(self, matrix):
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):
                top, buttom = l, r 

                topLeft = matrix[top][l + i]

                matrix[top][l + i] = matrix[buttom - i][l]

                matrix[buttom - i][l] = matrix[buttom][r - i]

                matrix[buttom][r-i] = matrix[top + i][r]

                matrix[top + i][r] = topLeft
            
            l += 1
            r -= 1



class Solution(object):
    def rotate(self, matrix):
        m = len(matrix)
        for l in range(m):
            for r in range(l, m):
                matrix[l][r], matrix[r][l] = matrix[r][l], matrix[l][r]
        
        for i in range(m):
            matrix[i] = matrix[i][::-1]