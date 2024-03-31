class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, r, zeros = 0, 0, 0
        res = 0

        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            
            res = max(res, r - l + 1 - zeros)

            r += 1
        
        if res == len(nums):
            return res - 1
        else:
            return res







class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, right = 0, 0
        zeros = 0
        
        max_length = 0  
        
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
            
            right += 1
        
        if max_length > 0:
            return max_length - 1
        else:
            return 0

