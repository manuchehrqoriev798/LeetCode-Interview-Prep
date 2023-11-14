class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # # Check if the root is None, and return None if it is.
        # if not root:
        #     return None
        
        # # Initialize a deque (double-ended queue) with the root.
        # q = deque([root])
        
        # # Create an empty list to store the values of each level.
        # level_values = []

        # # Continue the loop until the deque is not empty.
        # while q:
        #     # Get the number of nodes at the current level.
        #     level_size = len(q)

        #     # Iterate through each node at the current level.
        #     for i in range(level_size):
        #         # Pop the leftmost node from the deque.
        #         node = q.popleft()
                
        #         # Append the value of the current node to the list.
        #         level_values.append(node.val)

        #         # If the node has a left child, add it to the deque.
        #         if node.left:
        #             q.append(node.left)
                
        #         # If the node has a right child, add it to the deque.
        #         if node.right:
        #             q.append(node.right)

        # # Sort the list of level values.
        # level_values.sort()

        # # Return the kth smallest element if it exists, otherwise, return None.
        # return level_values[k - 1] if k <= len(level_values) else None


       # Solution 2: Iterative inorder DFS
        stack = []
        count = 0
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            count += 1
            if count == k:
                return root.val
            root = root.right

        stack = []
        
        
        
        
        
        # stack = []

        # while True:
        #     # Traverse left as far as possible, pushing nodes onto the stack.
        #     while root:
        #         stack.append(root)
        #         root = root.left

        #     # Pop the top node from the stack.
        #     node = stack.pop()

        #     # Decrease k by 1 since we've visited a node.
        #     k -= 1

        #     # If k becomes 0, we have found the kth smallest element.
        #     if k == 0:
        #         return node.val

        #     # Move to the right subtree.
        #     root = node.right