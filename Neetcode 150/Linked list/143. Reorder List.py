class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Check if the linked list is empty or has only one node
        if not head or not head.next:
            return

        # Find the middle of the linked list using two pointers (slow and fast)
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next  

        # Reverse the second half of the linked list
        second = slow.next  
        prev = slow.next = None  
        while second:
            tmp = second.next  
            second.next = prev  
            prev = second  
            second = tmp  

        # Merge the two parts of the linked list
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next  
            first.next = second  
            second.next = tmp1 
            first = tmp1  
            second = tmp2 
        











# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Create an empty list to store linked list nodes
        arr = []
        
        # Initialize a pointer 'cur' to the head of the linked list and 'length' to 0
        cur, length = head, 0

        # Traverse the linked list and store nodes in the 'arr' list
        while cur:
            arr.append(cur)  # Append the current node to the list
            cur, length = cur.next, length + 1  # Move to the next node and update length

        # Initialize two pointers, 'left' and 'right', and 'last' to the original head
        left, right = 0, length - 1
        last = head
        
        # Reorder the linked list by interleaving nodes from the first and reversed second halves
        while left < right:
            # Point the next of the left node to the right node
            arr[left].next = arr[right]
            left += 1  # Move to the next left node
            
            # Check if 'left' has reached 'right' to avoid duplicate connections
            if left == right:
                last = arr[right]  # Update 'last' to the right node
                break

            # Point the next of the right node to the left node
            arr[right].next = arr[left]
            right -= 1  # Move to the next right node
            
            last = arr[left]  # Update 'last' to the left node

        # Set the 'next' of the last node to None to terminate the modified linked list
        if last:
            last.next = None
