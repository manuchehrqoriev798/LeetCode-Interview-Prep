# TODO not understood
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return res[0]


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            # Use 'nonlocal' to indicate that 'res' refers to the variable in the outer scope
            nonlocal res
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)
            return 1 + max(left, right)
        
        dfs(root)
        return res








# understood:
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ldepth = self.depth(root.left)
        rdepth = self.depth(root.right)
        
        # Recursively find the diameter of the left and right subtrees
        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)

        return max(ldepth + rdepth, max(ldiameter, rdiameter))

    def depth(self, node) -> int:
        if not node:
            return 0
        
        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)
        
        # Return the max depth from the current node, that's if why 1 +. 1 is current node
        return 1 + max(left_depth, right_depth)