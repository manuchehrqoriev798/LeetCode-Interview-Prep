# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None          # This will keep track of the previous node.
        curr = head          # Start from the head of the linked list.

        while curr is not None:
            # Store a reference to the next element (node) in the list.
            nxt = curr.next  # gets the next element
            
            # Reverse the direction of the two elements (change current node's next to point to the previous node).
            curr.next = prev  # changes direction of the two elements
            
            # Move 'prev' and 'curr' pointers one step forward for the next iteration.
            prev = curr  # changes 'curr' to 'prev'
            curr = nxt   # changes 'nxt' to 'curr'

        return prev





class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead







class Solution:
    def reverseList(self, head):
        slow, fast = None, head
        while fast:
            fast.next, slow, fast = slow, fast, fast.next
        return slow