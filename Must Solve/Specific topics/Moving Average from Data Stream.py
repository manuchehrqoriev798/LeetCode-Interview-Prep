class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize a MovingAverage object with the specified size.
      
        :param size: The size of the moving window for which the average 
                     should be calculated.
        """
        self.queue = [0] * size  # Initialize a fixed-size list to store the values.
        self.window_sum = 0  # Sum of elements currently within the moving window.
        self.count = 0  # Total count of values processed, used to calculate the index.

    def next(self, val: int) -> float:
        """
        Calculate the moving average by adding a new value and 
        removing the oldest one from the sum if necessary.

        :param val: The new value to be added in the moving average calculation.
        :returns: The current moving average after adding the new value.
        """
        # Calculate the index of the oldest value based on the count of elements processed modulo the window size.
        index = self.count % len(self.queue)
      
        # Update the sum by adding the new value and subtracting the value that is being replaced.
        self.window_sum += val - self.queue[index]
      
        # Replace the oldest value in the queue with the new value.
        self.queue[index] = val
      
        # Increment the count of values processed.
        self.count += 1
      
        # Calculate and return the moving average. 
        # Use min to get the correct count of elements if the window is not fully filled.
        return self.window_sum / min(self.count, len(self.queue))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
