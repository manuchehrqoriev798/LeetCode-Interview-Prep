class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        
        arr = []
        for _ in range(len(nums) + 1):
            arr.append([])

        for key, value in hashmap.items():
            arr[value].append(key)
        

        res = []
        for i in range(len(arr) - 1, -1, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res






class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        arr = []
        for i in range(len(nums) + 1):
            arr.append([])
        

        for key, value in d.items():
            arr[value].append(key)
        
        res = []
        for i in range(len(arr) - 1, -1, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res





class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            if num in num_freq:
                num_freq[num] += 1
            else:
                num_freq[num] = 1

        unique_nums = list(num_freq.keys())

        unique_nums.sort(key=lambda x: num_freq[x], reverse=True)

        result = []
        for i in range(k):
            result.append(unique_nums[i])

        return result



