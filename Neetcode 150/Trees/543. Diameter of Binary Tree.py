# TODO: revise

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize a list to store the maximum diameter found so far
        res = [0]

        # Define a helper function for depth-first search
        def dfs(root):
            # If the tree is empty, return -1
            if not root:
                return -1 
            # Recursively find the maximum diameter of the left subtree
            left = dfs(root.left)
            # Recursively find the maximum diameter of the right subtree
            right = dfs(root.right)
            # Update the maximum diameter found so far. The diameter at a node is 
            # the sum of the heights of its left and right subtrees plus 2 (for the 
            # two edges connecting the node to the longest paths in its subtrees)
            res[0] = max(res[0], left + right + 2)
            # becasue the hight of the Nul tree is -1 and in order to cancel it we have to put +1 to make it 0.
            return 1 + max(left, right)
        
        # Call the helper function on the root of the tree
        dfs(root)
        # Return the maximum diameter found
        return res[0]









class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        ldepth = self.depth(root.left)
        rdepth = self.depth(root.right)
        
        # Recursively find the diameter of the left and right subtrees
        ldiameter = self.diameterOfBinaryTree(root.left)
        rdiameter = self.diameterOfBinaryTree(root.right)
        
        # Return the maximum of three values:
        # 1. Sum of depths of left and right subtrees
        # 2. Diameter of the left subtree
        # 3. Diameter of the right subtree
        return max(ldepth + rdepth, max(ldiameter, rdiameter))

    def depth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)
        
        # Return the depth of the subtree, which is 1 plus the maximum depth of left and right subtrees
        return 1 + max(left_depth, right_depth)




class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def depth(p):
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left+right)
            return 1 + max(left, right)
        depth(root)
        return self.ans




