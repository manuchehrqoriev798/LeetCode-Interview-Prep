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






# # Ilkhom 4th problem..
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        d = {}
        ans = []
        count = 0

        for i in range(len(A)):
            if A[i] not in d:
                d[A[i]] = 1
            else:
                d[A[i]] += 1
            
            if d[A[i]] == 2:
                count += 1
            
            if B[i] not in d:
                d[B[i]] = 1
            else:
                d[B[i]] += 1
            
            if d[B[i]] == 2:
                count += 1  
            
            ans.append(count)
        
        return ans 
    
    











# 1 Artur problem
def count_unique_subsequences(s):
    hashset = set()
    l, r = 0, 0  
    count = 0
    cur = 0
    while r < len(s):
        if s[r] not in hashset:
            hashset.add(s[r])
            cur += 1
            count += cur
            r += 1
        else:
            while s[l] != s[r]:
                hashset.remove(s[l]) 
                cur -= 1
                l += 1
            hashset.remove(s[l])  
            cur -= 1
            l += 1
            count += cur  
    return count

s = "abca"
answer = count_unique_subsequences(s)
print(f"Number of unique subsequences: {answer}")  





# 2 Arthur problem
def shortest_path(s):
    x_index = -1
    y_index = -1
    for i, char in enumerate(s):
        if char == 'x':
            x_index = i
        elif char == 'y' and x_index != -1:
            y_index = i
            break
    if x_index != -1 and y_index != -1 and 'x' not in s[x_index:y_index]:
        return y_index - x_index + 1
    else:
        return 0

print(shortest_path('xoooyxx'))  












# # 1 Arisbek problem
# def product_except_self(nums):
#     n = len(nums)
#     result = [1] * n
#     left_product = 1
#     right_product = 1
#     for i in range(n):
#         result[i] *= left_product
#         left_product *= nums[i]
#     for i in range(n - 1, -1, -1):
#         result[i] *= right_product
#         right_product *= nums[i]
#     return result

# print(product_except_self([1, 2, 3, 4]))



# # 2 Arisbek problem
# def vertical_line_reflection(points):
#     point_set = set()
#     min_x = float('inf')
#     max_x = float('-inf')
#     for x, y in points:
#         point_set.add((x, y))
#         min_x = min(min_x, x)
#         max_x = max(max_x, x)
#     x_sum = min_x + max_x
#     for x, y in points:
#         if (x_sum - x, y) not in point_set:
#             return False
#     return True

# print(vertical_line_reflection([[1, 2], [2, 2], [3, 2]]))





# 3 Arisbek problem
def subarray_sum(nums, target):
    d = {}
    total = 0
    for i, num in enumerate(nums):
        total += num
        if total - target in d:
            return [d[total - target], i]
        d[total] = i + 1
    return []




# print(subarray_sum([1, 3, 2, 6], 5))

# 4 Arisbek problem
def summarize_ranges(nums):
    ranges = []
    i = 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        if i == j:
            ranges.append(str(nums[i]))
        else:
            ranges.append(f"{nums[i]}-{nums[j]}")
        i = j + 1
    return ','.join(ranges)

print(summarize_ranges([1, 3, 2, 6]))








