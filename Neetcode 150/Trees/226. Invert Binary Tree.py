class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check basecase
        if root is None:
            return None
        
        # swap
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        # call recursive
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root