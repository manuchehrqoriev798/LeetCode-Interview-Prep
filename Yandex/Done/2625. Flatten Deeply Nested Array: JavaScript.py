def flatten_array(arr, n):
    def flatten_helper(arr, depth):
        result = []
        for item in arr:
            if depth < n and type(item) == list:
                for sub_item in flatten_helper(item, depth + 1):
                    result.append(sub_item)
            else:
                result.append(item)
        return result
    
    return flatten_helper(arr, 0)

# Test cases
arr1 = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n1 = 0
print(flatten_array(arr1, n1))  # Output: [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]

arr2 = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n2 = 1
print(flatten_array(arr2, n2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, [9, 10, 11], 12, 13, 14, 15]

arr3 = [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
n3 = 2
print(flatten_array(arr3, n3))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
