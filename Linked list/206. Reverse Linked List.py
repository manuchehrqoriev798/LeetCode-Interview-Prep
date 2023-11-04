# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers to keep track of the previous and current nodes
        prev = None
        current = head
        
        while current is not None:
            # Store the next node temporarily
            next_node = current.next
            # Reverse the current node's pointer to the previous node
            current.next = prev
            # Move the prev and current pointers one step forward
            prev = current
            current = next_node
        
        # At the end, 'prev' will be pointing to the new head of the reversed list
        return prev
