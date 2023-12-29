class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        # Iterate over the temperatures using the enumerate function to get both the index and temperature.
        for i, temp in enumerate(temperatures):
            # While the stack is not empty and the current temperature is higher than the temperature at the top of the stack.
            while stack and temperatures[stack[-1]] < temp:
                # Pop the index from the stack.
                prev_index = stack.pop()
                # Update the result at the popped index with the number of days until a warmer temperature.
                res[prev_index] = i - prev_index

            # Push the current index onto the stack.
            stack.append(i)

        return res




class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = i - prev_index

            stack.append(i)

        return res








class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        def backtracking(index):
            if index >= len(temperatures):
                return

            while stack and temperatures[index] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                res[prev_index] = index - prev_index

            stack.append(index)
            backtracking(index + 1)

        backtracking(0)

        return res
    










# Time limit:
# class Solution:
#     def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         stack = []
#         res = [0] * len(temperatures)

#         def backtracking(temp1):
#             if temp1 >= len(temperatures):
#                 return

#             for temp2 in range(temp1 + 1, len(temperatures)):
#                 if temperatures[temp1] < temperatures[temp2]:
#                     res[temp1] = temp2 - temp1
#                     break
#             else:
#                 res[temp1] = 0

#             backtracking(temp1 + 1)

#         backtracking(0)

#         return res