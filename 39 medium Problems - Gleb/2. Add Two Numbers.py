class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None)
        cur = dummy

        carry = 0

        while l1 or l2 or carry:
            if not l1:
                val1 = 0
            else:
                val1 = l1.val

            if not l2:
                val2 = 0
            else:
                val2 = l2.val

            total = val1 + val2 + carry
            carry = total // 10
            reminder = total % 10

            cur.next = ListNode(reminder)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

