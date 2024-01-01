class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)

        while q:
            qlen = len(q)
            level = []
            
            for i in range(qlen):
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    
                    # Append the left and right children of the current node to the deque
                    q.append(node.left)
                    q.append(node.right)
            
            # Check if the level list is not empty and append it to the result
            if level:
                res.append(level)

        return res






class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []

        q = deque([root])

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level:
                res.append(level)
        
        return res