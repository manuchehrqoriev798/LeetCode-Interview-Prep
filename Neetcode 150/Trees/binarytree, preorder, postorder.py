class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                res.append(node.val)

        dfs(root)
        return res
    
depends on positon of res.append