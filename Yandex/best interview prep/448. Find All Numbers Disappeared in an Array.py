class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums1 = set(nums)
        res = []

        for i in range(1, len(nums) + 1):
            if i not in nums1:
                res.append(i)
        
        return res
            



class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        res = []
        
        for num in range(1, len(nums) + 1):
            if num in nums:
                d[num] = 1
            else:
                d[num] = 0
        
        
        for key, value in d.items():
            if value == 0:
                res.append(key)
        
        return res
            