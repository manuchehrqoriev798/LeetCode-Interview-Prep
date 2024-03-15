class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
   

        def dfs(node, path):
            if not node:
                return

            path.append(str(node.val)) 

            dfs(node.left, path)
            dfs(node.right, path)

            if not node.left and not node.right:
                res.append('->'.join(path))
            path.pop()
            return

        dfs(root, [])
        return res




class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        q = deque([(root, "")])

        res = []

        while q:
            for i in range(len(q)):
                node, path = q.popleft()

                if not node.left and not node.right:
                    res.append(path + str(node.val))
                else:
                    if node.left:
                        q.append((node.left, path + str(node.val) + "->"))
                    if node.right:
                        q.append((node.right, path + str(node.val) + "->"))
        
        return res