# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        
        prev, cur = None, slow

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        firstHalf, secondHalf = head, prev


        
        while firstHalf and secondHalf:
            if firstHalf.val == secondHalf.val:
                firstHalf = firstHalf.next
                secondHalf = secondHalf.next
            else:
                return False
        
        return True
