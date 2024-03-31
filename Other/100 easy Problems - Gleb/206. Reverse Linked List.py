# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        return prev





class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None

        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        return prev