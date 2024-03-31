class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        
        return prev




class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        return prev