class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count_s = {}
        char_count_t = {}
        
        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1
        
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1
        
        return char_count_s == char_count_t




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))
        if sorted_s != sorted_t:
            return False
        else:
            return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}

        for char in s:
            if char in s_dict:
               s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        for char in t:
            if char in s_dict and s_dict[char] > 0:
                s_dict[char] -= 1
            else:
                return False
    

        return sum(s_dict.values()) == 0


