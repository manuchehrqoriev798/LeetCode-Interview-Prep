class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS
        
        def dfs(node, maxVal):
            if not node:
                return 0
            
            if node.val >= maxVal:
                res =  1
            else:
                res = 0
            
            maxVal = max(maxVal, node.val)

            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res
        
        return dfs(root, float('-inf'))






class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # BFS
        
        if not root:
            return 0
        
        counter = 0
        maxVal = root.val

        q = deque([(root, maxVal)])

        while q:
            node, maxVal = q.popleft()

            if node:
                if node.val >= maxVal:
                    counter += 1
                else:
                    counter = counter
                
                maxVal = max(maxVal, node.val)

                if node.left:
                    q.append([node.left, maxVal])
                if node.right:
                    q.append([node.right, maxVal])
        
        return counter