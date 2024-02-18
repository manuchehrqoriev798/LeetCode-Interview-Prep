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