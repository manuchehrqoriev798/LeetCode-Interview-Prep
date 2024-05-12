class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        res = []
        l, r = 0, 0

        while l < len(nums1) and r < len(nums2):
            if nums1[l] == nums2[r] and nums2[r] not in res:
                res.append(nums2[r])
                l += 1
                r += 1
            elif nums1[l] < nums2[r]:
                l += 1
            else:
                r += 1
        
        return res




class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()

        for num in nums1:
            if num in nums2:
                res.add(num)
        
        return res