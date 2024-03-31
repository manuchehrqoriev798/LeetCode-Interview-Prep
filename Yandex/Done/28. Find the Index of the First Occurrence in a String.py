class Solution(object):
    def strStr(self, haystack, needle):
        lh, ln = len(haystack), len(needle)
        for i in range(lh - ln + 1):
            if haystack[i:i + ln] == needle:
                return i
        
        return -1



class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1




class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0  # Return 0 if needle is an empty string
        
        l, r = 0, 0

        while l < len(haystack) and r < len(needle):
            if haystack[l] == needle[r]:
                l += 1
                r += 1
            elif r > 0:
                l = l - r + 1
                r = 0
            else:
                l += 1

        if r == len(needle):
            return l - r
        else:
            return -1