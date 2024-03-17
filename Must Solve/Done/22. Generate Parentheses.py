class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []


        def stacking(openS, closeS):
            if openS == closeS == n:
                res.append("".join(stack))
            if openS < n:
                stack.append("(")
                stacking(openS + 1, closeS)
                stack.pop()
            if closeS < openS:
                stack.append(")")
                stacking(openS, closeS + 1)
                stack.pop()
        
        stacking(0, 0)

        return res
                