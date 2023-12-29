class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxA = 0

        for index, height in enumerate(heights):
            start_index = index
            while stack and stack[-1][1] > height:
                popped_i, popped_h = stack.pop()
                maxA = max(maxA, popped_h * (index - popped_i))
                start_index = popped_i
            
            stack.append((start_index, height))
        
        for index, height in stack:
            maxA = max(maxA, height * (len(heights) - index))
        
        return maxA