from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.window = deque()
        self.window_sum = 0
        self.count = 0
    
    def next(self, val: int) -> float:
        self.count += 1
        self.window.append(val)
        self.window_sum += val
        
        if self.count > self.size:
            removed_element = self.window.popleft()
            self.window_sum -= removed_element
            return self.window_sum / self.size
        else:
            return self.window_sum / self.count
