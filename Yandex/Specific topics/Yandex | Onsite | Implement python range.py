def myrange(start, end=None, step=1):
    if end is None:
        end = start
        start = 0

    if step == 0:
        raise ValueError("Step cannot be zero")

    result = []
    if step > 0:
        while start < end:
            result.append(start)
            start += step
    else:
        while start > end:
            result.append(start)
            start += step

    return result

# Test cases
# print(myrange(-5))          # Output: [0, 1, 2, 3, 4]
print(myrange(1, 5))       # Output: [1, 2, 3, 4]
print(myrange(10, -20, -3)) # Output: [-10, -7, -4, -1, 2, 5, 8, 11, 14, 17]
print(myrange(10, -20, -3))