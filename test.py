# target = int(input())
# num_list = [1, 2, 3, 4, 1, 1, 1, 1, 65, 76, 87, 87, 98, 8]
# my_dict = {}  # Initialize an empty dictionary
# result = []

# for index, element in enumerate(num_list):
#     # my_dict[index] = element
#     pair = target - element
#     if pair in my_dict:
#         result.append((my_dict[pair], index))
#     my_dict[element] = index

# print(result)


# num = int(input())
# for i in range(num):
#     number = int(input())
#     if number
# def sum(number):
#     for num1 in range(1, number):
#         for num2 in range(num1 + 1, number):
#             for num3 in range(num2 + 1, number):
#                 if num1 % 3 != 0 and num2 % 3 != 0 and num3 % 3 != 0 and num1 != num2 and num2 != num3 and num1 != num3:
#                     if num1 + num2 + num3 == number:
#                         print('YES')
#                         print(num1, num2, num3)

# n = int(input(""))

# for _ in range(n):
#     num = int(input(""))
#     sum(num)


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     if (n -3) % 3 == 0:
#         print("YES")
#         print(1, 2, n-3)
#     elif (n-6) % 3 == 0:
#         print('YES')
#         print(2, 4, n-6)
#     else: 
#         print('NO')
    

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         char_s = {}
#         char_t = {}
#         for char1 in s:
#             if char1 not in char_s:
#                 char_s[char1] = 1
#             else: 
#                 char_s[char1] += 1
#         for char2 in t:
#             if char2 not in char_t:
#                 char_t[char2] = 1
#             else: 
#                 char_t[char2] += 1
#         return char_s == char_t