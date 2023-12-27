class Solution:
    def isValid(self, s):
        stack = []
        
        closeToOpen = {")":"(", "]":"[", "}":"{"}
        
        for element in s:
            if element in closeToOpen:
                if stack and stack[-1] == closeToOpen[element]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(element)
        
        return not stack




class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if(s[i]=="(" or s[i]=="{" or s[i]=="["):
                stack.append(s[i])

            else:
                if(len(stack)!=0):
                    ele=stack.pop()            # pop the element

                    if(s[i]==")" and ele=="("): # check if poped element was match
                        continue

                    elif(s[i]=="}" and ele=="{"):
                        continue

                    elif(s[i]=="]" and ele=="["):
                        continue

                    else:
                        return False           # False if poped element did not match

                else:
                    return False               # False if stack is not empty in the end

        if(len(stack)==0):
            return True                        # True if stack is empty in the end

        return False
        