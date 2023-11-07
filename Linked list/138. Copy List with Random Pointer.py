"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Create a dictionary to map original nodes to their corresponding copied nodes.
        oldToCopy = {None: None}

        # Start at the head of the original linked list.
        cur = head

        # First Pass: Create a shallow copy of the linked list, mapping each original node to its copy.
        while cur:
            # Create a new node with the same value as the current original node.
            copy = Node(cur.val)

            # Map the current original node to its copy in the dictionary.
            oldToCopy[cur] = copy

            # Move to the next node in the original list.
            cur = cur.next

        # Reset the 'cur' pointer to the head of the original linked list.
        cur = head

        # Second Pass: Update the 'next' and 'random' pointers of the copied nodes.
        while cur:
            # Get the copy of the current original node from the dictionary.
            copy = oldToCopy[cur]

            # Update the 'next' pointer of the copied node to point to the copy of the next original node.
            copy.next = oldToCopy[cur.next]

            # Update the 'random' pointer of the copied node to point to the copy of the original node's random node.
            copy.random = oldToCopy[cur.random]

            # Move to the next node in the original list.
            cur = cur.next

        # Return the head of the copied linked list, which is the value associated with the 'head' key in the dictionary.
        return oldToCopy[head]
