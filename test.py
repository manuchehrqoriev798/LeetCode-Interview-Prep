

























    


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