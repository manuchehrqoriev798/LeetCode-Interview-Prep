class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Check if t is an empty string, return an empty string if true
        if t == "":
            return ""

        # Initialize dictionaries to store the count of characters in t and the current window
        countT, window = {}, {}

        # Count the occurrences of each character in t and store in countT dictionary
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # Variables to keep track of the characters needed and currently have in the window
        have, need = 0, len(countT)

        # Variables to store the result (window indices) and its length
        res, resLen = [-1, -1], float("infinity")
        
        # Initialize the left pointer of the window
        left = 0

        # Iterate over the characters in the input string s
        for right in range(len(s)):
            # Update the count of the current character in the window
            window[s[right]] = 1 + window.get(s[right], 0)

            # Check if the current character is in t and the window count matches the target count
            if s[right] in countT and window[s[right]] == countT[s[right]]:
                have += 1

            # Check if all characters in t are present in the current window
            while have == need:
                # Update the result if the current window is smaller than the previous result
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = (right - left + 1)

                # Move the left pointer to shrink the window
                window[s[left]] -= 1

                # Update the 'have' count if the leftmost character in the window is in t
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                # Move the left pointer to the right
                left += 1

        # Return the substring from the result indices or an empty string if no valid window is found
        return s[res[0]: res[1] + 1] if resLen != float("infinity") else ""
























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
