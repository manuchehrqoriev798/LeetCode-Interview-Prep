























# It is answer by just providing the min length in the terms of number not the substring
class Solution:
    def minWindow(self, s: str, t: str) -> int:
        if not s or not t:
            return 0

        char_count_t = {}
        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1

        required_chars = len(char_count_t)
        formed_chars = 0
        l = 0
        min_length = float('inf')
        ans = ""

        for r in range(len(s)):
            char_r = s[r]
            if char_r in char_count_t:
                char_count_t[char_r] -= 1
                if char_count_t[char_r] == 0:
                    formed_chars += 1

            while formed_chars == required_chars:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    ans = s[l:r+1]

                char_l = s[l]
                if char_l in char_count_t:
                    char_count_t[char_l] += 1
                    if char_count_t[char_l] > 0:
                        formed_chars -= 1

                l += 1

        return min_length if min_length != float('inf') else 0
