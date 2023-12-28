class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = []
        def backtracking(OpenS, CloseS):
            if OpenS == CloseS == n:
                result.append(''.join(stack))
            if OpenS < n:
                stack.append('(')
                backtracking(OpenS+1, CloseS)
                stack.pop()
            if CloseS < OpenS:
                stack.append(')')
                backtracking(OpenS, CloseS + 1)
                stack.pop()
        backtracking(0, 0)
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