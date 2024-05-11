class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []

        for word in strs:
            sortedWord = "".join(sorted(word))
            # sortedWord = tuple(sorted(word))
            
            
            if sortedWord in hashmap:
                hashmap[sortedWord].append(word)
            else:
                hashmap[sortedWord] = [word]
        
        for key, value in hashmap.items():
            res.append(hashmap[key])
        
        return res




