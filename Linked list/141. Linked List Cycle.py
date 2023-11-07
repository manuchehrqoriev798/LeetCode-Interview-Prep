# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False


    # def hasCycle(self, head: Optional[ListNode]) -> bool:
    #     visited = set()
    #     cur = head

    #     while cur is not None:
    #         if cur in visited:
    #             return True  # Cycle detected
    #         visited.add(cur)
    #         cur = cur.next

    #     return False  # No cycle found