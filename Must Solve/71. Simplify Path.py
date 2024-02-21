class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []

        for d in path:
            if stack and d == "..":
                stack.pop()
            elif d not in ["", ".", ".."]:
                stack.append(d)
        
        if not stack:
            return "/"  
        else:
            res = "/"

        for d in stack:
            res += d + "/"
        
        if res and res[-1] == "/":
            return res[:-1] 
        else:
            return res






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







class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for val in path:
            if val == '' or val == '.':
                continue
            if val == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(val)
        return '/'+'/'.join(stack)