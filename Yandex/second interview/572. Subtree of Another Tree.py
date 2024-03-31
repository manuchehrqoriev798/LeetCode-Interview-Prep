class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    
    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        else:
            return False





class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        


    def sameTree(self, root, subRoot):
        qroot = deque([root])
        qsubRoot = deque([subRoot])

        while qsubRoot:
            for i in range(len(qsubRoot)):
                node_root, node_q = qroot.popleft(), qsubRoot.popleft()

                if not node_root and not node_q:
                    continue

                if not node_root or not node_q or node_root.val != node_q.val:
                    return False

                qroot.append(node_root.left)
                qroot.append(node_root.right)
                qsubRoot.append(node_q.left)
                qsubRoot.append(node_q.right)

        return True
