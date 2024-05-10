class Solution:
    def doubleIt(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        
        prev = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        cur = prev
        carry = 0
        while cur:
            digit = cur.val * 2 + carry
            cur.val = digit % 10
            carry = digit // 10
            cur = cur.next
        
        if carry:
            cur = prev
            while cur.next:
                cur = cur.next
            cur.next = ListNode(carry)
        
        new_head = None
        while prev:
            tmp = prev.next
            prev.next = new_head
            new_head = prev
            prev = tmp
        
        return new_head
