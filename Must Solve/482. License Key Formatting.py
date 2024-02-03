class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        stack = []
        count = 0

        for i in range(len(s)-1, -1, -1):
            if count == k:
                stack.append("-")
                count = 0
            if s[i] != "-":
                stack.append(s[i].upper())
                count += 1
        
        if not stack: return ''
        if stack[-1] == '-':
            stack.pop()
                
        return "".join(reversed(stack))



class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        res = ""

        for i in range(len(s) - 1, -1, -1):
            if len(res) > 0 and (len(s) - i - 1) % k == 0:
                res += "-"
            res += s[i]

        return res[::-1]



class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        q = deque([])
        count = 0

        for i in range(len(s)-1, -1, -1):
            if count == k:
                q.appendleft("-")
                count = 0
            if s[i] != "-":
                q.appendleft(s[i].upper())
                count += 1
        
        if not q: return ''
        if q[0] == '-':
            q.popleft()
                
        return "".join(q)