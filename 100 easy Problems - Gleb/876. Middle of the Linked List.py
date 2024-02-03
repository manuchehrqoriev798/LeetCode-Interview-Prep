class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        res = head
        count = 0

        while cur:
            count += 1
            cur = cur.next
        
        target = count // 2 
        count = 0

        while count < target:
            count += 1
            res = res.next
        
        return res




class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow