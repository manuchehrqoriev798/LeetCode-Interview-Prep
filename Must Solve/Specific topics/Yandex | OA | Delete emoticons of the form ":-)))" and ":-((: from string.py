def remove_emoticons(s):
    stack = []
    i = 0
    while i < len(s):
        stack.append(s[i])
        
        while len(stack) >= 3 and stack[-3] == ':' and stack[-2] == '-' and stack[-1] == ')':
            stack.pop()
            stack.pop()
            stack.pop()
            while i < len(s) and s[i] == ')':
                i += 1

        while len(stack) >= 3 and stack[-3] == ':' and stack[-2] == '-' and stack[-1] == '(':
            stack.pop()
            stack.pop()
            stack.pop()
            while i < len(s) and s[i] == '(':
                i += 1
        i += 1
    return ''.join(stack)

# Test cases
strings = [
    "I work in google :-)))))))",
    "Cool :-) and I failed assesment there:-((",
    "lol:)",
    "YEEEEE BOIIII!!!! :-))(())",
    "Cringe :-)))))))))))))))"
]

for string in strings:
    print(remove_emoticons(string))