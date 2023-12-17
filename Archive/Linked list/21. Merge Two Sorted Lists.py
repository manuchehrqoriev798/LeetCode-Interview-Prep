class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy   # empty node

        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # While both input lists are not empty.
        while list1 and list2:
            # Compare the values of the current nodes in list1 and list2.
            if list1.val <= list2.val:
                # Connect the 'tail' to the current node from 'list1'.
                tail.next = list1   # Connect 'tail' to the current node in 'list1'.
                
                # Move to the next node in 'list1' for further values.
                list1 = list1.next  # Move to the next node in 'list1'.
            else:
                tail.next = list2   
                
                list2 = list2.next  

            # Move 'tail' to the last node in the merged list.
            tail = tail.next      # Move 'tail' to the last node in the merged list.

        
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next