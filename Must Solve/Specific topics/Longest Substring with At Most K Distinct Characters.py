def longest_substring_with_k_distinct_characters(s, k):
    if k == 0:
        return 0

    charset = set()
    l, r = 0, 0
    max_length = 0

    while r < len(s):
        charset.add(s[r])

        while len(charset) > k:
            charset.remove(s[l])
            l += 1

        max_length = max(max_length, r - l + 1)
        
        r += 1

    return max_length

# Example usage:
s = "eceba"
k = 2
print(longest_substring_with_k_distinct_characters(s, k))  # Output: 3





def longest_substring_with_k_distinct_characters(s, k):
    if k == 0:
        return 0

    hashmap = {}
    l, r = 0, 0
    max_length = 0

    while r < len(s):
        if s[r] not in hashmap or hashmap[s[r]] <= 0:  
            hashmap[s[r]] = 1
        else:
            hashmap[s[r]] += 1
        
        while len(hashmap) > k:
            hashmap[s[l]] -= 1
            if hashmap[s[l]] == 0:
                del hashmap[s[l]]
            l += 1

        max_length = max(max_length, r - l + 1)
        r += 1 

    return max_length

# Example usage:
s = "eceba"
k = 2
print(longest_substring_with_k_distinct_characters(s, k))  # Output: 3











