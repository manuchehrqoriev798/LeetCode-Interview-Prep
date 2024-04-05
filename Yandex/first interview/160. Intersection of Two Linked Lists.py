class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        one = headA
        two = headB

        while one != two:
            if one is None:
                one = headB
            else:
                one = one.next

            if two is None:
                two = headA
            else:
                two = two.next

        return one









