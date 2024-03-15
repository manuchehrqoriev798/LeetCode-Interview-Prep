class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num1 + num2)
            elif char == "-":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num2 - num1)
            elif char == "*":
                num1, num2 = stack.pop(), stack.pop()
                stack.append(num1 * num2)
            elif char == "/":
                num1, num2 = stack.pop(), stack.pop()

                stack.append(int(num2 / num1))
            else:
                stack.append(int(char))
        
        return stack[-1]



class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {"+":True, "-":True, "*":True, "/":True}
        for i in tokens:
            if(i not in op):
                stack.append(int(i))
            else:
                right = stack.pop()
                left = stack.pop()

                if(i == '+'):
                    stack.append(left + right)
                elif(i == '-'):
                    stack.append(left - right)
                elif(i == '*'):
                    stack.append(left * right)
                elif(i == '/'):
                    stack.append(int(left / right))
        return stack.pop()