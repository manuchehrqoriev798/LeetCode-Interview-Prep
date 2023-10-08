from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False
    
# Create an instance of the Solution class
solution = Solution()

# Test the containsDuplicate method with a list of numbers
nums = [1, 2, 1]  # This list contains a duplicate (1)
result = solution.containsDuplicate(nums)

if result:
    print("The list contains duplicates.")
else:
    print("The list does not contain duplicates.")
