class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        hashmap = {}

        for char in jewels:
            if char not in hashmap:
                hashmap[char] = True
            
       
        for char in stones:
            if char in hashmap:
                count += 1
        
        return count


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for l in jewels:
            for r in stones:
                if l == r:
                    count += 1
        
        return count