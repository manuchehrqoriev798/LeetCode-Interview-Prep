class Solution:
    def convertString(self, s: str) -> str:
        hashmap = {}

        res = []
        count = 1

        for char in s:
            if char not in hashmap:
                hashmap[char] = count
                count += 1
            
            res.append(hashmap[char])
        
        return res
        
    def isIsomorphic(self, s, t):
        return self.convertString(s) == self.convertString(t)





class Solution:
    def convertString(self, s: str) -> str:
        hashmap = {}

        res = []
        count = 1

        for char in s:
            if char not in hashmap:
                hashmap[char] = count
                count += 1
            
            res.append(str(hashmap[char]))
        
        return "".join(res)
        
    def isIsomorphic(self, s, t):
        return self.convertString(s) == self.convertString(t)




class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}

        for i in range(len(s)):
            if s[i] not in d1:
                d1[s[i]] = t[i]
            else:
                if d1[s[i]] != t[i]:
                    return False
            
            if t[i] not in d2:
                d2[t[i]] = s[i]
            else:
                if d2[t[i]] != s[i]:
                    return False
        
        return True