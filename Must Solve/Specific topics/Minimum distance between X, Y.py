def min_distance(arr, x, y):
    minDistance = float('inf')
    prevIndex = -1

    for i in range(len(arr)):
        if arr[i] == x or arr[i] == y:
            if prevIndex != -1 and arr[prevIndex] != arr[i]:
                minDistance = min(minDistance, i - prevIndex)
            prevIndex = i

    return minDistance

arr = [1, 2, 3, 4, 5]
x = 2
y = 4
# Expected output: 2 (Distance between indices of x and y is 2)

min_distance(arr, x, y)








