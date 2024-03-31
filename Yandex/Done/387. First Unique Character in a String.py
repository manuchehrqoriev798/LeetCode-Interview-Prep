class Solution:
    def firstUniqChar(self, s: str) -> int:
        key = 'abcdefghijklmnopqrstuvwxyz'
        idx = 10**5
        for i in key:
            x = s.find(i)
            if x != -1 and x == s.rfind(i):
                idx = min(idx,x)
        return idx if idx != 10**5 else -1





class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}

        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        

        for key, value in d.items():
            if value == 1:
                return s.find(key)
        
        return -1




class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}

        for char in s:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1
        
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
                
        return -1