class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        res = []

        l, r = 0, 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] == nums2[r] and nums1[l] not in res:
                res.append(nums1[l])
                l += 1
                r += 1
            elif nums1[l] > nums2[r]:
                r += 1
            else:
                l += 1
        
        return res



class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.add(nums1[i])
        
        return res



class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))

        res = set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                res.add(nums1[i])
        
        return res