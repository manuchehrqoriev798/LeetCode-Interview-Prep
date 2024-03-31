class Solution(object):
    def simplifyPath(self, path):
        path = path.split("/")
        stack = []

        for d in path:
            if stack and d == "..":
                stack.pop()
            elif d not in ["", ".", ".."]:
                stack.append(d)
                

        if not stack:
            return "/"
        
        res = "/"
        for char in stack:
            res += char + "/"
        
        return res[:-1]
        




class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []

        for d in path:
            if stack and d == "..":
                stack.pop()
            elif d not in [".", "", ".."]:
                stack.append(d)

        return '/' + '/'.join(stack)



