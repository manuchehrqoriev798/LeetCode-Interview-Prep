class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = {}

        for word in words:
            if word in hashmap:
                hashmap[word] += 1
            else:
                hashmap[word] = 1
        
        arr = []
        for i in range(len(words) + 1):
            arr.append([])
        
        for key, value in hashmap.items():
            arr[value].append(key)
        
        for i in range(len(arr)):
            arr[i].sort()
            
        res = []
        for i in range(len(arr) - 1, -1, -1):
            for char in arr[i]:
                res.append(char)
                if len(res) == k:
                    return res
