
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


# Example usage:
s1 = "abc"
t1 = "abd"
print(is_one_edit_distance_apart(s1, t1))  # Output: True

s2 = "abc"
t2 = "ab"
print(is_one_edit_distance_apart(s2, t2))  # Output: True

s3 = "abc"
t3 = "def"
print(is_one_edit_distance_apart(s3, t3))  # Output: False





def is_one_edit_distance_apart(s, t):
    ls, lt = len(s), len(t)

    if abs(ls - lt) > 1 or s == t:
        return False
    
    for i in range(min(ls, lt)):
        if s[i] != t[i]:
            return s[i + 1] == t[i] or s[i] != t[i + 1] or s[i + 1] == t[i + 1]
    
    return True




