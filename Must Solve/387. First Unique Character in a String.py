class Solution:
    def firstUniqChar(self, s: str) -> int:
        key = 'abcdefghijklmnopqrstuvwxyz'
        idx = 10**5
        for i in key:
            x = s.find(i)
            if x != -1 and x == s.rfind(i):
                idx = min(idx,x)
        return idx if idx != 10**5 else -1
