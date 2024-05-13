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
    hashmap = {}
    l, r = 0, 0  
    count = 0
    while r < len(s):
        if s[r] not in hashmap:
            hashmap[s[r]] = 1
            count += r - l + 1
        else:
            hashmap[s[r]] += 1
            while hashmap[s[r]] != 1:
                hashmap[s[l]] -= 1
                l += 1
            count += r - l + 1
        r += 1
    return count

s = "abcb"
answer = count_unique_subsequences(s)
print(f"Number of unique subsequences: {answer}")




# 2 Arthur problem
def min_distance(arr, x, y):
    min_dist = float('inf')
    prev_index = -1

    for i in range(len(arr)):
        if arr[i] == x or arr[i] == y:
            if prev_index != -1 and arr[prev_index] != arr[i]:
                min_dist = min(min_dist, i - prev_index)
            prev_index = i

    return min_dist

arr = [1, 2, 3, 4, 5]
x = 2
y = 4
# Expected output: 2 (Distance between indices of x and y is 2)

min_distance(arr, x, y)












# 1 Arisbek problem
def product_except_self(nums):
    n = len(nums)
    result = [1] * n
    left_product = 1
    right_product = 1
    for i in range(n):
        result[i] *= left_product
        left_product *= nums[i]
    for i in range(n - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    return result

print(product_except_self([1, 2, 3, 4]))






# 2 Arisbek problem
def isReflected(nums):
    if not nums:
        return False
    
    minValue = float("inf")
    maxValue = float("-inf")
    
    seen = {}
    
    for x, y in nums:
        minValue = min(minValue, x)
        maxValue = max(maxValue, x)
        if (x, y) in seen:
            seen[(x, y)] += 1
        else:
            seen[(x, y)] = 1
    
    total = minValue + maxValue
    
    for x, y in nums:
        if (total - x, y) not in seen or seen[(total - x, y)] == 0:
            return False
        seen[(total - x, y)] -= 1
    
    return True

# Example 1
nums1 = [(1, 1), (1, 1), (1, 1), (4, 1), (4, 1)]
print(isReflected(nums1))  # Output: True






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















def find_two_maximums(arr):
    # Initialize first and second maximums with negative infinity
    first_max = float('-inf')
    second_max = float('-inf')
    
    # Iterate through the array to find the two maximum values
    for num in arr:
        # Update the maximums as needed
        if num > first_max:
            # If current number is greater than the first max, update the second max and first max
            second_max = first_max
            first_max = num
        elif num > second_max and num < first_max:
            # If current number is between first max and second max, update the second max
            second_max = num
    
    # Return the first and second maximum values
    return first_max, second_max
















# Two biggest in the array 
# Test Case
arr = [3, 6, 8, 2, 10, 7]
first = float("-inf")
second = float("-inf")

for i in range(len(arr)):
    if arr[i] > first:
        second = first
        first = arr[i]
    elif arr[i] > second:
        second = arr[i]

print(f"The two biggest numbers in the array are: {first} + {second}")


























from collections import deque

class UniqueQueue:
    def __init__(self):
        self.queue = deque()

    def add(self, number):
        if number not in self.queue:
            self.queue.append(number)
            print(f"{number} added to the line.")
        else:
            print(f"{number} already exists in the line.")

    def check(self, number):
        if number in self.queue:
            print(f"{number} is unique in the line.")
        else:
            print(f"{number} is not unique in the line.")

# Example usage
queue = UniqueQueue()
queue.add(5)
queue.add(2)
queue.add(5)  # This should print that 5 already exists
queue.add(8)
queue.check(2)  # This should print that 2 is unique
queue.check(5)  # This should print that 5 is not unique
