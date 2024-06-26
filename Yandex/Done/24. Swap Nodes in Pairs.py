# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head

        prev = dummy

        while head and head.next:
            first = head
            second = first.next
            first.val, second.val = second.val, first.val

            head = head.next.next
        
        return dummy.next