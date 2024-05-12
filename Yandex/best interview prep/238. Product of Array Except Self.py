class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 0
        total = 1
        for num in nums:
            if num == 0:
                count += 1
            else:
                total *= num
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0 and count == 1:
                res[i] = total
            elif nums[i] != 0 and count > 0:
                res[i] = 0
            else:
                if nums[i] != 0:
                    res[i] = int(total / nums[i])
                else:
                    res[i] = 0


        return res




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        total = 1
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                total = total * num

        for i in range(len(nums)):
            if zeros == 0:
                nums[i] = total // nums[i]
            elif zeros == 1 and nums[i] == 0:
                nums[i] = total
            else:
                nums[i] = 0
        
        return nums





class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)


        prefix = 1
        for i in range(len(nums)):
            res[i] = res[i] * prefix
            prefix = prefix * nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]
        
        return res