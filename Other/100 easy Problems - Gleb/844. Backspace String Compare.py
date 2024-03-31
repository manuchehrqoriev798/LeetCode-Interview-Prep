class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def backspace(s):
            stack = []
            for char in s:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack

        return backspace(s) == backspace(t)
