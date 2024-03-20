# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==p or root==q or root is None:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left or right






from collections import deque


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root: None}
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
                parents[node.left] = node
            if node.right:
                queue.append(node.right)
                parents[node.right] = node

        visited = set()
        queue.extend([p,q])

        while queue:
            node = queue.popleft()
            if not node:
                continue
            
            if node in visited:
                return node

            visited.add(node)
            queue.append(parents[node])