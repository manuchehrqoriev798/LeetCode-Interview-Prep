class Solution:
    def maxArea(self, height: List[int]) -> int:
        # #Brute force
        # res = 0
        # for l in range(len(height)):
        #     for r in range(l+1, len(height)):
        #         area = (r-l) * min(height[l], height[r])
        #         res = max(res, area)
        # return res
        
        # Linear time solution: 0(n)
        res = 0
        l, r = 0, len(height)-1
        while l < r:
            area = (r-l)* min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res




class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        best = 0 

        while l < r and best < max(height) * (r - l): 
            cur = (r - l) * (min(height[r], height[l]))
            best = max(cur, best)
            if height[r] > height[l]: 
                l += 1
            else:
                r -= 1
            
        return best 








class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        best = 0 

        maxh = max(height)

        while l < r and best < maxh * (r - l): 
            cur = (r - l) * (min(height[r], height[l]))
            best = max(cur, best)
            if height[r] > height[l]: 
                l += 1
            else:
                r -= 1
            
        return best 