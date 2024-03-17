from collections import Counter

def minWindow(s, t):
    if not s or not t:
        return ""

    # Count the characters in t
    t_freq = Counter(t)

    # Set up pointers
    left = 0
    right = 0
    formed = 0
    window_counts = {}

    # Variables to track the smallest window
    min_length = float('inf')
    min_window = ""

    # Move the right pointer to find a valid window
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in t_freq and window_counts[char] == t_freq[char]:
            formed += 1

        # Shrink the window from the left side
        while formed == len(t_freq) and left <= right:
            char = s[left]

            # Update the smallest window
            if right - left + 1 < min_length:
                min_length = right - left + 1
                min_window = s[left:right + 1]

            window_counts[char] -= 1
            if char in t_freq and window_counts[char] < t_freq[char]:
                formed -= 1

            left += 1

        right += 1

    return min_window

# Example usage:
s1 = "ADOBECODEBANC"
t1 = "ABC"
print(minWindow(s1, t1))  # Output: "BANC"

s2 = "a"
t2 = "a"
print(minWindow(s2, t2))  # Output: "a"

s3 = "a"
t3 = "aa"
print(minWindow(s3, t3))  # Output: ""
