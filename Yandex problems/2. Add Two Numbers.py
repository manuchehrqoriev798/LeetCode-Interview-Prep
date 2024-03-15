# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        carry = 0
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            
            if l2:
                val2 = l2.val
            else:
                val2 = 0

            total = val1 + val2 + carry
            reminder = total % 10
            carry = total / 10

            cur = ListNode(reminder)
            tail.next = cur
            tail = tail.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next
