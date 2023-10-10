





# def is_balanced(expression):
#     stack = []
#     brackets = {"(": ")", "{": "}", "[": "]"}
    
#     for char in expression:
#         if char in brackets.keys():
#             stack.append(char)
#         elif char in brackets.values():
#             if not stack or brackets[stack.pop()] != char:
#                 return False

#     return not stack

# # Usage:
# print(is_balanced("{[()]}"))  # Output: True
# print(is_balanced("{[(])}"))  # Output: False

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         closeToOpen = {')' : '(', '}' : '{', ']' : '['}
#         for i in s:
#             if i in closeToOpen:
#                 if stack and stack[-1] == closeToOpen[i]:
#                     stack.pop()
#                 else: 
#                     return False
#             else: 
#                 stack.append(i)
#         return not stack










# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()

#     def peek(self):
#         if not self.is_empty():
#             return self.items[-1]

#     def is_empty(self):
#         return len(self.items) == 0

#     def size(self):
#         return len(self.items)

# # Usage:
# my_stack = Stack()
# my_stack.push(1)
# my_stack.push(2)
# print(my_stack.peek())  # Output: 2
# print(my_stack.pop())   # Output: 2









# def reverse_string(input_str):
#     stack = []
#     for char in input_str:
#         stack.append(char)
    
#     reversed_str = ""
#     while stack:
#         reversed_str += stack.pop()
    
#     return reversed_str

# # Usage:
# print(reverse_string("Hello"))  # Output: "olleH"









# def evaluate_postfix(expression):
#     stack = []
#     operators = set(["+", "-", "*", "/"])

#     for char in expression:
#         if char.isdigit():
#             stack.append(int(char))
#         elif char in operators:
#             operand2 = stack.pop()
#             operand1 = stack.pop()
#             if char == "+":
#                 stack.append(operand1 + operand2)
#             elif char == "-":
#                 stack.append(operand1 - operand2)
#             elif char == "*":
#                 stack.append(operand1 * operand2)
#             elif char == "/":
#                 stack.append(operand1 / operand2)

#     return stack.pop()

# # Usage:
# print(evaluate_postfix("23*5+"))  # Output: 11
