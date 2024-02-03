class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(root):
            if not root:
                return True, 0
            
            lb, lh = helper(root.left)
            rb, rh = helper(root.right)

            if not lb or not rb:
                return False, -1 
            
            return abs(lh - rh) < 2, 1 + max(lh, rh)
        
        return helper(root)[0]


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