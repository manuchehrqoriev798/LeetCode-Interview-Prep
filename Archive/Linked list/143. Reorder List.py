# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Check if the linked list is empty or has only one node
        if not head or not head.next:
            return

        # Find the middle of the linked list using two pointers (slow and fast)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next  # Move the slow pointer one step at a time
            fast = fast.next.next  # Move the fast pointer two steps at a time

        # Reverse the second half of the linked list
        second = slow.next  # The second half starts from the node after the middle
        prev = slow.next = None  # Initialize prev and cut off the first half from the middle
        while second:
            tmp = second.next  # Store the next node of the second half
            second.next = prev  # Reverse the pointer to the previous node
            prev = second  # Update the previous node
            second = tmp  # Move to the next node in the second half

        # Merge the two parts of the linked list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next  # Store the next nodes to connect
            first.next = second  # Connect the current node from the first half to the second half
            second.next = tmp1  # Connect the current node from the second half to the rest of the first half
            first = tmp1  # Move to the next node in the first half
            second = tmp2  # Move to the next node in the second half
