# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr is not None:
            nxt = curr.next  # gets the next element
            curr.next = prev # changes direction of the two element
            prev = curr # changes curr to prev
            curr = nxt # changes nxt to curr
        
        return prev



        # if not head:
        #     return None
        
        # newHead = head
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        # head.next = None

        # return newHead
