class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 2:
            return int(tokens[0])
        stack = []
        res = 0
        for char in tokens:
            if char == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num1 + num2
                stack.append(res)
            elif char == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num2 - num1
                stack.append(res)
            elif char == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num2 / num1)
                stack.append(res)
            elif char == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num1 * num2
                stack.append(res)
            else:
                stack.append(int(char))
        
        return res



class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for char in tokens:
            if char == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num1 + num2
                stack.append(res)
            elif char == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num2 - num1
                stack.append(res)
            elif char == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                res = int(num2 / num1)
                stack.append(res)
            elif char == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num1 * num2
                stack.append(res)
            else:
                stack.append(int(char))
        
        return stack[0]







class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
            elif char == "-":
                num1, num2= stack.pop(), stack.pop()
                stack.append(num2 - num1)
            elif char == "/":
                num1, num2= stack.pop(), stack.pop()
                stack.append(int(num2 / num1))
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(char))
        
        return stack[0]






class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {"+":True, "-":True, "*":True, "/":True}
        for char in tokens:
            if char in op:
                r = stack.pop()
                l = stack.pop()

                if char == "+":
                    stack.append(r + l)
                elif char == "*":
                    stack.append(r * l)
                elif char == "-":
                    stack.append(l - r)
                elif char == "/":
                    stack.append(int(l / r))
            else:
                stack.append(int(char))
        
        return stack[0]
            