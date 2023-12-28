class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        def stacking(OpenS, CloseS):
            if OpenS == CloseS == n:
                result.append(''.join(stack))
            if OpenS < n:
                stack.append('(')
                stacking(OpenS+1, CloseS)
                stack.pop()
            if CloseS < OpenS:
                stack.append(')')
                stacking(OpenS, CloseS + 1)
                stack.pop()
        stacking(0, 0)
        return result
                


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def back(openN, closeN, s):
            if len(s) == n * 2:
                res.append(s)
                return
            
            if openN < n:
                back(openN + 1, closeN, s + "(")
            if closeN < openN:
                back(openN, closeN + 1, s + ")")
            
        back(0,0,"")

        return res