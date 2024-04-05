class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and ((char.islower() and stack[-1].isupper() and stack[-1].lower() == char) or (stack[-1].islower() and char.isupper() and stack[-1].upper() == char)):
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)






# class Solution:
#     def makeGood(self, s: str) -> str:
#         stack = []  
#         for char in s:
#             if stack and abs(ord(char) - ord(stack[-1])) == 32:
#                 stack.pop()
#             else:
#                 stack.append(char)

#         return ''.join(stack)





class Solution:
    def makeGood(self, s: str) -> str:
        result = []

        for char in s:
            if result and char.upper() == result[-1].upper() and char != result[-1]:
                result.pop()  
            else:
                result.append(char) 

        return ''.join(result)
