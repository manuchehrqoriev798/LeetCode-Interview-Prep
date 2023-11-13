# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS
        # Define a recursive function to perform depth-first search (DFS)
        def dfs(node, maxVal):
            # Base case: if the current node is None, return 0
            if not node:
                return 0

            # Initialize a variable to count the good nodes
            # A node is considered good if its value is greater than or equal to the maximum value along the path
            if node.val >= maxVal:
                res = 1
            else:
                res = 0

            # Update the maximum value along the path
            maxVal = max(maxVal, node.val)

            # Recursively call the function for the left and right children of the current node
            # Accumulate the count of good nodes from both subtrees
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        # Start the DFS from the root node with the initial maximum value set to the root's value
        return dfs(root, root.val)




        # BFS
        # # Check if the root is None
        # if not root:
        #     return 0

        # # Initialize a variable to count the good nodes
        # good_nodes_count = 0

        # # Use a deque for BFS and initialize it with the root and the maximum value encountered so far
        # queue = deque([(root, root.val)])

        # # Perform BFS
        # while queue:
        #     # Get the current node and the maximum value encountered so far on this path
        #     current_node, max_val = queue.popleft()

        #     # Check if the current node is good
        #     if current_node.val >= max_val:
        #         good_nodes_count += 1

        #     # Update the maximum value for the child nodes
        #     max_val_for_children = max(max_val, current_node.val)

        #     # Add the left child to the queue if it exists
        #     if current_node.left:
        #         queue.append((current_node.left, max_val_for_children))

        #     # Add the right child to the queue if it exists
        #     if current_node.right:
        #         queue.append((current_node.right, max_val_for_children))

        # # Return the count of good nodes
        # return good_nodes_count
