def normalize_string(s):
    return ' '.join(s.split())

# Test
input_str = "good       string                   "
output_str = normalize_string(input_str)
print(output_str)  # Output: "good string"



def normalize_string(s):
    normalized = ""
    l, r = 0, 0
    
    while r < len(s):
        while l < len(s) and s[l] == " ":
            l += 1
            
        r = l
        while r < len(s) and s[r] != " ":
            r += 1
        
        if r < len(s) and len(normalized) > 0:
            normalized += ' '  # Add space only if it's not the first word
        normalized += s[l:r]
        
        r += 1
        l = r
    
    return normalized

# Test
input_str = "good       string                   "
output_str = normalize_string(input_str)
print(output_str)  # Output: "good string"