class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap = {}

        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        
        count = 0

        for key, value in hashmap.items():
            if value % 2 == 0:
                count += value
            else:
                count += value - 1
        
        if len(s) > count:
            return count + 1
        else:
            return count 