class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        char_count = {}


        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        max_count = max(char_count.values())


        result_chars = []


        for char in reversed(s):
            if char_count[char] == max_count and char not in result_chars:
                result_chars.append(char)


        result = ''.join(reversed(result_chars))

        return result
