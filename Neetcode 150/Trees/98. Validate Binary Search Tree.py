class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #DFS
        def dfs(node, left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False

            left_valid = dfs(node.left, left, node.val)

            right_valid = dfs(node.right, node.val, right)

            # Return True only if both subtrees are valid
            return left_valid and right_valid

        return dfs(root, float('-inf'), float('inf'))




class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # BFS
        if not root:
            return True

        q = deque([(root, float('-inf'), float('inf'))])

        while q:
            node, left, right = q.popleft()
            if not (left < node.val < right):
                return False
            
            if node:
                if node.left:
                    q.append([node.left, left, node.val])
                if node.right:
                    q.append([node.right, node.val, right])
        
        return True