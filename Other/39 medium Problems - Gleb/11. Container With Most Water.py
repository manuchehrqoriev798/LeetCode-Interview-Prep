class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_water = 0

        while l <= r:
            if height[l] < height[r]:
                max_water = max(max_water, height[l] * (r - l))
                l += 1
            else:
                max_water = max(max_water, height[r] * (r - l))
                r -= 1
        
        return max_water

