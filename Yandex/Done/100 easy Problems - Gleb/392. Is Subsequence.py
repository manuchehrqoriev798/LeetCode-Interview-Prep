class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False

        count = 0
        
        for char in t:
            if char == s[count]:
                count += 1
                if count == len(s):
                    return True
        
        return False




class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0

        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1

            r += 1

        return l == len(s)                 
