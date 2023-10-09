target = int(input())
num_list = [1, 2, 3, 4, 1, 1, 1, 1, 65, 76, 87, 87, 98, 8]
my_dict = {}  # Initialize an empty dictionary
result = []

for index, element in enumerate(num_list):
    # my_dict[index] = element
    pair = target - element
    if pair in my_dict:
        result.append((my_dict[pair], index))
    my_dict[element] = index

print(result)
