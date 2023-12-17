# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     # Recursive DFS
    #     if not root:
    #         return True  # An empty tree is considered balanced
        
    #     # Check if the left and right subtrees are balanced
    #     left_height = self.maxDepth(root.left)
    #     right_height = self.maxDepth(root.right)
        
    #     if abs(left_height - right_height) > 1:
    #         return False

    #     # Recursively check balance for left and right subtrees
    #     return self.isBalanced(root.left) and self.isBalanced(root.right)

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     # Recursive DFS
    #     if not root:
    #         return 0  # The maximum depth of an empty tree is 0

    #     # Calculate the maximum depth of the left and right subtrees
    #     left_depth = self.maxDepth(root.left)
    #     right_depth = self.maxDepth(root.right)

    #     # The maximum depth of the tree is the maximum of the depths of the left and right subtrees plus 1
    #     return max(left_depth, right_depth) + 1




        def dfs(root):
            # If the node is None (indicating that it's an empty tree), return [True, 0]
            # True indicates that the tree is balanced, and 0 is the height of the tree
            if not root:
                return [True, 0]

            # Recursively call the dfs function for the left and right children of the root
            left, right = dfs(root.left), dfs(root.right)

            # The tree is balanced if:
            # - The left subtree is balanced (left[0] is True)
            # - The right subtree is balanced (right[0] is True)
            # - The absolute difference between the heights of the left and right subtrees is at most 1
            balance = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            # Return a list where:
            # - The first element is a boolean indicating whether the tree is balanced
            # - The second element is the height of the tree, which is 1 plus the maximum height of the left and right subtrees
            return [balance, 1 + max(left[1], right[1])]

        # Call the dfs function for the root of the tree
        # The function returns a list, and we return the first element of the list (which indicates whether the tree is balanced)
        return dfs(root)[0]
