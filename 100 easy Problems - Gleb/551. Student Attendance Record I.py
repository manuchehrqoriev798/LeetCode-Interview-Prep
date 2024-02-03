class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count("A") < 2 and s.count("LLL") == 0


class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0
        for char in s:
            if char == "A":
                count += 1
        if "LLL" in s or count >= 2:
            return False
        else:
            return True



class Solution:
    def checkRecord(self, s: str) -> bool:
        a_count = 0
        l_count = 0

        for char in s:
            if char == "A":
                a_count += 1
                if  a_count > 1:
                    return False
            
            if char == "L":
                l_count += 1
                if l_count > 2:
                    return False
            else:
                l_count = 0
        
        return True