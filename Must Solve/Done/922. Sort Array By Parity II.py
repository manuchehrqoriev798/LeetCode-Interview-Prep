class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l, r = 0, 0

        while r < len(nums):
            if nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1
        
        l, r = 0, len(nums) - 1
        flag = False

        while l < r:
            if flag:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
                flag = False
            else:
                l += 1
                r -= 1
                flag = True
        
        return nums




class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        lst=[]
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
                
        for i in range(len(even)):
            lst.append(even[i])
            lst.append(odd[i])
        return lst