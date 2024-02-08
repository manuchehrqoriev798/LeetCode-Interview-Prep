class Solution:
    def checkInclusion( self, s1, s2) -> bool:
        appender, remover = 0, 0 

        res = []

        for char in s1:
            res.append(char)

        while appender < len(s2):
            if remover < len(s2) and s2[remover] in res:
                res.remove(s2[remover])
                remover += 1
            else:
                res.append(s2[appender])
                appender += 1
            
            if not res:
                return True
        
        return False




class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l, r = 0, len(s1)
        sorted_s1 = sorted(list(s1))

        while r < len(s2):
            if sorted(list(s2[l:r])) == sorted_s1:
                return True
            
            l += 1
            r += 1
        
        return False




class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        l, r = 0, len(s1) - 1
        sorted_s1 = sorted(list(s1))

        while r < len(s2):
            if sorted(list(s2[l:r + 1])) == sorted_s1:
                return True
            
            l += 1
            r += 1
        
        return False
