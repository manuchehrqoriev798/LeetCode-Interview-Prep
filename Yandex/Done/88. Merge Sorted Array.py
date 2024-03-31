class Solution(object):
    def merge(self, nums1, m, nums2, n):
        l1, l2 = m - 1, n - 1
        r = m + n - 1

        while l1 >= 0 and l2 >= 0:
            if nums1[l1] < nums2[l2]:
                nums1[r] = nums2[l2]
                l2 -= 1
                r -= 1
            else:
                nums1[r] = nums1[l1]
                l1 -= 1
                r -= 1
        

        while l1 >= 0:
            nums1[r] = nums1[l1]
            l1 -= 1
            r -= 1
        
        while l2 >= 0:
            nums1[r] = nums2[l2]
            l2 -= 1
            r -= 1
        
        return nums1

