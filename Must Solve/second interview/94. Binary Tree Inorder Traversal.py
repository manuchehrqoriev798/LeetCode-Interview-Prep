class Solution(object):
    def inorderTraversal(self, root):
        def dfs(node):
            if not node:
                return

            dfs(node.left)
            res.append(node.val)  
            dfs(node.right)


        res = []
        dfs(root)
        return res



