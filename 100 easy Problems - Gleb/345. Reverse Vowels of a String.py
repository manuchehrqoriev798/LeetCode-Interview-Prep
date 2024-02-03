class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r= 0,  len(s) - 1
        Vowels = "aeiou"+"AEIOU"
        s = list(s)

        while l < r:
            if s[l] not in Vowels:
                l += 1
            if s[r] not in Vowels:
                r -= 1
            if s[r] in Vowels and s[l] in Vowels:
                s[l],s[r] = s[r],s[l]
                r -= 1
                l += 1
            
        return ''.join(s)


        


class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1

        s = list(s)
        archive = "aeiouAEIOU"
        while l < r:
            if s[l] in archive and s[r] in archive:
                s[l], s[r] = s[r], s[l]
                r -= 1
                l += 1
            elif s[l] in archive and s[r] not in archive:
                r -= 1
            else:
                l += 1
        
        return "".join(s)




class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1

        s = list(s)
        archive = "aeiouAEIOU"
        while l < r:
            while l < r and s[l] not in archive:
                l += 1
            while l < r and s[r] not in archive:
                r -= 1
            
            s[l], s[r] = s[r], s[l]
            r -= 1
            l += 1
        
        return "".join(s)
                