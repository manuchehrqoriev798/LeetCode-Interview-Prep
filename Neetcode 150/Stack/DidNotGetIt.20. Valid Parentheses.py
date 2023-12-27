class Solution:
    def isValid(self, s):
        stack = []
        closeToOpen = {')' : '(', '}' : '{', ']' : '['}
        for i in s:
            if i in closeToOpen:
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                else: 
                    return False
            else: 
                stack.append(i)
        return not stack


s = "()[]{}"
Solution().isValid(s)