def longest_monotonic_subsequence(arr):
    n = len(arr)
    max_inc_length = 1
    max_dec_length = 1
    inc_start_index = 0
    dec_start_index = 0

    inc_length = 1
    dec_length = 1

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            inc_length += 1
            if inc_length > max_inc_length:
                max_inc_length = inc_length
                inc_start_index = i - max_inc_length + 1
        else:
            inc_length = 1

        if arr[i] < arr[i - 1]:
            dec_length += 1
            if dec_length > max_dec_length:
                max_dec_length = dec_length
                dec_start_index = i - max_dec_length + 1
        else:
            dec_length = 1

    return (inc_start_index, inc_start_index + max_inc_length - 1), (dec_start_index, dec_start_index + max_dec_length - 1)

# Example usage:
arr = [1, 2, 3, 4, 6, 9, 7]
inc_subseq, dec_subseq = longest_monotonic_subsequence(arr)

print("Longest Increasing Subsequence:", arr[inc_subseq[0]:inc_subseq[1]+1], "Start index:", inc_subseq[0], "End index:", inc_subseq[1])
print("Longest Decreasing Subsequence:", arr[dec_subseq[0]:dec_subseq[1]+1], "Start index:", dec_subseq[0], "End index:", dec_subseq[1])








Arthur: one edit distance:

def is_one_edit_distance_apart(s, t):
    ls, lt = len(s), len(t)

    if abs(ls - lt) > 1 or s == t:
        return False
    
    for i in range(min(ls, lt)):
        if s[i] != t[i]:
            return s[i + 1:] == t[i + 1:] or s[i] == t[i + 1] or s[i + 1] == t[i]
    
    return True



def is_one_edit_distance_apart(s, t):
    ls, lt = len(s), len(t)

    if abs(ls - lt) > 1 or s == t:
        return False
    
    # replacement
    if ls == lt:
        count = 0
        for i in range(ls):
            if s[i] != t[i]:
                count += 1
            if count > 1:
                return False
        return True
    
    # deletion
    if ls - lt == 1:
        count = 0
        l, r = 0, 0
        while l < ls and r < lt:
            if s[l] != t[r]:
                count += 1
                if count > 1:
                    return False
                l += 1
            else:
                l += 1
                r += 1
        return True

    if ls - lt == -1:
        count = 0
        l, r = 0, 0
        while l < ls and r < lt:
            if s[l] != t[r]:
                count += 1
                if count > 1:
                    return False
                r += 1
            else:
                l += 1
                r += 1
        return True

    return False 