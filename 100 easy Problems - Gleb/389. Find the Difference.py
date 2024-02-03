class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t_hashmap = {}

        for char in t:
            if char in t_hashmap:
                t_hashmap[char] += 1
            else:
                t_hashmap[char] = 1
        
        for char in s:
            if char in t_hashmap and t_hashmap[char] > 0:
                t_hashmap[char] -= 1

        for char, count in t_hashmap.items():
            if count > 0:
                return char


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for char in t:
            if t.count(char) != s.count(char):
                return char



class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s)==0:
            return t

        for char in t:
            if s.count(char) != t.count(char):
                return char
        
        
        