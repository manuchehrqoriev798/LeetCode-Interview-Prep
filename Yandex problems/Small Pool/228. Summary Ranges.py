class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        l, r = 0, 0
        res = []

        while r < len(nums):
            while r + 1 < len(nums) and nums[r + 1] - nums[r] == 1:
                r += 1
            
            if l == r:
                res.append(f"{nums[l]}")
            else:
                res.append(f"{nums[l]}->{nums[r]}")
            
            r += 1
            l = r
        
        return res







class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        l, r = 0, 1

        res = []

        while l < len(nums):
            while r < len(nums) and nums[r] - nums[r - 1] == 1:
                r += 1
            
            if r - l > 1:
                res.append(f"{nums[l]}->{nums[r-1]}")
            else:
                res.append(f"{nums[l]}")
            
            l = r
            r += 1
        

        return res



# decimal.getcontext().prec = 10         # Ten digits  
# decimal.getcontext().prec = 100        # One hundred digits
# decimal.getcontext().prec = 1000       # One thousand digits
# decimal.getcontext().prec = 10000      # Ten thousand digits
# decimal.getcontext().prec = 100000     # One hundred thousand digits.
# decimal.getcontext().prec = 1000000    # One million digits. Takes like 12 seconds.
# decimal.getcontext().prec = 2000000    # Two million digits. Takes like 28 seconds.
# decimal.getcontext().prec = 2500000    # Two million five hundred thousand digits. Takes like 40 seconds.
# decimal.getcontext().prec = 2600000    # Two million six hundred thousand digits. Takes like 42 seconds.
# decimal.getcontext().prec = 2700000    # Two million seven hundred thousand digits. Takes like 42 seconds.
# decimal.getcontext().prec = 2800000    # Two million eight hundred thousand digits. Takes like 43 seconds.
# decimal.getcontext().prec = 2900000    # Two million nine hundred thousand digits. Takes like 43 seconds.
# decimal.getcontext().prec = 2950000    # Two million five hundred fifty thousand digits. Takes like 44 seconds.
# decimal.getcontext().prec = 2990000    # Two million five hundred ninety thousand digits. Takes like 44 seconds.
# decimal.getcontext().prec = 2999000    # Two million nine hundred ninety-nine thousand. Takes like 44 seconds.
# decimal.getcontext().prec = 2999470    # Two million nine hundred ninety-nine thousand four hundred seventy. Takes like 44 seconds.

decimal.getcontext().prec = 2999471    # Max: Two million nine hundred ninety-nine thousand four hundred seventy-one. Takes like 44 seconds.
