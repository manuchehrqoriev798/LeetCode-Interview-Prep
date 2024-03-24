class Solution:
    def isValid(self, s: str) -> bool:
        dictionary = {")": "(", "}": "{", "]": "["}
        stack = []

        for i in range(len(s)):
            if s[i] in "([{":
                stack.append(s[i])
            elif stack and dictionary[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False
        
        return not stack



