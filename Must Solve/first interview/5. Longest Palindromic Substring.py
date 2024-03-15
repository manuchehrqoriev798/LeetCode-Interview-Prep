class Solution(object):
    def longestPalindrome(self, s):
        res = ""

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r+1]
                l -= 1
                r += 1
        
        return res




class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2:
            return s
        
        max_length = 0
        start = 0
        
        for i in range(len(s)):
            length1 = self.expand_around_center(s, i, i)
            length2 = self.expand_around_center(s, i, i + 1)
            
            max_len = max(length1, length2)
            
            if max_len > max_length:
                max_length = max_len
                start = i - (max_length - 1) // 2
        
        return s[start:start + max_length]
    
    def expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
