class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {'}': '{', ']': '[', ')': '(', }
        stack = []

        for char in s:
            if char not in dictionary:
                stack.append(char)
            else:
                if stack and stack[-1] == dictionary[char]:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0



class Solution(object):
    def isValid(self, s):
        d = {")":"(", "]":"[", "}":"{"}
        stack = []

        for char in s:
            if char in d:
                if stack and stack[-1] == d[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0