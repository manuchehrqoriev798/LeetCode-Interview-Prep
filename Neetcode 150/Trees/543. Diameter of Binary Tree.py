# TODO revise
# The diameter of a tree is the number of nodes on the longest path between two leaves in the tree.

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize a list to store the maximum diameter found so far
        res = [0]

        def dfs(root):
            # Check if the current node is empty (base case)
            if not root:
                return 0
            # Recursively calculate the height of the left subtree
            left = dfs(root.left)
            # Recursively calculate the height of the right subtree
            right = dfs(root.right)
            # Update the maximum diameter found so far. The diameter at a node is 
            # the sum of the heights of its left and right subtrees plus 2 (for the 
            # two edges connecting the node to the longest paths in its subtrees)
            res[0] = max(res[0], left + right + 2)
            # Because the height of the Null tree is -1, and to cancel it, we add 1 to make it 0.
            return 1 + max(left, right)
        
        # Start the depth-first search from the root
        dfs(root)
        # Return the maximum diameter found during the traversal
        return res[0]


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize a variable to store the maximum diameter found so far
        res = 0

        def dfs(root):
            # Use 'nonlocal' to indicate that 'res' refers to the variable in the outer scope
            nonlocal res
            # Check if the current node is empty (base case)
            if not root:
                return 0

            # Recursively calculate the height of the left subtree
            left = dfs(root.left)
            # Recursively calculate the height of the right subtree
            right = dfs(root.right)
            # Update the maximum diameter found so far. The diameter at a node is 
            # the sum of the heights of its left and right subtrees
            res = max(res, left + right)
            # Because the height of the Null tree is -1, and to cancel it, we add 1 to make it 0.
            return 1 + max(left, right)
        
        # Start the depth-first search from the root
        dfs(root)
        # Return the maximum diameter found during the traversal
        return res







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

    def depth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        
        left_depth = self.depth(node.left)
        right_depth = self.depth(node.right)
        
        # Return the max depth from the current node, that's if why 1 +. 1 is current node
        return 1 + max(left_depth, right_depth)