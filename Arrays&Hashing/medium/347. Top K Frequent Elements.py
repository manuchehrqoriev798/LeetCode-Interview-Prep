class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Create a dictionary to store the frequency of each number.
        num_freq = {}
        for num in nums:
            # If the number is already in the dictionary, increment its frequency.
            if num in num_freq:
                num_freq[num] += 1
            else:
                # If the number is not in the dictionary, add it with a frequency of 1.
                num_freq[num] = 1

        # Step 2: Create a list of unique numbers from the dictionary keys.
        unique_nums = list(num_freq.keys())

        # Step 3: Sort the unique_nums list based on the frequency (in descending order).
        # We use a lambda function as the key for sorting, which retrieves the frequency of each number from num_freq.
        # Sorting in reverse order ensures that the most frequent numbers come first.
        unique_nums.sort(key=lambda x: num_freq[x], reverse=True)

        # Step 4: Create the result list with the top k most frequent elements.
        result = []
        for i in range(k):
            # Append the first k elements from the sorted unique_nums list to the result.
            result.append(unique_nums[i])

        return result
