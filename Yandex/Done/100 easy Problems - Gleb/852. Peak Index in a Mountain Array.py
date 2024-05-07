class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if arr[mid-1] < arr[mid] > arr[mid + 1]:
                return mid
            
            if arr[mid] > arr[mid-1]:
                l = mid 
            else:
                r = mid 
        
        return -1



class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] < arr[mid + 1]:
                # The peak is on the right side of mid
                left = mid + 1
            else:
                # The peak is on the left side of mid or mid is the peak
                right = mid

        # At the end of the loop, left and right will be pointing to the peak
        return left

        