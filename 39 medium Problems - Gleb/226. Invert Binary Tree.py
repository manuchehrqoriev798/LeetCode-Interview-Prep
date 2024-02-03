class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        q = deque([root])

        while q:
            for i in range(len(q)):
                node = q.popleft()

                node.left, node.right = node.right, node.left

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
        return root