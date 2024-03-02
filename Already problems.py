# 1 Ilkhom  problem
def longest_monotonic_subsequence(arr):
    n = len(arr)

    max_dec_length = 0  
    dec_length = 0
    dec_start_index = 0

    max_inc_length = 0
    inc_length = 0
    inc_start_index = 0

    for i in range(n-1):  
        if arr[i] > arr[i + 1]:
            dec_length += 1
            if dec_length > max_dec_length:
                max_dec_length = dec_length
                dec_start_index = i - max_dec_length + 1
        else:
            dec_length = 0

    for i in range(n-1):  
        if arr[i] < arr[i + 1]:
            inc_length += 1
            if inc_length > max_inc_length:
                max_inc_length = inc_length
                inc_start_index = i - inc_length + 1
        else:
            inc_length = 0  

    if (dec_start_index, dec_start_index + max_dec_length) > (inc_start_index, inc_start_index + max_inc_length):
        return (dec_start_index, dec_start_index + max_dec_length)
    else:
        return (inc_start_index, inc_start_index + max_inc_length)


arr = [1, 2, 3, 4, 3, 6, 7, 8, 9]
result = longest_monotonic_subsequence(arr)
print("Longest Monotonic Subsequence:", arr[result[0]:result[1]])






# 2 Ilkhom problem
def merge_sorted_arrays(arr1, arr2):
    result = []
    l = 0
    r = 0
    
    while l < len(arr1) and r < len(arr2):
        if arr1[l] < arr2[r]:
            result.append(arr1[l])
            l += 1
        else:
            result.append(arr2[r])
            r += 1
    
    while l < len(arr1):
        result.append(arr1[l])
        l += 1
    
    while r < len(arr2):
        result.append(arr2[r])
        r += 1
    
    return result

arr1 = [1, 2, 3]
arr2 = [3, 4, 5]
result = merge_sorted_arrays(arr1, arr2)


def merge_sorted_arrays(arr1, arr2):
    arr1 = arr1 + len(arr2) * [0]
    l, r = len(arr1) - len(arr2), len(arr2) - 1
    idx = len(arr1) - 1
    
    while l >= 0 and r >= 0:
        if arr1[l] < arr2[r]:
            arr1[idx] = arr2[r]
            idx -= 1
            r -= 1
        else:
            arr1[idx] = arr1[l]
            idx -= 1
            l -= 1

    while r >= 0:
        arr1[idx] = arr2[r]
        idx -= 1
        r -= 1

    return arr1

arr1 = [1, 2, 3]
arr2 = [3, 4, 5]
print(merge_sorted_arrays(arr1, arr2))






# # Ilkhom 4th problem. I did not get quite. If you understood it can you help.
# def intersection(arr1, arr2):
#     res = []
#     d = {}
#     l, r = 0, 0
#     cur = 0
    
#     while l < len(arr1) and r < len(arr2):
#         if arr1[l] not in d:
#             d[arr1[l]] = 1
#         else:
#             cur += 1
        
#         if arr2[r] not in d:
#             d[arr2[r]] = 1
#         else:
#             cur += 1
        
#         res.append(cur)
#         l += 1
#         r += 1
        
    
#     return res
    
    

# array1 = [1, 2, 3]
# array2 = [1, 2, 3]
# result = intersection(array1, array2)
# print(result)












# # 1 Artur problem
# def count_unique_subsequences(s):
#     hashset = set()
#     l, r = 0, 0  
#     count = 0
#     cur = 0
#     while r < len(s):
#         if s[r] not in hashset:
#             hashset.add(s[r])
#             cur += 1
#             count += cur
#             r += 1
#         else:
#             while s[l] != s[r]:
#                 hashset.remove(s[l]) 
#                 cur -= 1
#                 l += 1
#             hashset.remove(s[l])  
#             cur -= 1
#             l += 1
#             count += cur  
#     return count

# s = "abca"
# answer = count_unique_subsequences(s)
# print(f"Number of unique subsequences: {answer}")  





# # 2 Arthur problem
# def shortest_path(s):
#     x_index = -1
#     y_index = -1
#     for i, char in enumerate(s):
#         if char == 'x':
#             x_index = i
#         elif char == 'y' and x_index != -1:
#             y_index = i
#             break
#     if x_index != -1 and y_index != -1 and 'x' not in s[x_index:y_index]:
#         return y_index - x_index + 1
#     else:
#         return 0

# print(shortest_path('xoooyxx'))  


