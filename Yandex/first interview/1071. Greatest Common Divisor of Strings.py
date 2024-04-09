class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        if str1 + str2 != str2 + str1:
            return ""
        gcd_length = self.gcd(len1, len2)
        return str1[:gcd_length]
    
    def gcd(self, a: int, b: int) -> int:
        return a if b == 0 else self.gcd(b, a % b)






class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 == str2 + str1:
            return str1[:gcd(len(str1),len(str2))]
        else:
            return""