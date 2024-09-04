# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# # Sample input
# nums = [2, 7, 11, 15]
# target = 9

# solution = Solution()

# result = solution.twoSum(nums, target)

# print(result)





target = int(input())
num_list = [1, 2, 3, 4, 1, 1, 1, 1, 65, 76, 87, 87, 98, 8]
my_dict = {}  
result = []

for index, element in enumerate(num_list):
    # my_dict[index] = element
    pair = target - element
    if pair in my_dict:
        result.append((my_dict[pair], index))
    my_dict[element] = index

print(result)









from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashmap:
                return [hashmap[compliment], i]
            hashmap[nums[i]] = i
        


# Test case
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(result)  # Expected output: [0, 1]