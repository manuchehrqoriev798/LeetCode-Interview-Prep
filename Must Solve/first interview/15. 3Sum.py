class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()


        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  

            l, r = i + 1, len(nums) - 1

            while l < r:
                target = nums[i] + nums[l] + nums[r]
                
                if target == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1  
                    
                elif target > 0:
                    r -= 1
                else:
                    l += 1
        
        return res




class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        
        return res
