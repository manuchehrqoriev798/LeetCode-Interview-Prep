class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        star = []
        for idx, char in enumerate(s):
            if char == '(':
                stack.append(idx)
            elif char == ')':
                if stack:
                    stack.pop()
                elif star:
                    star.pop()
                else:
                    return False
            else:
                star.append(idx)
                
        while stack and star:
            if stack[-1] > star[-1]:
                return False
            
            stack.pop()
            star.pop()
        
        return len(stack) == 0







class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0








class Solution:
    def checkValidString(self, s: str) -> bool:
        l_min, l_max = 0, 0

        for c in s:
            if c == '(':
                l_min += 1
                l_max += 1
            elif c == ')':
                if l_max <= 0:
                    return False

                l_min = max(0, l_min - 1)
                l_max -= 1
            else:
                l_min = max(0, l_min - 1)
                l_max += 1
        
        return l_min == 0