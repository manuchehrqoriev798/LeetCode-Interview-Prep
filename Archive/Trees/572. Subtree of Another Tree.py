class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base case: if subRoot is None, it is always a subtree (empty subtree)
        if not subRoot:
            return True
        # Base case: if root is None but subRoot is not, subRoot cannot be a subtree
        if not root:
            return False

        # Check if the current tree rooted at 'root' is the same as the 'subRoot' tree
        if self.sameTree(root, subRoot):
            return True
        
        # Recursively check if 'subRoot' is a subtree of the left or right child of 'root'
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):
        # Base case: if both trees are empty, they are the same
        if not root and not subRoot:
            return True
        # If both nodes are not empty and have the same value,
        # recursively check their left and right subtrees
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and 
                    self.sameTree(root.right, subRoot.right))
        # If any of the above conditions is not met, the trees are not the same
        return False
