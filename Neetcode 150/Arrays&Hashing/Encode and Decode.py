def encode(s):
    res = ""
    for char in s:
        length = len(char)
        l = f"{length}#"
        res = f"{res}{l}{char}"
    
    return res

s = ["hello", "world"]

print(encode(s))