class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        window_count = Counter(s[:len(p)])
        p_count = Counter(p)

        res = []

        for i in range(len(s) - len(p)):
            if p_count == window_count:
                res.append(i)

            window_count[s[i]] -= 1
            if window_count[s[i]] == 0:
                del window_count[s[i]]
            window_count[s[i + len(p)]] += 1
            
        if p_count == window_count:
            res.append(len(s) - len(p))
 
        return res
    
    
    


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []

        window_count = Counter(s[:len(p)])
        p_count = Counter(p)

        res = []

        for i in range(len(s) - len(p) + 1):  
            if p_count == window_count:
                res.append(i)

            if i + len(p) < len(s): 
                window_count[s[i]] -= 1
                if window_count[s[i]] == 0:
                    del window_count[s[i]]
                window_count[s[i + len(p)]] += 1
        
        return res




