class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            left = dfs(root.left)
            right = dfs(root.right)

            # The tree is balanced if:
            # - The left subtree is balanced (left[0] is True)
            # - The right subtree is balanced (right[0] is True)
            # - The absolute difference between the heights of the left and right subtrees is at most 1
            balance = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            return [balance, 1 + max(left[1], right[1])]

        return dfs(root)[0]









class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        if abs(left_height - right_height) >= 2:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        if not root:
            return 0  
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)









class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        if abs(left_height - right_height) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)

        return False

    def maxDepth(self, root):
        if not root:
            return 0  
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)
