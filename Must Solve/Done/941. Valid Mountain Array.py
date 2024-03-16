class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l, r = 0, len(arr) - 1

        while l + 1 < len(arr) and arr[l] < arr[l + 1]:
            l += 1
        
        while r > 1 and arr[r - 1] > arr[r]:
            r -= 1
            
        if l != 0 and l == r and r != len(arr) - 1:
            return True
        else:
            return False
    
    

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l, r = 0, len(arr) - 1

        while l + 1 < len(arr) and arr[l] < arr[l + 1]:
            l += 1
        
        while r > 1 and arr[r - 1] > arr[r]:
            r -= 1
        

        return l == r and 0 < l < len(arr) - 1