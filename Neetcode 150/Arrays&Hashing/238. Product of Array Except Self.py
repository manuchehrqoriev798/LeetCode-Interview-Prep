class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Using division and also it is slow
        # total = 1
        # zero_count = 0

        # for num in nums:
        #     if num == 0:
        #         zero_count += 1
        #         continue
        #     else:
        #         total *= num

        # res = []
        # for num in nums:
        #     if zero_count > 1:
        #         res.append(0)
        #     elif zero_count == 1 and num == 0:
        #         res.append(total)
        #     elif zero_count == 0:
        #         res.append(total // num)
        #     else:
        #         res.append(0)

        # return res
        
        
        
        
        # n = len(nums)
        
        # pre, post = 1, 1
        # pr = [0 for i in range(n)]
        # pst = [0 for i in range(n)]
        
        # for i in range(n):
        #     pr[i] = pre
        #     pre *= nums[i]
            
        # for i in range(n - 1, -1, -1):
        #     pst[i] = post
        #     post *= nums[i]
            
        # ans = [0 for i in range(n)]
        # for i in range(n):
        #     ans[i] = pr[i] * pst[i]
            
        # return ans
        
        
        res = [1] * len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res





class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        counter = 0
        total = 1
        for i in range(len(nums)):
            if nums[i] != 0:
                total = total * nums[i]
            else:
                counter += 1
        
        res = [1] * len(nums)

        for i in range(len(res)):
            if counter == 0:
                res[i] = total // nums[i]
            elif counter == 1 and nums[i] == 0:
                res[i] = total 
            else:
                res[i] = 0
        
        return res