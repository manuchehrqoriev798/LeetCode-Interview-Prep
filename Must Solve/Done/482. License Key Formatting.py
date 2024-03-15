class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()

        res = ""
        count = 0

        for i in range(len(s) - 1 , -1, -1):
            if count == k:
                res += "-"
                count = 0
            
            res += s[i]
            count += 1
        
        return res[::-1]




class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = ""

        s = s.replace("-","").upper()
        
        s = s[::-1]

        for i in range(0, len(s), k):
            res += s[i:i+k]
            res += "-"

        res = res[::-1]

        if res != "" and res[0] == "-":
            return res[1:]
        else:
            return res
 
 
 


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