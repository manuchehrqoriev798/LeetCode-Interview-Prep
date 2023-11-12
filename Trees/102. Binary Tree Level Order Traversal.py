class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # # Initialize an empty list to store the result
        # res = []
        
        # # Check if the root is None (empty tree)
        # if not root:
        #     return res
        
        # # Initialize a deque with the root node
        # q = deque([root])
        
        # # Loop until the deque is not empty
        # while q:
        #     # Get the number of nodes at the current level
        #     level_size = len(q)
        #     # Initialize a list to store values at the current level
        #     level_values = []
            
        #     # Loop through nodes at the current level
        #     for i in range(level_size):
        #         # Pop the leftmost node from the deque
        #         node = q.popleft()
        #         # Append the value of the current node to the level_values list
        #         level_values.append(node.val)
                
        #         # If the left child exists, append it to the deque
        #         if node.left:
        #             q.append(node.left)
                
        #         # If the right child exists, append it to the deque
        #         if node.right:
        #             q.append(node.right)
            
        #     # Append the list of values at the current level to the result
        #     res.append(level_values)
        
        # # Return the final result
        # return res


        # Initialize an empty list to store the result
        res = []
        # Initialize a deque
        q = deque()
        # Append the root node to the deque
        q.append(root)

        # Loop until the deque is not empty
        while q:
            # Get the number of nodes at the current level
            qlen = len(q)
            # Initialize a list to store values at the current level
            level = []
            
            # Loop through nodes at the current level
            for i in range(qlen):
                # Pop the leftmost node from the deque
                node = q.popleft()
                
                # Check if the node is not None
                if node:
                    # Append the value of the current node to the level list
                    level.append(node.val)
                    
                    # Append the left and right children of the current node to the deque
                    q.append(node.left)
                    q.append(node.right)
            
            # Check if the level list is not empty and append it to the result
            if level:
                res.append(level)

        # Return the final result
        return res
