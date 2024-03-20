def min_distance(arr, x, y):
    min_dist = float('inf')
    prev_index = -1

    for i in range(len(arr)):
        if arr[i] == x or arr[i] == y:
            if prev_index != -1 and arr[prev_index] != arr[i]:
                min_dist = min(min_dist, i - prev_index)
            prev_index = i

    return min_dist

arr = [1, 2, 3, 4, 5]
x = 2
y = 4
# Expected output: 2 (Distance between indices of x and y is 2)

min_distance(arr, x, y)