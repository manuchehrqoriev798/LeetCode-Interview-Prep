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