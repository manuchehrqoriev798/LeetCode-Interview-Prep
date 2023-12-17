# One Tescase is not Passing


class Solution:
    def removeNthFromStart(self, head, n):
        # Check if the linked list is empty
        if not head:
            return None

        # If n is greater than the length of the linked list, do nothing
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        if n > length or n <= 0:
            return head

        # If n is equal to the length, remove the head
        if n == length:
            return head.next

        # Traverse to the (n-1)-th node
        prev = None
        current = head
        for _ in range(n - 1):
            prev = current
            current = current.next

        # Remove the nth node
        if current.next:
            current.value = current.next.value
            current.next = current.next.next
        else:
            prev.next = None

        return head





class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def print_linked_list(head):
    result = []
    current = head
    while current:
        result.append(current.value)
        current = current.next
    return result

def run_test_cases():
    solution = Solution()

    # Test Case 1: Remove the second node from the start
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n1 = 2
    result1 = solution.removeNthFromStart(head1, n1)
    actual1 = print_linked_list(result1)
    expected1 = [1, 2, 3, 5]
    print(f"Test Case 1: Actual: {actual1}, Expected: {expected1}")
    if actual1 == expected1:
        print("Test Case 1 Passed")
    else:
        print("Test Case 1 Failed")

    # Test Case 2: Remove the first node from the start
    head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n2 = 1
    result2 = solution.removeNthFromStart(head2, n2)
    actual2 = print_linked_list(result2)
    expected2 = [2, 3, 4, 5]
    print(f"Test Case 2: Actual: {actual2}, Expected: {expected2}")
    if actual2 == expected2:
        print("Test Case 2 Passed")
    else:
        print("Test Case 2 Failed")

    # Test Case 3: Remove the last node from the start
    head3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n3 = 5
    result3 = solution.removeNthFromStart(head3, n3)
    actual3 = print_linked_list(result3)
    expected3 = [1, 2, 3, 4]
    print(f"Test Case 3: Actual: {actual3}, Expected: {expected3}")
    if actual3 == expected3:
        print("Test Case 3 Passed")
    else:
        print("Test Case 3 Failed")

    # Test Case 4: Remove a node from the middle
    head4 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    n4 = 3
    result4 = solution.removeNthFromStart(head4, n4)
    actual4 = print_linked_list(result4)
    expected4 = [1, 2, 4, 5]
    print(f"Test Case 4: Actual: {actual4}, Expected: {expected4}")
    if actual4 == expected4:
        print("Test Case 4 Passed")
    else:
        print("Test Case 4 Failed")

    print("All test cases executed.")



# Run the test cases
run_test_cases()
