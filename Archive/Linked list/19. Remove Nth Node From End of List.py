# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head 
        
        # to create n space between right and intial left. so that in the second loop the left will reach 
        # one before the node which we want to delete
        while n > 0 and right is not None:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        # delete the node
        left.next = left.next.next

        return dummy.next