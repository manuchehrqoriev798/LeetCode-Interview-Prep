class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return ''.join(stack)



class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        i = 0

        for char in s:
            if i > 0 and res[i - 1] == char:
                res.pop()
                i -= 1
            else:
                res.append(char)
                i += 1

        return ''.join(res)