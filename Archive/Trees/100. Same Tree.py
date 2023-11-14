class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Check if both nodes are None (empty trees)
        if not p and not q:
            return True
        
        # Check if only one of the nodes is None (trees are not the same)
        if not p or not q:
            return False
        
        # Check if the values of the current nodes are equal
        if p.val != q.val:
            return False

        # Recursively check the left and right subtrees
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
        


        # # Alternative implementation using a separate recursive helper function
        # def dfs(p, q):
        #     # Check if both nodes are None (empty trees)
        #     if not p and not q:
        #         return True

        #     # Check if only one of the nodes is None (trees are not the same)
        #     if not p or not q:
        #         return False

        #     # Check if the values of the current nodes are equal
        #     if p.val != q.val:
        #         return False

        #     # Recursively check the left and right subtrees
        #     return dfs(p.left, q.left) and dfs(p.right, q.right)

        # # Return the result of the alternative implementation using dfs function
        # return dfs(p, q)




        # if p and q:
        #     return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # return not p and not q