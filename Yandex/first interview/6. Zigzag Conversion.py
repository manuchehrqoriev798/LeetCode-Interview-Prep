class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        res = ""

        for r in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(r, len(s), increment):
                res += s[i]
                if (r > 0 and r < numRows - 1 and 
                    i + increment - 2 * r < len(s)):
                    res += s[i + increment - 2 * r]
        
        return res



class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        res = [''] * numRows
        row, jump = 0, 1

        for char in s:
            res[row] += char
            if row == 0:
                jump = 1
            elif row == numRows - 1:
                jump = -1
            row += jump
        
        return ''.join(res)
