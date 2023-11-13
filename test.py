
























# # Creating file and managine it using a script
# info = open("read.txt")
# wholeThing = info.readline()
# print(wholeThing)

# # info = open("read.txt")
# # wholeThing = info.readlines()
# # print(wholeThing[2])

# # def main():
# #     fname = input('Enter filename:')
# #     info = open(fname, 'r')
# #     data = info.read()
# #     print(data)
# # main()
















# """
# In a file named absolute.py, implement a program in Python that prompts the
# user to enter as integers the number of rows r and the number of columns c of a table
# and then uses two user-defined functions:
#     - The function mytable(r,c) to create a table having r rows and c columns
#     of random negative integer numbers in the range (-20,-1). Use the function mytable(r,c)
#     to create a table named t.
#     - The function absolute(t) that takes the absolute value of all the values in the given
#     table. This function modifies the table.
# Example:
#     Input:
#         Enter the number of rows: 3
#         Enter the number of columns: 3
#     Output:
#         The table is: [[-18, -16, -17], [-7, -14, -4], [-18, -7, -3]]
#         The table with absolute values is: [[18, 16, 17], [7, 14, 4], [18, 7, 3]]
#     Input:
#         Enter the number of rows: 2
#         Enter the number of columns: 2
#     Output:
#         The table is: [[-17, -1], [-13, -16]]
#         The table with absolute values is: [[17, 1], [13, 16]]
# Hint:
#     To generate a random negative integer number in the range (-20,-1), use the following commands:
#         from random import randint
#         randint(-20,-1)
# """

# def absolute(t):
#     """Take the absolute value of all the values in the given table. This
#     function modifies the table.
#     Preconditions:  t is a table of negative integer numbers
#                     t is not empty
#     """
#     num_rows= len(t)
#     num_cols= len(t[0])
#     for i in range(num_rows):
#         for j in range(num_cols):
#             t[i][j] = abs(t[i][j])

# def mytable(r,c):
#     """ This function generates a table having r rows and c columns
#     of random negative integer numbers in the range (-20,-1).
#     Parameters:
#         r is the number of rows
#         c is the number of columns
#     """
#     from random import randint
#     mytable = [[randint(-20,-1) for _ in range(c)] for _ in range(r)]
#     return mytable

# # Demonstrate the functions mytable and absolute
# def main():
#     r = int(input("Enter the number of rows: "))
#     c = int(input("Enter the number of columns: "))
#     t = mytable(r, c)
#     print("The table is:", t)
#     absolute(t)
#     print("The table with absolute values is:", t)

# # Call the main function if the file has not been imported
# if __name__ == "__main__":
#     main()































































    


# # Given an array. Sort quadratic form of numbers in increasing order
# def getX2Array(arrayNum):
#     res = []
#     l, r = 0, len(arrayNum) - 1
#     if len(arrayNum) == 0:
#         return []
#     if len(arrayNum) == 1:
#         return res.append(arrayNum[0]**2)
        
#     while l <= r:
#         if abs(arrayNum[l]) >= abs(arrayNum[r]):
#             res.append(arrayNum[l]**2)
#             l += 1
#         else:
#             res.append(arrayNum[r]**2)
#             r -= 1
            
#     return res[::-1]

# test = [-3, -2, 1, 4]
# sol = getX2Array(test)
# print(sol)