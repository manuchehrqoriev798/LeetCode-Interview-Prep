# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify the linked list addition.
        dummy = ListNode()
        cur = dummy  # Initialize a pointer 'cur' to the dummy node.

        carry = 0  # Initialize a variable to store the carry from the previous addition.

        # Loop until there are nodes left in either of the input lists or there's a carry.
        while l1 or l2 or carry:
            # Get the values from the current nodes (or 0 if the node is None).
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            # if l2:
            #     v2 = l2.val
            # else:
            #     v2 = 0

            # Calculate the sum of the current digits and the carry from the previous step.
            val = v1 + v2 + carry
            carry = val // 10  # Calculate the carry for the next step.
            val = val % 10  # Calculate the current digit value.

            # Create a new node with the current digit and link it to the result list.
            cur.next = ListNode(val)

            # Move the 'cur' pointer to the newly added node.
            cur = cur.next

            # Move to the next nodes in the input lists if they exist.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the result linked list starting from the node after the dummy node.
        return dummy.next




class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        l1num = ''
        l2num = ''

        # Traverse l1 and build l1num as a string
        while l1:
            l1num += str(l1.val)
            l1 = l1.next

        # Traverse l2 and build l2num as a string
        while l2:
            l2num += str(l2.val)
            l2 = l2.next

        # Reverse the strings and convert them to integers
        l1num = int(l1num[::-1])
        l2num = int(l2num[::-1])

        # Calculate the sum of the two numbers
        total = l1num + l2num

        # Convert the total back to a string and reverse it
        total_str = str(total)[::-1]

        # Build the result linked list
        for digit in total_str:
            tail.next = ListNode(int(digit))
            tail = tail.next

        return dummy.next