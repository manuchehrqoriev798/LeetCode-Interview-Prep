class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Start from the root of the tree
        cur =  root
        
        # Continue until the current node is not None
        while cur:
            # If both nodes are greater than the current node, move to the right subtree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # If both nodes are smaller than the current node, move to the left subtree
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            # If one node is smaller and the other is greater, the current node is the lowest common ancestor (LCA)
            else:
                return cur  # Return the LCA node as it is the lowest common ancestor of p and q
