class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        hashmap = {}

        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1


        for key, value in hashmap.items():
            if value % 2 == 0:
                res += value
            else:
                res += value - 1
                odd = True

        if len(s) > res:
            return res + 1
        else:
            return res


class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        hashmap = {}

        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = 1
            else:
                hashmap[s[i]] += 1

        odd = False

        for key, value in hashmap.items():
            if value % 2 == 0:
                res += value
            else:
                res += value - 1
                odd = True

        if odd:
            return res + 1
        else:
            return res



class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)

        potential_res = 0

        for val in count.values():
            if val % 2 == 0:
                potential_res += val
            else:
                potential_res += val - 1
            
        if len(s) > potential_res:
            return potential_res + 1
        else:
            return potential_res