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
            char_s, char_t = s[i], t[i]

            if char_s in d1:
                if d1[char_s] != char_t:
                    return False
            else:
                d1[char_s] = char_t

            if char_t in d2:
                if d2[char_t] != char_s:
                    return False
            else:
                d2[char_t] = char_s

        return True