res = []
l, r = 0, 0
while l < len(s1) and r < len(s2):
    if s1[l] > s2[r]:
        res.append(s2[r])
        r += 1
    else:
        res.append(s1[l])
        l += 1
    

if not s1 and s2:
    res.append(s2)

if not s2 and s1:
    res.append(s1)

return res