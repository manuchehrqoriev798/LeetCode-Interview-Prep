class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hashmap = {}

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            
        sorted_elements = sorted(hashmap, key=hashmap.get, reverse=True)

        return sorted_elements[:k]
        
    
    
    
    
    
        # num_freq = {}
        # result = []

        # for num in nums:
        #     if num in num_freq:
        #         num_freq[num] += 1
        #     else:
        #         num_freq[num] = 1

        # sorted_elements = sorted(num_freq, key=num_freq.get, reverse=True)

        # for i in range(k):
        #     result.append(sorted_elements[i])
            
        # return result








        # # Step 1: Create a dictionary to store the frequency of each number.
        # num_freq = {}
        # for num in nums:
        #     # If the number is already in the dictionary, increment its frequency.
        #     if num in num_freq:
        #         num_freq[num] += 1
        #     else:
        #         # If the number is not in the dictionary, add it with a frequency of 1.
        #         num_freq[num] = 1

        # # Step 2: Create a list of unique numbers from the dictionary keys.
        # unique_nums = list(num_freq.keys())

        # # Step 3: Sort the unique_nums list based on the frequency (in descending order).
        # # We use a lambda function as the key for sorting, which retrieves the frequency of each number from num_freq.
        # # Sorting in reverse order ensures that the most frequent numbers come first.
        # unique_nums.sort(key=lambda x: num_freq[x], reverse=True)

        # # Step 4: Create the result list with the top k most frequent elements.
        # result = []
        # for i in range(k):
        #     # Append the first k elements from the sorted unique_nums list to the result.
        #     result.append(unique_nums[i])

        # return result
