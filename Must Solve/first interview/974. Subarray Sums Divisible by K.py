class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        count = 0
        total = 0
        for num in nums:
            total += num
            modulus = total % k  
            if modulus in hashmap:
                count += hashmap[modulus]
                hashmap[modulus] += 1
            else:
                hashmap[modulus] = 1

        return count
