class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

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








class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        left = dummy
        right = head

        for _ in range(n):
            if right is not None:
                right = right.next
            else:
                # Handle the case where n is greater than the length of the linked list
                return head

        while right is not None:
            left = left.next
            right = right.next


        left.next = left.next.next

        return dummy.next
