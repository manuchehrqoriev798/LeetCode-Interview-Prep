import math
def minimum_distance_x_y(s):
    last_x = last_y = None
    ans = math.inf

    for i, char in enumerate(s):
        if char == "X":
            if last_y:
                ans = min(ans, i - last_y)
            last_x = i
            
        elif char == "Y":
            if last_x:
                ans = min(ans, i - last_x)
            last_y = i

    if (last_y and last_x):
        return ans
    return 0







def min_distance(arr, x, y):
    min_dist = float('inf')
    prev_index = -1

    for i in range(len(arr)):
        if arr[i] == x or arr[i] == y:
            if prev_index != -1 and arr[prev_index] != arr[i]:
                min_dist = min(min_dist, i - prev_index)
            prev_index = i

    return min_dist

# Test case
arr1 = [1, 2]
x1 = 1
y1 = 2
print(f"Minimum distance between {x1} and {y1} is {min_distance(arr1, x1, y1)}")

arr2 = [3, 4, 5]
x2 = 3
y2 = 5
print(f"Minimum distance between {x2} and {y2} is {min_distance(arr2, x2, y2)}")

arr3 = [3, 5, 4, 2, 6, 5, 6, 6, 5, 4, 8, 3]
x3 = 3
y3 = 6
print(f"Minimum distance between {x3} and {y3} is {min_distance(arr3, x3, y3)}")

arr4 = [2, 5, 3, 5, 4, 4, 2, 3]
x4 = 3
y4 = 2
print(f"Minimum distance between {x4} and {y4} is {min_distance(arr4, x4, y4)}")
