class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        
        if len(s) == 0:
            return True
        
        if len(t) == 0:
            return False
        
        cur = 0

        for char in t:
            if char == s[cur]:
                cur += 1
                if cur == len(s):
                    return True
        
        return False




class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0

        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
                r += 1 
            else:
                r += 1
        
        if l == len(s):
            return True
        else:
            False