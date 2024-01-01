class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False

        # Recursively check the left and right subtrees
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        






class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False


        def dfs(p, q):
            if not p and not q:
                return True
            
            if not p or not q:
                return False

            # Recursively compare the values of the current nodes and their left subtrees.
            left = dfs(p.left, q.left)
            
            # Recursively compare the values of the current nodes and their right subtrees.
            right = dfs(p.right, q.right)

            # The current nodes' values must be equal, and both left and right subtrees must be the same.
            return p.val == q.val and left and right

        return dfs(p, q)








class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False


        # Alternative implementation using a separate recursive helper function
        def dfs(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            # Recursively check the left and right subtrees
            return dfs(p.left, q.left) and dfs(p.right, q.right)

        # Return the result of the alternative implementation using dfs function
        return dfs(p, q)