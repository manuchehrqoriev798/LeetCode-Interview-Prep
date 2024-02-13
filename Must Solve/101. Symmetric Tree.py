class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def dfs(left, right):
            if not left and not right:
                return True
            if left and right and left.val == right.val:
                return (dfs(left.left, right.right) and 
                    dfs(left.right, right.left))
            return False

        return dfs(root, root)

        
        



class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([root])

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append(None)
            
            if level != level [::-1]:
                return False
        
        return True