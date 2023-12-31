class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS
        
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))





class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS

        if not root:
            return 0
        level = 0
        # q = [root]  # list
        q = deque([root])
        while q:
            for i in range(len(q)):
                # node = q.pop(0)  # list
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level




class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Iterative DFS
        
        if not root:
            return 0

        level = 1
        
        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop()
            if node:
                level = max(level, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return level


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        stack = [[root, 1]]
        level = 1

        while stack:
            node, depth = stack.pop()
            if node:
                level = max(level, depth)
                if node.left:                               # it avoids adding None to the stack and saves some iterations
                    stack.append([node.left, depth + 1])
                if node.right:
                    stack.append([node.right, depth + 1])
        
        return level