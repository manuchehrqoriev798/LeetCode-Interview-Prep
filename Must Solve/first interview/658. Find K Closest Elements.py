class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, k
        cur = right

        while cur < len(arr):
            if abs(arr[cur] - x) < abs(arr[left] - x):
                right = cur + 1
                left = cur - k  + 1
            cur += 1
        return arr[left:right]




class Solution:
    def findClosestElements(self, arr, k, x):
        l, r = 0, len(arr) - k
        while l < r:
            mid = l + (r - l) // 2
            if (x - arr[mid]) > (arr[mid + k] - x):
                l = mid + 1
            else:
                r = mid
        return arr[l:l + k]