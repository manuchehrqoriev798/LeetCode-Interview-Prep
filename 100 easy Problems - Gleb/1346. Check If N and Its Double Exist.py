class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap = {}
        for num in arr:
            if num * 2 in hashmap or num / 2 in hashmap:
                return True
            
            if num not in hashmap:
                hashmap[num] = 1

        return False



class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashset = set()
        for num in arr:
            if num * 2 in hashset or num / 2 in hashset:
                return True
            hashset.add(num)

        return False




class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap = {}
        for num in arr:
            if num * 2 in hashmap or num / 2 in hashmap:
                return True
            
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        return False
