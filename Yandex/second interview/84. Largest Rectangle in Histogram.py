class Solution(object):
    def largestRectangleArea(self, heights):
        stack = [] # pair: (index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                popped_i, popped_h = stack.pop()
                max_area = max(max_area, popped_h * (i - popped_i))
                start = popped_i
            
            stack.append((start, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area