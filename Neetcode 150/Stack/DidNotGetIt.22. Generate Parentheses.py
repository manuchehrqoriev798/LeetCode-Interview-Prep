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
                
